from database.db import DB

def create_tables():
    DB.Query.create_table('ingredients', ['id INTEGER PRIMARY KEY', 
                                   'ingredient TEXT'])

    DB.Query.create_table('products', ['id INTEGER PRIMARY KEY', 
                                    'product TEXT', 
                                    'barcode TEXT'])

    DB.Query.create_table('symptoms_available', ['id INTEGER PRIMARY KEY', 
                                            'symptom TEXT'])

    DB.Query.create_table('symptom_times', ['id INTEGER PRIMARY KEY', 
                                        'symptom TEXT', 
                                        'severity INTEGER CHECK(severity >= 1 AND severity <= 10)'])

    DB.Query.create_table('product_ingredients', ['product_id INTEGER',
                                            'ingredient_id INTEGER',
                                            'FOREIGN KEY(product_id) REFERENCES products(id)',
                                            'FOREIGN KEY(ingredient_id) REFERENCES ingredients(id)',
                                            'PRIMARY KEY (product_id, ingredient_id)'])