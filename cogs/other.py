import discord
from discord.ext import commands

class Other(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(help="Sends a bug report to the owner with what you specify!", aliases=['br','bug','reportbug'], usage="mshi?bugreport <bug (replace this with the bug you want to report)>")
  async def bugreport(self, ctx, bug, bug2=None, bug3=None, bug4=None, bug5=None):
    owner = self.client.get_user(697414293712273408)
    bug = str(bug)

    if bug2 is None:
      bug2 = ""
    else: 
      bug2 = str(bug2)
    
    if bug3 is None:
      bug3 = ""
    else: 
      bug3 = str(bug3)
    
    if bug4 is None:
      bug4 = ""
    else: 
      bug4 = str(bug4)

    if bug5 is None:
      bug5 = ""
    else: 
      bug5 = str(bug5)
    
    big_bug = bug + " " + bug2 + " " + bug3 + " " + bug4 + " " + bug5

    # return print(owner.username)

    success_embed = discord.Embed(title="Bug Successfully Reported!", color=discord.Color.from_rgb(0,255,0), description=f"You have successfully reported the bug \"{big_bug}\" to **{owner}**")
    bug_embed = discord.Embed(title="New Bug Reported!", color=discord.Color.from_rgb(255,255,25), description=f"A new bug was reported in **{ctx.guild.name}**!")
    bug_embed.add_field(name="Reporter", value=ctx.author)
    bug_embed.add_field(name="Bug Reported", value=bug + " " + bug2 + " " + bug3 + " " + bug4 + " " + bug5)
    await owner.send(embed = bug_embed)
    await ctx.send(f"Successfully sent DM to **{owner}**!", embed = success_embed)
    print(f"A bug was reported from {ctx.guild.name}!")

def setup(client):
  client.add_cog(Other(client))
    