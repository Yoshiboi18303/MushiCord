import discord
from discord.ext import commands

class Client_Guild_Events(commands.Cog):

  def __init__(self, client):
    self.client = client
  
  @commands.Cog.listener()
  async def on_guild_join(self, guild):
    members = 0
    channel = self.client.get_channel(882308952744939520)
    members += len(guild.members)
    join_embed = discord.Embed(title="Joined a guild", color=discord.Color.green(), description="The client joined a guild!")
    join_embed.add_field(name="Guild Name", value=guild.name)
    join_embed.add_field(name="Members In Guild", value=members)
    join_embed.add_field(name="New Guild Count", value=len(self.client.guilds) + 1)
    await channel.send(embed = join_embed)
    print("The client joined a guild!")
  @commands.Cog.listener()
  async def on_guild_remove(self, guild):
    members = 0
    channel = self.client.get_channel(882308952744939520)
    members += len(guild.members)
    join_embed = discord.Embed(title="Left a guild", color=discord.Color.red(), description="The client left a guild...")
    join_embed.add_field(name="Guild Name", value=guild.name)
    join_embed.add_field(name="Members In Guild", value=members)
    join_embed.add_field(name="New Guild Count", value=len(self.client.guilds) - 1)
    await channel.send(embed = join_embed)
    print("The client got removed from a guild...")

def setup(client):
  client.add_cog(Client_Guild_Events(client))