
# handlers/admin_handlers.py
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ADMIN_IDS = [123456789]  # Replace with actual admin IDs

def register_admin_handlers(app: Client):
    @app.on_message(filters.command("admin") & filters.user(ADMIN_IDS))
    async def admin_panel(client, message):
        await message.reply(
            "🔧 Admin Panel",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("➕ Add Tour List", callback_data="add_tour_list")],
                [InlineKeyboardButton("📃 Tour List", callback_data="tour_list")],
                [InlineKeyboardButton("🔨 Ban User", callback_data="ban_user")]
            ])
        )
