import discord
import os

from discord.ext import commands
from discord.flags import Intents
from discord.utils import get

intents = discord.Intents.all()
discord.member = True
discord.reaction = True

bot = commands.Bot('-', intents = intents)




# @bot.event
# async def on_raw_reaction_add(payload: discord.RawReactionActionEvent):
#     if payload.message_id != self.role_message_id:
@bot.command()
async def whitelist(ctx):
    # print()
    l = []
    for member in ctx.guild.members:
        if not member.bot:
            member.joined_at

@bot.command()
@commands.has_role("Creator")
async def rolegive(ctx):
    emoji_list = ['Red', 'Orange', 'Yellow', 'Green', 'Cyan', 'Blue', 'Purple']

    msg = await ctx.send("Choose your color:")

    for emoji in emoji_list:
        emoji = get(ctx.guild.emojis, name = emoji)
        await msg.add_reaction(emoji)

@bot.event
async def on_raw_reaction_add(payload):
    emoji_list = ['Red', 'Orange', 'Yellow', 'Green', 'Cyan', 'Blue', 'Purple']
    msg_id = os.environ.get('MESSAGE_ID')
    if payload.message_id == int(msg_id) and payload.emoji.name in emoji_list:

        for role in payload.member.roles:
            if role.name in emoji_list:
                role = discord.utils.get(payload.member.guild.roles, name = role.name)
                await payload.member.remove_roles(role)

#         emoji = bot.get_emoji(payload.emoji.id)
#         await payload.member.send(f'You got {emoji} color')

        role = discord.utils.get(payload.member.guild.roles, name = payload.emoji.name)
        await payload.member.add_roles(role)


        channel = bot.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        reactions = message.reactions 
        for reaction in message.reactions:
            # print(reaction.me)
            if reaction.emoji.name != payload.emoji.name:
                await reaction.remove(payload.member)               
        else:
            return

        


            # channel = bot.get_channel(payload.channel_id)
            # message = await channel.fetch_message(payload.message_id)
            # user = bot.get_user(payload.user_id)
            # emoji = bot.get_emoji()
            # await message.remove_reaction(emoji, user)


@bot.event 
async def on_raw_reaction_remove(payload):
    emoji_list = ['Red', 'Orange', 'Yellow', 'Green', 'Cyan', 'Blue', 'Purple']
    msg_id = os.environ.get('MESSAGE_ID')
    if payload.message_id == int(msg_id) and payload.emoji.name in emoji_list and payload.user_id != bot.user.id:
        # for role in payload.member.roles:
        #     if role.name in emoji_list:
        #         role = discord.utils.get(payload.member.guild.roles, name = role.name)
        #         await payload.member.remove_roles(role)
        # print(payload)
        guild = bot.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)
        role = discord.utils.get(guild.roles, name = payload.emoji.name)
        await member.remove_roles(role)




token = os.environ.get('BOT_TOKEN')
bot.run(str(token))
