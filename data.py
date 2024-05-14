import json

from generate import Generate
from helpers import format_datetime

class Data:
    data = []

    def import_data(self):
        with open('data.json', 'r') as f:
            self.data = json.load(f)

    def export_data(self):
        with open('data.json', 'w') as f:
            json.dump(self.data, f)    

    def log_data(self):
        print("Here is the data that you have entered so far.")
        for index, i in enumerate(self.data, start=1):
            print()
            print(str(index) + '.')
            print("Barcode: " + i['barcode'])
            print("Product: " + i['product'])
            print("Ingredients: " + ', '.join(i['ingredients']))
            print("Date: " + i['date'])
            print("Time: " + i['time'])

    def add_data(self, retrievedData):
        self.data.append(retrievedData)

    def remove_data(self, index):
        self.data.pop(index)

    def delete_all_data(self):
        self.data = []

    def add_dummy_data(self, amount):
        for i in range(amount):
            barcode = Generate.barcode()
            ingredients = Generate.ingredients()
            date = Generate.date()
            time = Generate.time()
            self.add_data({
                'barcode': barcode,
                'product': "Dummy Product",
                'ingredientsRaw': ''.join(ingredients),
                'ingredients': ingredients,
                'date': date,
                'time': time,
            })
        


