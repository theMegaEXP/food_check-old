import json

from generate import Generate

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
        for i in self.data[::-1]:
            print()
            print("barcode: " + i['barcode'])
            print("Ingredients: " + ', '.join(i['ingredients']))
            print("Date: " + i['date'])
            print("Time: " + i['time'])

    def add_data(self, retrievedData):
        self.data.append(retrievedData)

    def add_dummy_data(self, amount):
        for i in range(amount):
            barcode = Generate.barcode()
            ingredients = Generate.ingredients()
            date = Generate.date()
            time = Generate.time()
            self.add_data({
                'id': i,
                'barcode': barcode,
                'ingredientsRaw': ''.join(ingredients),
                'ingredients': ingredients,
                'date': date,
                'time': time,
            })
        


