from pyrogram import Clients, filters

API_ID = ""
API_HASH = ""
BOT_TOKEN =""

bunny = Client(
  name="bunny",
  api_id = API_ID,
  api_hash = API_HASH,
  bot_token = BOT_TOKEN
)

print("bot was started")
bunny.run()
