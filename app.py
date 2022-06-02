import discord
import requests 
from time import sleep 
client = discord.Client()
token = "OTgxOTM3ODc4NDgzNTAxMTQ2.G5EfD3.QbPaWKSzRinEoMB6dJeZwfHYTDIjel4ipds43U"
@client.event
async def on_message(message):  
    Start = True
    if message.content.find("!ayah") != -1:
        while Start == True:
            url = requests.get("https://soud.me/api/Quran").json()
            a = url['info']['Ayah']
            await message.channel.send(f"{a}")
            sleep(600)
client.run(token)
