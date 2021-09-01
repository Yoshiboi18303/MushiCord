import discord
import os
from discord.ext import commands, tasks
from utils.errors import type_err
from utils.message_functions import msgreply
from random import choice
from asyncio import sleep
from classes.client import client

async def ch_pr():
  await client.wait_until_ready()

  statuses = [
  f"music in {len(client.guilds)} servers",
  f"with {len(client.users)} users in {len(client.guilds)} servers!",
  f"on {len(client.guilds)} servers!",
  "music bot made by Yoshiboi18303#4045"
  ]

  while not client.is_closed():
    status = choice(statuses)

    await client.change_presence(activity=discord.Game(name=status))

    await sleep(10)

def ready_bot(client_name, token, cogs_enabled):

  if client_name is not str(client_name):
    type_err("MushiCord", "String", "Integer or Boolean")
  if cogs_enabled is not bool(cogs_enabled):
    type_err("MushiCord", "Boolean", "Integer or String")
  
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
    @client.command(help="Loads a cog (owner only)", usage=f"{client.command_prefix}load <cog(.py)>")
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
    @client.command(help="Unloads a cog (owner only)", usage=f"{client.command_prefix}unload <cog(.py)>")
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
    @client.command(help="Reloads a cog (owner only)", usage=f"{client.command_prefix}reload <cog(.py)>")
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

  client.loop.create_task(ch_pr())
  client.run(token)
