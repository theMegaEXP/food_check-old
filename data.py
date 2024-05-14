import json

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

    def add_dummy_data(self):
        self.add_data({
            'barcode': '111111111',
            'ingredientsRaw': "Cherry, Orange, Grape",
            'ingredients': ['cherry', 'orange', 'grape'],
            'date': '05-14-2024',
            'time': '1:15PM',
        })
        self.add_data({
            'barcode': '222222222',
            'ingredientsRaw': "Milk, Wheat, Egg, Soy",
            'ingredients': ['milk', 'wheat', 'egg', 'soy'],
            'date': '05-26-2024',
            'time': '10:05AM',
        })


