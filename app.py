from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/keyboard')
def keyboard():
    return jsonify({
        "type" : "button",
        "buttons" : ["선택1", "선택2", "선택3"]
    })