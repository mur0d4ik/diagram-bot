import asyncio
from aiogram import Bot, Dispatcher
from handlers import bot_message, user_message

# Запуск бота
async def main():
    bot = Bot(token="token")
    dp = Dispatcher()

    dp.include_routers(
        user_message.router,
        bot_message.router
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

print('Бот запустился!')

if __name__ == "__main__":

    asyncio.run(main())
