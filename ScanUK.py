import requests
import discord
import unicodedata
from discord_webhook import *
from discord.ext import commands
import time
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
TOKEN = 'NzExMjU2NjU4NTkyMTM3MjM3.XsAXYQ.RsuGF9pIAtU3dguVz7-EclQRy34'
client = commands.Bot(command_prefix =  '!')
webhookurl = 'https://discord.com/api/webhooks/803110829801209868/EIfQlHKLH69f3-I4EZ2e1_3QxPAFq4K1YRd9a2X9WNYWGur8M3pGYeornKrwfMvnMlSv'
n = 0
query = "Founders"
query2 = "Founder's"
img = 'https://images.anandtech.com/doci/16197/geforce-rtx-3070-tns_678x452.png'

@client.event
async def on_ready():
    url = 'https://www.scan.co.uk/shop/computer-hardware/power-supplies/600w-to-780w-atx-power-supplies'
    result = requests.get(url, headers=headers)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    
    for image in soup.find_all('li', class_='product'):
        product_brand = soup.find('ul', attrs={'itemtype':'http://schema.org/BreadcrumbList'}).find('strong').text
        product_link = image.find('span', attrs={'class':'description'}).a.get('href')
        product_link = ('https://www.scan.co.uk'+product_link)
        product_name = image.find('span', attrs={'class':'description'}).a.text
        print(query2)
        print(query)
        print(product_name)
        if(query.lower() in product_name.lower() or query2.lower() in product_name.lower()):
            try:
                product_price = image.find('div', attrs={'class':'leftColumn'}).span.text
                print(product_price)
                n=0
                n+1
                webhook = DiscordWebhook(url=webhookurl, username="Scan UK", avatar_url='https://yt3.ggpht.com/ytc/AAUvwnhczu8vRkJ6JbAD3CR833BsVxilmrUi3NF2ikV3aQ=s88-c-k-c0x00ffffff-no-rj') 
                embed = DiscordEmbed(title = product_brand, url = product_link, colour = 3066993)
                embed.add_embed_field(name='Product Name', value=product_name, inline=False)
                embed.add_embed_field(name='Price', value=product_price, inline=True)
                embed.add_embed_field(name='Site', value='Scan UK', inline=True)
                embed.set_footer(text='Watson - Keywords = '+query+','+query2,icon_url='https://cdn.discordapp.com/app-icons/711256658592137237/74a1779046799c1665d03cda5bb9694f.png'
                ),
                embed.set_thumbnail(url=img)
                embed.set_timestamp()
                webhook.add_embed(embed)
                webhook.execute()
                print('ScanUK: Product Found -  '+product_brand)
                time.sleep(30)
            except:
                print('helpme2')
                n=0
                n+1
                webhook = DiscordWebhook(url=webhookurl, username="Scan UK", avatar_url='https://yt3.ggpht.com/ytc/AAUvwnhczu8vRkJ6JbAD3CR833BsVxilmrUi3NF2ikV3aQ=s88-c-k-c0x00ffffff-no-rj') 
                embed = DiscordEmbed(title = product_brand, url = product_link, colour = 3066993)
                embed.add_embed_field(name='Product Name', value=product_name, inline=False)
                embed.add_embed_field(name='Product Loaded', value='Product Loaded', inline=True)
                embed.add_embed_field(name='Site', value='Scan UK', inline=True)
                embed.set_footer(text='Watson - Keywords = '+query+','+query2,icon_url='https://cdn.discordapp.com/app-icons/711256658592137237/74a1779046799c1665d03cda5bb9694f.png'
                ),
                embed.set_thumbnail(url=img)
                embed.set_timestamp()
                webhook.add_embed(embed)
                webhook.execute()
                print('ScanUK: Product Found -  '+product_brand)
                time.sleep(5)
        else:
            print('ScanUK: No Product Detected')
            time.sleep(6)

client.run(TOKEN)
