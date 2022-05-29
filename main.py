import discord 
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
discord_token = os.getenv("TOKEN")

bot = discord.Client()

bot = commands.Bot(command_prefix = "#")

@bot.event
async def on_ready():
  print("The bot is ready")

@bot.event
async def on_message(msg):
  if msg.author == bot.user:
    return
  print("mails")
  await bot.process_commands(msg)

@bot.command()
async def game(ctx):
  myembed = discord.Embed(
    title="Game List", 
    colour=discord.Colour(0xbc708f),
    description="Select the game you would like to play:")

  myembed.set_author(name="#play", url="https://discordapp.com")
  myembed.set_footer(text="#play")
  myembed.add_field(name="Tic Tac Toe", value="A classic game of tic tac toe to play with your "
                                              "friends (1 vs 1) ```#play tictactoe @mention```")
  
  await ctx.reply(embed = myembed)

bot.run(discord_token)


