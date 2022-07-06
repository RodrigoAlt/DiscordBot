from discord_webhook import DiscordWebhook, DiscordEmbed
from discord.ext import commands

token=''
webhook = DiscordWebhook(url='https://discord.com/api/v10/webhooks/993729946172276847/g-bu82YiAQNKDHgNgkv_PSJk5Qz6J3kj0AYS12Lm2fZN3WeTB_fQ4Sd1p5u1gerpvEzI', username='Emisiones', avatar_url='https://i.imgur.com/itG7g5E.jpeg')
bot = commands.Bot(command_prefix='-')


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')    

#purge 'x' amount of messages
@bot.command(aliases= ["purge","delete"])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=None):
    if amount == None:
        await ctx.channel.purge(limit=2)
    else:
        await ctx.channel.purge(limit=int(amount))
bot.run(token)