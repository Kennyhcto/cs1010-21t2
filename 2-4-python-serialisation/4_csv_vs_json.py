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
  # open
  f = open('files/4_data.json', 'r')
  # read
  tutorials = json.loads(f.read())
  # close
  f.close()
  return tutorials

def write_json_file(data):
  # open
  f = open('files/4_data.json', 'w')
  # write
  f.write(json.dumps(data))
  # close
  f.close()


if __name__ == "__main__":
    stuff = get_sample_data()
    write_json_file(stuff)
