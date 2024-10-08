import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "27344784"))
  API_HASH = os.environ.get("API_HASH", "a12613f54c74d00bfb76cf8f0688c2ee")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "6923368496:AAFhmdZNztJWF-0PLwW3dBtl4tvAZUxm_70")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "Marathi_Serials_Provider_Bot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002056408106"))
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "1562792211"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Drxfile:Drxfile@drxfile.teugktb.mongodb.net/?retryWrites=true&w=majority")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002091923966")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002048118352"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
This is Permanent Files Store Bot! 🗃️
Send me any file I will save it in my Database. Also works for channel. Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.
**Any Issue Msg Me - @iTS_ViSHWA14** 😎

🤖 **My Name:** [Files Store Bot](https://t.me/{BOT_USERNAME})

📝 **Language:** [Python3](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 **Hosted on:** [Heroku](https://heroku.com)

🧑🏻‍💻 **Developer:** @iTS_ViSHWA14

👥 **Support Group:** [ViSHWA⚡](https://t.me/iTS_ViSHWA14)

📢 **Updates Channel:** [Marathi Serials](https://t.me/Marathi_Tv_Serialsx)
"""
ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [VISHWA](https://t.me/iTS_ViSHWA14)

Developer is Super Noob. Just Learning from Official Docs. Please Donate the developer for Keeping the Service Alive.

Also remember that developer will Delete Adult Contents from Database. So better don't Store Those Kind of Things.

[Donate Now](vishwamore@fam) (UPI)
"""
HOME_TEXT = """
 Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.
"""
