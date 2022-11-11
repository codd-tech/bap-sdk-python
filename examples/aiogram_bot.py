"""
This is a echo bot.
It echoes any incoming text messages.
"""

from aiogram import Bot, Dispatcher, executor, types

import bap

BOT_TOKEN = ''
AD_PROVIDER_TOKEN = ''

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
dp.setup_middleware(bap.BapMiddleware(AD_PROVIDER_TOKEN))


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
