#hello.py
import discord
from discord.ext import commands, tasks

class Hello(commands.Cog):
    """docstring forHello."""

    def __init__(self, client):
        self.client = client
        self._join_remove_channel_id = 829970999788699708

    ################################### Alizee
    @commands.command()
    

def setup(client):
    client.add_cog(Hello(client))
