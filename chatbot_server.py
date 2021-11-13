from chatbot import Chatbot


class Chatbot_Server:
    def __init__(self, app_debug=True):
        self.chatbot = Chatbot()

    def computer_answer(self, context, question):
        return self.chatbot.compute_answer(context, question)
