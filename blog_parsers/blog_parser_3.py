from datetime import datetime, timedelta
from my_utils.save_file import save_to_csv
from my_utils.initialize import initialize
import re

#슬랙 글 가져오기


def parse_blog_3(today, diff_days):
    # 크롤링할 대상 URL
    url = "https://slack.engineering"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    soup = initialize(headers,url)


    #가장 최신 블로그 글 주소를 찾기 위한 과정
    main_div = soup.find('div', class_='post-card__body')
    time_div = main_div.find('h2', class_='post-card__title')
    article_url = time_div.find('a')['href']


    #게시글 url을 가지고 다시 parsing하기
    soup = initialize(headers,article_url)

    datetime_str = soup.find('span', class_='c-post-meta__date').text
    datetime_str = datetime_str.split("•")[1].strip()
    diff = int(re.findall(r'\b\d+\b', datetime_str)[0])
    diff_timedelta = timedelta(days=diff.days)
    datetime_obj = today - timedelta(days=diff)

    if abs(diff_timedelta) <= timedelta(days=diff_days):
        print("The date difference is %d days or less." % diff_days)
        #글 가져오기 함수 호출 클래스 이름으로
        post_url = main_div.find('a')['href']
        get_articles(post_url,datetime_obj)
    else:
        print("The date difference is more than %d days" % diff_days)
        return
    









    
def get_articles(article_url,date_obj):
    final_text =[]
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    # 초기 세팅
    try:
        req = urllib.request.Request(article_url, headers=headers)
        response = urllib.request.urlopen(req)
        html = response.read().decode('utf-8')
    except urllib.error.HTTPError as e:
        print(f"HTTP Error {e.code}: {e.reason}")

    soup = BeautifulSoup(html, 'html.parser')

    main_texts = soup.find_all(class_='pw-post-body-paragraph')
    for texts in main_texts:
        final_text.append(texts.text)
        
    final_text = " ".join(final_text)
    save_to_csv('NETFLIX',date_obj,final_text)
