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
    f = open('week5/serialisation-answers/major_parts.json', 'w')
    f.write(json.dumps(data))
    f.close()


if __name__ == "__main__":
    major_parts = get_sample_data()
    write_json_file(major_parts)
