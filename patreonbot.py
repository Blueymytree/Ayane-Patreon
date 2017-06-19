import discord
import asyncio
from discord.ext import commands
import time
import platform
import random

bot = commands.Bot(command_prefix="a!!")
bot.remove_command("help")
console = discord.Object('326235437964197890')

ownerids = [
    '280158289667555328',
    '193637466421329920',
    '267207628965281792',
    '107130754189766656'
]

# ready
@bot.event
async def on_ready():
    server_count = 0
    member_count = 0
    for server in bot.servers:
        server_count += 1
        for member in server.members:
            member_count += 1
    print("Starting up bot:")
    print(bot.user.name)
    print(bot.user.id)
    print("====================")
    await bot.send_message(console, 'Ayane Patreon now ready! Preparing for use in `' + str(server_count) + '` servers for `' + str(member_count) + '` members!')


# on message
@bot.event
async def on_message(message):
    if message.author.bot == False:
        await bot.process_commands(message)

# commands
@bot.command(pass_context = True)
async def help(ctx):
    embed = discord.Embed(title='Ayane Patreon Bot Commands!', color=0xB76E79).add_field(name='Info',value='`help`, `ping`, `donate`, `invite`').set_footer(text='The prefix is a!!. Use a!!<command>!')
    await bot.send_message(ctx.message.channel, content=None, embed=embed)

@bot.command(pass_context = True)
async def ping(ctx):
    before = time.monotonic()
    await (await bot.ws.ping())
    after = time.monotonic()
    ping = (after - before) * 1000
    random.seed(time.time())
    var = int(random.random() * 5)

    if (var == 0):
        v = 'a'
    elif (var == 1):
        v = 'e'
    elif (var == 2):
        v = 'i'
    elif (var == 3):
        v = 'o'
    elif (var == 4):
        v = 'u'
    await bot.say("P" + str(v) + "ng! :ping_pong:\nThe message took **{0:.0f}ms**!".format(ping))

@bot.command(pass_context = True)
async def invite(ctx):
    embed = discord.Embed(title='Invite me to your server!', description='Hi there! Inviting me is a bit different than you may think. Since this is a patreon bot, you must donate at least **$1**! \nYou can find the patreon page [here!](https://patreon.com/AyaneBot) \nAfter donating, join the [support server](https://discord.gg/muPA9ME) and ping August, along with proof, so he can give you the Patreon Bot!', color=0xB76E79)
    await bot.send_message(ctx.message.channel, content=None, embed=embed)

@bot.command(pass_context = True)
async def info(ctx):
    version = discord.__version__
    before = time.monotonic()
    await (await bot.ws.ping())
    after = time.monotonic()
    ping = (after - before) * 1000
    pversion = platform.python_version()
    server_count = 0
    member_count = 0
    for server in bot.servers:
        server_count += 1
        for member in server.members:
            member_count += 1
    await bot.say("```prolog\n --------- Bot Information --------- \n\nCommands: 5\nVersion: 0.0.1\nDiscord.py Version: " + str(version) + "\nPython Version: " + str(pversion) + "\nPing: {0:.0f}ms\n\n --------- Guild Information --------- \n\nGuilds: ".format(ping) + str(server_count) + "\nUsers: " + str(member_count) + "\nHost: Desii```")

# owner
@bot.command(pass_context = True)
async def status(ctx, *, setGame: str):
    member = ctx.message.author

    if member.id not in ownerids:
        await bot.say('You do not have permission to change my game.')
    else:
        await bot.change_presence(game=discord.Game(name=setGame))
        await bot.say("Set my playing status to `" + setGame + "`!")
        await bot.send_message(console, '`' + ctx.message.author.name + '#' + ctx.message.author.discriminator + '` changed my playing status to `' + setGame + '`.')
    
# run bot
bot.run('token')
