import time
import threading


class ProcessAgent:

    def __init__(self, name):

        self.name = name

        self.lock = threading.Lock()

        self.busy = False

        self.failed = False

    def handle_message(self, message):

        # ---------------------------------
        # Simulate failure
        # ---------------------------------

        if message.performative == "SET_FAILURE":

            self.failed = True

            print(f"[{self.name}] FAILED")

            return

        # ---------------------------------
        # Recover process
        # ---------------------------------

        if message.performative == "RECOVER":

            self.failed = False

            print(f"[{self.name}] RECOVERED")

            return

        # ---------------------------------
        # Reserve process
        # ---------------------------------

        if message.performative == "REQUEST_PROCESS":

            with self.lock:

                if not self.busy and not self.failed:

                    self.busy = True

                    return {
                        "accepted": True
                    }

                else:

                    return {
                        "accepted": False
                    }

        # ---------------------------------
        # Start process
        # ---------------------------------

        if message.performative == "START_PROCESS":

            print(f"[{self.name}] Processing started")

            time.sleep(3)

            print(f"[{self.name}] Processing finished")

            self.busy = False

            return {
                "performative": "PROCESS_FINISHED"
            }