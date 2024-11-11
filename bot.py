
# bot.py
from pyrogram import Client, filters
from config import BOT_TOKEN, API_ID, API_HASH, REQUIRED_CHANNEL_ID
from handlers.user_handlers import register_user_handlers
from handlers.admin_handlers import register_admin_handlers

# Create the Pyrogram client
app = Client("tourBot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

# Welcome message on start
@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("👋 Welcome! To use the bot, you must join our channel.")

# Register user and admin handlers
register_user_handlers(app)
register_admin_handlers(app)

# Run the bot
app.run()
