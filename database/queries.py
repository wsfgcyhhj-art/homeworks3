survey_table = """
CREATE TABLE IF NOT EXISTS trial_lessons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    phone TEXT NOT NULL
)
"""

insert_survey = """
INSERT INTO trial_lessons (name, age, phone)
VALUES (?, ?, ?)
"""

products_table = """
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    price INTEGER,
    photo TEXT
)
"""

insert_product = """
INSERT INTO products (name, description, price, photo)
VALUES (?, ?, ?, ?)
"""

select_all_products = """
SELECT name, description, price, photo FROM products
"""