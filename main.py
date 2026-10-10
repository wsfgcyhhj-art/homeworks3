import asyncio
import logging
<<<<<<< Updated upstream
from handlers import commands, echo, quiz 
from config import bot, dp

async def main():
    dp.include_router(commands.router_commands)
    dp.include_router(quiz.router_quiz)
    dp.include_router(echo.router_echo)

=======
import sys
from aiogram import Bot, Dispatcher


from handlers import fsm  # роутер анкеты


async def main():
  
    bot = Bot(token="8905040488:AAFTgHYiSLgR7JEp9AjatLgurzd29vZ56mg")
    dp = Dispatcher()

    dp.include_router(fsm.router)

    
>>>>>>> Stashed changes
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())