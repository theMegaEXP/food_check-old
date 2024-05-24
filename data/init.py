from data.data import Foods, SymptomTimes, SymptomsAvailable, IgnoredIngredients, Data

Data.import_data()

foods = Foods()
foods.retrieve_data() 

symptomsAvailable = SymptomsAvailable()
symptomsAvailable.retrieve_data()

symptomTimes = SymptomTimes()
symptomTimes.retrieve_data()

ignoredIngredients = IgnoredIngredients()
ignoredIngredients.retrieve_data()