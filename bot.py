
import contextlib
import asyncio

from aiogram.types import ChatJoinRequest, Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram import Bot, Dispatcher, F
import logging

from aiogram.filters import Command

TOKEN = "7224024850:AAFcX5b6XNdiKSmSZqH-lw2r0ecGGnJNjOw"
CHANNEL_ID = -1002207462735
ADMIN_ID = 383100244

bot = Bot(TOKEN)   
dp = Dispatcher()

def keyboard():
    builder = ReplyKeyboardBuilder()
    builder.button(text="СТАРТ")
    return builder.as_markup(resize_keyboard=True)

async def approve_request(chat_join: ChatJoinRequest, bot: Bot): 
    msg = "Добро пожаловать!"
    await bot.send_message(chat_id=chat_join.from_user.id, text=msg, reply_markup=keyboard())
    await chat_join.approve()

# @dp.message(Command("start"))
# async def read_start(message:Message) -> None:
#    await message.answer("Привіт! Виберіть опцію:", reply_markup=keyboard())

@dp.message(F.text.lower() == "старт")
async def func(message: Message):
       await message.answer("Дякую ви натиснули на кнопку")

async def start():
    logging.basicConfig(level=logging.DEBUG, 
                        format="%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")

             
    dp.chat_join_request.register(approve_request, F.chat.id==CHANNEL_ID)
    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    except Exception as ex:
        logging.error(f"[Exception] - {ex}", exc_info=True)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    with contextlib.suppress(KeyboardInterrupt, SystemExit):
        asyncio.run(start())