#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @ Time     : 19-3-25 下午7:53
  @ Author   : Vodka
  @ File     : Entity2Token.py
  @ Software : PyCharm
"""
from flask import request
from flask import Flask
from gevent.pywsgi import WSGIServer
import json,sys,requests,logging
from ShallowParser import ShallowParser
from ErPredictor import ErPredictor
import json
# encoding=utf8
import sys
import time
reload(sys)
sys.setdefaultencoding('utf8')

app = Flask(__name__)


s = ShallowParser()
e = ErPredictor()

@app.route('/dbpediaEntity2Token', methods=['POST'])
def dbpediaEntity2Token():
    question = request.get_json(silent=True)['question']
    result_key_chunks = s.shallowParse(question)
    er_predict_result = e.erpredict(result_key_chunks)
    print er_predict_result
    print question
    #　[{'chunk': 'father', 'surfacelength': 6, 'class': 'relation', 'surfacestart': 13}, {'chunk': 'Kobe Bryant', 'surfacelength': 11, 'class': 'entity', 'surfacestart': 23}, {'chunk': 'born', 'surfacelength': 4, 'class': 'relation', 'surfacestart': 35}]
    res = question
    # print res
    for item in er_predict_result:
        if item['class'] == 'entity':
            res = res.replace(item['chunk'], "<Entity>")
    return json.dumps(res)

if __name__ == '__main__':
    http_server = WSGIServer(('', int(sys.argv[1])), app)
    http_server.serve_forever()
