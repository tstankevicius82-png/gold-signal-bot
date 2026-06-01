async def tp1(update:Update,context:ContextTypes.DEFAULT_TYPE): await update.message.reply_text("✅ TP1 HIT\n\n🔒 Stop Loss moved to Break Even.\n📈 Trade progressing well.")

async def tp2(update:Update,context:ContextTypes.DEFAULT_TYPE): await update.message.reply_text("✅ TP2 HIT\n\n📈 Strong continuation.\nPartial profits secured.")

async def tp3(update:Update,context:ContextTypes.DEFAULT_TYPE): await update.message.reply_text("🏁 TP3 HIT — TRADE CLOSED\n\n🔥 Full target achieved.\nExcellent trade.")

async def be(update:Update,context:ContextTypes.DEFAULT_TYPE): await update.message.reply_text("🔒 Stop Loss moved to Break Even.")

async def sl(update:Update,context:ContextTypes.DEFAULT_TYPE): await update.message.reply_text("❌ Stop Loss Hit\n\nRisk managed properly.\nWaiting for next setup.")
app.add_handler(CommandHandler("tp1",tp1))
app.add_handler(CommandHandler("tp2",tp2))
app.add_handler(CommandHandler("tp3",tp3))
app.add_handler(CommandHandler("be",be))
app.add_handler(CommandHandler("sl",sl))
