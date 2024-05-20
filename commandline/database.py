import re

from database.init import cursor as c, conn
from database.db import DB
from commandline.print import Print
from database.import_sql import data_to_db

def run_db_query():
    Print.bold("You have entered the place to access the database.")
    print("Type 'exit' to exit. Type 'show' followed by a table to show a table.")
    
    while True:
        query_input = input()
        
        if query_input == 'exit':
            break

        elif query_input == 'reset':
            DB.Operations.reset()

        elif query_input == 'start':
            data_to_db()

        elif re.search(r'^show ([^\s]+)$', query_input):
            table_name = query_input.split(' ')[1]
            
            try:
                DB.View.table(table_name)
            except ValueError:
                Print.red(f"Table {table_name} does not exist.")
           
        else:
            try:
                c.execute(query_input)
                print(c.fetchall())
            except ValueError:
                print(ValueError)

        