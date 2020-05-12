#basic web scrapping with the bs4 module
import requests
import bs4 as bs

souce = requests.get('https://pythonprogramming.net/parsememcparseface/')
soup = bs.BeautifulSoup(souce.text,'lxml')

for pa in soup.find_all('p'):
    print(pa.text)