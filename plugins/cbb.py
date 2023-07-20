# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de
# Recode new by @MSDZULQURNAIN
# t.me/MSPR0JECT & t.me/MsSUPP0RT


from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from telegram import ParseMode
from bot import Bot
from config import BUTTONS, START_MSG
from .button import start_button
from MSDZULQURNAIN.ztext import zinfo, CMD_TEXT, BTN_TEXT, TUTOR_TEXT

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "home":
        out = start_button(client)
        await query.message.edit_text(
            text=START_MSG.format(
                first=message.from_user.first_name,
                last=message.from_user.last_name,
                username=f"@{message.from_user.username}"
                if message.from_user.username
                else None,
                mention=message.from_user.mention,
                id=message.from_user.id,
            ),
            reply_markup=InlineKeyboardMarkup(out),
            disable_web_page_preview=True
            )
    elif data == "about":
        await query.message.edit_text(
            text=f"{zinfo}",
            disable_web_page_preview=True,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("Kembali", callback_data="home")]]
            ),
        )
    elif data == "cmd":
        await query.message.edit_text(
            text=CMD_TEXT,
            disable_web_page_preview=True,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("Kembali", callback_data="home")]]
            ),
        )
    elif data == "btn":
        await query.answer(
            text=BTN_TEXT.format(BUTTONS),
            show_alert=True
            )
    elif data == "tutor":
        await query.message.edit_text(
            text=TUTOR_TEXT,
            disable_web_page_preview=True,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("Kembali", callback_data="home")]]
            ),
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except BaseException:
            pass
