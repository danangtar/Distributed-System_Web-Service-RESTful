import json
import urllib2
import time

tstart = time.time()

# request to REST web service
url1 = 'http://192.168.43.80:5000'
url2 = 'http://192.168.43.40:5001'

hasil1 = urllib2.urlopen(url1)
hasil1 = json.load(hasil1)

hasil2 = urllib2.urlopen(url2)
hasil2 = json.load(hasil2)
hasil2 = dict(hasil2)

for freq in hasil1:
    if freq[0] in hasil2:
        hasil2[freq[0]] = hasil2[freq[0]] + freq[1]
    else:
        hasil2[freq[0]] = freq[1]

hasil2 = sorted(hasil2.items(), key=lambda x: x[1], reverse=True)


i = 0
while i < 10:
    print hasil2[i]
    i = i + 1

tend = time.time()
print("Total elapsed time: %d msec" % ((tend-tstart)*1000))