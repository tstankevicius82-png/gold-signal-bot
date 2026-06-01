from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "PASTE_YOUR_BOT_TOKEN"

async def buy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 GOLD SIGNAL\n\n🟢 BUY\nEntry: 3350\nSL: 3344\nTP: 3365"
    )

async def sell(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 GOLD SIGNAL\n\n🔴 SELL\nEntry: 3350\nSL: 3356\nTP: 3340"
    )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("buy", buy))
app.add_handler(CommandHandler("sell", sell))

app.run_polling()
