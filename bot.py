from telegram.ext import ApplicationBuilder, CommandHandler
import os

TOKEN=os.getenv("BOT_TOKEN")

async def buy(update,context): await update.message.reply_text("BUY WORKING")

app=ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("buy",buy))

app.run_polling()
