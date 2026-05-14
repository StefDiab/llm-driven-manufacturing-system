import json


def load_positions():

    with open("config/positions.json", "r") as file:

        positions = json.load(file)

    return positions