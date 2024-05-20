from data.init import foods, symptomsAvailable as symptoms, symptoms as symptomTimes
from database.db import DB

def data_to_db():
    
    ingredients_added = []
    for food in foods.data:
        
        # Insert products and product times into products and product_times
        productExists = food['product'] != 'N/A' or ''
        barcodeExists = food['barcode'] != 'N/A' or ''

        if not DB.Query.value_exists('products', 'product', food['product']) and not DB.Query.value_exists('products', 'product', food['barcode']):
            if (productExists and barcodeExists):
                DB.Query.insert_into('products', ['product', 'barcode'], [food['product'], food['barcode']])
            elif (productExists):
                DB.Query.insert_into('products', ['product'], [food['product']])
            elif (barcodeExists):
                DB.Query.insert_into('products', ['barcode'], [food['barcode']])

       
        for ingredient in food['ingredients']:
            
             # Insert ingredients and ingredient times into ingredients and ingredient_times tables
            if ingredient not in ingredients_added:
                DB.Query.insert_into('ingredients', ['ingredient'], [ingredient])
            
            id = DB.Query.fetch_id('ingredients', 'ingredient', ingredient)
            DB.Query.insert_into('ingredient_times', ['ingredient_id', 'date', 'time', 'datetime'], [id, food['date'], food['time'], food['datetime']])
            
            ingredients_added.append(ingredient)

            # Join ingredients and products
            

    del ingredients_added 

