from pyrogram import Clients, filters

API_ID = "27094161"
API_HASH = "39477b23f5e6abea95fe0f92b7f00de0"
BOT_TOKEN ="7008178074:AAFQNeFSqBmMQgMaeeDmOdWXmeMX8Z1CMtA"

bunny = Client(
  name="bunny",
  api_id = API_ID,
  api_hash = API_HASH,
  bot_token = BOT_TOKEN
)
@bunny.on_message(filters.command("start"))
async def start_cmd(Client, message):
  await message.reply_text("hi itz bunny time")
@bunny.on_message(filters.command("help"))
async def help_cmd(Client, message):
  await message.reply_text("feel free to ask call me")
                  


print("bot was started")
bunny.run()
