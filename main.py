#coding=utf-8

from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer
from janome.tokenfilter import *
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app, supports_credentials=True)

@app.route('/',methods=['POST'])
def hello_world():
    input = request.json
    s = input['text']
    a = Analyzer(token_filters=[ POSKeepFilter(['名詞','動詞','副詞','形容詞']) ])
    t = Tokenizer()
    res =[]
    for token in a.analyze(s):
        res.append(str(token))
    return jsonify(res)
 
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
