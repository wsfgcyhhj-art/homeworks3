# Таблица 1: Основная информация о записи на пробное занятие
survey_table = """
CREATE TABLE IF NOT EXISTS trial_lessons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    lesson_id TEXT NOT NULL,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    phone TEXT NOT NULL
);
"""

# Вставка данных в первую таблицу
insert_survey = """
INSERT INTO trial_lessons (lesson_id, name, age, phone)
VALUES (?, ?, ?, ?);
"""

# Таблица 2: Дополнительная информация по теме (направление и формат обучения)
lesson_details_table = """
CREATE TABLE IF NOT EXISTS lesson_details (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    lesson_id TEXT NOT NULL,
    direction TEXT NOT NULL,
    study_format TEXT NOT NULL
);
"""

# Вставка данных во вторую таблицу
insert_lesson_details = """
INSERT INTO lesson_details (lesson_id, direction, study_format)
VALUES (?, ?, ?);
"""

# Запрос на выборку данных из двух таблиц через INNER JOIN по общему полю lesson_id
select_all_lessons_with_details = """
SELECT 
    trial_lessons.lesson_id,
    trial_lessons.name,
    trial_lessons.age,
    trial_lessons.phone,
    lesson_details.direction,
    lesson_details.study_format
FROM trial_lessons
INNER JOIN lesson_details ON trial_lessons.lesson_id = lesson_details.lesson_id;
"""

# Таблица продуктов (из прошлых уроков)
products_table = """
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    price INTEGER,
    photo TEXT
);
"""

insert_product = """
INSERT INTO products (name, description, price, photo)
VALUES (?, ?, ?, ?);
"""

select_all_products = """
SELECT name, description, price, photo FROM products;
"""