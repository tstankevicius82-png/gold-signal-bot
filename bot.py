from telegram import Update
from telegram.ext import Application,CommandHandler,ContextTypes
import os

TOKEN=os.getenv("BOT_TOKEN")
CHANNEL="@CARYPTOGOLDEDGE"

async def buy(update:Update,context:ContextTypes.DEFAULT_TYPE): entry=float(context.args[0]);tp1=entry+3;tp2=entry+5;tp3=entry+10;sl=entry-5;msg=f"📊 GOLD SIGNAL — XAU/USD\n\n🟢 BUY\n\n📍 Entry: {entry}\n🛑 Stop Loss: {sl}\n🎯 TP1: {tp1}\n🎯 TP2: {tp2}\n🎯 TP3: {tp3}\n\n⚠️ Move SL to BE after TP1\n#gold #xauusd"; await context.bot.send_message(chat_id=CHANNEL,text=msg)

async def sell(update:Update,context:ContextTypes.DEFAULT_TYPE): entry=float(context.args[0]);tp1=entry-3;tp2=entry-5;tp3=entry-10;sl=entry+5;msg=f"📊 GOLD SIGNAL — XAU/USD\n\n🔴 SELL\n\n📍 Entry: {entry}\n🛑 Stop Loss: {sl}\n🎯 TP1: {tp1}\n🎯 TP2: {tp2}\n🎯 TP3: {tp3}\n\n⚠️ Move SL to BE after TP1\n#gold #xauusd"; await context.bot.send_message(chat_id=CHANNEL,text=msg)

async def tp1(update:Update,context:ContextTypes.DEFAULT_TYPE): await context.bot.send_message(chat_id=CHANNEL,text="✅ TP1 HIT\n\n🔒 Stop Loss moved to Break Even\n📈 Trade progressing well")

async def tp2(update:Update,context:ContextTypes.DEFAULT_TYPE): await context.bot.send_message(chat_id=CHANNEL,text="✅ TP2 HIT\n\n💰
