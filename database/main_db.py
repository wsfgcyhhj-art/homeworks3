import sqlite3
from database import queries


def create_table():
    """Создаёт таблицу при старте бота"""
    conn = sqlite3.connect("cafe.db")
    cursor = conn.cursor()
    cursor.execute(queries.products_table)
    conn.commit()
    conn.close()


def save_product(name, description, price, photo=None):
    """Сохраняет продукт в базу"""
    conn = sqlite3.connect("cafe.db")
    cursor = conn.cursor()
    cursor.execute(queries.insert_product, (name, description, price, photo))
    conn.commit()
    conn.close()


def get_all_products():
    """Получает все продукты для команды /drinks"""
    conn = sqlite3.connect("cafe.db")
    cursor = conn.cursor()
    cursor.execute(queries.select_all_products)
    rows = cursor.fetchall()
    conn.close()
    return rows