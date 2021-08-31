import discord
import os
from discord.ext import commands
from utils.errors import type_err
from utils.message_functions import msgreply

def ready_bot(client_name, token, cogs_enabled):
  from classes.client import client

  if client_name is not str(client_name):
    type_err("MushiCord", "String", "Integer or Boolean")
  if cogs_enabled is not bool(cogs_enabled):
    type_err("MushiCord", "Boolean", "Integer or String")
  
  @client.event
  async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Streaming(name=f"Music in many servers! | mshi?help", url="https://www.twitch.tv/yoshiboi18303"))
    print(f'{client_name} is ready to go!')
  
  @client.event
  async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send(msgreply(ctx.author, "Please pass in all required arguemnts."))
    elif isinstance(error, commands.BotMissingPermissions):
      await ctx.send(msgreply(ctx.author, "The client doesn't have the right permissions to use this command!"))
  
  if cogs_enabled or cogs_enabled == True:
    for cog in os.listdir('./cogs'):
      if cog.endswith('.py'):
        client.load_extension(f'cogs.{cog[:-3]}')
        print(f'Auto-loaded cog: "cogs.{cog[:-3]}"')
  
  client.run(token)
