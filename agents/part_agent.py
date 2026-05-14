import threading
import time

from messages import Message


class PartAgent(threading.Thread):

    def __init__(
        self,
        part_id,
        part_type,
        source_name,
        crane,
        process1,
        process2,
        backup_process,
        sink
    ):

        super().__init__()

        self.part_id = part_id
        self.part_type = part_type

        self.source_name = source_name

        self.crane = crane

        self.process1 = process1
        self.process2 = process2

        self.backup_process = backup_process

        self.sink = sink

        # ---------------------------------
        # Dynamic process plans
        # ---------------------------------

        if self.part_type == 1:

            self.route = [
                ("Process1", self.process1)
            ]

        elif self.part_type == 2:

            self.route = [
                ("Process2", self.process2),
                ("Process1", self.process1)
            ]

    def run(self):

        print(
            f"[Part {self.part_id}] "
            f"Started with type {self.part_type}"
        )

        current_location = self.source_name

        # ---------------------------------
        # Loop through process plan
        # ---------------------------------

        for station_name, process_agent in self.route:

            # ---------------------------------
            # Request process reservation
            # ---------------------------------

            request_msg = Message(
                sender=self,
                receiver=process_agent,
                performative="REQUEST_PROCESS",
                content={}
            )

            response = process_agent.handle_message(request_msg)

            retry_count = 0

            while not response["accepted"]:

                print(
                    f"[Part {self.part_id}] "
                    f"Waiting for {station_name}"
                )

                time.sleep(1)

                retry_count += 1

                # ---------------------------------
                # Failure recovery / rerouting
                # ---------------------------------

                if retry_count >= 5 and station_name != "ProcessBackup":
                    print(
                        f"[Part {self.part_id}] "
                        f"{station_name} failed -> rerouting"
                    )

                    station_name = "ProcessBackup"

                    process_agent = self.backup_process

                    request_msg = Message(
                        sender=self,
                        receiver=process_agent,
                        performative="REQUEST_PROCESS",
                        content={}
                    )

                response = process_agent.handle_message(request_msg)

            # ---------------------------------
            # Move to station
            # ---------------------------------

            move_msg = Message(
                sender=self,
                receiver=self.crane,
                performative="REQUEST_MOVE",
                content={
                    "part_id": self.part_id,
                    "from": current_location,
                    "to": station_name
                }
            )

            self.crane.handle_message(move_msg)

            # ---------------------------------
            # Start process
            # ---------------------------------

            process_msg = Message(
                sender=self,
                receiver=process_agent,
                performative="START_PROCESS",
                content={}
            )

            process_agent.handle_message(process_msg)

            current_location = station_name

        # ---------------------------------
        # Move to sink
        # ---------------------------------

        move_sink_msg = Message(
            sender=self,
            receiver=self.crane,
            performative="REQUEST_MOVE",
            content={
                "part_id": self.part_id,
                "from": current_location,
                "to": "Sink"
            }
        )

        self.crane.handle_message(move_sink_msg)

        # ---------------------------------
        # Send to sink
        # ---------------------------------

        sink_msg = Message(
            sender=self,
            receiver=self.sink,
            performative="RECEIVE_PART",
            content={}
        )

        self.sink.handle_message(sink_msg)

        print(f"[Part {self.part_id}] Finished")