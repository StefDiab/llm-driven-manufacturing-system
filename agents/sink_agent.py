class SinkAgent:

    def __init__(self, name):
        self.name = name

    def handle_message(self, message):

        if message.performative == "RECEIVE_PART":

            print(f"[{self.name}] Part completed and removed")