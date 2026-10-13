from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message

from database import main_db

router_fsm = Router()


class TrialLessonForm(StatesGroup):
    name = State()
    age = State()
    phone = State()


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
    data = await state.get_data()

    # Сохраняем анкету в базу данных
    main_db.add_trial_lesson(
        name=data["name"],
        age=data["age"],
        phone=data["phone"]
    )

    await message.answer(
        "✅ <b>Заявка успешно принята и сохранена в базу данных!</b>\n\n"
        f"👤 Имя: {data['name']}\n"
        f"🎂 Возраст: {data['age']}\n"
        f"📞 Телефон: {data['phone']}",
        parse_mode="HTML"
    )
    await state.clear()
