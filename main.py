import commandline.terminal_loop as terminal_loop
import database.tables as tables
from database.db import DB


def main():
    DB.Operations.reset()
    tables.create_tables()
    DB.View.show_tables()
    terminal_loop.start()
    

if __name__ == "__main__":
    main()