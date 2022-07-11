import discord
import asyncio
from discord.ext import commands
bot = commands.bot(Command_prefix = "!")
token = "OTYyNzEwMzQxNjY0NTEwMDAy.Gb_Nph.e9ONiQc4PzUC6YGtyFgr_LOSiVyn2n2mkX0az8"


@bot.event
async def on_ready():
    print("bot log run shode")

@bot.event
async def on_message_edit(b, a):
    print('before: ',b , 'after: ',a)

@bot.command()
async def test(ctx):
    await ctx.send(ctx.massage)


bot.run(token)