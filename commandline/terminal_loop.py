import re
from datetime import datetime

from helpers import format_datetime, ingredients_to_array
from data.init import Data, foods, symptomsAvailable, symptoms
from data.barcode_search import get_product_ingredients
from commandline.print import Print
from commandline.validation import Validate
from commandline.database import run_db_query
from database.db import DB


def start():
    while True:
        Print.underline("Press 1 to enter data. Press 2 to view data. Press 3 to exit. Press 4 to access the database.")
        start_input = Validate.integer(1, 4)

        if start_input == 1:
            Print.underline("Press 1 to search with a barcode. Press 2 to manually enter ingredients. Press 3 to add a symptom you are having. Press 4 to enter when you have a symptom.")
            secondary_input = Validate.integer(1, 4)

            if secondary_input == 1:
                InsertData.barcode()
            elif secondary_input == 2:
                InsertData.entry()
            elif secondary_input == 3:
                InsertData.available_symptom()
            elif secondary_input == 4:
                InsertData.symptom()
            else: 
                Print.red("You did not enter the specified fields. Program staring over...")
                continue

        elif start_input == 2:
            Print.underline("Press 1 to view food items submitted. Press 2 to view symptoms submitted. Press 3 to view symptom times submitted.")
            secondary_input = Validate.integer(1, 3)

            if secondary_input == 1:
                ViewData.foods()
            elif secondary_input == 2:
                ViewData.availableSymptoms()
            elif secondary_input == 3:
                ViewData.symptoms()
            else: 
                Print.underline("You did not enter the specified fields. Program staring over...")
                continue
            
        
        elif start_input == 3:
            foods.send_data()
            symptomsAvailable.send_data()
            symptoms.send_data()
            Data.export_data()
            DB.Operations.close()
            Print.green("Data saved and app exited.")
            break
        
        elif start_input == 4:
            run_db_query()

        else:
            continue

class InsertData:
    def datetime():
        date = Validate.date()
        Print.key_value("Date: ", date)

        time = Validate.time()
        Print.key_value("Time: ", time)
        

        return date, time

    def barcode():
        barcode = Validate.barcode(False)
        product, ingredients = get_product_ingredients(barcode)

        if ingredients == False or len(barcode) != 12:
            Print.red("Unable to retreive ingredients based on barcode data")
        else:
            Print.key_value("Ingredients: ", ingredients)

            date, time = InsertData.datetime()

            print("Enter a product name. You can leave this field blank.")

            print()
            Print.key_value("Barcode", barcode)
            Print.key_value("Product", product)
            Print.key_value("Ingredients", ingredients)
            Print.key_value("Date", date)
            Print.key_value("Time", time)

            if (Validate.confirmation("Does the above look correct?")):
                foods.add_data({
                    'barcode': barcode,
                    'product': product,
                    'ingredientsRaw': ingredients,
                    'ingredients': ingredients_to_array(ingredients) if isinstance(ingredients, str) else ingredients,
                    'date': date,
                    'time': time,
                    'datetime': format_datetime(date, time)
                })
                Print.green("Data submitted.")
        

    def entry():
        Print.bold("Enter ingredients seperated by a comma and a space ', '")
        ingredients, ingredients_raw = Validate.ingredients()

        date, time = InsertData.datetime()

        print("Enter a product name. You can leave this field blank.")
        product = Validate.product()
        
        print("Entering a barcode will allow you to reference that barcode to keep ingredients the same.")
        print("Leave the barcode blank if you don't want to specify a barcode")
        barcode = Validate.barcode(True)



        while True:
            print()
            Print.bold("Do all of the ingredietns look correct?")
            for index, value in enumerate(ingredients, start=1):
                Print.number_value(index, value)
            print("Enter the number of any ingredient that you want to edit.")
            print("Type the number -d to delete an ingredient")
            print("Type add to add an item")
            print("Type done if the information looks correct")
            print("Type exit if you made a mistake and would like to restart")
            print()

            ingr_input = input()
            
            if ingr_input.isdigit():
                ingr_input = int(ingr_input)
                if ingr_input < len(ingredients) and ingr_input > 0:
                    index = ingr_input - 1
                    ingredients[index] = input(f"Raneme {ingredients[index]} to: ")
                else:
                    Print.red("The number you entered is out of range.")
             
            elif re.search(r'\d+ -d', ingr_input):
                index = int(ingr_input.split(' ')[0]) - 1
                if index < len(ingredients) and index >= 0:
                    Print.green(f"{ingredients[index]} removed.")
                    ingredients.pop(index)
                else:
                    Print.red("The number you entered is out of range.")
            
            elif ingr_input == 'add':
                added_ingr = input("Enter the ingredient that you would like to add: ")
                ingredients.append(added_ingr)
            
            elif ingr_input == 'done':
                foods.add_data({
                    'barcode': barcode,
                    'product': product,
                    'ingredientsRaw': ingredients_raw,
                    'ingredients': ingredients,
                    'date': date,
                    'time': time,
                    'datetime': format_datetime(date, time)
                })
                Print.green("Data submitted.")
                break
            
            elif ingr_input == 'exit':
                break
    

    def available_symptom():
        symptom = input("Enter a symptom you are having: ")

        while True:
            print()
            print("Type 'edit' to edit the symptom.")
            print("Type 'exit' to exit without saving this symptom.")
            print("Press ENTER to save this symptom")
            symp_input = input()

            if symp_input == 'edit':
                symptom = input("Enter a symptom you are having: ")
            
            elif symp_input == 'exit':
                break

            elif symp_input == '':
                symptomsAvailable.add_data({
                    'symptom': symptom,
                })
                Print.green("Data submitted.")
                break
            else:
                Print.red("You did not enter a value correctly")  
    
    def symptom():
        while True:
            symptom = input("Enter an exising symptom you are experiencing: ")
            if symptom == 'exit':
                break
            elif any(d.get('symptom') == symptom for d in symptomsAvailable.data):
                severity = Validate.severity()
                date, time = InsertData.datetime()
                print()
                Print.key_value("Symptom: ", symptom)
                Print.key_value("Symptom: ", severity)
                Print.key_value("Date", date)
                Print.key_value("Time", time)
                if Validate.confirmation("Does the information above look correct?"):
                    symptoms.add_data({
                        'symptom': symptom,
                        'severity': severity,
                        'date': date,
                        'time': time,
                        'datetime': format_datetime(date, time)
                    })
                    print()
                    Print.green("Data submitted.")
                    break
            else:
                Print.red("That symptom does not exist. Please add it first.")

class ViewData:
    def basicView(type):
        while True:
            print()
            type.log_data()
            print()
            print("Type the id followed by -d [n -d] to delete a entry")
            print("Type clear if you want to delete everything")
            print("Press ENTER to exit")
            viewing_input = input()

            if re.search(r'\d+ -d', viewing_input):
                index = int(viewing_input.split(' ')[0]) - 1
                if index < len(type.data) and index >= 0:
                    Print.green(f"{type.data[index]} removed.")
                    type.remove_data(index)
                else:
                    Print.red("The number you entered is out of range.")
            elif viewing_input == 'clear':
                type.delete_all_data()
                Print.green("Data cleared.")
            elif viewing_input == '':
                break
            else:
                Print.red("You did not enter a correct value.")
                
    def foods():
       ViewData.basicView(foods)

    def availableSymptoms():
        ViewData.basicView(symptomsAvailable)

    def symptoms():
        ViewData.basicView(symptoms)
