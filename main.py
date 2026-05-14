from agents.crane_agent import CraneAgent
from agents.source_agent import SourceAgent
from agents.process_agent import ProcessAgent
from agents.sink_agent import SinkAgent
from messages import Message
from config_loader import load_positions


def main():

    positions = load_positions()

    crane = CraneAgent(positions)

    process1 = ProcessAgent("Process1")
    failure_msg = Message(
        sender="system",
        receiver=process1,
        performative="SET_FAILURE",
        content={}
    )

    process1.handle_message(failure_msg)
    process2 = ProcessAgent("Process2")

    backup_process = ProcessAgent("ProcessBackup")

    sink = SinkAgent("Sink")

    source1 = SourceAgent(
        name="Source1",
        crane=crane,
        process1=process1,
        process2=process2,
        backup_process=backup_process,
        sink=sink
    )

    source2 = SourceAgent(
        name="Source2",
        crane=crane,
        process1=process1,
        process2=process2,
        backup_process=backup_process,  
        sink=sink
    )

    # Type 1
    source1.generate_part(part_type=1)

    # Type 2
    source2.generate_part(part_type=2)


if __name__ == "__main__":
    main()