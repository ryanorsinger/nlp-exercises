# imports
from requests import get
from bs4 import BeautifulSoup
import os

url = 'https://site-to-scrape.glitch.me/'
headers = {'user-agent': 'codeup bayes data science'}
response = get(url, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')

# Using CSS selector
paragraphs = soup.select("p")

print(paragraphs)
