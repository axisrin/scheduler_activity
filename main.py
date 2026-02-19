import asyncio
from os import getenv
from app.config import BOT_TOKEN, TZ, DB_PATH, REDIS_URL

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

dp = Dispatcher()

# Обрабатываем начальное сообщение.
@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.answer("Привет, это чат бот который поможет тебе не забывать свои дела!")

# Запуск бота
async def main() -> None:
    bot = Bot(BOT_TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    