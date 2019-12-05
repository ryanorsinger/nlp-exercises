# imports
from requests import get
from bs4 import BeautifulSoup
import os
import pandas as pd

def get_blog_posts():
    filename = './codeup_blog_posts.csv'

    # check for presence of the file or make a new request
    if path.exists(filename):
        return pd.read_csv(filename)
    else:
        return make_new_request()

def make_dictionary_from_article(url):
    headers = {'user-agent': 'Codeup Bayes Instructor Example'}
    response = get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.title
    body = soup.select("div.mk-single-content.clearfix")[0].get_text()

    return {
        "title": title,
        "body": body
    }

def make_new_request():
    urls = [
        "https://codeup.com/codeups-data-science-career-accelerator-is-here/",
        "https://codeup.com/data-science-myths/",
        "https://codeup.com/data-science-vs-data-analytics-whats-the-difference/",
        "https://codeup.com/10-tips-to-crush-it-at-the-sa-tech-job-fair/",
        "https://codeup.com/competitor-bootcamps-are-closing-is-the-model-in-danger/",
    ]

    output = []
    
    for url in urls:
        output.append(make_dictionary_from_article(url))

    df = pd.DataFrame(output)
    df.to_csv('./codeup_blog_posts.csv') 

    return df