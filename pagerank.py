from crawler import load_redirect_map

def pagerank():
    redirect = load_redirect_map()
    d = 0.25
    pageranks = dict()    
    for page in redirect:
    	summa = 0 
    	for links in redirect:
    		for item in redirect.get(links):
    			if item == page:
    				summa += (1/len(redirect))/len(redirect.get(links))
    	pr = ((1-d)/len(redirect))+d*summa
    	pageranks.update({page: pr})
    return pageranks

if __name__ == "__main__":
	print(pagerank())