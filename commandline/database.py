import re

from database.init import cursor as c, conn
from database.db import DB
from commandline.print import Print
from database.import_sql import data_to_db
import database.tables as tables

def run_db_query():
    Print.bold("You have entered the place to access the database.")
    print("Type 'exit' to exit. Type 'show' followed by a table to show a table.")
    print("Type 'reset' to reset the database.")
    print("Type 'show' followed by a table name to view a DB table.")
    print("Yype 'start' to start inserting data into the database.")
    print("Type -q followed by a query to query the database. WARNING: If you edit any tables, you may need to restart the app.")
    
    while True:
        query_input = input()
        
        if query_input == 'exit':
            break

        elif query_input == 'reset':
            DB.Operations.reset()
            tables.create_tables()

        elif query_input == 'start':
            data_to_db()

        elif re.search(r'^show ([^\s]+)$', query_input):
            table_name = query_input.split(' ')[1]
            
            try:
                DB.View.table(table_name)
            except Exception:
                Print.red(f"Table {table_name} does not exist.")
           
        elif re.search(r'^-q .*', query_input):
            try:
                query = query_input[3::]
                c.execute(query)
                print(c.fetchall())
            except Exception:
                Print.red("This query raised an error.")

        else:
            Print.red("Your value is not valid.")

        