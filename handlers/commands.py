from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from handlers.keyboards import reply_keyboard, inline_keyboard 

router_commands = Router()

@router_commands.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f"Привет, {message.from_user.full_name}, я твой первый бот!",
        reply_markup=reply_keyboard 
    )

@router_commands.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        "/start - приветствие\n"
        "/help - список команд",
        reply_markup=inline_keyboard
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