import requests

import config

API_URL = 'https://openapi.naver.com/v1/search/image'

def search(keyword):
    """
    네이버 이미지 검색을 행합니다.
    keyword : 검색 키워드
    """

    response = requests.get(API_URL, params = { 'query' : keyword }, headers ={
        "X-Naver-Client-Id" : config.CLIENT_KEY,
        "X-Naver-Client-Secret" : config.CLIENT_SECRET
    })
    
    if response.code is not 200:
        raise Exception("요청에 실패 하였습니다.")
    

    return response.json()