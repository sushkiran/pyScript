"""
Create a csv file with name and hyperlink after fetching it from the web page
"""
import requests
from bs4 import BeautifulSoup

home = 'https://www.thomascook.in'
content = requests.get(home).content
soup = BeautifulSoup(content, "html.parser")

file = open('ThomasCook.csv', 'w')
file.write('Name, Link\n')
text = '{}, {}\n'

for tag in soup.find_all('a'):
    if tag.get('title') not in (None, ''):
        prefix = '' if tag.get('href').startswith('http') else home
        file.write(text.format(tag.get('title').strip().replace(',', ''), prefix + tag.get('href')))

file.close()
