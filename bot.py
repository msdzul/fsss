
import pyromod.listen
import sys

from pyrogram import Client

from config import (
    API_HASH,
    APP_ID,
    CHANNEL_ID,
    FSUB1,
    FSUB2,
    FSUB3,
    FSUB4,
    FSUB5,
    FSUB6,
    FSUB7,
    FSUB8,
    FSUB9,
    FSUB10,
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

        if FSUB1:
            try:
                info = await self.get_chat(FSUB1)
                link = info.invite_link
                if not link:
                    await self.export_chat_invite_link(FSUB1)
                    link = info.invite_link
                self.invitelink = link
                self.LOGGER(__name__).info(
                    f"FSUB1 detected!\n┌ Title: {info.title}\n└ Chat ID: {info.id}\n——"
                )
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "BOT TIDAK BISA MENERIMA INVITE LINK DARI CHANNEL FSUB1"
                )
                self.LOGGER(__name__).warning(
                    f"JADIKAN @{self.username} SEBAGAI ADMIN DI CHANNEL FSUB1 JIKA SUDAH SILAKAN CEK KEMBALI😗: {FSUB1}"
                )
                self.LOGGER(__name__).info(
                    "BOT BERHENTI😞. Join https://t.me/MsSUPP0RT untuk info lebih lanjut"
                )
                sys.exit()

        if FSUB2:
            try:
                info = await self.get_chat(FSUB2)
                link = info.invite_link
                if not link:
                    await self.export_chat_invite_link(FSUB2)
                    link = info.invite_link
                self.invitelink2 = link
                self.LOGGER(__name__).info(
                    f"FSUB2 detected!\n┌ Title: {info.title}\n└ Chat ID: {info.id}\n——"
                )
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "BOT TIDAK BISA MENERIMA INVITE LINK DARI FSUB2"
                )
                self.LOGGER(__name__).warning(
                    f"JADIKAN @{self.username} SEBAGAI ADMIN DI FSUB2 JIKA SUDAH SILAKAN CEK KEMBALI😗: {FSUB2}"
                )
                self.LOGGER(__name__).info(
                    "BOT BERHENTI😞. Join https://t.me/MsSUPP0RT untuk info lebih lanjut"
                )
                sys.exit()

        if FSUB3:
            try:
                info = await self.get_chat(FSUB3)
                link = info.invite_link
                if not link:
                    await self.export_chat_invite_link(FSUB3)
                    link = info.invite_link
                self.invitelink3 = link
                self.LOGGER(__name__).info(
                    f"FSUB3 detected!\n┌ Title: {info.title}\n└ Chat ID: {info.id}\n——"
                )
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "BOT TIDAK BISA MENERIMA INVITE LINK DARI FSUB3"
                )
                self.LOGGER(__name__).warning(
                    f"JADIKAN @{self.username} SEBAGAI ADMIN DI FSUB3 JIKA SUDAH SILAKAN CEK KEMBALI😗: {FSUB3}"
                )
                self.LOGGER(__name__).info(
                    "BOT BERHENTI😞. Join https://t.me/MsSUPP0RT untuk info lebih lanjut"
                )
                sys.exit()

        if FSUB4:
            try:
                info = await self.get_chat(FSUB4)
                link = info.invite_link
                if not link:
                    await self.export_chat_invite_link(FSUB4)
                    link = info.invite_link
                self.invitelink4 = link
                self.LOGGER(__name__).info(
                    f"FSUB4 detected!\n┌ Title: {info.title}\n└ Chat ID: {info.id}\n——"
                )
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "BOT TIDAK BISA MENERIMA INVITE LINK DARI FSUB4"
                )
                self.LOGGER(__name__).warning(
                    f"JADIKAN @{self.username} SEBAGAI ADMIN DI FSUB4 JIKA SUDAH SILAKAN CEK KEMBALI😗: {FSUB4}"
                )
                self.LOGGER(__name__).info(
                    "BOT BERHENTI😞. Join https://t.me/MsSUPP0RT untuk info lebih lanjut"
                )
                sys.exit()

        if FSUB5:
            try:
                info = await self.get_chat(FSUB5)
                link = info.invite_link
                if not link:
                    await self.export_chat_invite_link(FSUB5)
                    link = info.invite_link
                self.invitelink5 = link
                self.LOGGER(__name__).info(
                    f"FSUB5 detected!\n┌ Title: {info.title}\n└ Chat ID: {info.id}\n——"
                )
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "BOT TIDAK BISA MENERIMA INVITE LINK DARI FSUB5"
                )
                self.LOGGER(__name__).warning(
                    f"JADIKAN @{self.username} SEBAGAI ADMIN DI FSUB5 JIKA SUDAH SILAKAN CEK KEMBALI😗: {FSUB5}"
                )
                self.LOGGER(__name__).info(
                    "BOT BERHENTI😞. Join https://t.me/MsSUPP0RT untuk info lebih lanjut"
                )
                sys.exit()

        if FSUB6:
            try:
                info = await self.get_chat(FSUB6)
                link = info.invite_link
                if not link:
                    await self.export_chat_invite_link(FSUB6)
                    link = info.invite_link
                self.invitelink6 = link
                self.LOGGER(__name__).info(
                    f"FSUB6 detected!\n┌ Title: {info.title}\n└ Chat ID: {info.id}\n——"
                )
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "BOT TIDAK BISA MENERIMA INVITE LINK DARI FSUB6"
                )
                self.LOGGER(__name__).warning(
                    f"JADIKAN @{self.username} SEBAGAI ADMIN DI FSUB6 JIKA SUDAH SILAKAN CEK KEMBALI😗: {FSUB6}"
                )
                self.LOGGER(__name__).info(
                    "BOT BERHENTI😞. Join https://t.me/MsSUPP0RT untuk info lebih lanjut"
                )
                sys.exit()

        if FSUB7:
            try:
                info = await self.get_chat(FSUB7)
                link = info.invite_link
                if not link:
                    await self.export_chat_invite_link(FSUB7)
                    link = info.invite_link
                self.invitelink7 = link
                self.LOGGER(__name__).info(
                    f"FSUB7 detected!\n┌ Title: {info.title}\n└ Chat ID: {info.id}\n——"
                )
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "BOT TIDAK BISA MENERIMA INVITE LINK DARI FSUB7"
                )
                self.LOGGER(__name__).warning(
                    f"JADIKAN @{self.username} SEBAGAI ADMIN DI FSUB7 JIKA SUDAH SILAKAN CEK KEMBALI😗: {FSUB7}"
                )
                self.LOGGER(__name__).info(
                    "BOT BERHENTI😞. Join https://t.me/MsSUPP0RT untuk info lebih lanjut"
                )
                sys.exit()

        if FSUB8:
            try:
                info = await self.get_chat(FSUB8)
                link = info.invite_link
                if not link:
                    await self.export_chat_invite_link(FSUB8)
                    link = info.invite_link
                self.invitelink8 = link
                self.LOGGER(__name__).info(
                    f"FSUB8 detected!\n┌ Title: {info.title}\n└ Chat ID: {info.id}\n——"
                )
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "BOT TIDAK BISA MENERIMA INVITE LINK DARI FSUB8"
                )
                self.LOGGER(__name__).warning(
                    f"JADIKAN @{self.username} SEBAGAI ADMIN DI FSUB8 JIKA SUDAH SILAKAN CEK KEMBALI😗: {FSUB8}"
                )
                self.LOGGER(__name__).info(
                    "BOT BERHENTI😞. Join https://t.me/MsSUPP0RT untuk info lebih lanjut"
                )
                sys.exit()

        if FSUB9:
            try:
                info = await self.get_chat(FSUB9)
                link = info.invite_link
                if not link:
                    await self.export_chat_invite_link(FSUB9)
                    link = info.invite_link
                self.invitelink9 = link
                self.LOGGER(__name__).info(
                    f"FSUB9 detected!\n┌ Title: {info.title}\n└ Chat ID: {info.id}\n——"
                )
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "BOT TIDAK BISA MENERIMA INVITE LINK DARI FSUB9"
                )
                self.LOGGER(__name__).warning(
                    f"JADIKAN @{self.username} SEBAGAI ADMIN DI FSUB9 JIKA SUDAH SILAKAN CEK KEMBALI😗: {FSUB9}"
                )
                self.LOGGER(__name__).info(
                    "BOT BERHENTI😞. Join https://t.me/MsSUPP0RT untuk info lebih lanjut"
                )
                sys.exit()

        if FSUB10:
            try:
                info = await self.get_chat(FSUB10)
                link = info.invite_link
                if not link:
                    await self.export_chat_invite_link(FSUB10)
                    link = info.invite_link
                self.invitelink10 = link
                self.LOGGER(__name__).info(
                    f"FSUB10 detected!\n┌ Title: {info.title}\n└ Chat ID: {info.id}\n——"
                )
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "BOT TIDAK BISA MENERIMA INVITE LINK DARI FSUB10"
                )
                self.LOGGER(__name__).warning(
                    f"JADIKAN @{self.username} SEBAGAI ADMIN DI FSUB10 JIKA SUDAH SILAKAN CEK KEMBALI😗: {FSUB10}"
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
            self.LOGGER(__name__).info(
                f"CHANNEL_ID Database detected!\n┌ Title: {db_channel.title}\n└ Chat ID: {db_channel.id}\n——"
            )
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
