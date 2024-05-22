from data.data import Foods, SymptomTimes, SymptomsAvailable, Data

Data.import_data()

foods = Foods()
foods.retrieve_data() 

symptomsAvailable = SymptomsAvailable()
symptomsAvailable.retrieve_data()

symptomTimes = SymptomTimes()
symptomTimes.retrieve_data()