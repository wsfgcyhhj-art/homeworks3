import sqlite3
from database import queries

DB_PATH = "cafe.db"


def create_table():
    """Создаёт таблицы при старте бота, если их ещё нет"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(queries.survey_table)
    cursor.execute(queries.products_table)
    conn.commit()
    conn.close()


def add_trial_lesson(name: str, age: int, phone: str):
    """Сохраняет запись анкеты на пробное занятие в базу данных"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(queries.insert_survey, (name, age, phone))
    conn.commit()
    conn.close()


def save_product(name: str, description: str, price: int, photo: str = None):
    """Сохраняет продукт в базу"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(queries.insert_product, (name, description, price, photo))
    conn.commit()
    conn.close()


def get_all_products():
    """Получает все продукты для команды /drinks"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(queries.select_all_products)
    rows = cursor.fetchall()
    conn.close()
    return rows