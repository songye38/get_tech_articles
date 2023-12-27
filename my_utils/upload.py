import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# 필요한 환경 변수 불러오기
access_token = os.getenv("ACCESS_TOKEN")
blog_name = os.getenv("BLOG_NAME")
category_id = os.getenv("CATEGORY_ID")
password = os.getenv("PASSWORD")

# Tistory API 엔드포인트
api_url = "https://www.tistory.com/apis/post/write"

# 필요한 파라미터 설정
params = {
    'access_token': access_token,
    'output': 'json',
    'blogName': blog_name,
    'title': 'Your Title',
    'content': 'Your Content',
    'visibility': '3',  # 0: 비공개, 1: 보호, 3: 공개
    'category': category_id,
    'published': 'now',  # 또는 'scheduled', 'draft'
    'slogan': 'Your Slogan',
    'tag': 'tag1, tag2',
    'acceptComment': '1',  # 1: 댓글 허용, 0: 댓글 비허용
    'password': password,
}

# POST 요청 보내기
response = requests.post(api_url, params=params)

# 응답 확인
print(response.status_code)
print(response.json())  # 만약 JSON 형식의 응답이라면 출력


def upload():
    pass