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
async def s(ctx, *args):
    unit_surplus = {'R':2, 'B':2, 'G':4, 'S':4, 'N':4, 'L':4, 'P':18}   #飛車、角行、金将、銀将、桂馬、香車、歩兵
    
    chars = list(args[0])
    result1 = ''
    x = ''
    for c in chars:
        x = c.upper()
        if x in unit_surplus:
            unit_surplus[x] -= 1
        result1 += c
    
    result2 = ''
    d = ''
    if len(args) > 1:
        chars = list(args[1])
        for c in chars:
            if c.isdecimal():
                d += c
            
            x = c.upper()
            if x in unit_surplus:
                if not d:
                    d = '1'
                unit_surplus[x] -= int(d)
                d = ''
            result2 += c
    
    for k, v in unit_surplus.items():
        if v > 0:
            result2 += str(v) + k.lower()
    
    await ctx.send('.81 sfen ' + result1 + ' b ' + result2 + ' 1')
    
    result3 = ''
    for k, v in unit_surplus.items():
        result3 += k + ':' + str(v) + ','
        
    await ctx.send(result3)
    
bot.run(token)
