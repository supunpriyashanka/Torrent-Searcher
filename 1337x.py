import os
import aiohttp
import json
from pyrogram import Client, filters, emoji
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


app = Client("trntsrcbot", api_id=int(os.environ.get("API_ID")), api_hash=os.environ.get("API_HASH"), bot_token=os.environ.get("BOT_TOKEN"))


print("\nBot Started\n")


@app.on_message(filters.command(['start']))
async def start(_, message):
    await message.reply_text("Hi. I'm Torrent Sercher Bot 🇱🇰\nSend /help To Show Help Screen\nBot by @NET_HACKER_BOTs_chat 🇱🇰")



@app.on_message(filters.command(['help']))
async def help(_, message):
    await message.reply_text("Example: /find Film Name\n Made By Supun Priyashanka 🇱🇰")

m = None
i = 0
a = None
query = None


@app.on_message(filters.command(["find"]))
async def find(_, message):
    global m
    global i
    global a
    global query
    try:
        await message.delete()
    except:
        pass
    if len(message.command) < 2:
        await message.reply_text("Usage: /find query")
        return
    query = message.text.split(None, 1)[1].replace(" ", "%20")
    m = await message.reply_text("Searching 🤫\nPlease Wait 😍")
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://api.api-zero.workers.dev/1337x/{query}") \
                    as resp:
                a = json.loads(await resp.text())
    except:
        await m.edit("Found Nothing.")
        return
    result = (
        f"**Page - {i+1}**\n\n"
        f"➲Name: `{a[i]['Name']}`\n"
        f"➲By {a[i]['UploadedBy']} "
        f"{a[i]['DateUploaded']}\n" 
        f"➲{a[i]['Type']} "
        f"{a[i]['Category']}\n"
        f"➲Poster: {a[i]['Poster']}\n"
        f"➲Language: {a[i]['Language']} || "
        f"➲Checked: {a[i]['LastChecked']}\n"
        f"➲Seeds: {a[i]['Seeders']} & "
        f"➲Leeches: {a[i]['Leechers']}\n"
        f"➲Magnet: `{a[i]['Magnet']}`\n\n\n"
    )
    await m.edit(
        result,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(f"Next",
                                         callback_data="next"),
                    InlineKeyboardButton(f"{emoji.CROSS_MARK}",
                                         callback_data="delete")
                ]
            ]
        ),
        parse_mode="markdown",
    )


@app.on_callback_query(filters.regex("next"))
async def callback_query_next(_, message):
    global i
    global m
    global a
    global query
    i += 1
    result = (
        f"**Page - {i+1}**\n\n"
        f"➲Name: `{a[i]['Name']}`\n"
        f"➲By {a[i]['UploadedBy']} "
        f"{a[i]['DateUploaded']}\n" 
        f"➲{a[i]['Type']} "
        f"{a[i]['Category']}\n"
        f"➲Poster: {a[i]['Poster']}\n"
        f"➲Language: {a[i]['Language']} || "
        f"➲Checked: {a[i]['LastChecked']}\n"
        f"➲Seeds: {a[i]['Seeders']} & "
        f"➲Leeches: {a[i]['Leechers']}\n"
        f"➲Magnet: `{a[i]['Magnet']}`\n\n\n"
    )
    await m.edit(
        result,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(f"Prev",
                                         callback_data="previous"),
                    InlineKeyboardButton(f"{emoji.CROSS_MARK}",
                                         callback_data="delete"),
                    InlineKeyboardButton(f"Next",
                                         callback_data="next")
                    
                ]
            ]
        ),
        parse_mode="markdown",
    )


@app.on_callback_query(filters.regex("previous"))
async def callback_query_previous(_, message):
    global i
    global m
    global a
    global query
    i -= 1
    result = (
        f"**Page - {i+1}**\n\n"
        f"➲Name: `{a[i]['Name']}`\n"
        f"➲By {a[i]['UploadedBy']} "
        f"{a[i]['DateUploaded']}\n" 
        f"➲{a[i]['Type']} "
        f"{a[i]['Category']}\n"
        f"➲Poster: {a[i]['Poster']}\n"
        f"➲Language: {a[i]['Language']} || "
        f"➲Checked: {a[i]['LastChecked']}\n"
        f"➲Seeds: {a[i]['Seeders']} & "
        f"➲Leeches: {a[i]['Leechers']}\n"
        f"➲Magnet: `{a[i]['Magnet']}`\n\n\n"
    )
    await m.edit(
        result,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(f"Prev",
                                         callback_data="previous"),
                    InlineKeyboardButton(f"{emoji.CROSS_MARK}",
                                         callback_data="delete"),
                    InlineKeyboardButton(f"Next",
                                         callback_data="next")
                ]
            ]
        ),
        parse_mode="markdown",
    )


@app.on_callback_query(filters.regex("delete"))
async def callback_query_delete(_, message):
    global m
    global i
    global a
    global query
    await m.delete()
    m = None
    i = 0
    a = None
    query = None


app.run()
