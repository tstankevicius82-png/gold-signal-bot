```python
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

CHANNEL_ID = "@CARYPTOGOLDEDGE"


# BUY SIGNAL
async def buy(update: Update, context: ContextTypes.DEFAULT_TYPE):

    msg = """
📊 GOLD SIGNAL — XAU/USD

🟢 BUY

━━━━━━━━━━━━
📍 Entry: 3350.2
🛑 Stop Loss: 3344.8

🎯 TP1: 3355.0
🎯 TP2: 3360.5
🎯 TP3: 3368.0
━━━━━━━━━━━━

⚠️ Risk: 1%
📈 Manage risk properly

#gold #xauusd
"""

    await context.bot.send_message(chat_id=CHANNEL_ID, text=msg)


# SELL SIGNAL
async def sell(update: Update, context: ContextTypes.DEFAULT_TYPE):

    msg = """
📊 GOLD SIGNAL — XAU/USD

🔴 SELL

━━━━━━━━━━━━
📍 Entry: 3350.2
🛑 Stop Loss: 3356.0

🎯 TP1: 3345.0
🎯 TP2: 3340.5
🎯 TP3: 3332.0
━━━━━━━━━━━━

⚠️ Risk: 1%
📈 Manage risk properly

#gold #xauusd
"""

    await context.bot.send_message(chat_id=CHANNEL_ID, text=msg)


# TP HIT
async def tp(update: Update, context: ContextTypes.DEFAULT_TYPE):

    msg = """
✅ TP1 HIT — GOLD SIGNAL

📈 Partial profits secured
🔒 Stop Loss moved to Break Even

Trade continues running.
"""

    await context.bot.send_message(chat_id=CHANNEL_ID, text=msg)


# SL HIT
async def sl(update: Update, context: ContextTypes.DEFAULT_TYPE):

    msg = """
❌ STOP LOSS HIT

Risk managed properly.
Waiting for next clean setup.
"""

    await context.bot.send_message(chat_id=CHANNEL_ID, text=msg)


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("buy", buy))
app.add_handler(CommandHandler("sell", sell))
app.add_handler(CommandHandler("tp", tp))
app.add_handler(CommandHandler("sl", sl))

print("BOT RUNNING...")

app.run_polling()
```
