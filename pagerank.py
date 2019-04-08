from crawler import load_redirect_map
import operator

def pagerank(answers):
    redirect = load_redirect_map()
    d = 0.25
    N = len(answers)
    pageranks = dict()    
    for page in answers:
    	summa = 0 
    	for links in redirect:
    		for item in redirect.get(links):
    			if item == page:
    				summa += (1/N)/len(redirect.get(links))
    	pr = ((1-d)/N)+d*summa
    	pageranks.update({page: pr})
    pageranks = sorted(pageranks.items(), key=operator.itemgetter(1), reverse=True)
    return pageranks
