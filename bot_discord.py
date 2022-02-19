import discord
from discord.ext import commands

food = 0

settings = {
    'token': 'OTMxNjgwNjEzMDk2OTE0OTQ0.YeH9Lw.nS0znMQArjAQguKizmEPh5FJKkY',
    'bot': 'SkeleBot',
    'id': 931680613096914944,
    'prefix': '!'
}

bot = commands.Bot(command_prefix = settings['prefix'])

@bot.command() 
async def give_eat(ctx): 
    global food
    author = ctx.message.author 

    food += 1
    if food % 100 == 12 or food % 100 == 13 or food % 100 == 14:
        await ctx.send(f'Меня покормили уже {food} раз, спасибо Господин {author.mention}!')
    elif food % 10 == 2 or food % 10 == 3 or food % 10 == 4:
        await ctx.send(f'Меня покормили уже {food} разa, спасибо Господин {author.mention}!')
    else:
        await ctx.send(f'Меня покормили уже {food} раз, спасибо Господин {author.mention}!')

bot.run(settings['token'])