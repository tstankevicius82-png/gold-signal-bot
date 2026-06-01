import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

# BUY COMMAND

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

⚠️ Risk: 1%
#gold #xauusd
"""

```
await update.message.reply_text(msg)
```

# SELL COMMAND

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

⚠️ Risk: 1%
#gold #xauusd
"""

```
await update.message.reply_text(msg)
```

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("buy", buy))
app.add_handler(CommandHandler("sell", sell))

app.run_polling()
