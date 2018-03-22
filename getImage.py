#coding=utf-8

import urllib
import re

# 获取整个页面数据
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

# 筛选页面中想要的数据
def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = 0
# 将页面筛选的数据保存到本地
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'%s.jpg' % x)
        x+=1


html = getHtml("http://tieba.baidu.com/p/2460150866")

print getImg(html)