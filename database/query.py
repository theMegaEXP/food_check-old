from init import cursor as c, conn

class Query:
    def query(query: str):
        c.execute(query)
        print(c.fetchall())
   
    def create_table(table: str, columns: list[str]):
        columns_str = ', '.join(columns)
        
        c.execute(f"CREATE TABLE IF NOT EXISTS {table} ({columns_str});")
        conn.commit()

    def show_table(table: str):
        c.execute(f"SELECT * FROM {table};")

    