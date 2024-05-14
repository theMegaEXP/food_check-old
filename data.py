import json

class Data:
    data = []

    def importData(self):
        with open('data.json', 'r') as f:
            self.data = json.load(f)

    def exportData(self):
        with open('data.json', 'w') as f:
            json.dump(self.data, f)

    def getData(self):
        for i in self.data:
            print("barcode: " + i['barcode'])
            print("Ingredients: " + i['ingredients'])
            print("Date: " + i['date'])
            print("Date: " + i['time'])

    def addData(self, retrievedData):
        self.data.append(retrievedData)


