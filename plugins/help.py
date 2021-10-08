from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = HI I AM DATAKINGDOM YOUTUBE BOT🤖....SEND YOUR YT URL TO DOWNLOAD ✅ඔබගේ YOUTUBE URL ය 
මාවෙත ඒවන්න..ඉන්පසුව මම ඔබට download කර දෙන්නම්✅ "
    await message.reply_text(helptxt)
