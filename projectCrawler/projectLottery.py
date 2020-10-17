import requests
from bs4 import BeautifulSoup

url = 'https://www.taiwanlottery.com.tw/index_new.aspx'
u = requests.get(url)
u.encoding = 'UTF-8'
sp = BeautifulSoup(u.text, 'html.parser')
#
# print(u.text)

# print(sp.select('span'))
datas = sp.find('div', class_='contents_box02')
title = datas.find('span', 'font_black15').text
