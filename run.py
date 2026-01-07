import asyncio

import logging

from aiogram import Bot, Dispatcher, F

from aiogram.filters import CommandStart, Command

from aiogram.types import Message

from config import TOKEN

bot = Bot(token=TOKEN)

dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):

    await message.answer("What's up, bro?")

@dp.message(Command("help"))
async def cmd_help(message: Message):
    
    await message.reply("Telegramdan murojaat qilish uchun: @aabbdullayeevv")

@dp.message(Command("about"))
async def cmd_about(message: Message):
    await message.reply("Bu bot @aabbdullayeevv tomonidan yaratilgan.")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    
    logging.basicConfig(level=logging.INFO)
    
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot to'xtatildi.")