# Project one Crawler - Requests

### 1. Use Requests to get information and display.
my_headers = {'cookie': 'over18=1;'}
QQ_url = 'https://www.ptt.cc/bbs/Beauty/index.html'
res = requests.get(QQ_url, headers = my_headers)
print(res.status_code)
print(res.text)

### 2. Use payload (Get)
### Question: How to ignore the page of limitation?
# payload = {'key1': 'value1', 'key2': 'value2'}
# html = requests.get("https://www.ptt.cc/bbs/Beauty/index.html", params=payload)
# print(html.url)

### 3. Use payload (post)
# my_headers = {'cookie': 'over18=1;'}
# url = 'https://www.ptt.cc/bbs/Beauty/index.html'
# payload = {'key1': 'value1', 'key2': 'value2'}
# html = requests.post(url, data=payload, headers = my_headers)
# print(html.text)

## 4. Cookie
# payload = {
#     'from': 'https://www.ptt.cc/bbs/Beauty/index.html', 'yes': 'yes'
# }
# headers = {
#     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
# }
# rs = requests.Session()
# rs.post('https://www.ptt.cc/bbs/Beauty/index.html', data=payload, headers=headers)
# res = rs.get('https://www.ptt.cc/bbs/Beauty/index.html', headers=headers)
#
# soup = BeautifulSoup(res.text, 'html.parser')
# items = soup.select('.r-ent')
# for item in items:
#     print(item.select('.date')[0].text, item.select('.author')[0].text, item.select('.title')[0].text)

## 5. Next page
# for i in range(1, 100):
#     url='https://www.ptt.cc/bbs/Beauty/index3453.html'+str(i)


