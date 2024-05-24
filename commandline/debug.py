import re

from helpers import index_exists
from database.init import cursor as c, conn
from database.db import DB
from database.import_sql import data_to_db
import database.tables as tables
from commandline.print import Print
from data.init import foods, symptomsAvailable, symptomTimes

class Debug:
    def database():
        Print.bold("You have entered the debug area for the database.")
        print("Type 'exit' to exit. Type 'show' followed by a table to show a table.")
        print("Type 'reset' to reset the database.")
        print("Type 'show' followed by a table name to view a DB table.")
        print("Type -q followed by a query to query the database.")
        Print.orange("WARNING: If you edit any tables, you may need to restart the app.")
        
        while True:
            query_input = input("Command: ")
            
            if query_input == 'exit':
                break

            elif query_input == 'reset':
                DB.Operations.reset()
                tables.create_tables()

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
                Print.red("This command is not valid.")

    def data():
        Print.bold("You have entered the debug area for the data.")
        print("Data: foods, symptomsAvailable, symptomTimes")
        print("Enter the name of the data you want to change before anything else.")
        print("Type add followed by the number of how much dummy data you want to add.")
        print("Type 'remove' to remove all dummy data from that data.")
        print("Type 'remove all' to remove all dummy data.")
        print("Type 'exit' to exit.")

        availableDatapoints = ['foods', 'symptomsAvailable', 'symptomTimes']

        while True:
            data_input = input("Command: ").split(' ')
            datapoint_input = data_input[0]
            command1_input = data_input[1] if index_exists(data_input, 1) else ''
            command2_input = data_input[2] if index_exists(data_input, 2) else ''

            if datapoint_input == 'exit':
                break

            data_obj = ''
            if datapoint_input not in availableDatapoints:
                Print.red("You did not enter a coorect datapoint.")
                continue
            else:
                data_obj = globals()[datapoint_input]

            if command1_input == 'add' and command2_input != '' and command2_input.isdigit:
                if not command2_input.isdigit():
                    Print.red("You did not enter a number.")
                elif int(command2_input) > 50:
                    Print.red("You can not enter more than 50 dummy data entries at once.")
                elif int(command2_input) < 0:
                    Print.red("Your value is too small.")
                else:
                    data_obj.add_dummy_data(int(command2_input))

            else:
                Print.red("You did not enter a correct value.")

