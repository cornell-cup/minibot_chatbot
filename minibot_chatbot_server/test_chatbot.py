from minibot_chatbot_server.chatbot import Chatbot

chatbot = Chatbot()
# print(chatbot.context_stack)
print(chatbot.compute_answer("what is ice cream?"))
print(chatbot.compute_answer("How is ice cream made?"))
print(chatbot.compute_answer("What is the meaning of life?"))
