import os
from telegram.ext import ApplicationBuilder, CommandHandler

TOKEN = os.getenv("BOT_TOKEN")

async def buy(update, context):
await update.message.reply_text("BUY WORKING")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("buy", buy))

app.run_polling()
await update.message.reply_text("BUY WORKING")
async def buy(update, context):
  async def buy(update, context):
    await ...
    
