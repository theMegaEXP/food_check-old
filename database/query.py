from database.init import cursor as c

class Query:
    def create_table(table: str, columns: list[str]):
        columns_str = ', '.join(columns)
        
        c.execute(f"CREATE TABLE IF NOT EXISTS {table} ({columns_str})")