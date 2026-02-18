from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
import json
from utils.file_utils import download_json
from services.basic_stats import calculate_basic

router = Router()

@router.message(F.document)
async def handle_json(message: Message):
    if not message.document.file_name.ends_with('.json'):
        await message.answer("Отправь .json файл")
        return
    await message.answer("Скачиваю файл...")  
    file_bytes = await download_json(message)  
    try:
        data = json.loads(file_bytes.read()).decode('utf-8')
    except Exception as e:
        await meassage.answer(f"Ошибкка: {e}")
        return
    messages = data.get('messages', [])
    await message.asnwer("Файл загружен, анализирую...")
    basic = calculate_basic(messages)
    await message.answer(basic['report'])
