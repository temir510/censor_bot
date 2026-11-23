import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

# Токен выдаёт @BotFather. Лучше хранить его в переменной окружения BOT_TOKEN.
TOKEN = os.getenv("BOT_TOKEN", "ВСТАВЬТЕ_ТОКЕН")

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"Здравствуйте! Этот бот создан для сохранения анонимности в чатах.")


@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer("Чтобы воспользоваться ботом в личном чате, отправьте сообщение/текстовый файл, " \
        "содержащее ФИО/номер телефона/электронную почту/адрес, и бот отправит сообщение/текстовый файл, " \
        "в котором эти данные будут заменены на [PERSON]/[PHONE]/[EMAIL]/[ADDRESS] соответственно.")


@router.message(F.document)
async def on_document(message: Message):
    await message.answer(f"Файл: {message.document.file_name}")


if __name__ == "__main__":
    asyncio.run(main())
