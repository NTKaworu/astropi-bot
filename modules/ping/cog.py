from nextcord.ext import commands
from nextcord import Interaction, Embed
import nextcord

TESTING_GUILD_ID = 1062129905007071253 # REMOVE THIS

class Ping(commands.Cog, name="🏓 Ping"):
    """Receives ping commands"""

    COG_EMOJI = "🏓"

    def __init__(self, bot: commands.Bot):
        self._bot = bot

    def cog_after_invoke(self, ctx: commands.Context) -> None:
        return 'pluto'


    @nextcord.user_command(guild_ids=[TESTING_GUILD_ID], name='show profile')
    async def show_profile(self, interaction: Interaction, memeber: nextcord.Member):

        em = Embed(title=f'{memeber.name} profile', description=f'Join date:{memeber.joined_at}\nID: {memeber.id}', color=nextcord.Color.green())
        em.set_thumbnail(memeber.avatar)
        em.add_field(name='Reputation', value='`good 🟢`')

        
        await interaction.response.send_message(embed=em, ephemeral=True)

    @nextcord.slash_command(guild_ids=[TESTING_GUILD_ID], name='ping', description='Checks for a response from the bot')
    async def ping(self, interaction: Interaction):
        """Checks for a response from the bot"""    
        await interaction.response.send_message(embed=Embed(title='🏓 Pong', color=nextcord.Colour.red()))

    # @nextcord.slash_command(guild_ids=[TESTING_GUILD_ID], name='pong', description='Checks for a response from the bot')
    # async def pong(self, interaction: Interaction, num: int):
    #    """Checks for a response from the bot"""    
    
    #    await interaction.response.send_message(embed=Embed(title=f'🏓 Ping -> {num}'))

def setup(bot: commands.Bot):
    bot.add_cog(Ping(bot))