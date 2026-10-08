from aiogram import F, Router
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

router_quiz = Router()

@router_quiz.callback_query(F.data == "quiz_start")
async def start_quiz(callback: CallbackQuery):
    answers_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Берлин", callback_data="answer_wrong")],
        [InlineKeyboardButton(text="Лондон", callback_data="answer_correct")],
        [InlineKeyboardButton(text="Париж", callback_data="answer_wrong")]
    ])

    await callback.message.answer("Вопрос: Назовите столицу Великобритании?", reply_markup=answers_kb)
    await callback.answer() 

@router_quiz.callback_query(F.data == "answer_correct")
async def correct_answer(callback: CallbackQuery):
    await callback.message.answer("Верно! 🎉")
    await callback.answer()

@router_quiz.callback_query(F.data == "answer_wrong")
async def wrong_answer(callback: CallbackQuery):
    await callback.message.answer("Неверно ❌ Правильный ответ: Лондон.")
    await callback.answer()