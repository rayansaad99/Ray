
#Author :Ray
#this program is for refreshing a page to find a KEY word in about page .
import sys
import urllib2

while true:
    about_page = urllib2.urlopen("insert url here").read()
    if "KEY" in about_page:
	
        print(about_page)
        sys.exit(0)
