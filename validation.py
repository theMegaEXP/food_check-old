import re
from datetime import datetime
from print import Print

class Validate:
    def barcode():
        barcode = input("Barcode: ")
        valid = True

        if len(barcode) != 12:
            Print.red("This barcode is invalid since it is not 12 digits")
            valid = False
        if not barcode.isdigit():
            Print.red("This barcode is not a digit")
            valid = False

        if valid:
            return barcode
        else:
            Validate.barcode()
    
    def date():
        date = input("Enter date (MM-DD-YYYY) [enter nothing for today's date]: ") or datetime.today().strftime('%m-%d-%Y')
        
        try:
            return datetime.strptime(date, '%m-%d-%Y')
        except ValueError:
           Print.red("This date is not valid")
           Validate.date()
        
    def time():
        time = input("Enter time (like this - 02:05AM) [enter nothing for the current time]: ") or datetime.now().strftime('%I:%M%p')
        
        try:
            return datetime.strptime(time, '%I:%M%p')
        except ValueError:
            Print.red("This time is not valid")
            Validate.time()

    def product():
        product = input("Product name: ")
        return product