# imports
from requests import get
from bs4 import BeautifulSoup
import os

url = 'https://site-to-scrape.glitch.me/'
headers = {'user-agent': 'codeup bayes data science'}
response = get(url, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')

# get the html of all paragraphs
# paragraphs = soup.find_all("p")


# output = []
# for paragraph in paragraphs:
#     output.append(paragraph.get_text())

# print(output)


# Using CSS selector
