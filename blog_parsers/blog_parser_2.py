import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

# 넷플렉스 블로그 글 가져오기

def parse_blog_2():
    # 크롤링할 대상 URL
    today = datetime.today().date()
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


    elements_with_u_flexCenter = soup.find_all(class_='u-flexCenter')

    for element in elements_with_u_flexCenter:
    # Find the first 'date' element within each 'u-flexCenter' element
        date_element = element.find('time')
        
        # Check if date_element is not None before accessing attributes
        if date_element:
            datetime_str = date_element['datetime']
            
            # Convert string to datetime object
            datetime_obj = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S.%fZ").date()
            diff = today - datetime_obj
            if abs(diff) <= timedelta(days=7):
                print("The date difference is 7 days or less.")
            else:
                print("The date difference is more than 7 days.")
            
