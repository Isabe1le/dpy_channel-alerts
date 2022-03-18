import discord
from discord.ext.commands import Bot
from discord.ext import commands

BOT_TOKEN = "token"
BOT_PREFIX = "prefix"

bot = commands.Bot(command_prefix=BOT_PREFIX, case_insensitive=True, intents=discord.Intents.default())

@bot.event
async def on_ready():
      print("Bot started")

@commands.has_permissions(view_audit_log=True)
@bot.command()
async def sendsplash(ctx, channel: discord.TextChannel=None, slots=None, role: discord.Role=None, *, data=None):
      data = data.split(" | ") or ["None"]
      if (channel is None) or (slots is None) or (role is None) or (len(data) != 2):
            return await ctx.send(f"{ctx.author.mention}, invalid command format. `{BOT_PREFIX}sendsplash #channel slots @role where it is | how to join it`\nExample: `{BOT_PREFIX}sendsplash #updates 10 @humans ontop of the hill | DM me.`")
      
      await channel.send(f"**Where:** {data[0]}\n**Positions:** {slots},\n**How to join:** {data[1]},\n**{role.mention}**")
      return await ctx.send(f"{ctx.author.mention}, your post in {channel.mention} has been sent."))

@bot.event
async def on_command_error(ctx, error):
      if isinstance(error, commands.MissingPermissions):
            return await ctx.send(f"{ctx.author.name}, you're lacking the following permission: `{list(error.missing_perms)[0]}`.")
      raise error

bot.run(BOT_TOKEN)
