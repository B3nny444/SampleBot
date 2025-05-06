from pyrogram import  Client,filters

BOT_TOKEN ="8029964850:AAH4tP4lunEiU6E-hBbFMx_p9omUMWm5K-Y"
API_ID ="27094161"
API_HASH = "39477b23f5e6abea95fe0f92b7f00de0"

Bunny = Client(
    name = "bunnyBot",
    api_id = API_ID,
    api_hash = API_HASH,
    bot_token = BOT_TOKEN
)
@Bunny.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.reply_txt("hi")

print("bot started")

Bunny.run()
