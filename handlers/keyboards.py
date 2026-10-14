from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)


reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="/form"), KeyboardButton(text="/lessons")],
        [KeyboardButton(text="/drinks"), KeyboardButton(text="Контакты")],
        [KeyboardButton(text="Каталог"), KeyboardButton(text="Корзина")],
    ],
    resize_keyboard=True
)

direction_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Python"), KeyboardButton(text="Frontend")],
        [KeyboardButton(text="UX/UI Design"), KeyboardButton(text="QA Testing")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

format_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Офлайн"), KeyboardButton(text="Онлайн")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Наш сайт", url="https://geeks.kg")],
        [InlineKeyboardButton(text="Наш Telegram-канал", url="https://t.me/telegram")],
        [InlineKeyboardButton(text="Начать игру", callback_data="quiz_start")],
        [InlineKeyboardButton(text="О нас", callback_data="about")],
    ]
)