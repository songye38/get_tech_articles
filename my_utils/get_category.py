import urllib.request

def get_access_token(client_id, client_secret, redirect_uri, code):
    # API 엔드포인트 URL
    api_url = "https://www.tistory.com/oauth/access_token"
    
    try:
        # API에 GET 요청 보내기
        response = urllib.request.get(api_url, params=params)
        
        # 응답이 성공인 경우
        if response.status_code == 200:
            # 응답을 문자열로 반환
            return response.text

        # 응답이 실패인 경우
        else:
            print(f"Error: {response.status_code} - {response.text}")
    
    except Exception as e:
        print(f"Error: {e}")
    
    return None


access_token_response = get_access_token()

if access_token_response:
    print("Access Token Response:")
    print(access_token_response)
else:
    print("Failed to get access token.")
