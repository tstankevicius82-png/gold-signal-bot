```python
import os
from telegram.ext import ApplicationBuilder, CommandHandler

TOKEN = os.getenv("BOT_TOKEN")

async def buy(update, context):
    await update.message.reply_text("🟢 BUY SIGNAL WORKING")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("buy", buy))

print("BOT RUNNING")

app.run_polling()
```
 
