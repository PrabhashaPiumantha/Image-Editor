# By @TroJanzHEX
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters
from script import script  # pylint:disable=import-error


@Client.on_message(filters.command(["start"]) & filters.private)
async def start(client: Client, message: Message):
    try:
        await message.reply_text(
            text=script.START_MSG.format(message.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Help ⛑", callback_data="help_data"),
                        InlineKeyboardButton("About 📖", callback_data="about_data"),
                    ],
                    [
                        InlineKeyboardButton(
                            "Source Code ℹ️",
                            url="https://github.com/prabhasha-p/Image-Editor",
                        )
                    ],
                ]
            ),
            reply_to_message_id=message.message_id,
        )
    except Exception:
        pass


@Client.on_message(filters.command(["help"]) & filters.private)
async def help(client, message):
    try:
        await message.reply_text(
            text=script.HELP_MSG,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Back 🔙", callback_data="start_data"),
                        InlineKeyboardButton("About 🤔", callback_data="about_data"),
                    ],
                    [
                        InlineKeyboardButton(
                            "Source Code ℹ️",
                            url="https://github.com/prabhasha-p/Image-Editor",
                        )
                    ],
                ]
            ),
            reply_to_message_id=message.message_id,
        )
    except Exception:
        pass


@Client.on_message(filters.command(["about"]) & filters.private)
async def about(client, message):
    try:
        await message.reply_text(
            text=script.ABOUT_MSG,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Back 🔙", callback_data="help_data"),
                        InlineKeyboardButton("Start 🏃", callback_data="start_data"),
                    ],
                    [
                        InlineKeyboardButton(
                            "Source Code ℹ️",
                            url="https://github.com/prabhasha-p/Image-Editor",
                        )
                    ],
                ]
            ),
            reply_to_message_id=message.message_id,
        )
    except Exception:
        pass
