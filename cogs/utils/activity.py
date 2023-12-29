import random
import disnake
from disnake.ext import commands, tasks


class CustomPresence(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.status_change.start()


    @tasks.loop(minutes=3)
    async def status_change(self):
        activities = [
            disnake.Activity(name="список участников", type=disnake.ActivityType.watching)
        ]

        activity = random.choice(activities)
        await self.bot.change_presence(activity=activity)


    @status_change.before_loop
    async def before_status_change(self):
        await self.bot.wait_until_ready()


def setup(bot):
    bot.add_cog(CustomPresence(bot))