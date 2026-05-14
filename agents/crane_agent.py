import time
import threading


class CraneAgent:

    def __init__(self, positions):

        self.lock = threading.Lock()
        self.positions = positions
    def handle_message(self, message):

        if message.performative == "REQUEST_MOVE":

            with self.lock:

                from_station = message.content["from"]
                to_station = message.content["to"]

                part_id = message.content["part_id"]
                from_pos = self.positions[from_station]
                to_pos = self.positions[to_station]
                print(
                    f"[Crane] Moving Part {part_id} "
                    f"from {from_station} ({from_pos['x']},{from_pos['y']}) "
                    f"to {to_station} ({to_pos['x']},{to_pos['y']})"
                )

                time.sleep(2)

                return {
                    "performative": "MOVE_FINISHED"
                }