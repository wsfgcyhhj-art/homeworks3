import sqlite3
from darabase import queries

path_db = "database/sqlite.db"

def init_db():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.products_table)
    print("DB connect.")
    conn.commit()
    conn.close()

def add_product_db(name, description, price, photo):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.insert_product, (name, description, price, photo))
    conn.commit()
    conn.close()