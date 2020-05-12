#this program is for downloading files (comic) from a web page and downloading
#the files on a local folder
import requests,os
import bs4 as bs

url = 'http://xkcd.com' #the url of the page
os.makedirs('xkcd folder',exist_ok=True) #for storing the comics

#will repeat this loop until the are no more previos pages
while not url.endswith('#'):

     #downloading the page
     print('Downloading the page %s...' %url)
     res = requests.get(url)

     #make sure the requests was made correctly otherwise throw an assertion error
     assert res.status_code == 200 
     soup = bs.BeautifulSoup(res.text,'lxml')
     comic = soup.select('#comic img')
     if comic == []:
        print('no comics where found!')
     else:
        comicUrl = comic[0].get('src')
        #download the image of the comic
        print('Downloading image %s...' %(comicUrl))
        res = requests.get('http://xkcd.com%s'%comicUrl)
        assert res.status_code == 200

        #write the on a local directory
        fileimage = os.path.join('xkcd folder',os.path.basename(comicUrl))
        with open(fileimage,'wb') as f:
            for chunk in res.iter_content(100000):
                f.write(chunk)
        
        #to do get the prev button's url
        prevlink = soup.select('a[rel=prev]')[0]
        url = 'http://xkcd.com' + prevlink.get('href')