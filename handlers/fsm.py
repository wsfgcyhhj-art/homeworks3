from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message
from database import db

router_fsm = Router()


class AddProductForm(StatesGroup):
    name = State()  
    description = State()
    price = State()


@router_fsm.message(Command("add_product"))
async def start_add_product(message: Message, state: FSMContext):
    await state.set_state(AddProductForm.name)
    await message.answer("Введите название напитка:")


@router_fsm.message(AddProductForm.name)
async def process_name(message: Message, state: FSMContext):
  
    if not message.text:
        await message.answer(
            "⚠️ Название должно быть текстом (не фото и не стикер)! Попробуйте еще раз:"
        )
        return

    await state.update_data(name=message.text)
    await state.set_state(AddProductForm.description)
    await message.answer("Введите описание напитка:")


@router_fsm.message(AddProductForm.description)
async def process_description(message: Message, state: FSMContext):
    if not message.text:
        await message.answer("⚠️ Описание должно быть текстом! Попробуйте еще раз:")
        return

    await state.update_data(description=message.text)
    await state.set_state(AddProductForm.price)
    await message.answer("Введите цену напитка:")


@router_fsm.message(AddProductForm.price)
async def process_price(message: Message, state: FSMContext):
    if not message.text:
        await message.answer("⚠️ Цена должна быть текстом! Попробуйте еще раз:")
        return

    await state.update_data(price=message.text)
    data = await state.get_data()

 
    db.add_product(data["name"], data["description"], data["price"])

    await message.answer(
        f"✅ Напиток «{data['name']}» успешно добавлен в меню!"
    )
    await state.clear()