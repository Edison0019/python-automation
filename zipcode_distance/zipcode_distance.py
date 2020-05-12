#this code is for getting the distance of a list of zip codes for a given zip code
#it returns a file with the elementes of the list as distance in KM
from uszipcode import SearchEngine

#getting the distance of two pair of coordinates
def coordkm(lat1,lon1,lat2,lon2):
    if lat2 == None:
        return 'None'
    #this will return the distance of two pair of coordinates in miles
    import math
    pi = math.pi
    D2R = pi / 180
    lat1 = D2R * lat1
    lat2 = D2R * lat2
    dLon = D2R * (lon2 - lon1) 

    x = math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(dLon)
    y = math.sqrt((math.cos(lat2) * math.sin(dLon)) ** 2 + (math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(dLon)) ** 2)
    result = math.atan2(x, y)
    return result

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
