from chatbot import Chatbot


class ChatbotServer:
    def __init__(self, app_debug=True):
        self.chatbot = Chatbot()
        print("Chatbot successfully created")

    def computer_answer(self, question, context):
        return self.chatbot.compute_answer(question, context)
