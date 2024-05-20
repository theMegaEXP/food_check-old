from data.data import Foods, SymptomTimes, SymptomsAvailable, Data

Data.import_data()

foods = Foods()
foods.retrieve_data() 
foods.add_dummy_data(30)

symptomsAvailable = SymptomsAvailable()
symptomsAvailable.retrieve_data()

symptoms = SymptomTimes()
symptoms.retrieve_data()