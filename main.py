import asyncio
import logging

from aiogram import Dispatcher

from app import for_work, general, send_request, manuals, offers, support, admin_conf, familiarization, payments, newsletter, admin_conf_branches, branches, profil, wallet, admin_conf_urls, req_urls

from config import bot


async def start():
    # Настройка логгера для записи в файл
    # logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    dp = Dispatcher()

    dp.include_routers(
        general.router,
        send_request.router,
        manuals.router,
        for_work.router,
        support.router,
        offers.router,
        admin_conf.router,
        familiarization.router,
        newsletter.router,
        branches.router,
        admin_conf_branches.router,
        payments.router,
        profil.router,
        wallet.router,
        admin_conf_urls.router,
        req_urls.router,
    )

    logging.basicConfig(level=logging.INFO)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(start())
