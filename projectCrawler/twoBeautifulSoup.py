import requests
from bs4 import BeautifulSoup
url = 'https://www.ptt.cc/bbs/Beauty/index.html'
html = requests.get(url)
html.encoding = 'UTF-8'
# sp = BeautifulSoup(html.text, 'lxml')

soup = BeautifulSoup(html.text, 'html.parser')
results = soup.select('div.title')
print(results)
