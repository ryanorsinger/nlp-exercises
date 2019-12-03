## Web Scraping With Beautiful Soup

### Example Request

```python
url = 'https://site-to-scrape.glitch.me/'
headers = {'User-Agent': 'Codeup Data Science Student'}
response = get(url, headers=headers)
print(response.text)
```

- Open up `view-source:https://site-to-scrape.glitch.me/` in your browser 
- Compare this text to the `response.text` from the script above.
- Now, navigate to https://site-to-scrape.glitch.me/ to compare the content
- What mechanism rendered the HTML? The Browser. So, we need a way to parse HTML to get text.

### Now that you have a response, we need to parse the HTML