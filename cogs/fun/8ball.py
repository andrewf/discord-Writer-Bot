import discord, lib, random
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from structures.guild import Guild

class EightBall(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="8ball")
    @commands.guild_only()
    async def old(self, context):
        """
        Old command.
        @param context:
        @return:
        """
        await context.send('This command has been migrated to use a Slash Command. More info: <https://github.com/cwarwicker/discord-Writer-Bot/wiki/Slash-Commands>')

    @commands.guild_only()
    @cog_ext.cog_slash(name="8ball", description="Ask the magic 8ball a question")
    async def _8ball(self, context: SlashContext, question):
        """
        Ask the magic 8-ball a question. Your question will be routed to a text-processing AI in order to properly analyze the content of the question and provide a meaningful answer.

        Examples: !8ball Should I do some writing?
        """
        if not Guild(context.guild).is_command_enabled('8ball'):
            return await context.send(lib.get_string('err:disabled', context.guild.id))

        guild_id = context.guild.id

        # Create array of possible answers to choose from
        answers = []

        # Load all 21 possible answers into an array to pick from
        for i in range(21):
            answers.append( lib.get_string('8ball:'+format(i), guild_id) )

        # Pick a random answer
        answer = random.choice(answers)

        # Send the message
        await context.send( context.author.mention + ', ' + format(answer) )


def setup(bot):
    bot.add_cog(EightBall(bot))