from query import Query

from init import cursor as c, conn

def show_tables():
    Query.query("SELECT name FROM sqlite_master WHERE type='table';")

def delete_tables():
    show_tables()


def create_tables():
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

    Query.create_table('product_ingredients', ['product_id INTEGER',
                                            'ingredient_id INTEGER',
                                            'FOREIGN KEY(product_id) REFERENCES products(id)',
                                            'FOREIGN KEY(ingredient_id) REFERENCES ingredients(id)',
                                            'PRIMARY KEY (product_id, ingredient_id)'
                                            ])
    
create_tables()
show_tables()
Query.insert_into('products', ['product', 'barcode'], ['Apple', 'N/A'])
print(Query.fetch_table('products'))
print()

conn.close()