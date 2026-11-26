import asyncio
import logging
import os

from aiogram import Bot, Dispatcher

from handlers.user_handlers import router


TOKEN = os.getenv("BOT_TOKEN", "ВСТАВЬТЕ_ТОКЕН")
bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
    dp.include_router(router)
    
    await bot.delete_webhook(drop_pending_updates=True)
    
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())

    except KeyboardInterrupt:
        print("Бот остановлен пользователем.")

    except Exception as e:
        print(f"Произошла ошибка: {e}")
