import discord
import datetime
from discord.ext import commands

class Member_Listeners(commands.Cog):

  def __init__(self, client):
    self.client = client
  
  @commands.Cog.listener()
  async def on_member_join(self, member):
    if str(member.guild.id) is not str(882289632673398806):
      return
    members = 0
    for guild in self.bot.guilds: 
        members += len(guild.members)
    true_member_count = len([m for m in member.guild.members if not m.bot])
    join = discord.Embed(title="Member Joined", description=f"{member.mention} ({member}) joined the server on {datetime.date}", color=0x0000ff)
    join.set_thumbnail(url=member.avatar_url)
    join.set_footer(text=f"{member.guild.name} now has {true_member_count} members and {members} including bots")
    channel = self.bot.get_channel(882059505419026483)
    await channel.send(embed=join)  
    
  @commands.Cog.listener()
  async def on_member_remove(self, member):
    if str(member.guild.id) is not str(882289632673398806):
      return
    members = 0
    for guild in self.bot.guilds: 
        members += len(guild.members)
    true_member_count = len([m for m in member.guild.members if not m.bot])
    leave = discord.Embed(title="Member Left", description=f"{member.mention} ({member}) left the server on {datetime.date}.", color=0xff0000)
    leave.set_thumbnail(url=member.avatar_url)
    leave.set_footer(text=f"{member.guild.name} now has {true_member_count} members and {members} including bots.")
    channel = self.bot.get_channel(882059505419026483)
    await channel.send(embed=leave)

def setup(client):
  client.add_cog(Member_Listeners(client))