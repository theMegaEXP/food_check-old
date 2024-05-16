import re
from datetime import datetime
from print import Print

class Validate:
    def barcode():
        while True:
            barcode_input = input("Barcode: ")

            if len(barcode_input) != 12:
                Print.red("This barcode is invalid since it is not 12 digits")
            elif not barcode_input.isdigit():
                Print.red("This barcode is not a number.")
            else:
                return barcode_input
    def date():
        date_format = '%m-%d-%Y'
        while True:
            date_input = input("Enter date (MM-DD-YYYY) [enter nothing for today's date]: ") or datetime.today().strftime(format)

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
        time_input = input("Enter time (like this - 02:05AM) [enter nothing for the current time]: ") or datetime.now().strftime('%I:%M%p')
        
        try:
            return datetime.strptime(time_input, '%I:%M%p')
        except ValueError:
            Print.red("This time is not valid")
            Validate.time()

    def product():
        product_input = input("Product name: ")
        return product_input