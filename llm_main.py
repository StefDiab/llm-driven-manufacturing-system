from planner import extract_orders

from config_loader import load_positions

from agents.crane_agent import CraneAgent
from agents.source_agent import SourceAgent
from agents.process_agent import ProcessAgent
from agents.sink_agent import SinkAgent

from messages import Message


def main():

    # ---------------------------------
    # Load layout
    # ---------------------------------

    positions = load_positions()

    # ---------------------------------
    # Create agents
    # ---------------------------------

    crane = CraneAgent(positions)

    process1 = ProcessAgent("Process1")
    process2 = ProcessAgent("Process2")

    backup_process = ProcessAgent("ProcessBackup")

    sink = SinkAgent("Sink")

    # ---------------------------------
    # Simulate failure
    # ---------------------------------

    failure_msg = Message(
        sender="system",
        receiver=process1,
        performative="SET_FAILURE",
        content={}
    )

    process1.handle_message(failure_msg)

    # ---------------------------------
    # Create sources
    # ---------------------------------

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

    # ---------------------------------
    # User order
    # ---------------------------------

    user_order = (
        "Produce 2 type1 parts and 3 type2 parts"
    )

    print("\nUSER ORDER:")
    print(user_order)

    # ---------------------------------
    # LLM planning
    # ---------------------------------

    orders = extract_orders(user_order)

    print("\nPARSED ORDERS:")
    print(orders)

    # ---------------------------------
    # Execute production
    # ---------------------------------

    type1_qty = orders.get("type1", 0)
    type2_qty = orders.get("type2", 0)

    for _ in range(type1_qty):

        source1.generate_part(part_type=1)

    for _ in range(type2_qty):

        source2.generate_part(part_type=2)


if __name__ == "__main__":
    main()