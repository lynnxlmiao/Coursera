import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

json_url = input("Enter location: ")
print("Retrieving http: ", json_url)
connection = urllib.request.urlopen(json_url, context=ctx)
data = connection.read().decode()
print("Retrieved", len(data), "characters")

js = json.loads(data)

count = 0
sum_number = 0

for comment in js["comments"]:
    sum_number += int(comment["count"])
    count += 1

print("count: ", count)
print("Sum: ", sum_number)
