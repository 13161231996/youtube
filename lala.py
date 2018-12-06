from selenium  import  webdriver
import time
import json
from lxml import etree
browser  = webdriver.Chrome()
browser.get('https://www.youtube.com/user/gordonramsay/videos')
js="var q=document.documentElement.scrollTop=10000"
browser.execute_script(js)
a = browser.page_source
html = etree.HTML(a)
#链接
a = html.xpath('//*[@id="video-title"]/@href')
#标题
title = html.xpath('//*[@id="video-title"]/text()')
c = {}
for (a,b) in zip(a,title):
    c[b] = 'https://www.youtube.com'+a
with open('1.json','a',encoding='utf-8')as f:
    f.write(json.dumps(c))