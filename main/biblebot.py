import discord 
from discord.ext import commands
from main import getverse
from main import getrandomverse

TOKEN = " "  # Put your OATH key here 

client = commands.Bot(command_prefix="$")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def passage(ctx, *, arg):  # FORMAT [Book Chapter:Verse]
    pasg = f'_{arg}_ ```{getverse(arg)}```'
    await ctx.send(pasg)

@client.command()
async def randompassage(ctx):
    pasg = f'```{getrandomverse()}```'
    await ctx.send(pasg)

@client.event
async def on_command_error(error, ctx):
    if isinstance(error, commands.CommandInvokeError):
        await client.send_message(ctx.message.author, "Passage too long")
        
while __name__ == "__main__":
    client.run(TOKEN)
