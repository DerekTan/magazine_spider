#!/usr/bin/python

#To do:
# how to use urllib
# how to login
# how to use re

import urllib.request as request
import urllib.parse as parse
import urllib.error as error
import re
import os
import string

#request_headers = { 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36' }
#myURL="http://jredu.vip.qikan.com/Text/TextMag.aspx?issn=08DC3C17-262E-4F58-B7D9-932AB966E582&year=2015&periodnum=1"

content = request.urlopen(myURL, None, request_headers).read()
print(content)
print("Hello world!")
