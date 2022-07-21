import asyncio
import math
import os
import dotenv
import random
import shutil
from datetime import datetime
from time import strftime, time

import heroku3
import requests
import urllib3
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError
from pyrogram import Client, filters
from pyrogram.types import Message

from config import (HEROKU_API_KEY, HEROKU_APP_NAME, UPSTREAM_BRANCH,
                    UPSTREAM_REPO)
from Hero import LOG_GROUP_ID, MUSIC_BOT_NAME, SUDOERS, app
from Hero.Database import get_active_chats, remove_active_chat, remove_active_video_chat
from Hero.Utilities.heroku import is_heroku, user_input
from Hero.Utilities.paste import isPreviewUp, paste_queue

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


__MODULE__ = "sᴇʀᴠᴇʀ"
__HELP__ = f"""

**Note:**
**Only for Sudo Users**

/get_log
- Get log of last 100 lines from Heroku.

/get_var
- Get a config var from Heroku or .env.

/del_var
- Delete any var on Heroku or .env.

/set_var [Var Name] [Value]
- Set a Var or Update a Var on heroku or .env. Seperate Var and its Value with a space.

/usage
- Get Dyno Usage.

/update
- Update Your Bot.

/restart 
- Restart Bot [All downloads, cache, raw files will be cleared too]. 
"""


XCB = [
    "/",
    "@",
    ".",
    "com",
    ":",
    "git",
    "heroku",
    "push",
    str(HEROKU_API_KEY),
    "https",
    str(HEROKU_APP_NAME),
    "HEAD",
    "main",
]


@app.on_message(filters.command("get_log") & filters.user(SUDOERS))
async def log_(client, message):
    if await is_heroku():
        if HEROKU_API_KEY == "" and HEROKU_APP_NAME == "":
            return await message.reply_text(
                "<b>HEROKU APP DETECTED!</b>\n\nIɴ ᴏʀᴅᴇʀ ᴛᴏ ᴜᴘᴅᴀᴛᴇ ʏᴏᴜʀ ᴀᴘᴘ, ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ sᴇᴛᴜᴘ ᴛʜᴇ `HEROKU_API_KEY` ᴀɴᴅ `HEROKU_APP_NAME` ᴠᴀʀs ʀᴇsᴘᴇᴄᴛɪᴠᴇʟʏ!"
            )
        elif HEROKU_API_KEY == "" or HEROKU_APP_NAME == "":
            return await message.reply_text(
                "<b>HEROKU APP DETECTED!</b>\n\n<b>Mᴀᴋᴇ sᴜʀᴇ ᴛᴏ ᴀᴅᴅ ʙᴏᴛʜ</b> `HEROKU_API_KEY` **ᴀɴᴅ** `HEROKU_APP_NAME` <b>ᴠᴀʀs ᴄᴏʀʀᴇᴄᴛʟʏ ɪɴ ᴏʀᴅᴇʀ ᴛᴏ ʙᴇ ᴀʙʟᴇ ᴛᴏ ᴜᴘᴅᴀᴛᴇ ʀᴇᴍᴏᴛᴇʟʏ!</b>"
            )
    else:
        return await message.reply_text("Oɴʟʏ ғᴏʀ ʜᴇʀᴏᴋᴜ ᴀᴘᴘs")
    try:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        happ = Heroku.app(HEROKU_APP_NAME)
    except BaseException:
        return await message.reply_text(
            " Pʟᴇᴀsᴇ, ᴍᴀᴋᴇ sᴜʀᴇ ʏᴏᴜʀ ʜᴇʀᴏᴋᴜ API ᴋᴇʏ, Yᴏᴜʀ ᴀᴘᴘ ɴᴀᴍᴇ ᴀʀᴇ ᴄᴏɴғɪɢᴜʀᴇᴅ ᴄᴏʀʀᴇᴄᴛʟʏ ɪɴ ᴛʜᴇ ʜᴇʀᴏᴋᴜ"
        )
    data = happ.get_log()
    if len(data) > 1024:
        link = await paste_queue(data)
        url = link + "/index.txt"
        return await message.reply_text(
            f"Hᴇʀᴇ ɪs ᴛʜᴇ ʟᴏɢ ғᴏʀ ʏᴏᴜʀ ᴀᴘᴘ [{HEROKU_APP_NAME}]\n\n[Cʟɪᴄᴋ ʜᴇʀᴇᴇᴇᴇᴇ]({url})"
        )
    else:
        return await message.reply_text(data)


@app.on_message(filters.command("get_var") & filters.user(SUDOERS))
async def varget_(client, message):
    usage = "**Usᴀɢᴇ:**\n/get_var [Var Name]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    check_var = message.text.split(None, 2)[1]
    if await is_heroku():
        if HEROKU_API_KEY == "" and HEROKU_APP_NAME == "":
            return await message.reply_text(
                "<b>HEROKU APP DETECTED!</b>\n\nIɴ ᴏʀᴅᴇʀ ᴛᴏ ᴜᴘᴅᴀᴛᴇ ʏᴏᴜʀ ᴀᴘᴘ, ʏᴘᴜ ɴᴇᴇᴅ ᴛᴏ sᴇᴛᴜᴘ ᴛʜᴇ `HEROKU_API_KEY` ᴀɴᴅ `HEROKU_APP_NAME` ᴠᴀʀs ʀᴇsᴘᴇᴄᴛɪᴠᴇʟʏ!"
            )
        elif HEROKU_API_KEY == "" or HEROKU_APP_NAME == "":
            return await message.reply_text(
                "<b>HEROKU APP DETECTED!</b>\n\n<b>Mᴀᴋᴇ sᴜʀᴇ ᴛᴏ ᴀᴅᴅ ʙᴏᴛʜ</b> `HEROKU_API_KEY` **ᴀɴᴅ** `HEROKU_APP_NAME` <b>ᴠᴀʀs ᴄᴏʀʀᴇᴄᴛʟʏ ɪɴ ᴏʀᴅᴇʀ ᴛᴏ ʙᴇ ᴀʙʟᴇ ᴛᴏ ᴜᴘᴅᴀᴛᴇ ʀᴇᴍᴏᴛᴇʟʏ!</b>"
            )
        try:
            Heroku = heroku3.from_key(HEROKU_API_KEY)
            happ = Heroku.app(HEROKU_APP_NAME)
        except BaseException:
            return await message.reply_text(
                " Pʟᴇᴀsᴇ, ᴍᴀᴋᴇ sᴜʀᴇ ʏᴏᴜʀ ʜᴇʀᴏᴋᴜ API ᴋᴇʏ, Yᴏᴜʀ ᴀᴘᴘ ɴᴇ ᴀʀᴇ ᴄᴏɴғɪɢᴜʀᴇᴅ ᴄᴏʀʀᴇᴄᴛʟʏ ɪɴ ᴛʜᴇ ʜᴇʀᴏᴋᴜ"
            )
        heroku_config = happ.config()
        if check_var in heroku_config:
            return await message.reply_text(
                f"**Hᴇʀᴏᴋᴜ ᴄᴏɴғɪɢ:**\n\n**{check_var}:** `{heroku_config[check_var]}`"
            )
        else:
            return await message.reply_text("Nᴏ sᴜᴄʜ ᴠᴀʀ")
    else:
        path = dotenv.find_dotenv()
        if not path:
            return await message.reply_text(".env ɴᴏᴛ ғᴏᴜɴᴅ.")
        output = dotenv.get_key(path, check_var)
        if not output:
            return await message.reply_text("Nᴏ sᴜᴄʜ ᴠᴀʀ")
        else:
            return await message.reply_text(f".env:\n\n**{check_var}:** `{str(output)}`")


@app.on_message(filters.command("del_var") & filters.user(SUDOERS))
async def vardel_(client, message):
    usage = "**Usᴀɢᴇ:**\n/del_var [Var Name]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    check_var = message.text.split(None, 2)[1]
    if await is_heroku():
        if HEROKU_API_KEY == "" and HEROKU_APP_NAME == "":
            return await message.reply_text(
                "<b>HEROKU APP DETECTED!</b>\n\nIɴ ᴏʀᴅᴇʀ ᴛᴏ ᴜᴘᴅᴀᴛᴇ ʏᴏᴜʀ ᴀᴘᴘ, ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ sᴇᴛᴜᴘ ᴛʜᴇ `HEROKU_API_KEY` ᴀɴᴅ `HEROKU_APP_NAME` ᴠᴀʀs ʀᴇsᴘᴇᴄᴛɪᴠᴇʟʏ!"
            )
        elif HEROKU_API_KEY == "" or HEROKU_APP_NAME == "":
            return await message.reply_text(
                "<b>HEROKU APP DETECTED!</b>\n\n<b>Mᴀᴋᴇ sᴜʀᴇ ᴛᴏ ᴀᴅᴅ ʙᴏᴛʜ</b> `HEROKU_API_KEY` **ᴀɴᴅ** `HEROKU_APP_NAME` <b>ᴠᴀʀs ᴄᴏʀʀᴇᴄᴛʟʏ ɪɴ ᴏʀᴅᴇʀ ᴛᴏ ʙᴇ ᴀʙʟᴇ ᴛᴏ ᴜᴘᴅᴀᴛᴇ ʀᴇᴍᴏᴛᴇʟʏ!</b>"
            )
        try:
            Heroku = heroku3.from_key(HEROKU_API_KEY)
            happ = Heroku.app(HEROKU_APP_NAME)
        except BaseException:
            return await message.reply_text(
                " Pʟᴇᴀsᴇ, Mᴀᴋᴇ sᴜʀᴇ ʏᴏᴜʀ ʜᴇʀᴏᴋᴜ API ᴋᴇʏ, Yᴏᴜʀ ᴀᴘᴘ ɴᴀᴍᴇ ᴀʀᴇ ᴄᴏɴғɪɢᴜʀᴇᴅ ᴄᴏʀʀᴇᴄᴛʟʏ ɪɴ ᴛʜᴇ ʜᴇʀᴏᴋᴜ"
            )
        heroku_config = happ.config()
        if check_var in heroku_config:
            await message.reply_text(
                f"**HEROKU VAR DELETION:**\n\n`{check_var}` ʜᴀs ʙᴇᴇɴ ᴅᴇʟᴇᴛᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ☑️"
            )
            del heroku_config[check_var]
        else:
            return await message.reply_text(f"Nᴏ sᴜᴄʜ ᴠᴀʀ")
    else:
        path = dotenv.find_dotenv()
        if not path:
            return await message.reply_text(".env ɴᴏᴛ ғᴏᴜɴᴅ.")
        output = dotenv.unset_key(path, check_var)
        if not output[0]:
            return await message.reply_text("Nᴏ sᴜᴄʜ ᴠᴀʀ")
        else:
            return await message.reply_text(f".env VAR DELETION:\n\n`{check_var}` ʜᴀs ʙᴇᴇɴ ᴅᴇʟᴇᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ☑️. Tᴏ ʀᴇsᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ, ᴛᴏᴜᴄʜ /restart ᴄᴏᴍᴍᴀɴᴅ.")


@app.on_message(filters.command("set_var") & filters.user(SUDOERS))
async def set_var(client, message):
    usage = "**Usᴀɢᴇ:**\n/set_var [Var Name] [Var Value]"
    if len(message.command) < 3:
        return await message.reply_text(usage)
    to_set = message.text.split(None, 2)[1].strip()
    value = message.text.split(None, 2)[2].strip()
    if await is_heroku():
        if HEROKU_API_KEY == "" and HEROKU_APP_NAME == "":
            return await message.reply_text(
                "<b>HEROKU APP DETECTED!</b>\n\nIɴ ᴏʀᴅᴇʀ ᴛᴏ ᴜᴘᴅᴀᴛᴇ ʏᴏᴜʀ ᴀᴘᴘ, ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ sᴇᴛ ᴜᴘ ᴛʜᴇ `HEROKU_API_KEY` ᴀɴᴅ `HEROKU_APP_NAME` ᴠᴀʀs ʀᴇsᴘᴇᴄᴛɪᴠᴇʟʏ!"
            )
        elif HEROKU_API_KEY == "" or HEROKU_APP_NAME == "":
            return await message.reply_text(
                "<b>HEROKU APP DETECTED!</b>\n\n<b>Mᴀᴋᴇ sᴜʀᴇ ᴛᴏ ᴀᴅᴅ ʙᴏᴛʜ</b> `HEROKU_API_KEY` **ᴀɴᴅ** `HEROKU_APP_NAME` <b>ᴠᴀʀs ᴄᴏʀʀᴇᴄᴛʟʏ ɪɴ ᴏʀᴅᴇʀ ᴛᴏ ʙᴇ ᴀʙʟᴇ ᴛᴏ ᴜᴘᴅᴀᴛᴇ ʀᴇᴍᴏᴛᴇʟʏ!</b>"
            )
        try:
            Heroku = heroku3.from_key(HEROKU_API_KEY)
            happ = Heroku.app(HEROKU_APP_NAME)
        except BaseException:
            return await message.reply_text(
                " Pʟᴇᴀsᴇ, ᴍᴀᴋᴇ sᴜʀᴇ ʏᴏᴜʀ ʜᴇʀᴏᴋᴜ API ᴋᴇʏ, Yᴏᴜʀ ᴀᴘᴘ ɴᴀᴍᴇ ᴀʀᴇ ᴄᴏɴғɪɢᴜʀᴇᴅ ᴄᴏʀʀᴇᴄᴛʟʏ ɪɴ ᴛʜᴇ ʜᴇʀᴏᴋᴜ"
            )
        heroku_config = happ.config()
        if to_set in heroku_config:
            await message.reply_text(
                f"**HEROKU VAR UPDATION:**\n\n`{to_set}` ʜᴀs ʙᴇᴇɴ ᴜᴘᴅᴀᴛᴇᴅ sᴜᴄᴄᴇsғᴜʟʟʏ ✅ Bᴏᴛ ᴡɪʟʟ ʀᴇsᴛᴀʀᴛ ɴᴏᴡ..."
            )
        else:
            await message.reply_text(
                f"Aᴅᴅᴇᴅ ɴᴇᴡ ᴠᴀʀ ᴡɪᴛʜ ɴᴀᴍᴇ `{to_set}`. Bᴏᴛ ᴡɪʟʟ ʀᴇsᴛᴀʀᴛ ɴᴏᴡ..."
            )
        heroku_config[to_set] = value
    else:
        path = dotenv.find_dotenv()
        if not path:
            return await message.reply_text(".env ɴᴏᴛ ғᴏᴜɴᴅ.")
        output = dotenv.set_key(path, to_set, value)
        if dotenv.get_key(path, to_set):
            return await message.reply_text(f"**.ENV VAR UPDATION:**\n\n`{to_set}`ʜᴀs ʙᴇᴇɴ ᴜᴘᴅᴀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ✅. Tᴏ ʀᴇsᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ, ᴛᴏᴜᴄʜ /restart ᴄᴏᴍᴍᴀɴᴅ.")
        else:
            return await message.reply_text(f"**.env dəyişən əlavə edilməsi:**\n\n`{to_set}` ʜᴀs ʙᴇᴇɴ ᴀᴅᴅᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ✅. Tᴏ ʀᴇsᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ, ᴛᴏᴜᴄʜ /restart ᴄᴏᴍᴍᴀɴᴅ.")


@app.on_message(filters.command("usage") & filters.user(SUDOERS))
async def usage_dynos(client, message):
    ### Credits CatUserbot
    if await is_heroku():
        if HEROKU_API_KEY == "" and HEROKU_APP_NAME == "":
            return await message.reply_text(
                "<b>HEROKU APP DETECTED!</b>\n\nIɴ ᴏʀᴅᴇʀ ᴛᴏ ᴜᴘᴅᴀᴛᴇ ʏᴏᴜʀ ᴀᴘᴘ, ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ sᴇᴛᴜᴘ ᴛʜᴇ `HEROKU_API_KEY` ᴀɴᴅ `HEROKU_APP_NAME` ᴠᴀʀs ʀᴇsᴘᴇᴄᴛɪᴠᴇʟʏ!"
            )
        elif HEROKU_API_KEY == "" or HEROKU_APP_NAME == "":
            return await message.reply_text(
                "<b>HEROKU APP DETECTED!</b>\n\n<b>Mᴀᴋᴇ sᴜʀᴇ ᴛᴏ ᴀᴅᴅ ʙᴏᴛʜ</b> `HEROKU_API_KEY` **ᴀɴᴅ** `HEROKU_APP_NAME` <b>ᴠᴀʀs ᴄᴏʀʀᴇᴄᴛʟʏ ɪɴ ᴏʀᴅᴇʀ ᴛᴏ ʙᴇ ᴀʙʟᴇ ᴛᴏ ᴜᴘᴅᴀᴛᴇ ʀᴇᴍᴏᴛᴇʟʏ!</b>"
            )
    else:
        return await message.reply_text("Oɴʟʏ ғᴏʀ ʜᴇʀᴏᴋᴜ ᴀᴘᴘs...")
    try:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        happ = Heroku.app(HEROKU_APP_NAME)
    except BaseException:
        return await message.reply_text(
            " Pʟᴇᴀsᴇ, Mᴀᴋᴇ sᴜʀᴇ ʏᴘᴜʀ ʜᴇʀᴏᴋᴜ API ᴋᴇʏ, Yᴏᴜʀ ᴀᴘᴘ ɴᴀᴍᴇ ᴀʀᴇ ᴄᴏɴғɪɢᴜʀᴇᴅ ᴄᴏʀʀᴇᴄᴛʟʏ ɪɴ ᴛʜᴇ ʜᴇʀᴏᴋᴜ"
        )
    dyno = await message.reply_text("Cʜᴇᴄᴋɪɴɢ ʜᴇʀᴏᴋᴜ ᴜsᴀɢᴇ...Pʟᴇᴀsᴇ ᴡᴀɪᴛ")
    account_id = Heroku.account().id
    useragent = (
        "Mozilla/5.0 (Linux; Android 10; SM-G975F) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/80.0.3987.149 Mobile Safari/537.36"
    )
    headers = {
        "User-Agent": useragent,
        "Authorization": f"Bearer {HEROKU_API_KEY}",
        "Accept": "application/vnd.heroku+json; version=3.account-quotas",
    }
    path = "/accounts/" + account_id + "/actions/get-quota"
    r = requests.get("https://api.heroku.com" + path, headers=headers)
    if r.status_code != 200:
        return await dyno.edit("Unable to fetch.")
    result = r.json()
    quota = result["account_quota"]
    quota_used = result["quota_used"]
    remaining_quota = quota - quota_used
    percentage = math.floor(remaining_quota / quota * 100)
    minutes_remaining = remaining_quota / 60
    hours = math.floor(minutes_remaining / 60)
    minutes = math.floor(minutes_remaining % 60)
    App = result["apps"]
    try:
        App[0]["quota_used"]
    except IndexError:
        AppQuotaUsed = 0
        AppPercentage = 0
    else:
        AppQuotaUsed = App[0]["quota_used"] / 60
        AppPercentage = math.floor(App[0]["quota_used"] * 100 / quota)
    AppHours = math.floor(AppQuotaUsed / 60)
    AppMinutes = math.floor(AppQuotaUsed % 60)
    await asyncio.sleep(1.5)
    text = f"""
**DYNO USAGE**

<u>Usᴀɢᴇ:</u>
Tᴏᴛᴀʟ ᴜsᴇᴅ: `{AppHours}`**ʜ**  `{AppMinutes}`**ᴍ**  [`{AppPercentage}`**%**]

<u>Rᴇᴍᴀɪɴɪɴɢ ǫᴜᴏᴛᴀ:</u>
Tᴏᴛᴀʟ ʟᴇғᴛ: `{hours}`**ʜ**  `{minutes}`**ᴍ**  [`{percentage}`**%**]"""
    return await dyno.edit(text)


@app.on_message(filters.command("update") & filters.user(SUDOERS))
async def update_(client, message):
    if await is_heroku():
        if HEROKU_API_KEY == "" and HEROKU_APP_NAME == "":
            return await message.reply_text(
                "<b>HEROKU APP DETECTED!</b>\n\nIɴ ᴏʀᴅᴇʀ ᴛᴏ ᴜᴘᴅᴀᴛᴇ ʏᴏᴜʀ ᴀᴘᴘ, ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ sᴇᴛᴜᴘ ᴛʜᴇ `HEROKU_API_KEY` ᴀɴᴅ `HEROKU_APP_NAME` ᴠᴀʀs ʀᴇsᴘᴇᴄᴛɪᴠᴇʟʏ!"
            )
        elif HEROKU_API_KEY == "" or HEROKU_APP_NAME == "":
            return await message.reply_text(
                "<b>HEROKU APP DETECTED!</b>\n\n<b>Mᴀᴋᴇ sᴜʀᴇ ᴛᴏ ᴀᴅᴅ ʙᴏᴛʜ</b> `HEROKU_API_KEY` **ᴀɴᴅ** `HEROKU_APP_NAME` <b>ᴠᴀʀs ᴄᴏʀʀᴇᴄᴛʟʏ ɪɴ ᴏʀᴅᴇʀ ᴛᴏ ʙᴇ ᴀʙʟᴇ ᴛᴏ ᴜᴘᴅᴀᴛᴇ ᴛʜᴇ ʙᴏᴛ ʀᴇᴍᴏᴛᴇʟʏ!</b>"
            )
    response = await message.reply_text("Cʜᴇᴄᴋɪɴɢ ғᴏʀ ᴀᴠᴀɪʟᴀʙʟᴇ ᴜᴘᴅᴀᴛᴇs..")
    try:
        repo = Repo()
    except GitCommandError:
        return await response.edit("Git Command Error")
    except InvalidGitRepositoryError:
        return await response.edit("Invalid Git Repsitory")
    to_exc = f"git fetch origin {UPSTREAM_BRANCH} &> /dev/null"
    os.system(to_exc)
    await asyncio.sleep(7)
    verification = ""
    REPO_ = repo.remotes.origin.url.split(".git")[0]  # main git repository
    for checks in repo.iter_commits(f"HEAD..origin/{UPSTREAM_BRANCH}"):
        verification = str(checks.count())
    if verification == "":
        return await response.edit("Bᴏᴛ ɪs ᴀʟʀᴇᴀᴅʏ ᴜᴘ-ᴛᴏ-ᴅᴀᴛᴇ!")
    updates = ""
    ordinal = lambda format: "%d%s" % (
        format,
        "tsnrhtdd"[
            (format // 10 % 10 != 1) * (format % 10 < 4) * format % 10 :: 4
        ],
    )
    for info in repo.iter_commits(f"HEAD..origin/{UPSTREAM_BRANCH}"):
        updates += f"<b>➣ #{info.count()}: [{info.summary}]({REPO_}/commit/{info}) ʙʏ -> {info.author}</b>\n\t\t\t\t<b>➥ Cᴏᴍᴍɪᴛᴇᴅ ᴏɴ:</b> {ordinal(int(datetime.fromtimestamp(info.committed_date).strftime('%d')))} {datetime.fromtimestamp(info.committed_date).strftime('%b')}, {datetime.fromtimestamp(info.committed_date).strftime('%Y')}\n\n"
    _update_response_ = "<b>A ɴᴇᴡ ᴜᴘᴅᴀᴛᴇ ɪs ᴀᴠᴀɪʟᴀʙʟᴇ ғᴏʀ ᴛʜᴇ ʙᴏᴛ!</b>\n\n➣ Pᴜsʜɪɴɢ ᴜᴘᴅᴀᴛᴇs ɴᴏᴡ</code>\n\n**<u>Uᴘᴅᴀᴛᴇs:</u>**\n\n"
    _final_updates_ = _update_response_ + updates
    if len(_final_updates_) > 4096:
        link = await paste_queue(updates)
        url = link + "/index.txt"
        nrs = await response.edit(
            f"<b>A ɴᴇᴡ ᴜᴘᴅᴀᴛᴇ ɪs ᴀᴠᴀɪʟᴀʙʟᴇ ғᴏʀ ᴛʜᴇ ʙᴏᴛ!</b>\n\n➣ Pᴜsʜɪɴɢ ᴜᴘᴅᴀᴛᴇs ɴᴏᴡ</code>\n\n**<u>Uᴘᴅᴀᴛᴇs:</u>**\n\n[Click Here to checkout Updates]({url})"
        )
    else:
        nrs = await response.edit(
            _final_updates_, disable_web_page_preview=True
        )
    os.system("git stash &> /dev/null && git pull")
    if await is_heroku():
        try:
            await response.edit(
                f"{nrs.text}\n\nBᴏᴛ ᴡᴀs ᴜᴘᴅᴀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ᴏɴ ʜᴇʀᴏᴋᴜ! Nᴏᴡ, ᴡᴀɪᴛ ғᴏʀ 2 - 3 ᴍɪɴs ᴜɴᴛɪʟ ᴛʜᴇ ʙᴏᴛ ʀᴇsᴛᴀʀᴛs ɪᴛsᴇʟғ!"
            )
            os.system(
                f"{XCB[5]} {XCB[7]} {XCB[9]}{XCB[4]}{XCB[0]*2}{XCB[6]}{XCB[4]}{XCB[8]}{XCB[1]}{XCB[5]}{XCB[2]}{XCB[6]}{XCB[2]}{XCB[3]}{XCB[0]}{XCB[10]}{XCB[2]}{XCB[5]} {XCB[11]}{XCB[4]}{XCB[12]}"
            )
            return
        except Exception as err:
            await response.edit(
                f"{nrs.text}\n\nSomething went wrong while initiating reboot! Please try again later or check logs for more info."
            )
            return await app.send_message(
                LOG_GROUP_ID,
                f"AN EXCEPTION OCCURRED AT #UPDATER DUE TO: <code>{err}</code>",
            )
    else:
        await response.edit(
            f"{nrs.text}\n\nBᴏᴛ ᴡᴀs ᴜᴘᴅᴀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ✅! Nᴏᴡ, ᴡᴀɪᴛ ғᴏʀ 1 - 2 ᴍɪɴs ᴜɴᴛɪʟ ᴛʜᴇ ʙᴏᴛ ʀᴇʙᴏᴏᴛs ɪᴛsᴇʟғ!"
        )
        os.system("pip3 install -r requirements.txt")
        os.system(f"kill -9 {os.getpid()} && bash start")
        exit()
    return


@app.on_message(filters.command("restart") & filters.user(SUDOERS))
async def restart_(_, message):
    response = await message.reply_text("Rᴇsᴛᴀʀᴛɪɴɢ....")
    if await is_heroku():
        if HEROKU_API_KEY == "" and HEROKU_APP_NAME == "":
            return await message.reply_text(
                "<b>HEROKU APP DETECTED!</b>\n\nIɴ ᴏʀᴅᴇʀ ᴛᴏ ʀᴇsᴛᴀʀᴛ ʏᴏᴜʀ ᴀᴘᴘ, ʏᴏᴜ ғɪʀsᴛ ɴᴇᴇᴅ ᴛᴏ sᴇᴛᴜᴘ ᴛʜᴇ `HEROKU_API_KEY` ᴀɴᴅ `HEROKU_APP_NAME` ᴠᴀʀs ʀᴇsᴘᴇᴄᴛᴏᴠᴇʟʏ!"
            )
        elif HEROKU_API_KEY == "" or HEROKU_APP_NAME == "":
            return await message.reply_text(
                "<b>HEROKU APP DETECTED!</b>\n\n<b>Mᴀᴋᴇ sᴜʀᴇ ᴛᴏ ᴀᴅᴅ ʙᴏᴛʜ</b> `HEROKU_API_KEY` **ᴀɴᴅ** `HEROKU_APP_NAME` <b>ᴠᴀʀs ᴄᴏʀʀᴇᴄᴛʟʏ ɪɴ ᴏʀᴅᴇʀ ᴛᴏ ʙᴇ ᴀʙʟᴇ ᴛᴏ ʀᴇsᴛᴀʀᴛ ʀᴇᴍᴏᴛᴇʟʏ!</b>"
            )
        try:
            served_chats = []
            try:
                chats = await get_active_chats()
                for chat in chats:
                    served_chats.append(int(chat["chat_id"]))
            except Exception as e:
                pass
            for x in served_chats:
                try:
                    await app.send_message(
                        x,
                        f"{MUSIC_BOT_NAME} ʜᴀs ᴊᴜsᴛ ʀᴇsᴛᴀʀᴛᴇᴅ ɪᴛsᴇʟғ. Wᴇ ʀ sᴏʀʀʏ ғᴏʀ ᴛʜᴇ ɪssᴜᴇs.\n\nSᴛᴀʀᴛ ᴘʟᴀʏɪɴɢ ᴀғᴛᴇʀ 10-15 sᴇᴄᴏɴᴅs ᴀɢᴀɪɴ",
                    )
                    await remove_active_chat(x)
                    await remove_active_video_chat(x)
                except Exception:
                    pass
            heroku3.from_key(HEROKU_API_KEY).apps()[HEROKU_APP_NAME].restart()
            await response.edit(
                "**Hᴇʀᴏᴋᴜ ʀᴇsᴛᴀʀᴛ 🔄**\n\nRᴇʙᴏᴏᴛ ʜᴀs ʙᴇᴇɴ ɪɴɪᴛɪᴀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ✅! Wᴀɪᴛ ғᴏʀ 1 - 2 ᴍɪɴᴜᴛᴇs ᴜɴᴛɪʟ ᴛʜᴇ ʙᴏᴛ ʀᴇsᴛᴀʀᴛs ɪᴛsᴇʟғ."
            )
            return
        except Exception as err:
            await response.edit(
                "Sᴏᴍᴇᴛʜɪɴɢ ʀᴇᴀʟʟʏ ᴡᴇɴᴛ ᴡʀᴏɴɢ ᴡʜɪʟᴇ ɪɴɪᴛɪᴀᴛɪɴɢ ʀᴇʙᴏᴏᴛ! Pʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ ʟᴀᴛᴇʀ ᴏʀ ᴄʜᴇᴄᴋ ʟᴏɢs ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏ."
            )
            return
    else:
        served_chats = []
        try:
            chats = await get_active_chats()
            for chat in chats:
                served_chats.append(int(chat["chat_id"]))
        except Exception as e:
            pass
        for x in served_chats:
            try:
                await app.send_message(
                    x,
                    f"{MUSIC_BOT_NAME} ʜᴀs ᴊᴜsᴛ ʀᴇsᴛᴀʀᴛᴇᴅ ɪᴛsᴇʟғ. Wᴇ ʀ sᴏʀʀʏ ғᴏʀ ᴛʜᴇ ɪssᴜᴇs.\n\nSᴛᴀʀᴛ ᴘʟᴀʏɪɴɢ ᴀғᴛᴇʀ 10-15 sᴇᴄᴏɴᴅs ᴀɢᴀɪɴ.",
                )
                await remove_active_chat(x)
                await remove_active_video_chat(x)
            except Exception:
                pass
        A = "downloads"
        B = "raw_files"
        C = "cache"
        D = "search"
        try:
            shutil.rmtree(A)
            shutil.rmtree(B)
            shutil.rmtree(C)
            shutil.rmtree(D)
        except:
            pass
        await asyncio.sleep(2)
        try:
            os.mkdir(A)
        except:
            pass
        try:
            os.mkdir(B)
        except:
            pass
        try:
            os.mkdir(C)
        except:
            pass
        try:
            os.mkdir(D)
        except:
            pass
        await response.edit(
            "Rᴇʙᴏᴏᴛ ʜᴀs ʙᴇᴇɴ ɪɴɪᴛɪᴀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ✅! Wᴀɪᴛ ғᴏʀ 1 - 2 ᴍɪɴᴜᴛᴇs ᴜɴᴛɪʟ ᴛʜᴇ ʙᴏᴛ ʀᴇsᴛᴀʀᴛs ɪᴛsᴇʟғ."
        )
        os.system(f"kill -9 {os.getpid()} && bash start")
