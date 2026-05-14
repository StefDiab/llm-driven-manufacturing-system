from agents.part_agent import PartAgent


class SourceAgent:

    global_part_counter = 0

    def __init__(self, name, crane, process1, process2, backup_process, sink):
        self.name = name
        self.crane = crane
        self.process1 = process1
        self.process2 = process2
        self.backup_process = backup_process
        self.sink = sink

    def generate_part(self, part_type):
        SourceAgent.global_part_counter += 1

        print(f"[{self.name}] New type {part_type} part created")

        part = PartAgent(
                part_id=SourceAgent.global_part_counter,
                part_type=part_type,
                source_name=self.name,
                crane=self.crane,
                process1=self.process1,
                process2=self.process2,
                backup_process=self.backup_process,
                sink=self.sink
        )

        part.start()