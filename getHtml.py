# /usr/bin/python3
# -*- coding uft-8 -*-
# Author Hjs
# @Time 2023/8/19 16:05

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from pandas import DataFrame

url = 'https://www.baidu.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
ret = Request(url, headers=headers)
# ret = Request(url)
res = urlopen(ret)
contents = res.read()
print(contents)

soup = BeautifulSoup(contents, "html.parser")

# for tag in soup.find_all('div', class_='s-news-rank-content'):
tags = soup.find_all('li', class_='hotsearch-item');
for tag in soup.find_all('li', class_='hotsearch-item'):
    m_name = tag.find('span', class_='title-content-title').get_text()
    m_url = tag.find('a')['href']
    m_index = tag['data-index']
    print("index:" + m_index + ", name:" + m_name + "    " + ", url:" + m_url)




