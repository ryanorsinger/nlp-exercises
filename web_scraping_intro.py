# Imports
from requests import get
from bs4 import BeautifulSoup
import os

url = 'https://site-to-scrape.glitch.me/'
headers = {'User-Agent': 'Codeup Bayes Data Science'}
response = get(url, headers=headers)
print(response.text)

