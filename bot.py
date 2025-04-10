from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

BOT_TOKEN = "7610665147:AAHm655LDvGwhDF2IJXOpC1K1Im5LLAprkA"
ADMIN_CHAT_ID = 5312763835

# /start komandasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Assalamu alaykum, shuyerdan Muhammadzohirga xabar qoldirishingiz mumkin!")

# Har qanday xabarga javob va admin uchun info
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    full_name = user.full_name
    username = user.username or "Username yo‘q"
    user_id = user.id
    text = update.message.text

    # Admin uchun xabar
    msg = (
        f"📨 Yangi xabar:\n\n"
        f"👤 Ism: {full_name}\n"
        f"🔗 Username: @{username}\n"
        f"🆔 ID: {user_id}\n"
        f"💬 Xabar: {text}"
    )
    await context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=msg)

    # Foydalanuvchiga javob
    await update.message.reply_text("Xabaringiz qabul qilindi. 😊")

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("🤖 Bot ishga tushdi...")
    app.run_polling()
