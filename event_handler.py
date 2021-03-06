import discord
import os
from discord.ext import commands, tasks
from utils.errors import type_err
from utils.message_functions import msgreply
from random import choice
from asyncio import sleep
from classes.client import client
from utils.mongo import ready_mongo

async def ch_pr():
  await client.wait_until_ready()

  statuses = [
  f"music in {len(client.guilds)} servers",
  f"with {len(client.users)} users in {len(client.guilds)} servers!",
  f"on {len(client.guilds)} servers!",
  "music bot made by Yoshiboi18303#4045",
  f"made by Yoshiboi18303#4045 and hosted on SoloNodes! | {client.command_prefix}host",
  f"{client.command_prefix}help",
  f"with all {len(client.commands)} commands | {client.command_prefix}help"
  ]

  while not client.is_closed():
    status = choice(statuses)

    await client.change_presence(activity=discord.Game(name=status), status=discord.Status.online)

    await sleep(30)
  
def ready_bot(client_name, token, cogs_enabled, use_mongo):
  connection_string = str(os.environ["MONGO_CONNECTION_STRING"])
  if client_name is not str(client_name):
    type_err("MushiCord", "client_name", "String", "Integer or Boolean")
  if cogs_enabled is not bool(cogs_enabled):
    type_err("MushiCord", "cogs_enabled", "Boolean", "Integer or String")
  if use_mongo is not bool(use_mongo):
    type_err("MushiCord", "use_mongo", "Boolean", "Integer or String")
  
  @client.event
  async def on_ready():
    print(f'{client_name} is ready to go! Prefix for {client_name} is "{client.command_prefix}",\nand {client_name} has {len(client.commands)} commands!')

  # @client.event
  # async def on_message(msg):
  #   if msg.author.bot:
  #     return
  #   else:
  #     pass
  
  @client.event
  async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send(msgreply(ctx.author, f"Please pass in all required arguments. Run {client.command_prefix}help <command> for more info on the arguments!"))
    elif isinstance(error, commands.BotMissingPermissions):
      await ctx.send(msgreply(ctx.author, "The client doesn't have the right permissions to use this command!"))
    elif isinstance(error, commands.BadArgument):
      error_embed = discord.Embed(title="Error", color=discord.Color.from_rgb(255,0,0), description="This command failed to run due to the following reason: ||Bad Argument!||")
      await ctx.send(f"<@{ctx.author.id}>", embed = error_embed)
    elif isinstance(error, commands.BadBoolArgument):
      error_embed = discord.Embed(title="Error", color=discord.Color.from_rgb(255,0,0), description="This command failed to run due to the following reason: ||Bad Boolean Argument!||")
      await ctx.send(f"<@{ctx.author.id}>", embed = error_embed)
    elif isinstance(error, commands.ArgumentParsingError):
      error_embed = discord.Embed(title="Error", color=discord.Color.from_rgb(255,0,0), description="This command failed to run due to the following reason: ||An Argument Parsing Error occurred!||")
      await ctx.send(f"<@{ctx.author.id}>", embed = error_embed)
    elif isinstance(error, commands.CommandInvokeError):
      error_embed = discord.Embed(title="Error", color=discord.Color.from_rgb(255,0,0), description=f"This command failed to run due to the following reason: ||Command Invoke Error, please report this with **{client.command_prefix}bugreport**!||")
      await ctx.send(f"<@{ctx.author.id}>", embed = error_embed)
      print(error)

  if cogs_enabled or cogs_enabled == True:
    for cog in os.listdir('./cogs'):
      if cog.endswith('.py'):
        client.load_extension(f'cogs.{cog[:-3]}')
        print(f'Auto-loaded cog: "cogs.{cog[:-3]}"')
    @client.command(help="Loads a cog (owner only)", usage=f"{client.command_prefix}load <cog(.py)>")
    async def load(ctx, extension):
      if str(ctx.author.id) != '697414293712273408':
        error_embed = discord.Embed(title="Error", color=discord.Color.from_rgb(255,0,0), description="You can not access this command due to the following reason: ||You are **NOT** the owner of this bot!||")
        return await ctx.send(f"<@{ctx.author.id}>", embed=error_embed)
      else:
        extension = str(extension)
        if extension.endswith('.py'):
          client.load_extension(f'cogs.{extension[:-3]}')
          await ctx.send(f'Loaded cog: "cogs.{extension[:-3]}"')
          print(f'Manually loaded cog: "cogs.{extension[:-3]}"')
        else:
          client.load_extension(f'cogs.{extension}')
          await ctx.send(f'Loaded cog: "cogs.{extension}"')
          print(f'Manually loaded cog: "cogs.{extension}"')
    @client.command(help="Unloads a cog (owner only)", usage=f"{client.command_prefix}unload <cog(.py)>")
    async def unload(ctx, extension):
      if str(ctx.author.id) != '697414293712273408':
        error_embed = discord.Embed(title="Error", color=discord.Color.from_rgb(255,0,0), description="You can not access this command due to the following reason: ||You are **NOT** the owner of this bot!||")
        return await ctx.send(f"<@{ctx.author.id}>", embed=error_embed)
      else:
        extension = str(extension)
        if extension.endswith('.py'):
         client.unload_extension(f'cogs.{extension[:-3]}')
         await ctx.send(f'Unloaded cog: "cogs.{extension[:-3]}"')
         print(f'Manually unloaded cog: "cogs.{extension[:-3]}"')
        else:
         client.unload_extension(f'cogs.{extension}')
         await ctx.send(f'Unloaded cog: "cogs.{extension}"')
         print(f'Manually unloaded cog: "cogs.{extension}"')
    @client.command(help="Reloads a cog (owner only)", usage=f"{client.command_prefix}reload <cog(.py)>")
    async def reload(ctx, extension):
      if str(ctx.author.id) != '697414293712273408':
        error_embed = discord.Embed(title="Error", color=discord.Color.from_rgb(255,0,0), description="You can not access this command due to the following reason: ||You are **NOT** the owner of this bot!||")
        return await ctx.send(f"<@{ctx.author.id}>", embed=error_embed)
      else:
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
    if use_mongo:
      ready_mongo(connection_string)

  client.loop.create_task(ch_pr())
  client.run(token)
