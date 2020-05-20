import discord
from discord import *
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext import *
from discord import *
from discord.ext import tasks

bot_token = "token"
bot_prefix = "prefix"

Client = discord.Client()
bot = commands.Bot(command_prefix = bot_prefix, case_insensitive=True)

@bot.event
async def on_ready():
      print("Bot started")

@commands.has_permissions(view_audit_log=True)
@bot.command()
async def sendsplash(ctx, channel_: discord.TextChannel=None, slots_=None, rank_: discord.Role=None, *, data="None"):
      data = data.split(" | ")
      if (channel_ == None) or (slots_ == None) or (rank_ == None) or (len(data) != 2):
            await ctx.send("%s, invalid format. `%ssendsplash #channel slots @rank where it is | how to join it`\nExample: `%ssendsplash #updates 10 @humans ontop of the hill | DM me.`" % (ctx.author.mention, bot_prefix, bot_prefix))
            return
      await channel_.send("""
**Where:** %s
**Positions:** %s,
**How to join:** %s,
**%s**
      """ % (data[0], slots_, data[1], rank_.mention))
      await ctx.send("%s, your post in %s has been sent." % (ctx.author.mention, channel_.mention))

@bot.event
async def on_command_error(ctx, error):
      if isinstance(error, commands.MissingPermissions):
            string = ""
            for permission in list(error.missing_perms):
                string = str(string)+str(permission)+", "
            await ctx.send("%s, you're lacking the following permission(s) `%s`." % (ctx.author.name, string[0:((len(string))-2)]))
      else:
            print(error)

bot.run(bot_token)