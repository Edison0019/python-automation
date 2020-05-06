import requests
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
res.raise_for_status() #this will make sure that the file exists otherwise will return an error
with open('story.txt','wb') as f:
    for chunk in res.iter_content(100000):
        f.write(chunk)
print('done!')
