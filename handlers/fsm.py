from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message

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
    await state.update_data(name=message.text)
    await state.set_state(TrialLessonForm.age)
    await message.answer("Укажите ваш возраст:")


@router_fsm.message(TrialLessonForm.age)
async def process_age(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Ошибка! Возраст должен быть числом. Попробуйте еще раз:")
        return

    await state.update_data(age=int(message.text))
    await state.set_state(TrialLessonForm.phone)
    await message.answer("Введите ваш номер телефона:")


@router_fsm.message(TrialLessonForm.phone)
async def process_phone(message: Message, state: FSMContext):
    await state.update_data(phone=message.text)
    data = await state.get_data()

    await message.answer(
        "Ваша заявка принята!\n\n"
        f"Имя: {data.get('name')}\n"
        f"Возраст: {data.get('age')}\n"
        f"Телефон: {data.get('phone')}"
    )
    await state.clear()