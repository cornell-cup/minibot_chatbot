from flask import Flask
from flask import request, render_template, jsonify, session, redirect
from flask_api import status
import os.path
import json
import sys
import time

import base_station


app = Flask(__name__)

# Error messages
NO_BOT_ERROR_MSG = "Please connect to a Minibot!"

# Update chatbot object's context upon submission


@app.route('/chatbot', methods=['POST', 'GET'])
def chatbot():
    """Toggles between the speech recognition feature for commands 
    and speech recognition features for chatbot. Returns the first message 
    in the BaseStation speech recognition queue for a GET request
    """
    if request.method == 'POST':
        data = request.get_json()
        bot_name = data['bot_name']

        if not bot_name:
            error_json = {"error_msg": NO_BOT_ERROR_MSG}
            return json.dumps(error_json), status.HTTP_400_BAD_REQUEST
        command = data["command"]
        base_station.toggle_speech_recognition(bot_name, command)
        return json.dumps(True), status.HTTP_200_OK
    else:
        # message = base_station.get_chatbot_status()
        message = base_station.chatbot_temp_context
        print("message is " + message)
        return json.dumps(message), status.HTTP_200_OK


@app.route('/chatbot_context_update', methods=['POST', 'GET'])
def update_chatbot_obj():
    """ Updates the chatbot object with the context inside the textbox from
    the GUI
    """
    if request.method == 'POST':
        data = request.get_json()
        context = data['context']
        base_station.update_chatbot_context(context)
        return json.dumps("successful"), status.HTTP_200_OK
    else:
        return status.HTTP_200_OK


@app.route('/chatbot_context/<email>', methods=['POST', 'GET'])
def chatbot_context(email):
    """ Updates the user's chatbot context if the route is a post request
    Sends the user's chatbot context to the GUI if it is a get request
    """
    # Send chatbot object's context to database
    if request.method == 'POST':
        # TODO? check user id here
        data = request.get_json()
        print("routes received", data)
        print(email)
        context = base_station.get_chatbot_obj_context()
        # print(context)
        user_id = base_station.get_user_id(email)
        base_station.update_chatbot_context_db(user_id, context)
        return json.dumps("successful"), status.HTTP_200_OK

    # Send context from database to chatbot
    else:
        message = "You are not logged in."
        if email != "":
            user_id = base_station.get_user_id(email)
            message = base_station.chatbot_get_context(user_id)
        return json.dumps(message), status.HTTP_200_OK
    # TODO add a close tab trigger for update_chatbot_context_db
    # base_station.update_chatbot_context_db(user_id, context)


@app.route('/switch_chatbot', methods=['GET'])
def switch_chatbot():
    base_station.toggle_chatbot()
    return json.dumps('successful'), status.HTTP_200_OK


@app.route('/chatbot_clear', methods=['POST', 'GET'])
def chatbot_clear_context():
    """write the documentation """
    if request.method == 'POST':
        base_station.chatbot_clear_context()
        return json.dumps('successful'), status.HTTP_200_OK
