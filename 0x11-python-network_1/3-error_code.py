#!/usr/bin/python3
"""This sends a request to a given URL and displays the response body.
Usage: ./3-error_code.py <URL>
  - Handles HTTP errors.
"""
import urllib.request
import urllib.parse
import urllib.error
import sys


def main(url,):
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))


if __name__ == '__main__':
    url = sys.argv[1]
    main(url)
