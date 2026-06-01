from telegram import Update
from telegram.ext import Application,CommandHandler,ContextTypes
import os
TOKEN=os.getenv("BOT_TOKEN")

async def buy(update:Update,context:ContextTypes.DEFAULT_TYPE): entry=float(context.args[0]);tp1=entry+3;tp2=entry+5;tp3=entry+10;sl=entry-5;msg=f"📊 GOLD SIGNAL — XAU/USD\n\n🟢 BUY\n\n📍 Entry: {entry}\n🛑 Stop Loss: {sl}\n🎯 TP1: {tp1}\n🎯 TP2: {tp2}\n🎯 TP3: {tp3}\n\n#gold #xauusd"; await update.message.reply_text(msg)

async def sell(update:Update,context:ContextTypes.DEFAULT_TYPE): entry=float(context.args[0]);tp1=entry-3;tp2=entry-5;tp3=entry-10;sl=entry+5;msg=f"📊 GOLD SIGNAL — XAU/USD\n\n🔴 SELL\n\n📍 Entry: {entry}\n🛑 Stop Loss: {sl}\n🎯 TP1: {tp1}\n🎯 TP2: {tp2}\n🎯 TP3: {tp3}\n\n#gold #xauusd"; await update.message.reply_text(msg)

app=Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("buy",buy))
app.add_handler(CommandHandler("sell",sell))
app.run_polling()
