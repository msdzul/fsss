# Credits: @MSDZULQURNAIN
# FROM FILE-SHARING-6-BUTT <https://github.com/MS-DZULQURNAIN/FILE-SHARING-6-BUTT/>
# t.me/MSPR0JECT & t.me/MsSUPP0RT

from config import FORCE_SUB_CHANNEL, FORCE_SUB_GROUP, FORCE_SUB_GROUP2, FORCE_SUB_GROUP3, FORCE_SUB_GROUP4, FORCE_SUB_GROUP5  

from pyrogram.types import InlineKeyboardButton


def start_button(client):
    if not FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP and not FORCE_SUB_GROUP2 and not FORCE_SUB_GROUP3 and not FORCE_SUB_GROUP4 and not FORCE_SUB_GROUP5:
        buttons = [
            [
                InlineKeyboardButton(text="Tentang saya👤", callback_data="about"),
                InlineKeyboardButton(text="Tutup💝", callback_data="close"),
            ],
        ]
        return buttons
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and FORCE_SUB_GROUP2 and not FORCE_SUB_GROUP3 and not FORCE_SUB_GROUP4 and not FORCE_SUB_GROUP5:
        buttons = [
            [
                InlineKeyboardButton(text="🄲ΉΛ𝐍𝐍ΞꝈ", url=client.invitelink2),
                InlineKeyboardButton(text="🄲ΉΛ𝐍𝐍ΞꝈ", url=client.invitelink3),
            ],
            [
                InlineKeyboardButton(text="Tentang saya👤", callback_data="about"),
                InlineKeyboardButton(text="Tutup💝", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP and not FORCE_SUB_GROUP2 and not FORCE_SUB_GROUP3 and not FORCE_SUB_GROUP4 and not FORCE_SUB_GROUP5:
        buttons = [
            [
                InlineKeyboardButton(text="🄲ΉΛ𝐍𝐍ΞꝈ", url=client.invitelink),
            ],
            [
                InlineKeyboardButton(text="Tentang saya👤", callback_data="about"),
                InlineKeyboardButton(text="Tutup💝", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and not FORCE_SUB_GROUP2 and not FORCE_SUB_GROUP3 and not FORCE_SUB_GROUP4 and not FORCE_SUB_GROUP5:
        buttons = [
            [
                InlineKeyboardButton(text="Tentang saya👤", callback_data="about"),
            ],
            [
                InlineKeyboardButton(text="🄲ΉΛ𝐍𝐍ΞꝈ", url=client.invitelink),
                InlineKeyboardButton(text="🄲ΉΛ𝐍𝐍ΞꝈ", url=client.invitelink2),
            ],
            [InlineKeyboardButton(text="Tutup💝", callback_data="close")],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and FORCE_SUB_GROUP2 and not FORCE_SUB_GROUP3 and not FORCE_SUB_GROUP4 and not FORCE_SUB_GROUP5:
        buttons = [
            [
                InlineKeyboardButton(text="Tentang saya👤", callback_data="about"),
            ],
            [
                InlineKeyboardButton(text="🄲ΉΛ𝐍𝐍ΞꝈ", url=client.invitelink),
                InlineKeyboardButton(text="🄲ΉΛ𝐍𝐍ΞꝈ", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="🄲ΉΛ𝐍𝐍ΞꝈ", url=client.invitelink3),
            ],
            [
                InlineKeyboardButton(text="Tutup💝", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and FORCE_SUB_GROUP2 and FORCE_SUB_GROUP3 and not FORCE_SUB_GROUP4 and not FORCE_SUB_GROUP5:
        buttons = [
            [
                InlineKeyboardButton(text="Tentang saya👤", callback_data="about"),
            ],
            [
                InlineKeyboardButton(text="🄲ΉΛ𝐍𝐍ΞꝈ", url=client.invitelink),
                InlineKeyboardButton(text="🄲ΉΛ𝐍𝐍ΞꝈ", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="🄲ΉΛ𝐍𝐍ΞꝈ", url=client.invitelink3),
                InlineKeyboardButton(text="🄲ΉΛ𝐍𝐍ΞꝈ", url=client.invitelink4),
            ],
            [
                InlineKeyboardButton(text="Tutup💝", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and FORCE_SUB_GROUP2 and FORCE_SUB_GROUP3 and FORCE_SUB_GROUP4 and not FORCE_SUB_GROUP5:
        buttons = [
            [
                InlineKeyboardButton(text="Tentang saya👤", callback_data="about"),
            ],
            [
                InlineKeyboardButton(text="🄲ΉΛ𝐍𝐍ΞꝈ", url=client.invitelink),
                InlineKeyboardButton(text="🄲ΉΛ𝐍𝐍ΞꝈ", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="🄲ΉΛ𝐍𝐍ΞꝈ", url=client.invitelink3),
                InlineKeyboardButton(text="🄲ΉΛ𝐍𝐍ΞꝈ", url=client.invitelink4),
            ],
            [
                InlineKeyboardButton(text="🄲ΉΛ𝐍𝐍ΞꝈ", url=client.invitelink5),
            ],
            [
                InlineKeyboardButton(text="Tutup💝", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and FORCE_SUB_GROUP2 and FORCE_SUB_GROUP3 and FORCE_SUB_GROUP4 and FORCE_SUB_GROUP5:
        buttons = [
            [
                InlineKeyboardButton(text="Tentang saya👤", callback_data="about"),
            ],
            [
                InlineKeyboardButton(text="🄲ΉΛ𝐍𝐍ΞꝈ", url=client.invitelink),
                InlineKeyboardButton(text="🄲ΉΛ𝐍𝐍ΞꝈ", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="🄲ΉΛ𝐍𝐍ΞꝈ", url=client.invitelink3),
                InlineKeyboardButton(text="🄲ΉΛ𝐍𝐍ΞꝈ", url=client.invitelink4),
            ],
            [
                InlineKeyboardButton(text="🄲ΉΛ𝐍𝐍ΞꝈ", url=client.invitelink5),
                InlineKeyboardButton(text="🄲ΉΛ𝐍𝐍ΞꝈ", url=client.invitelink6),
            ],
            [
                InlineKeyboardButton(text="Tutup💝", callback_data="close"),
            ],
        ]
        return buttons

def fsub_button(client, message):
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and not FORCE_SUB_GROUP2 and not FORCE_SUB_GROUP3 and not FORCE_SUB_GROUP4 and not FORCE_SUB_GROUP5:
        buttons = [
            [
                InlineKeyboardButton(text="🄹♢ɨ𝐍  🄲ΉΛ𝐍𝐍ΞꝈ", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Coba lagi",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP and not FORCE_SUB_GROUP2 and not FORCE_SUB_GROUP3 and not FORCE_SUB_GROUP4 and not FORCE_SUB_GROUP5:
        buttons = [
            [
                InlineKeyboardButton(text="🄹♢ɨ𝐍  🄲ΉΛ𝐍𝐍ΞꝈ", url=client.invitelink),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Coba lagi",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and not FORCE_SUB_GROUP2 and not FORCE_SUB_GROUP3 and not FORCE_SUB_GROUP4 and not FORCE_SUB_GROUP5:
        buttons = [
            [
                InlineKeyboardButton(text="🄹♢ɨ𝐍  🄲ΉΛ𝐍𝐍ΞꝈ", url=client.invitelink),
                InlineKeyboardButton(text="🄹♢ɨ𝐍  🄲ΉΛ𝐍𝐍ΞꝈ", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Coba lagi",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and FORCE_SUB_GROUP2 and not FORCE_SUB_GROUP3 and not FORCE_SUB_GROUP4 and not FORCE_SUB_GROUP5:
        buttons = [
            [
                InlineKeyboardButton(text="🄹♢ɨ𝐍  🄲ΉΛ𝐍𝐍ΞꝈ", url=client.invitelink),
                InlineKeyboardButton(text="🄹♢ɨ𝐍  🄲ΉΛ𝐍𝐍ΞꝈ", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="🄹♢ɨ𝐍  🄲ΉΛ𝐍𝐍ΞꝈ", url=client.invitelink3),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Coba lagi",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and FORCE_SUB_GROUP2 and FORCE_SUB_GROUP3 and not FORCE_SUB_GROUP4 and not FORCE_SUB_GROUP5:
        buttons = [
            [
                InlineKeyboardButton(text="🄹♢ɨ𝐍  🄲ΉΛ𝐍𝐍ΞꝈ", url=client.invitelink),
                InlineKeyboardButton(text="🄹♢ɨ𝐍  🄲ΉΛ𝐍𝐍ΞꝈ", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="🄹♢ɨ𝐍  🄲ΉΛ𝐍𝐍ΞꝈ", url=client.invitelink3),
                InlineKeyboardButton(text="🄹♢ɨ𝐍  🄲ΉΛ𝐍𝐍ΞꝈ", url=client.invitelink4),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Coba lagi",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
             pass
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and FORCE_SUB_GROUP2 and FORCE_SUB_GROUP3 and FORCE_SUB_GROUP4 and not FORCE_SUB_GROUP5:
        buttons = [
            [
                InlineKeyboardButton(text="🄹♢ɨ𝐍  🄲ΉΛ𝐍𝐍ΞꝈ", url=client.invitelink),
                InlineKeyboardButton(text="🄹♢ɨ𝐍  🄲ΉΛ𝐍𝐍ΞꝈ", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="🄹♢ɨ𝐍  🄲ΉΛ𝐍𝐍ΞꝈ", url=client.invitelink3),
                InlineKeyboardButton(text="🄹♢ɨ𝐍  🄲ΉΛ𝐍𝐍ΞꝈ", url=client.invitelink4),
            ],
            [
                InlineKeyboardButton(text="🄹♢ɨ𝐍  🄲ΉΛ𝐍𝐍ΞꝈ", url=client.invitelink5),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Coba lagi",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and FORCE_SUB_GROUP2 and FORCE_SUB_GROUP3 and FORCE_SUB_GROUP4 and FORCE_SUB_GROUP5:
        buttons = [
            [
                InlineKeyboardButton(text="🄹♢ɨ𝐍  🄲ΉΛ𝐍𝐍ΞꝈ", url=client.invitelink),
                InlineKeyboardButton(text="🄹♢ɨ𝐍  🄲ΉΛ𝐍𝐍ΞꝈ", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="🄹♢ɨ𝐍  🄲ΉΛ𝐍𝐍ΞꝈ", url=client.invitelink3),
                InlineKeyboardButton(text="🄹♢ɨ𝐍  🄲ΉΛ𝐍𝐍ΞꝈ", url=client.invitelink4),
            ],
            [
                InlineKeyboardButton(text="🄹♢ɨ𝐍  🄲ΉΛ𝐍𝐍ΞꝈ", url=client.invitelink5),
                InlineKeyboardButton(text="🄹♢ɨ𝐍  🄲ΉΛ𝐍𝐍ΞꝈ", url=client.invitelink6),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Coba lagi",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
