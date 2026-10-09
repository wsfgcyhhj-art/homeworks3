from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
from database import db
from handlers.keyboards import inline_keyboard, reply_keyboard

router_commands = Router()





@router_commands.message(Command("drinks"))
async def show_drinks(message: Message):
    products = db.get_all_products()

  
    if not products:
        await message.answer("Меню пока пустое")
        return

    text = "☕ Наше меню напитков:\n\n"
    for name, desc, price in products:
        text += f"🥤 <b>{name}</b> — {price}\n📝 {desc}\n\n"

    await message.answer(text, parse_mode="HTML")