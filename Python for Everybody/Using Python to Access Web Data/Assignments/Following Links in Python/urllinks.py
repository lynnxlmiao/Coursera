# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Enter main url
url = input('Enter url - ')

# Enter count repeat times comment_counts
count = int (input('Enter Count - '))

# Enter the link at position (the first name is 1)
link_position = int (input ('Enter Position - '))

while count >= 0:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve the anchor tags
    tags = soup('a')

    print (url)
    url = tags[link_position - 1].get("href", None)
    count = count - 1
