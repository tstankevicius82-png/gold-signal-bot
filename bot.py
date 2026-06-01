from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL = "@CARYPTOGOLDEDGE"

# BUY SIGNAL

async def buy(update: Update, context: ContextTypes.DEFAULT_TYPE):

```
entry = float(context.args[0])

tp1 = entry + 3
tp2 = entry + 5
tp3 = entry + 10
sl = entry - 5

msg = f"""
```

📊 GOLD SIGNAL — XAU/USD

🟢 BUY

━━━━━━━━━━━━
📍 Entry: {entry}
🛑 Stop Loss: {sl}

🎯 TP1: {tp1}
🎯 TP2: {tp2}
🎯 TP3: {tp3}
━━━━━━━━━━━━

⚠️ Move SL to BE after TP1
#gold #xauusd
"""

```
await context.bot.send_message(chat_id=CHANNEL, text=msg)
```

# SELL SIGNAL

async def sell(update: Update, context: ContextTypes.DEFAULT_TYPE):

```
entry = float(context.args[0])

tp1 = entry - 3
tp2 = entry - 5
tp3 = entry - 10
sl = entry + 5

msg = f"""
```

📊 GOLD SIGNAL — XAU/USD

🔴 SELL

━━━━━━━━━━━━
📍 Entry: {entry}
🛑 Stop Loss: {sl}

🎯 TP1: {tp1}
🎯 TP2: {tp2}
🎯 TP3: {tp3}
━━━━━━━━━━━━

⚠️ Move SL to BE after TP1
#gold #xauusd
"""

```
await context.bot.send_message(chat_id=CHANNEL, text=msg)
```

# TP1

async def tp1(update: Update, context: ContextTypes.DEFAULT_TYPE):

```
msg = """
```

✅ TP1 HIT

🔒 Stop Loss moved to Break Even
📈 Trade progressing well
"""

```
await context.bot.send_message(chat_id=CHANNEL, text=msg)
```

# TP2

async def tp2(update: Update, context: ContextTypes.DEFAULT_TYPE):

```
msg = """
```

✅ TP2 HIT

📈 Strong continuation
💰 Partial profits secured
"""

```
await context.bot.send_message(chat_id=CHANNEL, text=msg)
```

# TP3

async def tp3(update: Update, context: ContextTypes.DEFAULT_TYPE):

```
msg = """
```

🏁 TP3 HIT — TRADE CLOSED

🔥 Full target achieved
"""

```
await context.bot.send_message(chat_id=CHANNEL, text=msg)
```

# BREAK EVEN

async def be(update: Update, context: ContextTypes.DEFAULT_TYPE):

```
msg = """
```

🔒 Stop Loss moved to Break Even
"""

```
await context.bot.send_message(chat_id=CHANNEL, text=msg)
```

# STOP LOSS

async def sl(update: Update, context: ContextTypes.DEFAULT_TYPE):

```
msg = """
```

❌ Stop Loss Hit

Risk managed properly.
Waiting for next setup.
"""

```
await context.bot.send_message(chat_id=CHANNEL, text=msg)
```

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("buy", buy))
app.add_handler(CommandHandler("sell", sell))
app.add_handler(CommandHandler("tp1", tp1))
app.add_handler(CommandHandler("tp2", tp2))
app.add_handler(CommandHandler("tp3", tp3))
app.add_handler(CommandHandler("be", be))
app.add_handler(CommandHandler("sl", sl))

print("BOT RUNNING...")

app.run_polling()
