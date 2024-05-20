import asyncio
import logging
import os
import sys
from os import getenv
from pathlib import Path

import requests
from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, FSInputFile
from dotenv import load_dotenv

import info
import keyboards
from config import data_path, cv_path, cv_url
from service import get_repo_by_name

load_dotenv()
# Bot token can be obtained via https://t.me/BotFather
TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()


def get_or_download_cv():
    Path(data_path).mkdir(parents=True, exist_ok=True)
    if not os.path.isfile(cv_path):
        response = requests.get(cv_url, allow_redirects=True)
        open(cv_path, "wb").write(response.content)

    return cv_path


@dp.message(CommandStart())
@dp.callback_query(F.data == "start")
async def command_start_handler(message_or_callback: Message | CallbackQuery) -> None:
    text = f"Welcome to Botfolio, %s\\!" % message_or_callback.from_user.first_name  # noqa
    if isinstance(message_or_callback, CallbackQuery):
        message_or_callback: CallbackQuery
        if message_or_callback.message.text:
            await message_or_callback.message.edit_text(text,
                                                        reply_markup=keyboards.HELLO)
        else:
            await message_or_callback.message.delete()
            await message_or_callback.message.answer(text,
                                                     reply_markup=keyboards.HELLO)
    else:
        message_or_callback: Message
        await message_or_callback.answer(text, reply_markup=keyboards.HELLO, show_alert=False)


@dp.callback_query(F.data == "about")
async def about(callback: CallbackQuery) -> None:
    await callback.message.edit_text(info.ABOUT, reply_markup=keyboards.BACK)


@dp.callback_query(F.data == "skills")
async def skills(callback: CallbackQuery) -> None:
    await callback.message.edit_text(text=info.SKILLS, reply_markup=keyboards.BACK)


@dp.callback_query(F.data.startswith("resume"))
async def resume(callback: CallbackQuery) -> None:
    if callback.data == "resume_pdf":
        file_path = os.path.join(get_or_download_cv())
        await callback.message.answer_document(FSInputFile(file_path), reply_markup=keyboards.BACK)
        await callback.message.delete()
    else:
        await callback.message.edit_text(info.RESUME, reply_markup=keyboards.RESUME)


@dp.callback_query(F.data == "projects")
async def projects(callback: CallbackQuery) -> None:
    await callback.message.edit_text(info.PROJECTS, reply_markup=keyboards.REPOSITORIES)


@dp.callback_query(F.data.startswith("repo_"))
async def repo(callback: CallbackQuery) -> None:
    repo_name = callback.data.split("_")[1]
    repo = get_repo_by_name(repo_name)
    await callback.message.edit_text(text=repo.get_repo_info(), parse_mode=ParseMode.HTML,
                                     reply_markup=keyboards.REPOSITORY)


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN_V2))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
