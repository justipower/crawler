import requests
from bs4 import BeautifulSoup

url = 'https://www.taiwanlottery.com.tw/index_new.aspx'
u = requests.get(url)
u.encoding = 'UTF-8'
sp = BeautifulSoup(u.text, 'html.parser')

datas = sp.find('div', class_='contents_box02')
# print(datas)
title = datas.find('span', class_='font_black15').text
print('威力彩期數: ', title)

nums = datas.find_all('div', class_='ball_tx ball_green')
print('開出順序: ', end='')
for i in range(0, 6):
    print(nums[i].text, end='')

print('\n大小順序: ', end='')
for i in range(6, 12):
    print(nums[i].text, end='')

num = datas.find('div', class_='ball_red').text
print('\n第二區: ', num)

# nums = datas.find_all('div', class_='ball_tx ball_green')
# print(nums)

##########################################################################
# import requests
# from bs4 import BeautifulSoup
#
# url = 'https://www.taiwanlottery.com.tw/index_new.aspx'
# u = requests.get(url)
# u.encoding = 'UTF-8'
# sp = BeautifulSoup(u.text, 'html.parser')
# #
# # print(u.text)
#
# # print(sp.select('span'))
# datas = sp.find('div', class_='contents_box02')
#
# # print(datas)
# # print(type(datas))
# # list = []
# # for data in datas:
# #     list += data
#     # print('-' * 5)
#     # print(list)
#     # print(type(data))
#
# title = datas.find('span', class_='font_black15').text
# print('威力彩期數: ', title)
#
# # # nums = data.find_all('div', class_='ball_tx ball_green')
# # # print(nums)
# #
