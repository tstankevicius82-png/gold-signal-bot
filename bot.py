import os
from telegram.ext import ApplicationBuilder, CommandHandler

TOKEN = os.getenv("BOT_TOKEN")

async def buy(update, context):
message = "BUY WORKING"
await update.message.reply_text(message)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("buy", buy))

print("BOT RUNNING")

app.run_polling()
async def buy(update, context):   
      message = "BUY WORKING"
      await update.message.reply_text(message)
  
