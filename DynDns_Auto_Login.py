#!/usr/bin/python

import mechanize
import time
import cookielib

#Account user/pass dyndns:
username ='XXXXXXX'
password = 'XXXXXXX'

#Setup CookieJar and Browser:
cj = cookielib.LWPCookieJar()
br = mechanize.Browser()
br.set_cookiejar(cj)

#Open the URL
r = br.open('https://account.dyn.com')
br.addheaders = [('User-agent', 'Firefox')]

#Loop through the forms looing for the login form
counter = 0
for form in br.forms():
    if "submit=Log in" in str(form):
        br.select_form(nr=counter)
    else:
		counter += 1

#Log into the form and submit
br.form['username'] = username
br.form['password'] = password
br.submit()

#Throw output into string
html = br.response().read()

if "Welcome" in str(html):
	print "Login succesful, waiting 5 seconds to logout..."
	time.sleep(5)
	r = br.open("https://account.dyn.com/entrance/?__logout=1")
	#print br.response().read()
else:
    print "ERROR: Unable to login"

	
