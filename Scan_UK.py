import requests
from requests_html import HTMLSession
import discord
from discord_webhook import *
import time
from bs4 import BeautifulSoup
from threading import Thread
from twocaptcha import TwoCaptcha

session = HTMLSession()
r = session.get('https://www.scan.co.uk/shop/computer-hardware/power-supplies/600w-to-780w-atx-power-supplies')
r.html.render()

solver = TwoCaptcha('fe98eb6f0b8f6042e62dbe4d3eaec3c0')
headers = {'User-Agent': 'Mozilla/5.0 (Android 4.4; Mobile; rv:41.0) Gecko/41.0 Firefox/41.0'}
TOKEN = 'NzExMjU2NjU4NTkyMTM3MjM3.XsAXYQ.RsuGF9pIAtU3dguVz7-EclQRy34'
client = discord.Client()
webhookurl = 'https://discord.com/api/webhooks/803110829801209868/EIfQlHKLH69f3-I4EZ2e1_3QxPAFq4K1YRd9a2X9WNYWGur8M3pGYeornKrwfMvnMlSv'
n = 0
query = "EVGA"
query2 = "Founder's"
img = 'https://images.anandtech.com/doci/16197/geforce-rtx-3070-tns_678x452.png'

url = 'https://www.scan.co.uk/shop/computer-hardware/power-supplies/600w-to-780w-atx-power-supplies'
print(url)
result = requests.get(r, headers=headers).text
soup = BeautifulSoup(result, 'lxml')
print(soup)
captchasite = soup.find('input', attrs={'name':'vc'}).get('value')
print(captchasite)
capresult = soup.funcaptcha(sitekey='dbc8eef2-aa58-4614-bd24-e0cd52d75438', challenge='12345678abc90123d45678ef90123a456b',url='https://www.scan.co.uk/shop/computer-hardware/power-supplies/600w-to-780w-atx-power-supplies')
time.sleep(5)
print(solver.getResult(capresult))
result = requests.get(url, headers=headers).text
soup = BeautifulSoup(result, 'lxml')
print(soup)
john = soup.find_all('li', class_='product')

    
def ScanUKLoop():
    print('work1')
    for image in john:
        print('work2')
        product_brand = soup.find('ul', attrs={'itemtype':'http://schema.org/BreadcrumbList'}).find('strong').text
        product_link = image.find('span', attrs={'class':'description'}).a.get('href')
        product_link = ('https://www.scan.co.uk'+product_link)
        product_name = image.find('span', attrs={'class':'description'}).a.text
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

@client.event
async def on_ready():
    thread1 = Thread(target=ScanUKLoop)
    thread1.start()

client.run(TOKEN)
