"""
Write a program to download all the videos from youtube.com for django from the hyperlink given below
"""
import requests
from bs4 import BeautifulSoup

link = 'https://www.youtube.com/playlist?list=PLxxA5z-8B2xk4szCgFmgonNcCboyNneMD'

content = requests.get(link).content
soup = BeautifulSoup(content, "html.parser")

print(soup.prettify())
'''for tag in soup.find_all(True):
    print()
    print(tag)

print([tag.name for tag in soup.find_all('url')])'''


