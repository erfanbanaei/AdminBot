from pyrogram import Client , filters
from pyrogram.types import * 
from pyromod import listen 
# ====================================================================
app = Client("MrTakRoBoT",config_file="config.ini")
# ====================================================================
Keyboard = ReplyKeyboardMarkup(
    [
        ["✍️ Send Message ✍️"],
        ["❗️ Help ❗️","ℹ️ Information ℹ️"]

    ],resize_keyboard=True
)
# ====================================================================
ADMINID = "@MrTakDev"
# ====================================================================
@app.on_message(filters.command("start"))
async def Start(client, message):
    await message.reply_text(f"""😃Hello <b>{message.from_user.mention}</b> , welcome to the message robot to the admin
If you have a suggested critical letter, you can use this robot🔥""",parse_mode="html",reply_markup=Keyboard)
# ====================================================================
async def Message(client, message):
    Message_To_Admin = await app.ask(message.from_user.id,"😃Send your message :) 🔥")
    await app.send_message(ADMINID,f"""
`┌┬` **New Message**
`│├` First Name:  `{message.from_user.first_name}`
`│├` Last Name:  `{message.from_user.last_name}`
`│├` Username:  `@{message.from_user.username}`
`│├` ID:  `{message.from_user.id}`
`│├` Text: {Message_To_Admin.text}
""",parse_mode="markdown")
    await message.reply("Message sent successfully :) ✅")
# ====================================================================
async def Information(client, message):
    await message.reply_text(f"""
`┌┬` __User info__
`│├` First Name:  `{message.from_user.first_name}`
`│├` Last Name:  `{message.from_user.last_name}`
`│├` Username:  `@{message.from_user.username}`
`│├` ID:  `{message.from_user.id}` """,reply_markup=Keyboard,parse_mode="markdown")
# ====================================================================
async def Help(client, message):
    await message.reply_text("""
    You can use the **✍️ Send Message ✍️** button to send a message to the admin and then send your message when you click the button :)""",parse_mode="markdown")
# ====================================================================
@app.on_message()
async def Main(client, message):
    Text = message.text
    if Text == "✍️ Send Message ✍️":
        await Message(client, message)
    elif Text == "ℹ️ Information ℹ️":
        await Information(client, message)
    elif Text == "❗️ Help ❗️":
        await Help(client, message)
# ====================================================================
app.run()