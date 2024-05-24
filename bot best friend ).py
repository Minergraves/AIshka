import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

TOKEN = '6554705021:AAFDOrIAl1559jZ3lKmvnRVdbqquZr2Jcnc'
#диспетчер
dp = Dispatcher()
#обработка команды старт
@dp.message(CommandStart())
async def echo(message: Message):
  await message.reply('Привет! Я ботик, который всегда может выслушать и дать совет. Расскажи мне о своей проблеме и я дам тебе решение :3')

@dp.message(F.text)
async def handle_message(message: Message):
  await message.reply('Иди нахуй')

# обработка команды help
@dp.message(F.text, Command("/help"))
async def echo(message: Message):
  await message.reply('Просто скажи мне свою проблему и я дам решение')

async def main() -> None:
  # Initialize Bot instance with default bot properties which will be passed to all API calls
  bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
  # And the run events dispatching
  await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())