from base_station import Chatbot as ChatbotT


def update_chatbot_context(self, context: str):
    """ Update user's context to the Chatbot object
    """
    self.chatbot.update_context(context)


def get_chatbot_obj_context(self):
    return self.chatbot.get_all_context()


def update_chatbot_context_db(self, user_id, context):
    """ Update user's context if user exists upon exiting the session
    (closing the GUI tab)
    """
    if user_id != "":
        user = ChatbotT.query.filter_by(id=user_id).first()

        # user is not logged in
        if user is None:
            # make new record in chatbot table
            new_context = ChatbotT(
                user_id=user_id,
                context=context
            )
            db.session.add(new_context)
        else:
            # do this if user exists in chatbot database already
            user.context += ". " + context

        db.session.commit()
    return


def chatbot_get_context(self, user_id):
    """Gets the stored context for the chatbot based on user_id.
            If user_id is nonexistent or empty, returns an empty
            json object. Otherwise, returns a json object with the context and its
            corresponding user_id """

    if user_id != "":
        user = ChatbotT.query.filter_by(id=user_id).first()

        if user is None:
            return {'context': '', 'user_id': ''}
        else:
            print("user's context: " + user.context)
            self.chatbot.context_stack = [user.context]
            data = {'context': user.context, 'user_id': user_id}
            return data
    else:
        return {'context': '', 'user_id': ''}


def chatbot_clear_context(self):
    self.chatbot.reset_context()
