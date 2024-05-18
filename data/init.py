from data.data import Foods, SymptomTimes, SymptomsAvailable, Data

Data.import_data()

foods = Foods()
foods.retrieve_data() 
foods.add_dummy_data(10)

symptomsAvailable = SymptomsAvailable()
symptomsAvailable.retrieve_data()
symptomsAvailable.add_dummy_data(5)

symptoms = SymptomTimes()
symptoms.retrieve_data()
symptoms.add_dummy_data(15)