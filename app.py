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
    
        return jsonify(get_reply(content))
        

def get_reply(content):
    if '안녕' in content:
        return make_response("안녕!")
    elif '사기리' in content:
        return make_response("사기리", "http://daybreak.fun/sagiri.jpg", 720, 1017)
    elif '메뉴' in content:
        return decide_menu()
    elif '누구' in content or '새벽' in content:
        return make_response("저에 대해 알고 싶으시다면 http://daybreak.fun/ 으로 와주세요!")
    elif content == '버튼':
        return make_response('버튼을 선택해 주세요', buttons = ['버튼 1', '버튼 2', '취소'])
    elif content == '버튼 1':
        return make_response('버튼 1을 눌렀습니다.')
    elif content == '버튼 2':
        return make_response('버튼 2을 눌렀습니다.')
    elif content == '취소':
        return make_response('취소 했습니다.')
    
    else:
        return make_response("무슨 말인지 모르겠어!")

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
