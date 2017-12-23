from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/keyboard')
def keyboard():
    return jsonify({
        "type" : "buttons",
        "buttons" : ["선택1", "선택2", "선택3"]
    })

@app.route('/message', methods=['POST'])
def message();
    return jsonify({
        'message' : {
            'text' : '안녕하세요! 아직은 개발 중이라 이 말밖에 못 해요!'
        }
    })