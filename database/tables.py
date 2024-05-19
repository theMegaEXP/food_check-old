from database.db import DB

def create_tables():
    DB.Query.create_table('ingredients', ['id INTEGER PRIMARY KEY', 
                                          'ingredient TEXT'])
    
    DB.Query.create_table('ingredient_times', ['id INTEGER PRIMARY KEY',
                                               'ingredient_id INTEGER',
                                               'date TEXT',
                                               'time TEXT',
                                               'datetime TEXT',
                                               'FOREIGN KEY (ingredient_id) REFERENCES ingredients(id)'])

    DB.Query.create_table('products', ['id INTEGER PRIMARY KEY', 
                                    'product TEXT', 
                                    'barcode TEXT'])
    
    DB.Query.create_table('product_ingredients', ['product_id INTEGER',
                                                  'ingredient_id INTEGER',
                                                  'FOREIGN KEY (product_id) REFERENCES products(id)',
                                                  'FOREIGN KEY (ingredient_id) REFERENCES ingredients(id)',
                                                  'PRIMARY KEY (product_id, ingredient_id)'])

    DB.Query.create_table('symptoms', ['id INTEGER PRIMARY KEY', 
                                       'symptom TEXT'])

    DB.Query.create_table('symptom_times', ['id INTEGER PRIMARY KEY', 
                                            'symptom_id INTEGER', 
                                            'severity INTEGER CHECK(severity >= 1 AND severity <= 10)',
                                            'date TEXT',
                                            'time TEXT',
                                            'datetime TEXT',
                                            'FOREIGN KEY (symptom_id) REFERENCES symptoms(id)'])

