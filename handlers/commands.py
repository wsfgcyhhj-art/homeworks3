from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from database import main_db
from handlers.keyboards import inline_keyboard, reply_keyboard

router_commands = Router()


@router_commands.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f"Привет, {message.from_user.full_name}, я твой бот!\n"
        "Используй /form для записи на пробное занятие или /lessons для просмотра всех заявок.",
        reply_markup=reply_keyboard,
    )


@router_commands.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        "📌 <b>Список доступных команд:</b>\n"
        "/start - приветствие\n"
        "/help - список команд\n"
        "/form - анкета (запись на пробное занятие)\n"
        "/lessons - список заявок (чтение через INNER JOIN)\n"
        "/drinks - меню напитков",
        reply_markup=inline_keyboard,
        parse_mode="HTML",
    )


@router_commands.message(F.text == "Контакты")
async def show_contacts(message: Message):
    await message.answer(
        "📍 Наш адрес: г. Бишкек, ул. Киевская, 1\n"
        "📞 Телефон: +996 555 123 456"
    )


@router_commands.message(F.text == "Каталог")
async def show_catalog(message: Message):
    await message.answer(
        "🛒 Наш каталог:\n\n"
        "1. Ноутбук ASUS - 80 000 сом\n"
        "2. Смартфон iPhone 15 - 100 000 сом\n"
        "3. Наушники AirPods - 15 000 сом"
    )


@router_commands.message(F.text.lower() == "группа")
async def cmd_group(message: Message):
    await message.answer("Твоя группа 70-2")


# Команда со списком: достаёт данные сразу из двух таблиц одним запросом с INNER JOIN
@router_commands.message(Command("lessons", "list", "records"))
async def show_lessons(message: Message):
    records = await main_db.get_all_lessons_with_details()

    if not records:
        await message.answer("Список записей на пробные занятия пока пуст.\nЗаполните анкету с помощью /form")
        return

    # Бот присылает всё вместе одним сообщением на каждую запись
    for lesson_id, name, age, phone, direction, study_format in records:
        text = (
            f"🎫 <b>Заявка №{lesson_id}</b>\n"
            f"👤 <b>Имя:</b> {name}\n"
            f"🎂 <b>Возраст:</b> {age}\n"
            f"📞 <b>Телефон:</b> {phone}\n"
            f"💻 <b>Направление:</b> {direction}\n"
            f"🏫 <b>Формат обучения:</b> {study_format}"
        )
        await message.answer(text, parse_mode="HTML")


@router_commands.message(Command("drinks"))
async def show_drinks(message: Message):
    products = await main_db.get_all_products()

    if not products:
        await message.answer("Меню пока пустое.")
        return

    for name, desc, price, photo in products:
        text = f"🥤 <b>{name}</b> — {price} сом\n📝 {desc}"
        await message.answer(text, parse_mode="HTML")
