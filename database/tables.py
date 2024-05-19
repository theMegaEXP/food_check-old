from database.query import Query

def show_tables():
    pass

Query.create_table('ingredients', ['id INTEGER PRIMARY KEY', 
                                   'ingredient TEXT'])

Query.create_table('products', ['id INTEGER PRIMARY KEY', 
                                'product TEXT', 
                                'barcode TEXT'])

Query.create_table('symptoms_available', ['id INTEGER PRIMARY KEY', 
                                          'symptom TEXT'])

Query.create_table('symptom_times', ['id INTEGER PRIMARY KEY', 
                                     'symptom TEXT', 
                                     'severity INTEGER CHECK(severity >= 1 AND severity <= 10)'])

Query.create_table('product_ingredients', ['product_id INTEGER'
                                           'ingredient_id INTEGER'
                                           'FOREIGN KEY(product_id) REFERENCES products(product_id)'
                                           'FOREIGN KEY(ingredient_id) REFERENCES ingredients(ingredient_id)'
                                           'PRIMARY KEY (product_id, course_id)'
                                           ])

