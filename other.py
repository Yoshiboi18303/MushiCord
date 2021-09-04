import discord
from discord.ext import commands
from utils.mongo import update_mongo
from utils.message_functions import msgreply

class Other(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(help="Sets your AFK", usage="mshi?afk [reason (replace with your reason)]")
  async def afk(self, ctx, reason=None):
    if reason is None:
      reason = "AFK Reason"
    else:
      reason = str(reason)
    
    await update_mongo("Bot-Data", "AFK-User-Data", { id: ctx.author.id, reason: reason})
    await ctx.send(msgreply(ctx.author, f"I've set your AFK Key to: {reason}"))

def setup(client):
  client.add_cog(Other(client))