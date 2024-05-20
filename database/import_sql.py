from data.init import foods, symptomsAvailable as symptoms, symptoms as symptomTimes
from database.db import DB
from commandline.print import Print

def data_to_db():
    Print.blue("Entering data into database tables...")

    ingredients_added = []
    for food in foods.data:
        product_id_value = ''
        product_id_column = ''

        # Insert products into products table
        productExists = food['product'] != 'N/A' or ''
        barcodeExists = food['barcode'] != 'N/A' or ''

        if not DB.Query.value_exists('products', 'product', food['product']) and not DB.Query.value_exists('products', 'product', food['barcode']):
            if (productExists and barcodeExists):
                DB.Query.insert_into('products', ['product', 'barcode'], [food['product'], food['barcode']])
                product_id_value = food['barcode']
                product_id_column = 'barcode'
            elif (productExists):
                DB.Query.insert_into('products', ['product'], [food['product']])
                product_id_value = food['product']
                product_id_column = 'product'
            elif (barcodeExists):
                DB.Query.insert_into('products', ['barcode'], [food['barcode']])
                product_id_value = food['barcode']
                product_id_column = 'barcode'

        product_id = DB.Query.fetch_id('products', product_id_column, product_id_value) if product_id_value else None

        # Insert product times into product_times table
        if product_id:
            DB.Query.insert_into('product_times', ['product_id', 'date', 'time', 'datetime'], [product_id, food['date'], food['time'], food['datetime']])

        for ingredient in food['ingredients']:
            
             # Insert ingredients and ingredient times into ingredients and ingredient_times tables
            if ingredient not in ingredients_added:
                DB.Query.insert_into('ingredients', ['ingredient'], [ingredient])
            
            ingredient_id = DB.Query.fetch_id('ingredients', 'ingredient', ingredient)
            DB.Query.insert_into('ingredient_times', ['ingredient_id', 'date', 'time', 'datetime'], [ingredient_id, food['date'], food['time'], food['datetime']])
            
            ingredients_added.append(ingredient)

            # Join ingredients and products
            if product_id and not DB.Query.composite_key_exists('product_ingredients', 'product_id', product_id, 'ingredient_id', ingredient_id):
                DB.Query.insert_into('product_ingredients', ['product_id', 'ingredient_id'], [product_id, ingredient_id])
            
    del ingredients_added 

    Print.purple("ingredients done.")
    Print.purple("ingredient_times done.")
    Print.purple("products done.")
    Print.purple("product_times done.")

    # Insert into symptoms table
    for symptom in symptoms.data:
        if not DB.Query.value_exists('symptoms', 'symptom', symptom['symptom']):
            DB.Query.insert_into('symptoms', ['symptom'], [symptom['symptom']])

    Print.purple("symptoms done.")

    # Insert into symptom_times table
    for symptom in symptomTimes.data:
        symptom_id = DB.Query.fetch_id('symptoms', 'symptom', symptom['symptom'])
        DB.Query.insert_into('symptom_times', ['symptom_id', 'severity', 'date', 'time', 'datetime'], [symptom_id, symptom['severity'], symptom['date'], symptom['time'], symptom['datetime']])

    Print.purple("symptom times done.")

    Print.green('Data added to database tables.')