import asyncio
from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    CommandHandler,
    ContextTypes,
    filters,
)

BOT_TOKEN = "7987255177:AAG31XQ9XjElOI9z-qWBitcftqR4_9mfvv0"  # Replace with your actual token


# ✨ Stylish Unicode Welcome Generator
def get_welcome_text(user):
    name = user.full_name
    username = f"@{user.username}" if user.username else "𝑵𝑶 𝑼𝑺𝑬𝑹𝑵𝑨𝑴𝑬"
    user_id = user.id

    return f"""
╔═════════════════════★
🌟 𝑾 𝑬 𝑳 𝑪 𝑶 𝑴 𝑬  🌟
★═════════════════════╗

┏━━━━━━━━━━━━━━━┓
┃ 💫 𝙉𝘼𝙈𝙀: <i>{name}</i>
┃ 🎯 𝙐𝙎𝙀𝙍𝙉𝘼𝙈𝙀: <i>{username}</i>
┃ 🆔 𝙄𝘿: <i>{user_id}</i>
┗━━━━━━━━━━━━━━━┛

⚡ <b>𝑨 𝑳𝒆𝒈𝒆𝒏𝒅 𝒉𝒂𝒔 𝑬𝒏𝒕𝒆𝒓𝒆𝒅 𝑻𝒉𝒆 𝑨𝒓𝒆𝒏𝒂!</b>
💥 <b>𝑳𝒆𝒕’𝒔 𝑴𝒂𝒌𝒆 𝑻𝒉𝒊𝒔 𝑮𝒓𝒐𝒖𝒑 𝑬𝒑𝒊𝒄!</b>

✨ <i>𝑬𝒏𝒋𝒐𝒚 𝒀𝒐𝒖𝒓 𝑺𝒕𝒂𝒚, 𝑳𝒆𝒈𝒆𝒏𝒅 💖</i>

╚═════════ 👑 𝑻𝑯𝑬 𝑬𝑵𝑫 👑 ═════════╝
"""

# 📸 Handle new group member
async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for user in update.message.new_chat_members:
        text = get_welcome_text(user)
        try:
            photos = await context.bot.get_user_profile_photos(user.id)
            if photos.total_count > 0:
                file_id = photos.photos[0][-1].file_id
                await context.bot.send_photo(
                    chat_id=update.effective_chat.id,
                    photo=file_id,
                    caption=text,
                    parse_mode=ParseMode.HTML,
                )
            else:
                await update.message.reply_text(text, parse_mode=ParseMode.HTML)
        except Exception as e:
            print(f"[Error]: {e}")
            await update.message.reply_text(text, parse_mode=ParseMode.HTML)

# 🔹 Handle /start in private chat
async def start_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.type == "private":
        await update.message.reply_text(
            "👋 𝑯𝒆𝒚 𝑳𝒆𝒈𝒆𝒏𝒅!\n\n"
            "➕ <b>Add me to your Telegram group</b> to activate stylish welcome powers! 💥✨\n\n"
            "🔹 <i>I’ll greet every new member with swag 😎</i>",
            parse_mode=ParseMode.HTML
        )

# 🚀 Start bot
def run_bot():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))
    app.add_handler(CommandHandler("start", start_cmd))
    print("🤖 Ultra Stylish Welcome Bot is running...")

    try:
        asyncio.get_event_loop().run_until_complete(app.run_polling())
    except RuntimeError:
        import threading
        threading.Thread(target=lambda: asyncio.run(app.run_polling())).start()

if __name__ == "__main__":
    run_bot()