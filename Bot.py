import discord
import requests
import json
import math
from bs4 import BeautifulSoup
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    arrCommand = message.content.split(" ")


    if arrCommand[0] == "погода":
        r = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={' '.join(arrCommand[1:])}&appid=a6756a7aff9564a61122501b4ad92a9b")
        jconData = json.loads(r.text)

        temp = math.floor(jconData["main"]["temp"] - 273.15)

        await message.channel.send(f"{temp} °C")

    if message.content == "menu":
        r = requests.get("https://kurgan.shashlikoff.com/")
        bs = BeautifulSoup(r.text, "lmxl")

        block = bs.find("section", attrs={"class": "row hits-items"})
        for child in block.children:
            title = child.find("h3", attrs={"class": "item-title"})

            print(title.a.text)


client.run('ODI5NjYyNTgzMjkxOTA0MDIx.YG7Zfg.VZuG-GwWfD83XI5-_ojrdZp0ghA')



