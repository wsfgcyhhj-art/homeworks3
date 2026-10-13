import asyncio
import logging

from config import bot, dp
from database import main_db
from handlers import commands, echo, fsm, quiz


async def on_startup():
    main_db.create_table()


async def main():
    # Регистрация функции при старте бота
    dp.startup.register(on_startup)

    # Регистрация роутеров
    dp.include_router(commands.router_commands)
    dp.include_router(quiz.router_quiz)
    dp.include_router(fsm.router_fsm)
    dp.include_router(echo.router_echo)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())