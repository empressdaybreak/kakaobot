from flask import Flask, jsonify, request

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
        if '안녕' in content:
            response = "안녕하세요!"
        else:
            response = "무슨 말인지 잘 모르겠어요.."
        return jsonify({
            'message' : {
                'text' : response
            }
        })