#-*-coding:utf-8-*-
import urllib,urllib2
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
def open_url(url):
    req=urllib2.Request(url,headers=headers)
    html=urllib2.urlopen(req)
    soup=BeautifulSoup(html,'html.parser')
    return soup
def get_url(content):
    data=content.find_all('img')
    urls=[]
    for i in data:
        urls.append(i.get('src'))
    return urls
def get_name(content):
    data = content.find_all('img')
    names = []
    for i in data:
        names.append(i.get('title'))
    return names
def down_load(url,name):
    urllib.urlretrieve(url,u'meizi\{}.jpg'.format(name))
if __name__=='__main__':
    url = 'https://www.dbmeinv.com'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36'}
    content=open_url(url)
    urls=get_url(content)
    names=get_name(content)
    for x,y in zip(urls,names):
        down_load(x,y)


