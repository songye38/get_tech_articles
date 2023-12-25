import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

def parse_blog_1():
    # 크롤링할 대상 URL
    url = "https://netflixtechblog.com/?gi=25d9e7be88d3"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    # 초기 세팅
    try:
        req = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(req)
        html = response.read().decode('utf-8')
    except urllib.error.HTTPError as e:
        print(f"HTTP Error {e.code}: {e.reason}")

    soup = BeautifulSoup(html, 'html.parser')


    # 내용 정제해서 가져오기
    elements_with_u_flexCenter = soup.find_all(class_='u-flexCenter')

    # Iterate through the elements with 'u-flexCenter' class
    for element in elements_with_u_flexCenter:
        # Find the 'date' element within each 'u-flexCenter' element
        date_element = element.find('time')
        print(date_element)