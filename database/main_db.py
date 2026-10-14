import aiosqlite
from database import queries

DB_PATH = "cafe.db"

# =====================================================================
# СТАРЫЙ КОД (sqlite3) — закомментирован для сравнения
# =====================================================================
# import sqlite3
#
# def create_table():
#     """Создаёт таблицы при старте бота, если их ещё нет"""
#     conn = sqlite3.connect(DB_PATH)
#     cursor = conn.cursor()
#     cursor.execute(queries.survey_table)
#     cursor.execute(queries.products_table)
#     conn.commit()
#     conn.close()
#
# def add_trial_lesson(name: str, age: int, phone: str):
#     """Сохраняет запись анкеты на пробное занятие в базу данных"""
#     conn = sqlite3.connect(DB_PATH)
#     cursor = conn.cursor()
#     cursor.execute(queries.insert_survey, (name, age, phone))
#     conn.commit()
#     conn.close()
#
# def save_product(name: str, description: str, price: int, photo: str = None):
#     """Сохраняет продукт в базу"""
#     conn = sqlite3.connect(DB_PATH)
#     cursor = conn.cursor()
#     cursor.execute(queries.insert_product, (name, description, price, photo))
#     conn.commit()
#     conn.close()
#
# def get_all_products():
#     """Получает все продукты для команды /drinks"""
#     conn = sqlite3.connect(DB_PATH)
#     cursor = conn.cursor()
#     cursor.execute(queries.select_all_products)
#     rows = cursor.fetchall()
#     conn.close()
#     return rows
# =====================================================================


# =====================================================================
# НОВЫЙ КОД (aiosqlite)
# =====================================================================

async def create_table():
    """Создаёт таблицы при старте бота (обе таблицы анкеты и продукты)"""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(queries.survey_table)
        await db.execute(queries.lesson_details_table)
        await db.execute(queries.products_table)
        await db.commit()


async def add_trial_lesson(lesson_id: str, name: str, age: int, phone: str):
    """Сохраняет запись анкеты в первую таблицу (trial_lessons)"""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(queries.insert_survey, (lesson_id, name, age, phone))
        await db.commit()


async def add_lesson_details(lesson_id: str, direction: str, study_format: str):
    """Сохраняет дополнительную информацию анкеты во вторую таблицу (lesson_details)"""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(queries.insert_lesson_details, (lesson_id, direction, study_format))
        await db.commit()


async def get_all_lessons_with_details():
    """Получает данные сразу из двух таблиц одним запросом через INNER JOIN"""
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute(queries.select_all_lessons_with_details)
        rows = await cursor.fetchall()
        return rows


async def save_product(name: str, description: str, price: int, photo: str = None):
    """Сохраняет продукт в базу через aiosqlite"""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(queries.insert_product, (name, description, price, photo))
        await db.commit()


async def get_all_products():
    """Получает все продукты для команды /drinks через aiosqlite"""
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute(queries.select_all_products)
        rows = await cursor.fetchall()
        return rows