from pyrogram import Client, filters

API_ID = "27094161"
API_HASH = "39477b23f5e6abea95fe0f92b7f00de0"
BOT_TOKEN = "7425029151:AAHkMU98HkWgamjUFcGBKZWdEx3_O9lN7Jo"

bunny = Client(
  name="bunny",
  api_id = API_ID,
  api_hash = API_HASH,
  bot_token = BOT_TOKEN
)

START_BUTTONS =[[
  inlineKeyboardButton("join my channel", url = "https://t.me/Kaiju_no8_in_tamil_dub")
]]
@bunny.on_message(filters.command("start"))
async def start_cmd(Client, message):
  await message.reply_photo(
    photo = "",
    text = "you have to join the channel to start me"
    reply_markup = inlineKeyboardMarkUp("START_BUTTONS")
    description = "hi im summoned by Bunny")
  )
  

                  


print("bot was started")
bunny.run()
