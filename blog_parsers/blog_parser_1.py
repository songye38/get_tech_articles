import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from my_utils.save_file import save_to_csv

#우버 tech blog 글 가져오기

def parse_blog_2(today, diff_days):
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


    main_div = soup.find('div', class_='col u-xs-marginBottom10 u-paddingLeft9 u-paddingRight12 u-paddingTop0 u-sm-paddingTop20 u-paddingBottom25 u-size4of12 u-xs-size12of12 u-marginBottom30')
    time_div = main_div.find('time')
    datetime_str = time_div['datetime']
    datetime_obj = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S.%fZ").date()
    diff = today - datetime_obj
    if abs(diff) <= timedelta(days=diff_days):
        print("The date difference is %d days or less." % diff_days)
        #글 가져오기 함수 호출 클래스 이름으로
        post_url = main_div.find('a')['href']
        get_articles(post_url)
    else:
        print("The date difference is more than %d days" % diff_days)
        return
    
def get_articles(article_url):