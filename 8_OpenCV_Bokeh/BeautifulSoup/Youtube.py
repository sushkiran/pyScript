"""
Write a program to download all the videos from youtube.com for django from the hyperlink given below
"""
'''import requests
from bs4 import BeautifulSoup

# link = 'https://www.youtube.com/playlist?list=PLxxA5z-8B2xk4szCgFmgonNcCboyNneMD'
link = 'https://www.youtube.com/watch?v=oT1A1KKf0SI&list=PLxxA5z-8B2xk4szCgFmgonNcCboyNneMD&index=1'
content = requests.get(link).content
soup = BeautifulSoup(content, "html.parser")
print(soup.prettify())'''

'''from pytube import YouTube

youtube_video_url = 'https://www.youtube.com/watch?v=DkU9WFj8sYo'

yt_obj = YouTube(youtube_video_url)

for stream in yt_obj.streams:
    print(stream)'''

from pytube import Playlist

try:
    playlist = Playlist('https://www.youtube.com/playlist?list=PLcow8_btriE11hzMbT3-B1sBg4YIc-9g_')

    playlist.videos()

except Exception as e:
    print(e)
