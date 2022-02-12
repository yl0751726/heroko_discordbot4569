import discord
import os
from pprint import pprint

TOKEN = os.environ['TOKEN']

@bot.event
async def on_ready():
    print('成功登入')
    
bot.run(TOKEN)
