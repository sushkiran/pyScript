"""
Write a program to fetch hyperlinks from any website which user enters
"""

import requests
from bs4 import BeautifulSoup

link = 'https://www.thomascook.in/'
content = requests.get(link).content
soup = BeautifulSoup(content, "html.parser")
links = [
    link.get('href') for link in soup.find_all('a')
    if link.get('href').startswith('http')
]

print('\n'.join(links))
