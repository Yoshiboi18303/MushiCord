from discord import Embed, Color
from discord.ext import commands
from utils.message_functions import msgreply

class Information(commands.Cog):

  def __init__(self, client):
    self.client = client
  
  @commands.command(help="Returns the latency of the bot!")
  async def ping(self, ctx):
    await ctx.send(msgreply(ctx.author, f"Pong! {round(self.client.latency * 1000)}ms"))

  @commands.command(help="Returns some info about the client!", aliases=['bi','binfo'])
  async def botinfo(self, ctx):
    botinfo_embed = Embed(title="MushiCord Info", color=Color.from_rgb(143,255,247))
    botinfo_embed.set_thumbnail(self.client.avatar_url)
    botinfo_embed.add_field(name="Server Count", value=len(self.client.guilds))
    botinfo_embed.add_field(name="User Count", value=len(self.client.users))
    await ctx.send(embed = botinfo_embed)

  # @commands.command(help="Returns some info on a given user (or yourself)!", usage="mshi?userinfo", aliases=['ui','uinfo'])
  # async def userinfo(self, ctx, user=None):
  #   if user is None:
  #     user = ctx.author
  #   else:
  #     user = discord.User
    
  #   return print(user)

  #   embed = discord.Embed(title=f"Info on {user}")

  @commands.command(help="Returns where the bot was hosted and links to where you can find it!")
  async def host(self, ctx):
    embed = Embed(title="MushiCord Host", color=Color.from_rgb(102,230,255), description="MushiCord has been hosted on SoloNodes, check it out by clicking on the text in the \"Host Link\" field!")
    embed.add_field(name="Host Link", value="[Click Me!](https://solonodes.xyz/)")
    await ctx.send(embed = embed)

def setup(client):
  client.add_cog(Information(client))