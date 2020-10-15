# import requests
# import time
# from bs4 import BeautifulSoup
# import os
# import re
# import urllib.request
# import json
#
# PTT_URL = 'https://www.ptt.cc/bbs/Beauty/index.html'
#
# def get_web_page(url):
#     resp = requests.get(url=url, cookies={'over18': '1'})
#     if resp.status_code != 200:
#         print('Invalid url:', resp.url)
#         return None
#     else:
#         return resp.text
#
# def get_articles(dom, date):
#     soup = BeautifulSoup(dom, 'html5lib')
#
#     paging_div = soup.find('div', 'btn-group btn-group-paging')
#     prev_url = paging_div.find_all('a')[1]['href']
#
# articles = []
#     divs = soup.find_all('div', 'r-ent')
#     for d in divs:
#         if d.find('div', 'date').text.strip() == date:
#             push_count = 0
#             push_str = d.find('div', 'nrec').text
#             if push_str:
#                 try:
#                     push_count = int(push_str)
#                 except ValueError:
#                     if push_str == '爆':
#                         push_count = 99
#                     elif push_str.startswith('X'):
#                         push_count = -10
#

import requests
from bs4 import BeautifulSoup
res = requests.get('https://www.ptt.cc/bbs/Food/')
# # soup = BeautifulSoup(res.text, 'lxml')
# print(res.text)
# for item in soup.select(".r-ent"):
#     print(item.select(".title")[0].text.strip())
print(sp.title)