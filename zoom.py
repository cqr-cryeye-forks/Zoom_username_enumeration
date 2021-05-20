# Required modules
import argparse
import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Just some colors and shit bro
white = '\033[97m'
green = '\033[1;32m'
red = '\033[1;31m'
yellow = '\033[1;33m'
end = '\033[1;m'
info = '\033[1;33m[!]\033[1;m'
que = '\033[1;34m[?]\033[1;m'
bad = '\033[1;31m[-]\033[1;m'
good = '\033[1;32m[+]\033[1;m'
run = '\033[1;97m[~]\033[1;m'

parser = argparse.ArgumentParser()  # defines the parser
parser.add_argument('-u', '--url', help='Target wordpress website')  # Adding argument to the parser
args = parser.parse_args()  # Parsing the arguments

if args.url:
    url = args.url
    response = requests.get('%s/wp-json/wp/v2/users' % url, verify=False).text
    if 'Sorry, you are not allowed to list users.' in response:
        print(' %s Not vulnerable' % bad)
    elif 'Not Found' in response or '!DOCTYPE html' in response or '404' in response or '<html>' in response:
        print('The requested URL was not found on this server')
    else:
        data = json.loads(response)
        print(data)
else:
    parser.print_help()
