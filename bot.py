import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

TOKEN = '6974689443:AAEpC2IWegBtPlDfuPMvmziEcqML2I2Jm9o'
#диспетчер
dp = Dispatcher()
#обработка команды старт
@dp.message(CommandStart())
async def echo(message: Message):
  await message.reply('Привет! Я бот, распознающий овощи и фрукты')

# обработка команды help
@dp.message(F.text, Command("test"))
async def echo(message: Message):
  await message.reply('Просто отправьте мне изображение, которое содержит овощ или фрукт')

async def main() -> None:
  # Initialize Bot instance with default bot properties which will be passed to all API calls
  bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
  # And the run events dispatching
  await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())