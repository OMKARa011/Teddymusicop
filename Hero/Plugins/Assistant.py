import random

from pyrogram import filters
from pyrogram.raw.functions.messages import DeleteHistory
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InlineQueryResultArticle,
                            InlineQueryResultPhoto, InputTextMessageContent,
                            Message)

from Hero import SUDOERS, app, random_assistant
from Hero.Database import get_assistant, save_assistant
from Hero.Utilities.assistant import get_assistant_details

__MODULE__ = "ᴀssɪsᴛᴀɴᴛ"
__HELP__ = f"""


`/checkassistant`
- ᴄʜᴇᴄᴋ ᴛʜᴇ ᴀʟʟᴏᴛᴇᴅ ᴀssɪsᴛᴀɴᴛ ᴏғ ʏᴏᴜʀ ᴄʜᴀᴛ


**ɴᴏᴛᴇ:**
-ᴏɴʟʏy ғᴏʀ sᴜᴅᴏ ᴜsᴇʀs

`/block` [ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ ᴍᴇssᴀɢᴇ] 
- ʙʟᴏᴄᴋs ᴛʜᴇ ᴜsᴇʀ ғʀᴏᴍ ᴀssɪsᴛᴀɴᴛ ᴀᴄᴄᴏᴜɴᴛ.

`/unblock` [ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ ᴍᴇssᴀɢᴇ] 
- ᴜɴʙʟᴏᴄᴋs ᴛʜᴇ ᴜsᴇʀ ғʀᴏᴍ ᴀssɪsᴛᴀɴᴛ ᴀᴄᴄᴏᴜɴᴛ.

`/approve` [ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ ᴍᴇssᴀɢᴇ] 
- ᴀᴘᴘʀᴏᴠᴇs ᴛʜᴇ ᴜsᴇʀ ғᴏʀ ᴅᴍ.

`/disapprove` [ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ ᴍᴇssᴀɢᴇ] 
- ᴅɪsᴀᴘᴘʀᴏᴠᴇs ᴛʜᴇ ᴜsᴇʀ ғᴏʀ ᴅᴍ.

`/pfp` [ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴘʜᴏᴛᴏ] 
- ᴄʜᴀɴɢᴇs ᴀssɪsᴛᴀɴᴛ ᴀᴄᴄᴏᴜɴᴛ ᴘғᴘ.

`/bio` [ʙɪᴏ ᴛᴇxᴛ] 
- ᴄʜᴀɴɢᴇs ʙɪᴏ ᴏғ ᴀssɪsᴛᴀɴᴛ ᴀᴄᴄᴏᴜɴᴛ.

`/changeassistant` [ASS NUMBER]
- ᴄʜᴀɴɢᴇ ᴛʜᴇ ᴘʀᴇᴠɪᴏɪᴜs ᴀʟʟᴏᴛᴇᴅ ᴀssɪsᴛᴀɴᴛ ᴛᴏ ɴᴇᴡ ᴏɴᴇ.

`/setassistant` [ᴀss ɴᴜᴍʙᴇʀ ᴏʀ ʀᴀɴᴅᴏᴍ]
- sᴇᴛ ᴀ ᴀssɪsᴛᴀɴᴛ ᴀᴄᴄᴏᴜɴᴛ ғᴏʀ ᴄʜᴀᴛ. 
"""


ass_num_list = ["1", "2", "3", "4", "5"]


@app.on_message(filters.command(["change", "changeassistant"]) & filters.user(SUDOERS))
async def assis_change(_, message: Message):
    usage = f"**Usage:**\n/changeassistant [ASS_NO]\n\nSelect from them\n{' | '.join(ass_num_list)}"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    num = message.text.split(None, 1)[1].strip()
    if num not in ass_num_list:
        return await message.reply_text(usage)
    ass_num = int(message.text.strip().split()[1])
    _assistant = await get_assistant(message.chat.id, "assistant")
    if not _assistant:
        return await message.reply_text(
            "No Pre-Saved Assistant Found.\n\nYou can set Assistant Via /setassistant"
        )
    else:
        ass = _assistant["saveassistant"]
    assis = {
        "saveassistant": ass_num,
    }
    await save_assistant(message.chat.id, "assistant", assis)
    await message.reply_text(
        f"**Changed Assistant**\n\nChanged Assistant Account from **{ass}** to Assistant Number **{ass_num}**"
    )


ass_num_list2 = ["1", "2", "3", "4", "5", "Random"]


@app.on_message(filters.command(["set", "setassistant"]) & filters.user(SUDOERS))
async def assis_change(_, message: Message):
    usage = f"**Usage:**\n/setassistant [ASS_NO or Random]\n\nSelect from them\n{' | '.join(ass_num_list2)}\n\nUse 'Random' to set random Assistant"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    query = message.text.split(None, 1)[1].strip()
    if query not in ass_num_list2:
        return await message.reply_text(usage)
    if str(query) == "Random":
        ran_ass = random.choice(random_assistant)
    else:
        ran_ass = int(message.text.strip().split()[1])
    _assistant = await get_assistant(message.chat.id, "assistant")
    if not _assistant:
        await message.reply_text(
            f"**__Yukki Music Bot Assistant Alloted__**\n\nAssistant No. **{ran_ass}**"
        )
        assis = {
            "saveassistant": ran_ass,
        }
        await save_assistant(message.chat.id, "assistant", assis)
    else:
        ass = _assistant["saveassistant"]
        return await message.reply_text(
            f"Pre-Saved Assistant Number {ass} Found.\n\nYou can change Assistant Via /changeassistant"
        )


@app.on_message(filters.command("checkassistant") & filters.group)
async def check_ass(_, message: Message):
    _assistant = await get_assistant(message.chat.id, "assistant")
    if not _assistant:
        return await message.reply_text(
            "No Pre-Saved Assistant Found.\n\nYou can set Assistant Via /play"
        )
    else:
        ass = _assistant["saveassistant"]
        return await message.reply_text(
            f"Pre-Saved Assistant Found\n\nAssistanty Number {ass} "
        )
