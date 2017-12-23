from flask import Flask, jsonify, request 
import random

app = Flask(__name__)

reply_list = ['밥', '면']

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
        return make_response(reply_list[random.randrange(0, len(reply_list) - 1)])
    else:
        return make_response("무슨 말인지 모르겠어!")

def make_response(text, image = None, width = 0, height = 0):

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

    return response