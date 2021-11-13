from chatbot_server import ChatbotServer
from minibot_chatbot_server import app
from flask import Flask
from flask import request, render_template, jsonify, session, redirect
from flask_api import status
import json

chatbot_server = ChatbotServer(app.debug)


@app.route('/qa', methods=['POST', 'GET'])
def qa():
    if request.method == "POST":
        data = request.get_json()
        question = data['question']
        context = data['context']
        answer = chatbot_server.computer_answer(question, context)
