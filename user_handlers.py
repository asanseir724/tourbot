
# handlers/user_handlers.py
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def register_user_handlers(app: Client):
    @app.on_message(filters.command("add_channel"))
    async def add_channel(client, message):
        await message.reply(
            "🔗 Please send your channel link.",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("✅ Confirm", callback_data="confirm_channel")],
                [InlineKeyboardButton("❌ Cancel", callback_data="cancel_channel")]
            ])
        )
