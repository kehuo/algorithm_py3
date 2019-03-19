#coding=utf-8
import bs4
#print(dir(bs4))
from bs4 import BeautifulSoup

from urllib.request import urlopen 

html=urlopen('http://www.pythonscraping.com/pages/page1.html')
print(html)

bsobj=BeautifulSoup(html.read())
print(bsobj.body.h1)


'''try except else 用法 
分别解释三个关键字：

try：执行可能会出错的试探性语句，即这里面的语句是可以导致致命性错误使得程序无法继续执行下去

except：如果try里面的语句无法正确执行，那么就执行except里面的语句，这里面可以是错误信息或者其他的可执行语句

else：如果try里面的语句可以正常执行，那么就执行else里面的语句（相当于程序没有碰到致命性错误
'''
