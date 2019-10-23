import discord
import toke
TOKEN = toke.toke()
client = discord.Client()


@client.event
async def on_ready():
    ch = 636554025160015874
    channel = client.get_channel(ch)
    await channel.send("login")


@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content[0] == "/":
        mess = message.content[1:]
        if mess == "ラーメン":
            message.channel.send("ラーメン")

client.run(TOKEN)
