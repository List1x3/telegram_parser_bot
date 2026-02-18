import os
import uuid
from aiogram.types import Message
from config import IMAGES_DIR

async def download_json(message: Message) -> bytes:
    file = await message.bot.get_file(message.document.file_id)
    file_bytes = await message.bot.download_file(file.file_path)
    return file_bytes.read()

async def generate_image_path():
    pass
