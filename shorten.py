#!/usr/bin/env python

import argparse
import requests

DEFAULT_ACCESS_TOKEN_FILE = "bitly.txt"

def ignore_warnings():
    from requests.packages.urllib3.exceptions import InsecureRequestWarning
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def set_args():
    global args
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="URL to shorten")
    parser.add_argument("--bitly", help=f"bit.ly API Access Token (Get one here: https://bitly.is/2KVHfgS). If not provided you need to create a '{DEFAULT_ACCESS_TOKEN_FILE}' file with the access token inside.")
    args = parser.parse_args()

def access_token(access_token):
    if access_token:
        token = access_token
    else:
        try:
            with open(DEFAULT_ACCESS_TOKEN_FILE, "r") as bitly:
                token = bitly.read()
        except FileNotFoundError:
            print(f"You need to create a '{DEFAULT_ACCESS_TOKEN_FILE}' file with the bit.ly API access token inside.\nGet one access token here: https://bitly.is/2KVHfgS")
            exit()
    return token.strip()

def shorten(uri, token=''):
    ignore_warnings()
    query_params = {
        'access_token': access_token(token),
        'longUrl': uri
    }

    endpoint = 'https://api-ssl.bitly.com/v3/shorten'
    response = requests.get(endpoint, params=query_params, verify=False)

    data = response.json()

    if data['status_code'] != 200:
        result = data['status_txt']
        if result == 'INVALID_URI':
            result = f"Invalid URI ({uri}). Example: https://www.google.com/"
        elif result == 'INVALID_ARG_ACCESS_TOKEN':
            result = f"Invalid Access Token ({query_params['access_token']}). Get one here: https://bitly.is/2KVHfgS"
    else:
        result = data['data']['url']
    return result

if __name__ == "__main__":
    set_args()
    print(shorten(args.url, args.bitly))