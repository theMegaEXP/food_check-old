import json

from generate import Generate
from helpers import format_datetime

class Data:

    data_all = {}

    def import_data(self):
        with open('data.json', 'r') as f:
            self.dataAll = json.load(f)

    def export_data(self):
        with open('data.json', 'w') as f:
            json.dump(self.dataAll, f)   

    def retrieve_data(self):
        class_name = self.__class__.__name__
        json_name = class_name[0].lower() + class_name[1:]
        self.data = self.dataAll[json_name]

    def send_data(self):
        class_name = self.__class__.__name__
        json_name = class_name[0].lower() + class_name[1:]
        self.data_all[json_name] = self.data

    def log_data(self):
        print("Here is the data that you have entered so far.")
        for index, i in enumerate(self.data, start=1):         
            print()
            print(str(index) + '.')
            for key, value in i.items():
                value = value if not isinstance(value, list) else ', '.join(value)
                print(f"{key.title()}: {value}")

    def add_data(self, retrievedData):
        self.data.append(retrievedData)

    def remove_data(self, index):
        self.data.pop(index)

    def delete_all_data(self):
        self.data = []

    
        

class Food(Data):
    def __init__(self):
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

class SymptomTimes(Data):
    def __init__(self):
        self.data = []


class SymptomsAvailable(Data):
    def __init__(self):
        self.data = []

    def add_dummy_data(self, amount):
        for i in range(amount):
            self.add_data({
                'symptom': Generate.symptom()
            })
        
