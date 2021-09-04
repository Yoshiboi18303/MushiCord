from discord.ext import commands
from os import environ

import statcord


class StatcordPost(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.key = environ['STATCORD_KEY']
        self.api = statcord.Client(self.client, self.key)
        self.api.start_loop()
        print("Statcord is ready!")

    @commands.Cog.listener()
    async def on_command(self,ctx):
        self.api.command_run(ctx)


def setup(client):
    client.add_cog(StatcordPost(client))