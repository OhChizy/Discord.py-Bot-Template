#At start you import your MODULES
import discord
from discord.ext import commands


#Define client so you can use "@client.command()" or "@client.event"
client = commands.Bot(command_prefix="!") #You can change ! with any other prefix you want



#Example commands

#Ping command
@client.command()#You can added inside the () either "aliases=['Command Alias']" OR "help = 'Command Description'"
async def ping(ctx):
    await ctx.send(f"Pong!\n{round(client.latency * 1000)}ms") #The "\n" is used to start another line


#Example events

#on_ready event | This event is basically a function that gets triggered once the bot is online
@client.event
async def on_ready():
    print("Bot is online!") #This prints "Bot is online!" in your terminal once the bot gets online




#Make connection with your bot
client.run('YOUR BOT TOKEN')#Replace 'YOUR BOT TOKEN' with your token from the Discord Developer Portal