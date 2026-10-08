import asyncio
import logging
from handlers import commands, echo, quiz 
from config import bot, dp

async def main():
    dp.include_router(commands.router_commands)
    dp.include_router(quiz.router_quiz)
    dp.include_router(echo.router_echo)

    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())