from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message


from database import db

router_fsm = Router()

class Add_product(StatesGroup):
    name = State()
    description = State()
    price = State()

@router_fsm.message(Command("add_product"))
async def add_product(message: Message, state: FSMContext):
    await message.answer("Введите название напитка:")
    await state.set_state(Add_product.name)


@router_fsm.message(Add_product.name)
async def add_product_name(message: Message, state: FSMContext):

    if not message.text:
        await message.answer("⚠️ Пожалуйста, введите название ТЕКСТОМ. Попробуйте еще раз:")
        return 

    await state.update_data(name=message.text)
    await message.answer("Введите описание напитка:")
    await state.set_state(Add_product.description)

@router_fsm.message(Add_product.description)
async def add_product_description(message: Message, state: FSMContext):
    if not message.text:
        await message.answer("⚠️ Описание должно быть ТЕКСТОМ. Попробуйте еще раз:")
        return

    await state.update_data(description=message.text)
    await message.answer("Введите цену напитка:")
    await state.set_state(Add_product.price)

@router_fsm.message(Add_product.price)
async def add_product_price(message: Message, state: FSMContext):
    if not message.text:
        await message.answer("⚠️ Цена должна быть ТЕКСТОМ. Попробуйте еще раз:")
        return

    await state.update_data(price=message.text)
    data = await state.get_data()

  
    try:
    
        db.add_product(data['name'], data['description'], data['price'])
    except AttributeError:
        print("Ошибка: Функция add_product не найдена в db.py")

    await message.answer(
        "✅ Напиток успешно добавлен!\n"
        f"Название: {data.get('name')}\n"
        f"Описание: {data.get('description')}\n"
        f"Цена: {data.get('price')}"
    )
    await state.clear()