from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

from config import MUSIC_BOT_NAME, SUPPORT_CHANNEL, SUPPORT_GROUP
from Hero import BOT_USERNAME


def setting_markup2():
    buttons = [
        [
            InlineKeyboardButton(text="📼 ᴀᴜᴅɪᴏ ǫᴜᴀʟɪᴛʏ", callback_data="AQ"),
            InlineKeyboardButton(text="🎛️ ᴀᴜᴅɪᴏ ᴠᴏʟᴜᴍᴇ", callback_data="AV"),
        ],
        [
            InlineKeyboardButton(
                text="👥 ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴜsᴇʀs", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="🖥️ ᴅᴀsʜʙᴏᴀʀᴅ", callback_data="Dashboard"
            ),
        ],
        [
            InlineKeyboardButton(text="🗑️ Cʟᴏsᴇ", callback_data="close"),
        ],
    ]
    return f"⚙️  **{MUSIC_BOT_NAME} sᴇᴛᴛɪɴɢs**", buttons


def start_pannel():
    if not SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Hᴇʟᴘᴇʀ ᴄᴏᴍᴍᴀɴᴅs ᴍᴇɴᴜ", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="⚙️ Sᴇᴛᴛɪɴɢs", callback_data="settingm"
                )
            ],
        ]
        return f"🎛  **Tʜɪs ɪs {MUSIC_BOT_NAME}**", buttons
    if not SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Hᴇʟᴘᴇʀ ᴄᴏᴍᴍᴀɴᴅs ᴍᴇɴᴜ", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="⚙️ Sᴇᴛᴛɪɴɢs", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🌸 Sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛  **Tʜɪs ɪs {MUSIC_BOT_NAME}*", buttons
    if SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Hᴇʟᴘᴇʀ ᴄᴏᴍᴍᴀɴᴅs ᴍᴇɴᴜ", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="⚙️ Sᴇᴛᴛɪɴɢs", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🌺 Oғғɪᴄɪᴀʟ ᴄʜᴀɴɴᴇʟ", url=f"{SUPPORT_CHANNEL}"
                ),
            ],
        ]
        return f"🎛  **Tʜɪs ɪs {MUSIC_BOT_NAME}**", buttons
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Hᴇʟᴘᴇʀ ᴄᴏᴍᴍᴀɴᴅs ᴍᴇɴᴜ", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="⚙️ Sᴇᴛᴛɪɴɢs", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🌸 Oғғɪᴄɪᴀʟ ᴄʜᴀɴɴᴇʟ", url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text="🌺 Sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛  **Tʜɪs ɪs {MUSIC_BOT_NAME}**", buttons


def private_panel():
    if not SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Hᴇʟᴘᴇʀ ᴄᴏᴍᴍᴀɴᴅs ᴍᴇɴᴜ", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ Aᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
        ]
        return f"🎛  **Tʜɪs ɪs {MUSIC_BOT_NAME}**", buttons
    if not SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Hᴇʟᴘᴇʀ ᴄᴏᴍᴍᴀɴᴅs ᴍᴇɴᴜ", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ Aᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="🌸 Sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛  **Tʜɪs ɪs {MUSIC_BOT_NAME}*", buttons
    if SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Hᴇʟᴘᴇʀ ᴄᴏᴍᴍᴀɴᴅs ᴍᴇɴᴜ", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ Aᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="🌺 Oғғɪᴄɪᴀʟ ᴄʜᴀɴɴᴇʟ", url=f"{SUPPORT_CHANNEL}"
                ),
            ],
        ]
        return f"🎛  **Tʜɪs ɪs {MUSIC_BOT_NAME}**", buttons
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Hᴇʟᴘᴇʀ ᴄᴏᴍᴍᴀɴᴅs ᴍᴇɴᴜ", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ Aᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="🌸 Oғғɪᴄɪᴀʟ ᴄʜᴀɴɴᴇʟ", url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text="🌺 Sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛  **Tʜɪs ɪs {MUSIC_BOT_NAME}**", buttons


def setting_markup():
    buttons = [
        [
            InlineKeyboardButton(text="📼 ᴀᴜᴅɪᴏ ǫᴜᴀʟɪᴛʏ", callback_data="AQ"),
            InlineKeyboardButton(text="🎛️ ᴀᴜᴅɪᴏ ᴠᴏʟᴜᴍᴇ", callback_data="AV"),
        ],
        [
            InlineKeyboardButton(
                text="👥 Aᴜᴛʜᴏʀɪᴢᴇᴅ ᴜsᴇʀs", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="🖥️ Dᴀsʜʙᴏᴀʀᴅ", callback_data="Dashboard"
            ),
        ],
        [
            InlineKeyboardButton(text="✖ Cʟᴏsᴇ", callback_data="close"),
            InlineKeyboardButton(text="🔙 Gᴏ ʙᴀᴄᴋ", callback_data="okaybhai"),
        ],
    ]
    return f"⚙️  **{MUSIC_BOT_NAME} Sᴇᴛᴛɪɴɢs**", buttons


def volmarkup():
    buttons = [
        [
            InlineKeyboardButton(
                text="🔄 Rᴇsᴇᴛ ᴀᴜᴅɪᴏ ᴠᴏʟᴜᴍᴇ 🔄", callback_data="HV"
            )
        ],
        [
            InlineKeyboardButton(text="🔈 Lᴏᴡ ᴠᴏʟ", callback_data="LV"),
            InlineKeyboardButton(text="🔉 Mᴇᴅɪᴜᴍ ᴠᴏʟ", callback_data="MV"),
        ],
        [
            InlineKeyboardButton(text="🔊 Hɪɢʜ ᴠᴏʟ", callback_data="HV"),
            InlineKeyboardButton(text="🔈 Aᴍᴘʟɪғɪᴇᴅ ᴠᴏʟ", callback_data="VAM"),
        ],
        [
            InlineKeyboardButton(
                text="🔽 Cᴜsᴛᴏᴍ ᴠᴏʟᴜᴍᴇ 🔽", callback_data="Custommarkup"
            )
        ],
        [InlineKeyboardButton(text="🔙 Gᴏ ʙᴀᴄᴋ", callback_data="settingm")],
    ]
    return f"⚙️  **{MUSIC_BOT_NAME} Sᴇᴛᴛɪɴɢs**", buttons


def custommarkup():
    buttons = [
        [
            InlineKeyboardButton(text="+10", callback_data="PTEN"),
            InlineKeyboardButton(text="-10", callback_data="MTEN"),
        ],
        [
            InlineKeyboardButton(text="+25", callback_data="PTF"),
            InlineKeyboardButton(text="-25", callback_data="MTF"),
        ],
        [
            InlineKeyboardButton(text="+50", callback_data="PFZ"),
            InlineKeyboardButton(text="-50", callback_data="MFZ"),
        ],
        [InlineKeyboardButton(text="🔼Cᴜsᴛᴏᴍ ᴠᴏʟᴜᴍᴇ 🔼", callback_data="AV")],
    ]
    return f"⚙️  **{MUSIC_BOT_NAME} Sᴇᴛᴛɪɴɢs**", buttons


def usermarkup():
    buttons = [
        [
            InlineKeyboardButton(text="👥 Eᴠᴇʀʏᴏɴᴇ", callback_data="EVE"),
            InlineKeyboardButton(text="🙍 Aᴅᴍɪɴs", callback_data="AMS"),
        ],
        [
            InlineKeyboardButton(
                text="📋 Aᴜᴛʜᴏʀɪᴢᴇᴅ ᴜsᴇʀs ʟɪsᴛs", callback_data="USERLIST"
            )
        ],
        [InlineKeyboardButton(text="🔙 Gᴏ ʙᴀᴄᴋ", callback_data="settingm")],
    ]
    return f"⚙️  **{MUSIC_BOT_NAME} Sᴇᴛᴛɪɴɢs**", buttons


def dashmarkup():
    buttons = [
        [
            InlineKeyboardButton(text="📡️ Uᴘᴛɪᴍᴇ", callback_data="UPT"),
            InlineKeyboardButton(text="💾 Rᴀᴍ", callback_data="RAT"),
        ],
        [
            InlineKeyboardButton(text="💻 Cᴘᴜ", callback_data="CPT"),
            InlineKeyboardButton(text="💽 Dɪsᴋ", callback_data="DIT"),
        ],
        [InlineKeyboardButton(text="🔙 Gᴏ ʙᴀᴄᴋ", callback_data="settingm")],
    ]
    return f"⚙️  **{MUSIC_BOT_NAME} Sᴇᴛᴛɪɴɢs**", buttons
