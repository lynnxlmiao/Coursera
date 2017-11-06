import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter url: ')

total_number = 0
sum = 0

print('Retrieving', url)
uh = urllib.request.urlopen(url)
xml = uh.read()
print('Retrieved', len(xml), 'charactiers')

tree = ET.fromstring(xml)
counts = tree.findall('.//count')
for count in counts:
    sum += int(count.text)
    total_number += 1

print('Count:', total_number)
print('Sum:', sum)
