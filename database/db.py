import sqlite3


def init_db():
    conn = sqlite3.connect("cafe.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            description TEXT,
            price TEXT
        )
    """)
    conn.commit()
    conn.close()


def add_product(name, description, price):
    conn = sqlite3.connect("cafe.db")
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO products (name, description, price) VALUES (?, ?, ?)",
        (name, description, price),
    )
    conn.commit()
    conn.close()


def get_all_products():
    conn = sqlite3.connect("cafe.db")
    cur = conn.cursor()
    cur.execute("SELECT name, description, price FROM products")
    rows = cur.fetchall()
    conn.close()
    return rows