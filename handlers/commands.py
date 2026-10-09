from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery


from handlers.keyboards import reply_keyboard, inline_keyboard 

from database import db 

router_commands = Router()

@router_commands.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f"Привет, {message.from_user.full_name}, я твой первый бот!",
        reply_markup=reply_keyboard 
    )

@router_commands.message(Command("menu"))
async def cmd_menu(message: Message):
    await message.answer(
        "📜 Наше меню команд:\n"
        "/start - Перезапуск бота\n"
        "/menu - Показать это сообщение\n"
        "/drinks - Посмотреть напитки в меню\n"
        "/add_product - Добавить товар в базу",
        reply_markup=inline_keyboard
    )


@router_commands.message(F.text.lower() == "пока")
async def say_goodbye(message: Message):
    await message.answer("До встречи!")


@router_commands.callback_query(F.data == "about")
async def about_cafe(callback: CallbackQuery):
    await callback.message.answer("☕ Мы — самое уютное кафе в городе! Готовим лучший кофе с любовью.")
    await callback.answer()


@router_commands.message(Command("drinks"))
async def show_drinks(message: Message):
    
    try:
        products = db.get_all_products() 
    except AttributeError:
        await message.answer("Ошибка: Функция получения товаров не найдена в db.py")
        return

    if not products:
        await message.answer("Меню пока пустое 😔")
        return

    text = "☕ Наши напитки:\n\n"
    
    for product in products:
        try:
          
             text += f"🥤 <b>{product[0]}</b> - {product[2]}\n📝 {product[1]}\n\n"
        except IndexError:
             text += f"🥤 Товар из БД: {product}\n"
    
    await message.answer(text, parse_mode="HTML")