import requests
import lxml
from lxml import html
from bs4 import BeautifulSoup

handled_url = []

def web(page, WebUrl, baseUrl, xpathList):
    if(page > 0):
        code = requests.get(WebUrl)
        s = BeautifulSoup(code.text, "html.parser")
        tree = html.fromstring(code.content)
        path=str('./pages/%d.txt'%(page))
        f = open(path, 'w')
        f.write(s.get_text())
        f.close()
        links = []
        for xpath in xpathList:
            links.extend(tree.xpath(xpath))
        print(links)
        for link in links:
            if (page > 0):
                if (isLinkValid(link)):
#                    print(href)
                    handled_url.append(link)
                    page -= 1  
                    web(page, str(baseUrl + link), baseUrl, xpathList)          

def isLinkValid(href):
    if (href == None):
        return False
    if len(href) <= 0:
        return False
    if href[0] in ["#", "h", "w"]:
        return False
    if href in handled_url:
        return False
    return True


web(100,'https://www.opennet.ru/opennews', 'https://www.opennet.ru',
        [
            '//table[@class="ttxt"]//td[@class="titlebr"]/a[@class="title2"]/@href',
            '//table[@class="ttxt"]//tr/td[@colspan="3"]/a/@href',
        ])
