from data.init import foods, symptomsAvailable as symptoms, symptoms as symptomTimes
from database.db import DB

def data_to_db():
    
    ingredients_added = []
    for food in foods.data:
        product_id_value = ''
        product_id_column = ''

        # Insert products and product times into products and product_times
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

        for ingredient in food['ingredients']:
            
             # Insert ingredients and ingredient times into ingredients and ingredient_times tables
            if ingredient not in ingredients_added:
                DB.Query.insert_into('ingredients', ['ingredient'], [ingredient])
            
            ingredient_id = DB.Query.fetch_id('ingredients', 'ingredient', ingredient)
            DB.Query.insert_into('ingredient_times', ['ingredient_id', 'date', 'time', 'datetime'], [ingredient_id, food['date'], food['time'], food['datetime']])
            
            ingredients_added.append(ingredient)

            print(product_id)
            print(ingredient_id)

            # Join ingredients and products
            if (product_id and not DB.Query.composite_key_exists('product_ingredients', 'product_id', product_id, 'ingredient_id', ingredient_id)):
                DB.Query.insert_into('product_ingredients', ['product_id', 'ingredient_id'], [product_id, ingredient_id])
            

    del ingredients_added 

