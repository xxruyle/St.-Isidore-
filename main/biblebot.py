import discord 
from discord.ext import commands
from main import getverse
from main import getrandomverse
from main import randompassage_withbook
from main import booklist

TOKEN = " " # Add OATH Key here

client = commands.Bot(command_prefix="$")
client.remove_command("help")

# When bot logs in 
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# Commands-------------------------------------------------------------------------------------------------------------------------

# Get a specific verse 
@client.command()
async def passage(ctx, *, passage):  # FORMAT [Book Chapter:Verse]
    pasg = f'_{passage}_ ```{getverse(passage)}```'
    await ctx.send(pasg)

# Get a random verse from the bible
@client.command()
async def randombv(ctx):
    pasg = f'```{getrandomverse()}```'
    await ctx.send(pasg)

# Get a random verse from the bible with a specific book 
@client.command()
async def randomv(ctx, book):
    pasg = f'```{randompassage_withbook(book)}```'
    await ctx.send(pasg)

# Shows all the books in the bible 
@client.command()
async def books(ctx):
    biblebooks = f'```{booklist()}```'
    await ctx.send(biblebooks)    

# Help commands------------------------------------------------------------------------------------------------------------------
@client.group(invoke_without_command=True)    
async def help(ctx):
    em = discord.Embed(title = "Help", description = "Use $help <command> for more info", color = ctx.author.color)

    em.add_field(name= "Commands" , value = "passage\nrandombv\nrandomv\nbooks")

    await ctx.send(embed = em)

@help.command()
async def passage(ctx):
    em = discord.Embed(title = "Bible Passage", description = "Get a specific passage from the bible\n\n>Syntax is case sensitive\n\n>Use $books to find the correct spelling of each book")
    
    em.add_field(name = "_Syntax_", value = "```$passage <book> <chapter>:<verse>-<endverse```")

    await ctx.send(embed = em)

@help.command()
async def randombv(ctx):
    em = discord.Embed(title = "Random Book Passage", description = "Gets a random passage from the bible")

    em.add_field(name = "_Syntax_", value = "```$randombv```")
    await ctx.send(embed = em)

@help.command()
async def randomv(ctx):
    em = discord.Embed(title = "Random Verse", description = "Gets a random passage from a specific book in the bible")

    em.add_field(name = "_Syntax_", value = "```$randomv <book>```")
    await ctx.send(embed = em)

@help.command()
async def books(ctx):
    em = discord.Embed(title = "Books of the Bible", description = "Shows all the books in the bible")

    em.add_field(name = "_Syntax_", value = "```$books```")

    await ctx.send(embed = em)
#---------------------------------------------------------------------------------------------------------------------------------

@client.event
async def on_command_error(error, ctx):
    if isinstance(error, commands.CommandInvokeError):
        await client.send_message(ctx.message.author, "Passage too long")

client.run(TOKEN)
