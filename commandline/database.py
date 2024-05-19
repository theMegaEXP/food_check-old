from database.init import cursor as c, conn

def run_db_query():
    while True:
        query_input = input()
        
        if query_input == 'exit':
            break
        
        try:
            c.execute(query_input)
            print(c.fetchall())
        except ValueError:
            print(ValueError)

        