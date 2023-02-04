# (©)Codexbotz
# Recode by @MSDZULQURNAIN
# t.me/MSPR0JECT & t.me/MsSUPP0RT

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from bot import Bot
from config import ADMINS
from helper_func import encode, get_message_id


@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command("posts"))
async def posts(client: Client, message: Message):
    while True:
        try:
            first_message = await client.ask(
                text="<b>Silahkan Forward Pesan PERTAMA dari Channel DataBase</b>\n\n\n<b>atau Kirim Link Postingan PERTAMA dari Channel Database</b>",
                chat_id=message.from_user.id,
                filters=(filters.forwarded | (filters.text & ~filters.forwarded)),
                timeout=60,
            )
        except BaseException:
            return
        f_msg_id = await get_message_id(client, first_message)
        if f_msg_id:
            break
        await first_message.reply(
            "❌ <b>SALAH</b>\n\n<b>BANDEL BANGET IHH😭</b>",
            quote=True,
        )
        continue

    while True:
        try:
            second_message = await client.ask(
                text="<b>Silahkan Forward Pesan TERAKHIR dari Channel DataBase</b>\n\n\n<b>atau Kirim Link Postingan TERAKHIR dari Channel Database</b>",
                chat_id=message.from_user.id,
                filters=(filters.forwarded | (filters.text & ~filters.forwarded)),
                timeout=60,
            )
        except BaseException:
            return
        s_msg_id = await get_message_id(client, second_message)
        if s_msg_id:
            break
        await second_message.reply(
            "❌ <b>SALAH</b>\n\n<b>BANDEL BANGET IHH😭</b>",
            quote=True,
        )
        continue

    string = f"get-{f_msg_id * abs(client.db_channel.id)}-{s_msg_id * abs(client.db_channel.id)}"
    base64_string = await encode(string)
    link = f"https://t.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "🔁 Bagikan link", url=f"https://telegram.me/share/url?url={link}"
                )
            ]
        ]
    )
    await second_message.reply_text(
        f"<b>Nih link nya👇👇👇</b>\n\n{link}",
        quote=True,
        reply_markup=reply_markup,
    )


@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command("buatlink"))
async def buatlink(client: Client, message: Message):
    while True:
        try:
            channel_message = await client.ask(
                text="<b>Silahkan Forward Pesan dari Channel DataBase</b>\n\n\n<b>atau Kirim Link Postingan dari Channel Database</b>",
                chat_id=message.from_user.id,
                filters=(filters.forwarded | (filters.text & ~filters.forwarded)),
                timeout=60,
            )
        except BaseException:
            return
        msg_id = await get_message_id(client, channel_message)
        if msg_id:
            break
        await channel_message.reply(
            "❌ <b>SALAH</b>\n\n<b>BANDEL BANGET IHH😭</b>",
            quote=True,
        )
        continue

    base64_string = await encode(f"get-{msg_id * abs(client.db_channel.id)}")
    link = f"https://t.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "🔁 Bagikan link", url=f"https://telegram.me/share/url?url={link}"
                )
            ]
        ]
    )
    await channel_message.reply_text(
        f"<b>Nih link nya👇👇👇</b>\n\n{link}",
        quote=True,
        reply_markup=reply_markup,
    )
