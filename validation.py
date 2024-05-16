import re
from datetime import datetime
from print import Print

class Validate:
    def barcode(allow_blank):
        while True:
            barcode_input = input("Barcode: ")

            if barcode_input == '' and allow_blank:
                return 'N/A'
            if len(barcode_input) != 12:
                Print.red("This barcode is invalid since it is not 12 digits")
            elif not barcode_input.isdigit():
                Print.red("This barcode is not a number.")
            else:
                return barcode_input

    def product():
        product_input = input("Product name: ")
        if product_input == '':
            return 'N/A'
        return product_input    

    def ingredients():
        while True:
            ingredients_input = input("Ingredients: ")
            ingredients = [elem.lower() for elem in ingredients_input.split(', ')]   

            if len(ingredients) == 1 and len(ingredients[0]) == 0:
                Print.red("You did not enter any ingredients.")
            elif len(ingredients) == 1 and len(ingredients[0]) > 20:
                Print.red("It looks like you didn't seperate your values correctly.")
            else:
                return ingredients, ingredients_input
    
    def date():
        date_format = '%m-%d-%Y'
        while True:
            date_input = input("Enter date (MM-DD-YYYY) [enter nothing for today's date]: ") or datetime.today().strftime(date_format)

            try:
                formatted = datetime.strptime(date_input, date_format)
                if formatted > datetime.now():
                    Print.red("You cannot enter a date into the future.")
                elif formatted.year != datetime.now().year:
                    Print.red("You cannot enter a date form the previous year.")
                else:
                    return formatted.strftime(date_format)
            except ValueError:
                Print.red("The date entered is invalid.")

    def time():
        time_format = '%I:%M%p'
        while True:
            time_input = input("Enter time (like this - 2:05AM) [enter nothing for the current time]: ") or datetime.now().strftime(time_format)
            
            try:
                formatted =  datetime.strptime(time_input, time_format)
                return formatted.strftime(time_format)
            except ValueError:
                Print.red("The time entered is not valid.")