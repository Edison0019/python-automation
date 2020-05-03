#this code is for getting the distance of a list of zip codes for a given zip code
#it returns a file with the elementes of the list as distance in KM
from uszipcode import SearchEngine

#getting the distance of two pair of coordinates
def coordkm(lat1,lon1,lat2,lon2):
    import math
    if lat2 == None or lon2 == None:
        return 'None'
    R = 6373.0
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance

def distance(reference,file):
    with open(file,'r') as f:
        dirtyzip = f.readlines()
        cleanzip = []
        for i in dirtyzip:
            cleanzip.append(int(i.replace('\n','')))

    #get latitude and longitud for each zip code and the reference zip code
    search = SearchEngine(simple_zipcode=True)
    zlatlog = []
    for z in cleanzip:
        x = search.by_zipcode(int(z))
        zlatlog.append((x.lat,x.lng))

    #get a list of distances
    refzip = search.by_zipcode(reference)
    kmdist = []
    for i in zlatlog:
        kmdist.append(coordkm(refzip.lat,refzip.lng,i[0],i[1]))
    
    #write the contents to a file
    with open(str(reference)+'.txt','w') as f:
        for i in kmdist:
            f.write(str(i)+'\n')

try:
    for i in [19403,19153]:
        distance(i,'zip.txt')
except EnvironmentError as e:
    print(e)
