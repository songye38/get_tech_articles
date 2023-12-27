import urllib.request
from bs4 import BeautifulSoup


def initialize(headers,url):
    try:
        req = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(req)
        html = response.read().decode('utf-8')
    except urllib.error.HTTPError as e:
        print(f"HTTP Error {e.code}: {e.reason}")

    soup = BeautifulSoup(html, 'html.parser')

    return soup