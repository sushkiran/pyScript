from bs4 import BeautifulSoup
import re


def two_attrs(tag): return len(tag.attrs) == 2
def one_char_name(tag): return len(tag.attrs) == 0 and len(tag.name) == 1


soup = BeautifulSoup(open('5.html'), "html.parser")

print('\n1.Well formatted\n', soup.prettify())

print('\n2.Print all b tags:', soup.find_all('b'))

print('\n3.Print all tag names starting with b:', list(set(tag.name for tag in soup.find_all(re.compile("^b")))))

print('\n4.Print text of title and p Tag:', [tag.text.strip() for tag in soup.find_all(['title', 'p'])])

print('\n5.Print all tag names:', list(set(tag.name for tag in soup.find_all(True))))

print('\n6.Tags with center-align:', soup.find_all(attrs={'align': 'center'}))

print('\n7.Tags with 2 attributes:', soup.find_all(two_attrs))

print('\n8.Tags with 0 attributes, one-char name:', soup.find_all(one_char_name))

xml_content = '<person name="Bob"><parent rel="mother" name="Alice">'

print('\n9.Print attributes with name as Alice:',
      BeautifulSoup(xml_content, 'html.parser').find_all(attrs={'name': 'Alice'}))

