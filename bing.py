from bs4 import BeautifulSoup
import requests

res= requests.get('https://bingwallpaper.com/')
soup= BeautifulSoup(res.text, 'lxml')
