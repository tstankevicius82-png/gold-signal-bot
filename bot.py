import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def buy(update: Update, context: ContextTypes.DEFAULT_TYPE):
await update.message.reply_text("BUY WORKING")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("buy", buy))

app.run_polling()
