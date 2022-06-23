import os
import discord
from replit import db

client = discord.Client()

@client.event
async def on_ready():
  print("we have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  author = f"{message.author}"
  db_keys = db.keys()

  if message.author == client.user:
    return

  if message.content.startswith("$hello"):
    await message.channel.send("Hello there fellow hare!")

  if message.content.startswith("$harefather"):
    await message.channel.send("opening confidential information 2/10:")
    await message.channel.send(file=discord.File('HareGodFather.jpg'))

  if message.content.startswith("$help me harefather"):
    await message.channel.send(file=discord.File('aDeal.gif'))

  if message.content.startswith("$give offer"):
    await message.channel.send(file=discord.File('DealOfNothing.gif'))

  if message.content.startswith("$give point"):
    if author in db_keys:
      db[f"{message.author}"] = db[f"{message.author}"] + 1
      print("Added 1 point to {}, Current points of {} are {}".format(author, author, db[f"{message.author}"]))
    else:
      db[f"{message.author}"] = 1

  if message.content.startswith("$show points"):
    await message.channel.send("total points of {} are / is {}".format(author, db[f"{message.author}"]))
    

    
    
client.run(os.environ['envDiscord'])
