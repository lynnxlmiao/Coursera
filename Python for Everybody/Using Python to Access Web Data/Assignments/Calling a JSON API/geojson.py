import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
serviceurl = "http://py4e-data.dr-chuck.net/geojson?"
url = serviceurl + urllib.parse.urlencode(
        {'address': address})

print("Retrieving http: ", url)

connection = urllib.request.urlopen(url, context=ctx)
data = connection.read().decode()
print("Retrieved", len(data), "characters")

js = json.loads(data)
print("Place id ", js["results"][0]["place_id"])
