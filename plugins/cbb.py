# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de
# Recode new by @MSDZULQURNAIN
# t.me/MSPR0JECT & t.me/MsSUPP0RT


from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from bot import Bot
from config import BUTTONS
from MSDZULQURNAIN.ztext import zinfo, CMD_TEXT, BTN_TEXT, TUTOR_TEXT

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text=f"{zinfo}",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("Tutup", callback_data="close")]]
            ),
        )
    elif data == "cmd":
        await query.message.edit_text(
            text=CMD_TEXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("Tutup", callback_data="close")]]
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
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("Tutup", callback_data="close")]]
            ),
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except BaseException:
            pass
