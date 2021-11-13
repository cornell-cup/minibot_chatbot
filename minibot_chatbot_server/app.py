from flask import Flask
from flask import request, render_template, jsonify, session, redirect
import os.path
import json
import sys


from chatbot import Chatbot
# from minibot_chatbot_server import app

app = Flask(__name__)

chatbot = Chatbot()


@app.route('/qa', methods=['POST', 'GET'])
def qa():
    if request.method == "POST":
        data = request.get_json()
        question = data['question']
        context = data['context']
        print(question, context)
        # answer = chatbot.compute_answer(question, context)
        chatbot.test()


app.run()
