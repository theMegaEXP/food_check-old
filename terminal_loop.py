import re
from datetime import datetime

from helpers import format_datetime, ingredients_to_array
from data import Food, SymptomTimes, SymptomsAvailable
from barcode_search import get_ingredients

food = Food()
food.delete_all_data()
food.export_data()
food.import_data()
food.add_dummy_data(5)

symptomsAvailable = SymptomsAvailable()

symptoms = SymptomTimes()

def start():
    while True:
        print("Press 1 to enter data. Press 2 to view data. Press 3 to exit.")
        start_input = int(input())

        if start_input == 1:
            print("Press 1 to search with a barcode. Press 2 to manually enter ingredients. Press 3 to add a symptom you are having.")
            secondary_input = int(input())

            if (secondary_input == 1):
                InsertData.barcode()
            elif (secondary_input == 2):
                InsertData.entry()
            elif (secondary_input == 3):
                InsertData.available_symptom()
            else: 
                print("You did not enter the specified fields. Program staring over...")
                continue

        elif start_input == 2:
            while True:
                print()
                food.log_data()
                print()
                print("Type the id followed by -d [n -d] to delete a entry")
                print("Type clear if you want to delete everything")
                print("Press ENTER to exit")
                secondary_input = input()

                if re.search(r'\d+ -d', secondary_input):
                    index = int(secondary_input.split(' ')[0]) - 1
                    if index < len(food.data) and index >= 0:
                        print(f"{food.data[index]} removed.")
                        food.remove_data(index)
                    else:
                        print("The number you entered is out of range.")
                elif secondary_input == 'clear':
                    food.delete_all_data()
                else:
                    break
        
        elif start_input == 3:
            food.export_data()
            print("Data saved and app exited.")
            break
        
        else:
            continue

class InsertData:
    def barcode():
        barcode = input("Enter the barcode: ")
        ingredients = get_ingredients(barcode)

        if ingredients == False or len(barcode) < 12 or len(barcode) > 14:
            print("Unable to retreive ingredients based on barcode data")
        else:
            print("Ingredients: " + ingredients)

            date = input("Enter date (MM-DD-YYYY) [enter nothing for today's date]: ") or datetime.today().strftime('%m-%d-%Y')
            print("Date: " + date)

            time = input("Enter time (like this - 12:00am) [enter nothing for the current time]") or datetime.now().strftime('%I:%M%p')
            print("Time: " + time)

            product = input("Product name: ")

            print(f"Does this look correct?\nBarcode: {barcode}\nIngredients: {ingredients}\nDate: {date}\nTime: {time}")
            print("y for yes, n for no")

            food.add_data({
                'barcode': barcode,
                'product': product,
                'ingredientsRaw': ingredients,
                'ingredients': ingredients_to_array(ingredients),
                'date': date,
                'time': time,
                'datetime': format_datetime(date, time)
            })
        

    def entry():
        print("Enter ingredients seperated by a comma and a space ', '")
        ingredients_str = input()
        ingredients = [elem.lower() for elem in ingredients_str.split(', ')]

        date = input("Enter date (MM-DD-YYYY) [enter nothing for today's date]: ") or datetime.today().strftime('%m-%d-%Y')
        print("Date: " + date)

        time = input("Enter time (like this - 12:00am) [enter nothing for the current time]") or datetime.now().strftime('%I:%M%p')
        print("Time: " + time)

        product = input("Product name: ")

        while True:
            print()
            print("Do all of the ingredietns look correct?")
            for index, value in enumerate(ingredients, start=1):
                print(f'{index}. {value}')
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
                    print("The number you entered is out of range.")
            
            elif re.search(r'\d+ -d', ingr_input):
                index = int(ingr_input.split(' ')[0]) - 1
                if index < len(ingredients) and index >= 0:
                    print(f"{ingredients[index]} removed.")
                    ingredients.pop(index)
                else:
                    print("The number you entered is out of range.")
            
            elif ingr_input == 'add':
                added_ingr = input("Enter the ingredient that you would like to add: ")
                ingredients.append(added_ingr)
            
            elif ingr_input == 'done':
                food.add_data({
                    'barcode': 'N/A',
                    'product': product,
                    'ingredientsRaw': ingredients_str,
                    'ingredients': ingredients,
                    'date': date,
                    'time': time,
                    'datetime': format_datetime(date, time)
                })
                break
            
            elif ingr_input == 'exit':
                break
            
            else:
                continue
    

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
                symptomsAvailable.add_data(symptom)
                break
            else:
                print("You did not enter a value correctly")
                continue     


    
    
