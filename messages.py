class Message:
    def __init__(self, sender, receiver, performative, content):
        self.sender = sender
        self.receiver = receiver
        self.performative = performative
        self.content = content