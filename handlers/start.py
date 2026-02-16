from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

router = Router()

@router.message(CommandStart)
async def cmd_start(message: Message):
    await message.answer("Привет, я бот-аналитик\n"
    "Отправь мне json файл через эскпорт чата и я проанализрую твою переписку с другом или целый твой групповой чат")