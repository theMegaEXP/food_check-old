from init import cursor as c, conn

class Query:
    def query(query: str):
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

    