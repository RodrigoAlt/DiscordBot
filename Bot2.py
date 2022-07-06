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
 

@bot.command()
async def embed(ctx):
    channel = ctx.channel #reutilizable val
    
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel
    
    #Get title of the embed
    await channel.send("Which will be the title of your embed?\n")
    title = await bot.wait_for("message", check=check)
    await channel.send("Embed title will be: `{}`".format(title.content))
   
 
 
    #webhook.add_embed(embed)
    #response=webhook.execute()
bot.run(token)