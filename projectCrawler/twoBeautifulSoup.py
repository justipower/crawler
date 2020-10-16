############## find() / find_all() ##############
# from bs4 import BeautifulSoup
# html = '''
# <html>
#     <head><meta charset="UTF-8"><title>我是網頁標題</title></head>
#     <body>
#         <p id="p1">我是段落一</p>
#         <p id="p2" class='red'>我是段落二</p>
#     </body>
# '''
# sp = BeautifulSoup(html, 'lxml')
# print(sp.find('p'))
# print(sp.find_all('p'))
# print(sp.find('p', {'id':'p2', 'class':'red'}))
# print(sp.find('p', id='p2', class_='red'))


############## PTT輸出title ##############

# 匯入requests
import requests
# 從bs4匯入BeautifulSoup
from bs4 import BeautifulSoup

# 將cookie的over18值定為1, 該值為1即表示略過18歲限制畫面, 將此設定放入變數my_headers
my_headers = {'cookie' : 'over18=1;'}
url = 'https://www.ptt.cc/bbs/Beauty/index.html'
# 直接進入Beauty版. 放入變數html
html = requests.get(url, headers=my_headers)
# 該網頁要使用的編碼為'UTF-8'
html.encoding = 'UTF-8'
# 建立名為sp的BeautifulSoup物件解析原始碼html text格式, 用python內建的解析器
sp = BeautifulSoup(html.text, 'html.parser')
# 使用模組select()方法讀取<div.title>標籤（選定要調整樣式的元素）
results = sp.select("div.title")

# 從results中撈到的值放到item
for item in results :
    # 取item的第一個值（item[0])裡的<a>
    a_item = item.select_one("a")
    # 傳回item去除掉標籤的html文字內容
    title = item.text
    # if a_item不為空
    if a_item :
        print(title, 'https://www.ptt.cc' + a_item.get('href'))

# 第二種方法
# for item in results:   #從results中去跑每一個item
#     a_item = item.select("a")   #
#     # print(a_item)
#     title = item.text
#     if a_item:
#         print(title, 'https://www.ptt.cc'+ a_item[0].get('href'))

############## PTT輸出title ##############
# import requests    #匯入requests
# from bs4 import BeautifulSoup   #從bs4匯入BeautifulSoup
#
# my_headers = {'cookie': 'over18=1;'}   #將cookie的over18值定為1, 該值為1即表示略過18歲限制畫面, 將此設定放入變數my_headers
# url = 'https://www.ptt.cc/bbs/Beauty/index.html'
# html = requests.get(url, headers=my_headers)   #直接進入Beauty版. 放入變數html
# html.encoding = 'UTF-8'
# sp = BeautifulSoup(html.text, 'lxml')
# print(sp.title)


# # 導入 模組(module)
# import requests
# # 導入 BeautifulSoup 模組(module)：解析HTML 語法工具
# import bs4
#
# # 文章連結
# URL = "https://www.ptt.cc/bbs/Gossiping/M.1590678355.A.246.html"
# # 設定Header與Cookie
# my_headers = {'cookie' : 'over18=1;'}
# # 發送get 請求 到 ptt 八卦版
# response = requests.get(URL, headers=my_headers)
#
# #  把網頁程式碼(HTML) 丟入 bs4模組分析
# soup = bs4.BeautifulSoup(response.text, "html.parser")
#
# ## PTT 上方4個欄位
# header = soup.find_all('span', 'article-meta-value')
#
# # 作者
# author = header[0].text
# # 看版
# board = header[1].text
# # 標題
# title = header[2].text
# # 日期
# date = header[3].text
#
# ## 查找所有html 元素 抓出內容
# main_container = soup.find(id='main-container')
# # 把所有文字都抓出來
# all_text = main_container.text
# # 把整個內容切割透過 "-- " 切割成2個陣列
# pre_text = all_text.split('--')[0]
#
# # 把每段文字 根據 '\n' 切開
# texts = pre_text.split('\n')
# # 如果你爬多篇你會發現
# contents = texts[2 :]
# # 內容
# content = '\n'.join(contents)
#
# # 顯示
# print('作者：' + author)
# print('看板：' + board)
# print('標題：' + title)
# print('日期：' + date)
# print('內容：' + content)
