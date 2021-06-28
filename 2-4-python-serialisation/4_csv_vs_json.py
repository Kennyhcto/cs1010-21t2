"""
Some formats can be represented in JSON
which cannot be represented in CSV files.
"""

import json


def get_sample_data():
    return {
        "fridge": ["chiller", "door", "shelves"],
        "dishwasher": ["motor", "rack", "tube"],
        "vacuum": ["hose", "motor", "bag"]}


def read_json_file():
    pass


def write_json_file(data):
    pass


if __name__ == "__main__":
    pass
