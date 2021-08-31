import discord
from discord.ext import commands
# from utils.prefix_functions import get_prefix
import youtube_dl
from utils.message_functions import msgreply


class Music(commands.Cog):
  
  def __init__(self, client):
    self.client = client
    
  @commands.command(help="Makes the client connect to the voice channel you're in!", usage=f"mshi?join", aliases=['connect'])
  # @commands.has_permissions(connect=True)
  async def join(self, ctx):
    if ctx.author.voice is None:
      return await ctx.send(msgreply(ctx.author, "Please join a Voice Channel!"))
    voice_channel = ctx.author.voice.channel
    voice_client = ctx.voice_client
    if voice_client is None:
      await voice_channel.connect()
    else:
      await voice_client.move_to(voice_channel)
    await ctx.send("Joined the voice channel!")
  @commands.command(help="Disconnects the client from the current voice channel it's in!", usage=f"mshi?disconnect", aliases=['dc'])
  async def disconnect(self, ctx):
    voice_client = ctx.voice_client
    if voice_client is None:
      return await ctx.send(f"<@{ctx.author.id}>, I'm not in a voice channel!")
    else:
      await voice_client.disconnect()
  @commands.command(help="Plays a certain song in the voice channel you're in via YouTube URL!", usage=f"mshi?play <song_url>")
  # @commands.has_permissions(connect=True)
  async def play(self, ctx, url):
    if ctx.author.voice is None:
      return await ctx.send('Please join a Voice Channel!')
    voice_channel = ctx.author.voice.channel
    voice_client = ctx.voice_client
    if voice_client is None:
      await ctx.send('I\'m not in your Voice Channel, please wait on me to connect...')
      await voice_channel.connect()
      await ctx.send('Connected! Please run the command again!')
    else:
      FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
      YDL_OPTIONS = {'format':"bestaudio"}

      with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(url, download=False)
        url2 = info['formats'][0]['url']
        source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
        voice_client.play(source)
        # await ctx.send(f'You have started the song "{source}"!')
  @commands.command(help="Pauses the music that is playing in the Voice Channel you're in!", usage="mshi?pause")
  async def pause(self, ctx):
    if ctx.author.voice is None:
      return await ctx.send("Please join a Voice Channel!")
    voice_client = ctx.voice_client
    await ctx.send('Paused the music!')
    await voice_client.pause()
  @commands.command(help="Resumes the music that is paused in the Voice Channel you're in!", usage="mshi?resume")
  async def resume(self, ctx):
    voice_client = ctx.voice_client
    await ctx.send('Music resumed!')
    await voice_client.resume()
  @commands.command(help="Stops the music.", usage="mshi?stop")
  async def stop(self, ctx):
    if ctx.author.voice is None:
      return await ctx.send("Please join a Voice Channel!")
    voice_client = ctx.voice_client
    await ctx.send(f'Music stopped!')
    await voice_client.stop()


def setup(client):
  client.add_cog(Music(client))
  