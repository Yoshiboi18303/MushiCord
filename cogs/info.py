import discord
from discord.ext import commands
from utils.message_functions import msgreply

class Information(commands.Cog):

  def __init__(self, client):
    self.client = client
  
  @commands.command(help="Returns the latency of the bot!")
  async def ping(self, ctx):
    await ctx.send(msgreply(ctx.author, f"Pong! {round(self.client.latency * 1000)}ms"))

def setup(client):
  client.add_cog(Information(client))