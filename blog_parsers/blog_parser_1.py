import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from my_utils.save_file import save_to_csv

HEADERS = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}

#우버 tech blog 글 가져오기

def parse_blog_1(today, diff_days):
    current_year = datetime.now().year
    # 크롤링할 대상 URL
    url = "https://www.uber.com/en-KR/blog/seoul/engineering/"
    headers =HEADERS

    # 초기 세팅
    try:
        req = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(req)
        html = response.read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        print("성공")
    except urllib.error.HTTPError as e:
        print(f"HTTP Error {e.code}: {e.reason}")
        return

    main_div = soup.find(attrs={'data-baseweb': 'flex-grid-item'})
    datetime_str = main_div.find('p',class_='c3 fe b5 hp b7 ff hz').text.replace(" / Global", "")
    datetime_str = f"{current_year} {datetime_str}"

    datetime_obj = datetime.strptime(datetime_str, "%Y %B %d").date()
    diff = today - datetime_obj
    if abs(diff) <= timedelta(days=diff_days):
        print("The date difference is %d days or less." % diff_days)
        #글 가져오기 함수 호출 클래스 이름으로
        post_url = "https://uber.com"+main_div.find('a')['href']
        get_articles(post_url)
    else:
        print("The date difference is more than %d days" % diff_days)
        return




def get_articles(article_url):
    print("get_articles 호출 성공")
    final_text =[]
    headers = HEADERS

    # 초기 세팅
    try:
        req = urllib.request.Request(article_url, headers=headers)
        response = urllib.request.urlopen(req)
        html = response.read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
    except urllib.error.HTTPError as e:
        print(f"HTTP Error {e.code}: {e.reason}")


    main_texts = soup.find(class_='bp bq gd e8 e9 gy gz')
    h1_texts = main_texts.find_all('p')
    for texts in h1_texts:
        final_text.append(texts.text)
        
    final_text = " ".join(final_text)
    save_to_csv(final_text)
    print("저장 완료")
