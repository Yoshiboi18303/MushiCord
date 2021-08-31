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
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name=f"Testing bot | tmshi?help", url="https://www.twitch.tv/yoshiboi18303"))
    print(f'{client_name} is ready to go!')

  # @client.event
  # async def on_message(msg):
  #   if msg.author.bot:
  #     return
  #   else:
  #     pass
  
  @client.event
  async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send(msgreply(ctx.author, "Please pass in all required arguments."))
    elif isinstance(error, commands.BotMissingPermissions):
      await ctx.send(msgreply(ctx.author, "The client doesn't have the right permissions to use this command!"))
    elif isinstance(error, commands.NotOwner):
      await ctx.send(msgreply(ctx.author, "You are **NOT** the owner of this bot!"))

  if cogs_enabled or cogs_enabled == True:
    for cog in os.listdir('./cogs'):
      if cog.endswith('.py'):
        client.load_extension(f'cogs.{cog[:-3]}')
        print(f'Auto-loaded cog: "cogs.{cog[:-3]}"')
    @client.command(help="Loads a cog", usage=f"{client.command_prefix}load <cog(.py)>")
    async def load(ctx, extension):
      commands.is_owner()
      extension = str(extension)
      if extension.endswith('.py'):
        client.load_extension(f'cogs.{extension[:-3]}')
        await ctx.send(f'Loaded cog: "cogs.{extension[:-3]}"')
        print(f'Manually loaded cog: "cogs.{extension[:-3]}"')
      else:
        client.load_extension(f'cogs.{extension}')
        await ctx.send(f'Loaded cog: "cogs.{extension}"')
        print(f'Manually loaded cog: "cogs.{extension}"')
    @client.command(help="Unloads a cog", usage=f"{client.command_prefix}unload <cog(.py)>")
    async def unload(ctx, extension):
      commands.is_owner()
      extension = str(extension)
      if extension.endswith('.py'):
        client.unload_extension(f'cogs.{extension[:-3]}')
        await ctx.send(f'Unloaded cog: "cogs.{extension[:-3]}"')
        print(f'Manually unloaded cog: "cogs.{extension[:-3]}"')
      else:
        client.unload_extension(f'cogs.{extension}')
        await ctx.send(f'Unloaded cog: "cogs.{extension}"')
        print(f'Manually unloaded cog: "cogs.{extension}"')
    @client.command(help="Reloads a cog", usage=f"{client.command_prefix}reload <cog(.py)>")
    async def reload(ctx, extension):
      commands.is_owner()
      extension = str(extension)
      if extension.endswith('.py'):
        client.unload_extension(f'cogs.{extension[:-3]}')
        client.load_extension(f'cogs.{extension[:-3]}')
        await ctx.send(f'Reloaded cog: "cogs.{extension[:-3]}"')
        print(f'Manually reloaded cog: "cogs.{extension[:-3]}"')
      else:
        client.unload_extension(f'cogs.{extension}')
        client.load_extension(f'cogs.{extension}')
        await ctx.send(f'Reloaded cog: "cogs.{extension}"')
        print(f'Manually reloaded cog: "cogs.{extension}"')
  
  client.run(token)
