#this program is meant to open several windows within a browser
#this way we can have several searchs based on a keyword without needing to open the tabs separately
import requests, bs4, webbrowser,sys
print('googling...')#this text is going to be display while the page loads
res = requests.get('https://google.com/search?q=%s' %(' '.join(sys.argv[1:])))
if res.status_code != 200:
    raise Exception('resquest not found')

soup = bs4.BeautifulSoup(res.text,'lxml')
links = soup.select('a') #this will search all the elements within an 'a' tag with the r class
opentabs = min(5,len(links))

for i in range(opentabs):
    webbrowser.open('http://google.com' + links[i].get('href'))
