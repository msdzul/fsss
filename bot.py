
import pyromod.listen
import sys

from pyrogram import Client

from config import (
    API_HASH,
    APP_ID,
    CHANNEL_ID,
    FORCE_SUB_CHANNEL,
    FORCE_SUB_GROUP,
    FORCE_SUB_GROUP2,
    FORCE_SUB_GROUP3,
    FORCE_SUB_GROUP4,
    FORCE_SUB_GROUP5,
    LOGGER,
    OWNER,
    TG_BOT_TOKEN,
    TG_BOT_WORKERS,
)


class Bot(Client):
    def __init__(self):
        super().__init__(
            "Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={"root": "plugins"},
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN,
        )
        self.LOGGER = LOGGER

    async def start(self):
        try:
            await super().start()
            usr_bot_me = await self.get_me()
            self.username = usr_bot_me.username
            self.namebot = usr_bot_me.first_name
            self.LOGGER(__name__).info(
                f"TG_BOT_TOKEN detected!\n┌ First Name: {self.namebot}\n└ Username: @{self.username}\n——"
            )
        except Exception as a:
            self.LOGGER(__name__).warning(a)
            self.LOGGER(__name__).info(
                "BOT BERHENTI😞. Join https://t.me/MsSUPP0RT untuk info lebih lanjut"
            )
            sys.exit()

        if FORCE_SUB_CHANNEL:
            try:
                link = (await self.get_chat(FORCE_SUB_CHANNEL)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_CHANNEL)
                    link = (await self.get_chat(FORCE_SUB_CHANNEL)).invite_link
                self.invitelink = link
                self.LOGGER(__name__).info(
                    f"FORCE_SUB_CHANNEL detected!\n┌ Title: {info.title}\n└ Chat ID: {info.id}\n——"
                )
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "BOT TIDAK BISA MENERIMA INVITE LINK DARI CHANNEL FORCE SUB!"
                )
                self.LOGGER(__name__).warning(
                    f"JADIKAN @{self.username} SEBAGAI ADMIN DI CHANNEL FORCE SUB JIKA SUDAH SILAKAN CEK KEMBALI😗: {FORCE_SUB_CHANNEL}"
                )
                self.LOGGER(__name__).info(
                    "BOT BERHENTI😞. Join https://t.me/MsSUPP0RT untuk info lebih lanjut"
                )
                sys.exit()

        if FORCE_SUB_GROUP:
            try:
                link = (await self.get_chat(FORCE_SUB_GROUP)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_GROUP)
                    link = (await self.get_chat(FORCE_SUB_GROUP)).invite_link
                self.invitelink2 = link
                self.LOGGER(__name__).info(
                    f"FORCE_SUB_GROUP detected!\n┌ Title: {info.title}\n└ Chat ID: {info.id}\n——"
                )
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "BOT TIDAK BISA MENERIMA INVITE LINK DARI FORCE SUB GRUB!"
                )
                self.LOGGER(__name__).warning(
                    f"JADIKAN @{self.username} SEBAGAI ADMIN DI FORCE SUB GRUB JIKA SUDAH SILAKAN CEK KEMBALI😗: {FORCE_SUB_GROUP}"
                )
                self.LOGGER(__name__).info(
                    "BOT BERHENTI😞. Join https://t.me/MsSUPP0RT untuk info lebih lanjut"
                )
                sys.exit()

        if FORCE_SUB_GROUP2:
            try:
                link = (await self.get_chat(FORCE_SUB_GROUP2)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_GROUP2)
                    link = (await self.get_chat(FORCE_SUB_GROUP2)).invite_link
                self.invitelink3 = link
                self.LOGGER(__name__).info(
                    f"FORCE_SUB_GROUP2 detected!\n┌ Title: {info.title}\n└ Chat ID: {info.id}\n——"
                )
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "BOT TIDAK BISA MENERIMA INVITE LINK DARI FORCE SUB GRUB2"
                )
                self.LOGGER(__name__).warning(
                    f"JADIKAN @{self.username} SEBAGAI ADMIN DI FORCE SUB GRUB2 JIKA SUDAH SILAKAN CEK KEMBALI😗: {FORCE_SUB_GROUP2}"
                )
                self.LOGGER(__name__).info(
                    "BOT BERHENTI😞. Join https://t.me/MsSUPP0RT untuk info lebih lanjut"
                )
                sys.exit()

        if FORCE_SUB_GROUP3:
            try:
                link = (await self.get_chat(FORCE_SUB_GROUP3)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_GROUP3)
                    link = (await self.get_chat(FORCE_SUB_GROUP3)).invite_link
                self.invitelink4 = link
                self.LOGGER(__name__).info(
                    f"FORCE_SUB_GROUP3 detected!\n┌ Title: {info.title}\n└ Chat ID: {info.id}\n——"
                )
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "BOT TIDAK BISA MENERIMA INVITE LINK DARI FORCE SUB GRUB3"
                )
                self.LOGGER(__name__).warning(
                    f"JADIKAN @{self.username} SEBAGAI ADMIN DI FORCE SUB GRUB3 JIKA SUDAH SILAKAN CEK KEMBALI😗: {FORCE_SUB_GROUP3}"
                )
                self.LOGGER(__name__).info(
                    "BOT BERHENTI😞. Join https://t.me/MsSUPP0RT untuk info lebih lanjut"
                )
                sys.exit()

        if FORCE_SUB_GROUP4:
            try:
                link = (await self.get_chat(FORCE_SUB_GROUP4)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_GROUP4)
                    link = (await self.get_chat(FORCE_SUB_GROUP4)).invite_link
                self.invitelink5 = link
                self.LOGGER(__name__).info(
                    f"FORCE_SUB_GROUP4 detected!\n┌ Title: {info.title}\n└ Chat ID: {info.id}\n——"
                )
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "BOT TIDAK BISA MENERIMA INVITE LINK DARI FORCE SUB GRUB4"
                )
                self.LOGGER(__name__).warning(
                    f"JADIKAN @{self.username} SEBAGAI ADMIN DI FORCE SUB GRUB4 JIKA SUDAH SILAKAN CEK KEMBALI😗: {FORCE_SUB_GROUP4}"
                )
                self.LOGGER(__name__).info(
                    "BOT BERHENTI😞. Join https://t.me/MsSUPP0RT untuk info lebih lanjut"
                )
                sys.exit()

        if FORCE_SUB_GROUP5:
            try:
                link = (await self.get_chat(FORCE_SUB_GROUP5)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_GROUP5)
                    link = (await self.get_chat(FORCE_SUB_GROUP5)).invite_link
                self.invitelink6 = link
                self.LOGGER(__name__).info(
                    f"FORCE_SUB_GROUP5 detected!\n┌ Title: {info.title}\n└ Chat ID: {info.id}\n——"
                )
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "BOT TIDAK BISA MENERIMA INVITE LINK DARI FORCE SUB GRUB5"
                )
                self.LOGGER(__name__).warning(
                    f"JADIKAN @{self.username} SEBAGAI ADMIN DI FORCE SUB GRUB5 JIKA SUDAH SILAKAN CEK KEMBALI😗: {FORCE_SUB_GROUP5}"
                )
                self.LOGGER(__name__).info(
                    "BOT BERHENTI😞. Join https://t.me/MsSUPP0RT untuk info lebih lanjut"
                )
                sys.exit()

        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id=db_channel.id, text="Test Message")
            await test.delete()
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(
                f"JADIKAN @{self.username} SEBAGAI ADMIN DI CHANNEL DATABASE JIKA SUDAH SILAKAN CEK KEMBALI😗: {CHANNEL_ID}"
            )
            self.LOGGER(__name__).info(
                "BOT BERHENTI😞. Join https://t.me/MsSUPP0RT untuk info lebih lanjut"
            )
            sys.exit()

        self.set_parse_mode("html")
        self.LOGGER(__name__).info(
            f"[BOT TELAH AKTIF🔥🔥🔥..!]\n\nBOT DIBUAT OLEH @{OWNER}\nJIKA @{OWNER} BUTUH BANTUAN, SILAKAN TANYA DI GRUB https://t.meMsSUPP0RT"
        )

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("BOT BERHENTI🚫")
