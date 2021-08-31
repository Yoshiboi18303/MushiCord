import discord
from discord.ext import commands
from utils.errors import refer_err

def msgreply(author, content):
  if author is None:
    refer_err("Author")
  if content is None:
    refer_err("Content")
  content = str(content)
  # author.id = str(author.id)
  return f"<@{author.id}>, {content}"