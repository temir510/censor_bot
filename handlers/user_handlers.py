import asyncio

from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"Здравствуйте! Этот бот создан для сохранения анонимности в чатах.")


@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer("Чтобы воспользоваться ботом в личном чате, отправьте сообщение/текстовый файл, " \
        "содержащее ФИО/номер телефона/электронную почту/адрес, и бот отправит сообщение/текстовый файл, " \
        "в котором эти данные будут заменены на [PERSON]/[PHONE]/[EMAIL]/[ADDRESS] соответственно.")


@router.message(F.text)
async def censor_text(message: Message):
    await message.answer(message.text)


@router.message(F.document)
async def censor_document(message: Message):
    await message.answer(f"Файл: {message.document.file_name}")
