from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


#@bot.command()
#async def hello(ctx):
#    await ctx.send('!hello')


@bot.command()
async def s(ctx, arg1, arg2):
    unit_surplus = {'R':2, 'B':2, 'G':4, 'S':4, 'N':4, 'L':4, 'P':18}   #飛車、角行、金将、銀将、桂馬、香車、歩兵
    
    chars = list(arg1)
    result1 = ''
    for c in chars:
        if c in unit_surplus:
            unit_surplus[c] = unit_surplus - 1
        result1 = result1 + c
        
    result2 = ''
    chars = list(arg2)
    for c in chars:
        result2 = result2 + c
        
    await ctx.send('.81 sfen ...' + result1 + ' b ' + result2 + '1')
    
    result3 = ''
    for u in unit_surplus:
        result3 = result3 + u + ':' + unit_surplus[u] + ','
        
    await ctx.send(result3)
    
bot.run(token)
