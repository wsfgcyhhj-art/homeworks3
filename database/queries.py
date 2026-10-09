products_table = """
CREATE TABLE IF NOT EXISTS products (
    id integer PRIMARY KEY AUTOINCREMENT
    name TEXT NOT NULL,
    description TEXT,
    price INTEGER,
    photo TEXT
)
"""

insert_product = "
INSERT INTO products (name, description, price, photo)
VALUES (?, ?, ?, ?)
"
