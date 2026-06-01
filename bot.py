from telegram import Update
from telegram.ext import Application,CommandHandler,ContextTypes
import os

TOKEN=os.getenv("BOT_TOKEN")

async def buy(update:Update,context:ContextTypes.DEFAULT_TYPE): entry=float(context.args[0]);tp1=entry+3;tp2=entry+5;tp3=entry+10;sl=entry-5;msg=f"📊 GOLD SIGNAL — XAU/USD\n\n🟢 BUY\n\n📍 Entry: {entry}\n🛑 Stop Loss: {sl}\n🎯 TP1: {tp1}\n🎯 TP2: {tp2}\n🎯 TP3: {tp3}\n\n#gold #xauusd"; await update.message.reply_text(msg)

async def sell(update:Update,context:ContextTypes.DEFAULT_TYPE): entry=float(context.args[0]);tp1=entry-3;tp2=entry-5;tp3=entry-10;sl=entry+5;msg=f"📊 GOLD SIGNAL — XAU/USD\n\n🔴 SELL\n\n📍 Entry: {entry}\n🛑 Stop Loss: {sl}\n🎯 TP1: {tp1}\n🎯 TP2: {tp2}\n🎯 TP3: {tp3}\n\n#gold #xauusd"; await update.message.reply_text(msg)

async def tp1(update:Update,context:ContextTypes.DEFAULT_TYPE): await update.message.reply_text("✅ TP1 HIT\n\n🔒 Stop Loss moved to Break Even.\n📈 Trade progressing well.")

async def tp2(update:Update,context:ContextTypes.DEFAULT_TYPE): await update.message.reply_text("✅ TP2 HIT\n\n📈 Strong continuation.\nPartial profits secured.")

async def tp3(update:Update,context:ContextTypes.DEFAULT_TYPE): await update.message.reply_text("🏁 TP3 HIT — TRADE CLOSED\n\n🔥 Full target achieved.")

async def be(update:Update,context:ContextTypes.DEFAULT_TYPE): await update.message.reply_text("🔒 Stop Loss moved to Break Even.")

async def sl(update:Update,context:ContextTypes.DEFAULT_TYPE): await update.message.reply_text("❌ Stop Loss Hit\n\nRisk managed properly.")

app=Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("buy",buy))
app.add_handler(CommandHandler("sell",sell))
app.add_handler(CommandHandler("tp1",tp1))
app.add_handler(CommandHandler("tp2",tp2))
app.add_handler(CommandHandler("tp3",tp3))
app.add_handler(CommandHandler("be",be))
app.add_handler(CommandHandler("sl",sl))

app.run_polling()
