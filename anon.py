from pyrogram import *
from configs import BOT_TOKEN , API_ID , API_HASH , ANON_TOKEN
from pyrogram.types import *
import anonfile
import os
import psutil

anon = ANON_TOKEN

anony = Client(name="Anony" ,
    bot_token= BOT_TOKEN ,
    api_id= API_ID,
    api_hash=API_HASH)



@anony.on_message(filters.command(["start"] ))
async def start(client, message):
    try:
        await message.reply_text(
        text=f"**Hello {message.from_user.first_name} 👋 !"
             "\n\nsearching for uploader who can upload from tg to other source? "
             "\n\ni am your solution!!. "
             "\n\nCheck About to know the use of me**",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("About", callback_data="About"),
                    InlineKeyboardButton("Help" , callback_data="Help")
                ]
            ]
        ),
        reply_to_message_id=message.id
    )
    except:
        await message.reply_text(
            text=f"**Hi 👋 !"
             "\n\nsearching for uploader who can upload from tg to other source? "
             "\n\ni am your solution!!. "
             "\n\nCheck About to know the use of me**",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("About", callback_data="About"),
                        InlineKeyboardButton("Help" , callback_data="Help")
                    ]
                ]
            ),
            reply_to_message_id=message.id
        )
    
@anony.on_message(filters.media)
async def media(client:anony, message):
    chat_id = message.chat.id
    await anony.send_message(chat_id , text="""
                             \n\nyour upload is in queue 
                             \n\nplease wait 
                             \n\n incase if bot doesnt reply even after few mins
                             \n\n join support group from /about message""")
    filname = await anony.download_media(message)
    upload = anon.upload(filname, progressbar=True)
    up_link =upload.url.geturl()
    last_text = "Here Is your Download link :" +"\n\n" + up_link
    await anony.send_message(chat_id , text=last_text)
    os.remove(filname)
    

@anony.on_message(filters.command("guidelines"))
async def guidelines(client:anony,message):
    chat_id = message.chat.id
    msg_text = """\n\n **Dont send Nsfw Stuffs**
    \n\n **Dont Share Contents thats contains more violance
    \n\n Thats All We are good to go"""

@anony.on_message(filters.command(["stats"]))
async def stats (client , message):
    user_id = message.from_user.id
    owner_id = int("1871813121")
    if user_id == owner_id:
        chat_id = message.chat.id 
        os_unmae = str( os.uname())
        disk_stat =  str(psutil.disk_usage('/'))
        status = str( "RUNNING with sadness😢")
        await message.reply_text(text = "**\n\nHOSTNAME:** " +os_unmae + " "+ " "  + " "+ " "+ "\n\n **STORAGE**:  " + disk_stat +  " " + " " +" " + " "+"\n\n **RUNNING STATUS :**" + status )
    else:
        await message.reply_text(text= "you are not a sudo user of @AnonChan69Bot")

@anony.on_message(filters.command(["about"], prefixes = ["." , "/" , "!"]))
async def about (client , message):
    keyboard = [
        [
            InlineKeyboardButton("JOIN",
                                          url="https://t.me/ProjectBaka"),
            InlineKeyboardButton("Support",
                                          url="https://t.me/BakaSupport"),
            InlineKeyboardButton("SHARE",url="https://t.me/share/url?url=https://t.me/AnonChan69Bot")
        ],
    ]
    await message.reply_text(text =
                              "<b>Hey! Im Anon Chan.</b>"
                              "\nI can Upload Files to anonfiles for You senpai."
                              "\n\n<b>About Me :</b>"
                              "\n\n  - <b>Name</b>        : <a href=\"https://t.me/raveen2k3/\">Anon Chan</a>"
                              "\n\n  - <b>Creator</b>      : <a href=\"https://t.me/ProjectBaka/\">Raveen</a>"
                              "\n\n  - <b>Language</b>  : <a href=\"https://www.python.org/\">Python 3</a>"
                              "\n\n  - <b>Library</b>       : <a href=\"https://docs.pyrogram.org//\">PYROGRAM</a>"
                              "\n\n  - <b>Source Code</b>  : <a href=\"https://github.com/raveen2k3/AnonChan\">Source Code</a>",    
        disable_web_page_preview = True ,
        reply_markup = InlineKeyboardMarkup(keyboard)
     )


@anony.on_callback_query()
async def cb_handler(neko, query):
    if query.data == "About":
        
        await query.answer()
        
        keyboard = [
            [
                InlineKeyboardButton("Updates",
                                            url="https://t.me/ProjectBaka"),
                InlineKeyboardButton("Support",
                                            url="https://t.me/BakaSupport"),
                InlineKeyboardButton("Share",url="https://t.me/share/url?url=https://t.me/AnonChan69Bot")
            ],
                    ]
        await query.message.edit_text(text =
                                "<b>Hey! Im Anon Chan.</b>"
                                "\nI can help you upload documents/videos/pictures to anonfiles.com."
                                "\nJust send me the document , i'll start the process adn give you the link!"
                                "\n\n<b>About Me :</b>"
                                "\n\n  - <b>Name</b>         : <a href=\"https://t.me/its_raveen/\">Anon Chan</a>"
                                "\n\n  - <b>Creator</b>      : <a href=\"https://t.me/its_raveen/\">Raveen</a>"
                                "\n\n  - <b>Language</b>     : <a href=\"https://www.python.org/\">Python 3</a>"
                                "\n\n  - <b>Api Source</b>   : <a href=\"https://github.com/nstrydom2/anonfile-api\">SOURCE</a>"
                                "\n\n  - <b>Library</b>      : <a href=\"https://docs.pyrogram.org/\">PYROGRAM</a>"
                                "\n\n  - <b>Source Code</b>  : <a href=\"https://github.com/raveen2k3/AnonChanBot\">Source Code</a>",    
            disable_web_page_preview = True ,
            reply_markup = InlineKeyboardMarkup(keyboard)
            
        )
        
    elif query.data == "Help":
        await query.answer()
        keyboard = [
            [
                InlineKeyboardButton("Announcements",
                                            url="https://t.me/ProjectBaka"),
                InlineKeyboardButton("Support",
                                            url="https://t.me/BakaSupport"),
                InlineKeyboardButton("Share",url="https://t.me/share/url?url=https://t.me/AiChan69Bot")
            ],
                    ]
        help_text ="""Hey Mate first checkout my /guidelines
        \n\n just send me your query i may able to answer it!
        \n\n Join Our Support group, for feature request or bug fixes
        """
        
        
        await query.message.edit_text(text=help_text, reply_markup = InlineKeyboardMarkup(keyboard))







anony.run()
