import requests
from bs4 import BeautifulSoup
def web(page,WebUrl):
    if(page > 0):
        code = requests.get(WebUrl).text
        s = BeautifulSoup(code, "html.parser")
        path=str('./pages/%d.txt'%(page))
        f = open(path, 'w')
        f.write(s.get_text())
        f.close()
        for link in s.findAll('a'):
            if (link.get('href') != None):
                page -= 1  
                web(page, str(WebUrl + link.get('href')))          
web(100,'http://ru.wikipedia.org/')