#!/usr/bin/env python

import string
import httplib
import time
import sys
import os
from socket import *
import re
import getopt

try:
    import requests
except:
    print "Request library not found, please install it before proceeding\n"
    sys.exit()

from discovery import *

try:
	filename = sys.argv[1]
	lines = [line.rstrip('\n') for line in open(str(filename))]

	if __name__ == '__main__':
		file = open("maillist.txt","w")
		all_emails=[]
		for x in lines:
			print "  searching mails in google -> " + x + ": \n"
			time.sleep(3)
			search = googlesearch.search_google(x.strip(), 50, 0)
			search.process()
			emails = search.get_emails()
			all_emails.extend(emails)
			print "google result: "
			print emails
			print "\n\r"

			print "  searching mails in bing -> " + x + ": \n"
			search = bingsearch.search_bing(x.strip(), 50, 0)
			search.process("no")
			emails = search.get_emails()
			all_emails.extend(emails)
			time.sleep(3)
			print "bing result: " 
			print emails
			print "\n\r"
			print "\n-------------------------\nWriting to file:\n-------------------------"
			for email in set(all_emails):
				if email[:email.index('@')]:
					print email
					file.write(email + "\n")
			all_emails = []
			print "\n\r"
		file.close()

except:
	print "Invalid file name. Usage: python multimail.py [filename]"


