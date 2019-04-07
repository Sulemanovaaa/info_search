import pickle
from typing import Dict, List

import requests
from bs4 import BeautifulSoup
from lxml import html

handled_url = []
link_map = dict()
redirect_map = dict()


def web(page, WebUrl, baseUrl, xpathList, from_page=None):
    if (page > 0):
        name = str(page) + '.txt'
        if from_page is not None:
            l = redirect_map.get(from_page, [])
            if len(l) == 0:
                redirect_map[from_page] = l
            l.append(name)
        link_map[name] = WebUrl
        code = requests.get(WebUrl)
        s = BeautifulSoup(code.text, "html.parser")
        tree = html.fromstring(code.content)
        path = str('./pages/' + name)
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
                    web(page, str(baseUrl + link), baseUrl, xpathList, name)


def save_link_map(lin: Dict[str, str]):
    with open('./links.pickle', 'wb') as f:
        pickle.dump(lin, f)


def load_link_map() -> Dict[str, str]:
    with open('./links.pickle', 'rb') as f:
        lin = pickle.load(f)
    return lin


def save_redirect_map(links: Dict[str, List[str]]):
    with open('./redirect.pickle', 'wb') as f:
        pickle.dump(links, f)


def load_redirect_map() -> Dict[str, List[str]]:
    with open('./redirect.pickle', 'rb') as f:
        red = pickle.load(f)
    return red


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


if __name__ == "__main__":
    web(100, 'https://www.opennet.ru/opennews', 'https://www.opennet.ru',
        [
            '//table[@class="ttxt2"]//td[@class="titlebr"]/a[@class="title2"]/@href',
            '//table[@class="ttxt2"]//tr/td[@colspan="3"]/a/@href',
        ])
    save_link_map(link_map)
    save_redirect_map(redirect_map)
