#   FB chat utilities
#   You can send and read message from facebook messenger
import fbchat


class FB_msg:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.client = fbchat.Client(self.username, self.password)

    def sendMessage(self, receiver, message):
        client = self.client
        friends = client.getUsers(receiver)  # return a list of names
        friend = friends[0]
        sent = client.send(friend.uid, message)
        if sent:
            print("Message sent successfully!")

    def readMessage(self, sender):
        client = self.client
        friends = client.getUsers(sender)  # return a list of names
        friend = friends[0]
        last_messages = client.getThreadInfo(friend.uid, last_n=20)
        last_messages.reverse()  # messages come in reversed order

        for message in last_messages:
            print(message.body)

    def sendImage(self, receiver, image_message, text_message):
        client = self.client
        friends = client.getUsers(receiver)
        friend = friends[0]
        client.sendLocalImage(friend,message=text_message, image=image_message)