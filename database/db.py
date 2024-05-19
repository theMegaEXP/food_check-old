from init import cursor as c, conn

class DB:

    class Query:
        def query_print(query: str):
            c.execute(query)
            print(c.fetchall())
    
        def create_table(table: str, columns: list[str]):
            columns_str = ', '.join(columns)
            
            c.execute(f"CREATE TABLE IF NOT EXISTS {table} ({columns_str});")
            conn.commit()

        def drop_table(table: str):
            c.execute(f"DROP TABLE IF EXISTS {table}")
            conn.commit()

        def insert_into(table: str, columns: list, values: list):
            columns_str = ", ".join(columns)
            values_str = ", ".join([f"'{value}'" for value in values])

            c.execute(f"INSERT INTO {table} ({columns_str}) VALUES ({values_str})")
            conn.commit()

        def fetch_table(table: str):
            c.execute(f"SELECT * FROM {table};")
            return c.fetchall()
    
    class View:
        def show_tables():
            DB.Query.query_print("SELECT name FROM sqlite_master WHERE type='table';")
        

    class Operations:
        def close():
            conn.close()

        def reset():
            c.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = c.fetchall()

            for table in tables:
                table_name = table[0]
                DB.Query.drop_table(table_name)
                print(f"{table_name} deleted.")
    