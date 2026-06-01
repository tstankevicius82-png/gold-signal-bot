import os
from telegram.ext import Updater,CommandHandler
TOKEN=os.getenv("BOT_TOKEN")
def buy(update,context): update.message.reply_text("BUY WORKING")
updater=Updater(TOKEN,use_context=True)
dp=updater.dispatcher
dp.add_handler(CommandHandler("buy",buy))
updater.start_polling()
updater.idle()
