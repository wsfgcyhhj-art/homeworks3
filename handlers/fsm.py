<<<<<<< Updated upstream
=======
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message

router = Router()

class TrialLessonForm(StatesGroup):
    name = State()
    age = State()
    phone = State()

@router.message(F.text == "/form")
async def cmd_form(message: Message, state: FSMContext):
    await state.set_state(TrialLessonForm.name)
    await message.answer("Добро пожаловать на запись! Введите ваше имя:")

@router.message(TrialLessonForm.name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(TrialLessonForm.age)
    await message.answer("Сколько вам лет? (Введите число)")

@router.message(TrialLessonForm.age)
async def process_age(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("⚠️ Возраст должен быть числом! Пожалуйста, введите возраст цифрами:")
        return
    
    await state.update_data(age=int(message.text))
    await state.set_state(TrialLessonForm.phone)
    await message.answer("Введите ваш номер телефона:")

@router.message(TrialLessonForm.phone)
async def process_phone(message: Message, state: FSMContext):
    await state.update_data(phone=message.text)
    data = await state.get_data()
    await state.clear()
    
    await message.answer(
        "✅ **Вы успешно записаны! Ваши данные:**\n\n"
        f"👤 Имя: {data.get('name')}\n"
        f"🎂 Возраст: {data.get('age')}\n"
        f"📞 Телефон: {data.get('phone')}"
    )
>>>>>>> Stashed changes
