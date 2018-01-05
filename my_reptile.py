# coding=utf-8
import requests
import re
from pyquery import PyQuery as pq


total_page = 30

# 代理
headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}

# 第一页的地址
root_url = 'http://www.sczfcg.com/CmsNewsController.do?method=recommendBulletinList&moreType=provincebuyBulletinMore&channelCode=jggg&rp=25&page=1'


def parseHtml(url):
    """根据传入的url去解析这个网页的内容"""

    # 爬取整个的内容
    html_content = requests.get(url, headers=headers)

    # 获取列表块的全部内容
    ultext = re.findall('<div class="colsList" name="loadAreat">(.*?)</div>', html_content.text, re.S)[0]

    # 获取每一项网址
    data = re.findall('<a href="(.*?)" id=', ultext, re.S)

    for each in data:
        if each.__len__() >= 95:  # 剔除无效连接
            parseItem(each)


def parseItem(item_url):
    """每一个案例的爬取"""

    item_content = requests.get(item_url, headers=headers)
    # 这里用而不用text主要是因为 content使用的网页原本的字符集，就不会出现中文乱码
    item_content.encoding="utf-8"
    table_text = re.findall('<table>(.*?)</table>', item_content.text, re.S)[0]
    data = re.findall('bordertt confont">(.*?)</td>', table_text, re.S)
    # data = re.findall('<td class="bordertt confont">(.*?)</td>', table_text, re.S)

    for itemDate in data:
        print itemDate
        # lineNum = 0
        # for line in itemDate.splitlines():
            # print line


# csv_file = open("allData.csv", "wb")
# file_heade=["ProjectName","ProjectNo.","PurchaseWay","AdministrativeRegion","NoticeType","NoticeTime","Purchaser","PurchaserCompany","ProjectBagNum",]

parseHtml(root_url)

# for i in range(2, total_page + 1):
#     new_link = re.sub('page=\d+', 'page=%d' % i, root_url, re.S)
#     parseHtml(new_link)
