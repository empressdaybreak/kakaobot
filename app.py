from flask import Flask, jsonify, request 
import random

import naver

app = Flask(__name__)

@app.route('/keyboard')
def keyboard():
    return jsonify({ 
        "type" : "text"
    })

@app.route('/message', methods=['POST'])
def process_message():
    message = request.json
    if message['type'] == 'photo':
        return jsonify({
            'message' : {
                'text' : '죄송합니다! 무슨 사진인지 잘 모르겠어요..'
            }
        })
    else:
        content = message['content']
        print('메시지 도착: %s' % content)
        try:
            return jsonify(get_reply(content))
        except Exception as e:
            return jsonify(
                make_response('오류가 발생했습니다: %s' % str(e))
            )
        

def get_reply(content):
    if '안녕' in content:
        return make_response("안녕!")
    elif '사기리' in content:
        return make_response("사기리", "http://daybreak.fun/sagiri.jpg", 720, 1017)
    elif '메뉴' in content:
        return decide_menu()
    elif content.startswith('검색:'):
        return decide_search(content)
    elif '누구' in content or '새벽' in content:
        return make_response("저에 대해 알고 싶으시다면 http://daybreak.fun/ 으로 와주세요!")
    elif '도와줘' in content:
        return make_response("아래에 있는 단어가 포함되도록 입력해주세요.\n'안녕'/'사기리'/'메뉴'/'새벽'/'버튼'/'뭐하지'")
    elif content == '뭐하지':
        return make_response('버튼을 선택해 주세요', buttons = ['만화', '애니메이션', '취소'])
    elif content == '만화':
        return make_response('http://marumaru.in')
    elif content == '애니메이션':
        return make_response('http://ani119.org')
    elif content == '취소':
        return make_response('취소 했습니다.')
    
    else:
        return make_response("무슨 말인지 모르겠어요!\n대화를 하고 싶다면 '도와줘' 라고 입력해주세요!")

def make_response(text, image = None, width = 0, height = 0, buttons = None):

    response = {
        'message' : {
            'text' : text
        }
    }

    if image:
        response['message']['photo'] = {
            'url' : image,
            'width' : width,
            'height' : height
        }
    
    if buttons:
        response['keyboard'] = {
            'type': 'buttons',
            'buttons': buttons
        }

    return response

def decide_menu():
    reply_list = ['피자', '치킨', '짜장면', '라면', '초밥', '김치찌개']
    menu = reply_list[random.randrange(0, len(reply_list))]
    search_result = naver.search(menu)
    
    image = search_result['items'][random.randrange(0, len(search_result['items']))]
    return make_response("오늘 메뉴는 '%s' 어떠신가요?" %menu, image['link'], int(image['sizewidth']), int(image['sizeheight']))

def decide_search(content):
    keyword = content.split('검색:')[1]
    search_result = naver.search(keyword)

    image = search_result['items'][random.randrange(0, len(search_result['items']))]
    return make_response("검색 결과 입니다. '%s'" %keyword, image['link'], int(image['sizewidth']), int(image['sizeheight']))

    