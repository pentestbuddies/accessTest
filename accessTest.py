#!/usr/bin/python3

import argparse
import requests

parser = argparse.ArgumentParser(description="Check to see if an authenticated or unauthenticated user has access to a set of URL's")
parser.add_argument("urls", help='A list of urls that will be check')
parser.add_argument("-c", "--cookie", help="The cookiename followed by the cookie Value", default='', nargs=2)

parser.add_argument("-t","--test", help="A test value to check for once you are logged in. This allows the script to see if the login was sucessful or not. This is the positive check if instead you want to do the negative check use -n or --negative.")
parser.add_argument("-n", "--negative", help="A value on the login page. This checks to see if the value is found to determine if you are still on the login page. This is the negative check the positive check is -t or --test.")

#TODO will be added as functionality increases 
#parser.add_argument("-s", "--status")
#parser.add_argument("-v", "--non_status")
#parser.add_argument("", "")
#parser.add_argument("-r", "--request", help="The request type sent (Currently only supports GET, POST and PUT", choices=["GET", "POST", "PUT"], default="GET")
#parser.add_argument("-p", "--payload", help="Any special payload to be sent. Must be in the form of name value")

args = parser.parse_args()


#Variables used in the script
#TODO
login_page_text = ""
logged_in_text = ""
bad_status = [403, 404, 302]
searchTerms = ['password', 'apikey', 'key', 'secret']

#checking if the cookie is set
if args.cookie:
    cookie = { args.cookie[0] : args.cookie[1]}

#Opening the list of URLS that will be checked
with open(args.urls) as f:
    data = f.read()

url_list = data.split("\n")




for urls in url_list:
    request = requests.get(url)
    
    if (request.status_code in badStatus) or (request.history in badStatus):
        continue
    
    pageText = request.text
    if pageText.find("") == -1:
        print(i + " " + str(request.status_code))
    
        

