import random

from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message

from database import main_db
from handlers.keyboards import direction_keyboard, format_keyboard, reply_keyboard

router_fsm = Router()


class TrialLessonForm(StatesGroup):
    name = State()          # 1 таблица: Имя
    age = State()           # 1 таблица: Возраст
    phone = State()         # 1 таблица: Телефон
    direction = State()     # 2 таблица: Направление
    study_format = State()  # 2 таблица: Формат обучения


@router_fsm.message(Command("form"))
async def start_form(message: Message, state: FSMContext):
    await state.set_state(TrialLessonForm.name)
    await message.answer("Здравствуйте! Начнем запись на пробное занятие.\nВведите ваше имя:")


@router_fsm.message(TrialLessonForm.name)
async def process_name(message: Message, state: FSMContext):
    if not message.text or message.text.startswith("/"):
        await message.answer("⚠️ Пожалуйста, введите корректное имя текстом:")
        return

    await state.update_data(name=message.text)
    await state.set_state(TrialLessonForm.age)
    await message.answer("Укажите ваш возраст (числом):")


@router_fsm.message(TrialLessonForm.age)
async def process_age(message: Message, state: FSMContext):
    if not message.text or not message.text.isdigit():
        await message.answer("⚠️ Возраст должен быть числом! Пожалуйста, введите ваш возраст цифрами:")
        return

    age = int(message.text)
    if age <= 0 or age > 120:
        await message.answer("⚠️ Пожалуйста, укажите реальный возраст:")
        return

    await state.update_data(age=age)
    await state.set_state(TrialLessonForm.phone)
    await message.answer("Введите ваш номер телефона:")


@router_fsm.message(TrialLessonForm.phone)
async def process_phone(message: Message, state: FSMContext):
    if not message.text or message.text.startswith("/"):
        await message.answer("⚠️ Пожалуйста, введите номер телефона:")
        return

    await state.update_data(phone=message.text)
    await state.set_state(TrialLessonForm.direction)
    await message.answer(
        "Выберите или напишите желаемое направление обучения:",
        reply_markup=direction_keyboard
    )


@router_fsm.message(TrialLessonForm.direction)
async def process_direction(message: Message, state: FSMContext):
    if not message.text or message.text.startswith("/"):
        await message.answer("⚠️ Пожалуйста, выберите направление обучения:")
        return

    await state.update_data(direction=message.text)
    await state.set_state(TrialLessonForm.study_format)
    await message.answer(
        "Выберите удобный формат обучения:",
        reply_markup=format_keyboard
    )


@router_fsm.message(TrialLessonForm.study_format)
async def process_study_format(message: Message, state: FSMContext):
    if not message.text or message.text.startswith("/"):
        await message.answer("⚠️ Пожалуйста, выберите формат обучения:")
        return

    await state.update_data(study_format=message.text)
    data = await state.get_data()

    # Генерируем общее поле (lesson_id) для связывания обеих таблиц
    lesson_id = f"TL-{random.randint(1000, 9999)}"

    # Вызываем две функции - по одной на каждую таблицу
    # 1. Сохраняем в первую таблицу (trial_lessons)
    await main_db.add_trial_lesson(
        lesson_id=lesson_id,
        name=data["name"],
        age=data["age"],
        phone=data["phone"]
    )

    # 2. Сохраняем во вторую таблицу (lesson_details)
    await main_db.add_lesson_details(
        lesson_id=lesson_id,
        direction=data["direction"],
        study_format=data["study_format"]
    )

    await message.answer(
        "✅ <b>Заявка успешно сохранена в обе таблицы базы данных!</b>\n\n"
        f"🎫 <b>Номер заявки (общий ID):</b> {lesson_id}\n"
        f"👤 <b>Имя:</b> {data['name']}\n"
        f"🎂 <b>Возраст:</b> {data['age']}\n"
        f"📞 <b>Телефон:</b> {data['phone']}\n"
        f"💻 <b>Направление:</b> {data['direction']}\n"
        f"🏫 <b>Формат:</b> {data['study_format']}\n\n"
        "Для просмотра всех записей через INNER JOIN используйте команду /lessons",
        parse_mode="HTML",
        reply_markup=reply_keyboard
    )
    await state.clear()
