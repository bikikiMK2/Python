import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="G")
bot = commands.Bot(command_prefix="?")
bot.remove_command("help")

@bot.event
async def on_ready():
    print("起動完了")

 @bot.command()
 async def ithub(ctx):
     await ctx.send("GitHubのHをｈにするな（迫真）")
     CHANNEL_ID - {your CHANNEL_ID}
     channel = client.get_channel(CHANNEL_ID)
 @bot.commnd()
 async def help (ctx):
      await ctx.send("helpなんてもう消したよww")
      CHANNEL_ID - {your CHANNEL_ID}
      channel = client.get_channel(CHANNEL_ID)
     
bot.run("your token")
