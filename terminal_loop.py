import re
from datetime import datetime

from data import Data
from barcode_search import get_ingredients

data = Data()
data.add_dummy_data()

def start():
    while True:
        print("Press 1 to enter data. Press 2 to view data. Press 3 to exit.")
        start_input = int(input())

        if start_input == 1:
            print("Press 1 to search with a barcode. Press 2 to manually enter ingredients")
            secondary_input = int(input())

            if (secondary_input == 1):
                InsertData.barcode()
            elif (secondary_input == 2):
                InsertData.entry()
            else: 
                print("You did not enter the specified fields. Program staring over...")
                continue

        elif start_input == 2:
            data.log_data()
        
        elif start_input == 3:
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

        print(f"Does this look correct?\nBarcode: {barcode}\nIngredients: {ingredients}\nDate: {date}\nTime: {time}")
        print("y for yes, n for no")

        data.add_data({
            'barcode': barcode,
            'ingredientsRaw': ingredients,
            'ingredients': ingredientsToArray(ingredients),
            'date': date,
            'time': time,
            'datetime': format_datetime(date, time)
        })

        print(data.data)

    def entry():
        print("Enter ingredients seperated by a comma and a space ', '")
        ingredients_str = input()
        ingredients = [elem.lower() for elem in ingredients_str.split(', ')]

        date = input("Enter date (MM-DD-YYYY) [enter nothing for today's date]: ") or datetime.today().strftime('%m-%d-%Y')
        print("Date: " + date)

        time = input("Enter time (like this - 12:00am) [enter nothing for the current time]") or datetime.now().strftime('%I:%M%p')
        print("Time: " + time)

        

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
                data.add_data({
                    'barcode': 'N/A',
                    'ingredientsRaw': ingredients_str,
                    'ingredients': ingredients,
                    'date': date,
                    'time': time,
                })
                break
            
            elif ingr_input == 'exit':
                break
            
            else:
                continue
    

def format_datetime(date_str, time_str):
    date = datetime.strptime(date_str, '%m-%d-%Y')
    time = datetime.strptime(time_str, '%I:%M%p')

    combined_datetime =  datetime(date.year, date.month, date.day, time.hour, time.minute)
    formatted_datetime = combined_datetime.strftime('%Y-%m-%d %H:%M:%S')

    return formatted_datetime

def ingredientsToArray(ingredients):
    return [elem for elem in re.split(r', |\(|\)', ingredients) if elem != '']


    
    
