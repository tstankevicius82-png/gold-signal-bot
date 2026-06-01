```python
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def buy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🟢 BUY SIGNAL WORKING")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("buy", buy))

print("BOT STARTED")

app.run_polling()
```
