import os
os.system("pip install -r requirements.txt")
import discord
from discord.ext import commands
import asyncio
import jishaku
import threading
import time

os.system("clear||cls")

os.environ["JISHAKU_HIDE"] = "True"
os.environ["JISHAKU_NO_UNDERSCORE"] = "True"
os.environ["JISHAKU_NO_DM_TRACEBACK"] = "True"
os.environ["JISHAKU_FORCE_PAGINATOR"] = "True"

# Config
owner_ids = []
prefix = ""
log_channel_id = 0 # if someone added your bot to server

async def start(self,token,reconnect):
  try:
    await self.login(token)
    await self.connect(reconnect=reconnect)
  except Exception as e:
    if "improper" in str(e).lower():
      print(f"Fuck You, Invalid Token: {token}")
    else:
      os.system("kill 1 && python3 main.py")


commands.Bot.start = start


tokens = open("tokens.txt","r").read().split("\n")

class DarkGaymer(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_ready(self):
    print(f"{self.bot.user} is hosted")
    await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name=f"{len(self.bot.guilds)} Guilds!"), status=discord.Status.idle)
    await self.bot.load_extension("jishaku")
  @commands.Cog.listener()
  async def on_disconnect(self):
    os.system("kill 1 && python3 main.py")
  @commands.Cog.listener()
  async def on_guild_join(self,guild):
    channel = self.bot.get_channel(log_channel_id)
    await channel.send(f"I Got Added To {guild.name}|{guild.member_count}.")



 
  @commands.command()
  async def guilds(self,ctx):
    await ctx.reply(embed=discord.Embed(description=f"{len(self.bot.guilds)} Guilds!",color=0000))


loop = asyncio.new_event_loop()
for token in tokens:
  bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all(), help_command=None,owner_ids=owner_ids)
  loop.create_task(bot.add_cog(DarkGaymer(bot)))
  try:
    loop.create_task(bot.start(token, reconnect=True))
  except:
    pass


threading.Thread(target=loop.run_forever).start()



while True:
  time.sleep(0)
  
