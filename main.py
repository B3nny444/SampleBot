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
@bunny.on_message(filters.command("start"))
async def start_cmd(Client, message):
  await message.reply_photo(
    photo = "",
    "hi im summoned by Bunny")
  
  

                  


print("bot was started")
bunny.run()
