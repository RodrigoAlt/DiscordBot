from discord_webhook import DiscordWebhook, DiscordEmbed
from discord.ext import commands

bot = commands.Bot(command_prefix='-')
token=''
webhook = DiscordWebhook(url='https://discord.com/api/v10/webhooks/993729946172276847/g-bu82YiAQNKDHgNgkv_PSJk5Qz6J3kj0AYS12Lm2fZN3WeTB_fQ4Sd1p5u1gerpvEzI', username='Emisiones', avatar_url='https://i.imgur.com/itG7g5E.jpeg')


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')    
    

@bot.command()
async def embed(ctx):
    titulo='.         ‣[Beatz-Anime] 5-Toubun no Hanayome Season 2 [BD 1080p]'
    d1='*De camino a casa después de beber sus penas tras ser rechazado por su enamorada, el asalariado de 26 años, Yoshida, encuentra a una chica de instituto llamada Sayu sentada a un lado de la carretera.*\n'
    d2='```      🖥️ Temp 2 • E13 • MKV • 1080p • 1.3GB x Capitulo```'
    embed=DiscordEmbed(title=titulo, description= d1+d2, color=0xf3e7e9)
    #embed.set_author(name='')
    #embed.add_embed_field(name='<:members:750956466210340865> Fansub', value='<:members:750956466210340865> `Kashikoi`', inline=True)
    embed.add_embed_field(name='<:rich_presence:750956517171396618> Subtítulos', value='🇲🇽 `Kashikoi`', inline=True)
    embed.add_embed_field(name='<:stream:750956517250957332> Video', value='`|•BDRip HVEC|`', inline=True)
    embed.add_embed_field(name='<:voice:750956517431181385> Audios', value='🇯🇵', inline=True)
 
 
    webhook.add_embed(embed)
    response=webhook.execute()
    
 
bot.run(token)
