#!/usr/bin/python3
"""This displays the X-Request-Id header variable of a request to a given URL.
Usage: ./5-hbtn_header.py <URL>
"""
import sys
import requests


def main(url,):
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))


if __name__ == '__main__':
    url = sys.argv[1]
    main(url)
