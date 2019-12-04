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
- Congratulations! You Have a big honkin' string of HTML with all the characters!

- Browsers render HTML, but we'll need to parse that string to search for its content.

### Front End Web Development Crash Course

- HTML is a tree data structure. This means that elements contain content or other elements.
- CSS is a declarative language for selecting HTML elements then styling and laying them out. 
- JS is the client side programming language of the browser. Lots of content is dynamically  generated using JS. What `request` gets is the same as putting `view-source:` in front of a URL.

### 

### Best Practices

- **Scrape ethically**. When in doubt, ask yourself "What would Salas say? What would Zach do?"
- **Build a local cache of your response results**. Because scraping involves sending requests, time, servers, and bandwidth, it's important to load results if you already have them and only send requests to get fresh data. Otherwise, you risk:
  - Getting yourself or your company banned or blacklisted.
  - **Ok, how to build a cache of results**



soup.find

soup.findall

