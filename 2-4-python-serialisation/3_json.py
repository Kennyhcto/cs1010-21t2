"""
JSON

JavaScript Object Notation (JSON) is a serialisation format with its origins in the Javascript language.
However, in recent times it has become a universal standard used by many languages and tools for storing data.

Important points:
 * JSON looks very similar to how we write data structures in Python.
 * JSON supports two structures:
   * Arrays, which are similar in to lists in Python
   * Objects, which are similar to dictionaries (keys *must* be strings)
 * Single values can be strings or numbers.

Side note: You can format your JSON documents by right-click->"Format Document"
"""

import json

def get_sample_data():
  return [ 
    {'tutorial': 'T15A', 'tutor': 'Sim', 'enrollments': 20},
    {'tutorial': 'T17A', 'tutor': 'Kai', 'enrollments': 23}
    ]

def read_json_file():
  # open
  f = open('files/3_data.json', 'r')
  # read
  tutorials = json.loads(f.read())
  # close
  f.close()
  return tutorials

def write_json_file(data):
  # open
  f = open('files/3_data.json', 'w')
  # write
  f.write(json.dumps(data))
  # close
  f.close()

if __name__ == "__main__":
  #tutorials = get_sample_data()
  #write_json_file(tutorials)

  tutorials = read_json_file()
  #print(tutorials)
  #print(tutorials[1]['tutor'])
  tutorials.append({
        "tutorial": "T15A",
        "tutor": "Liz",
        "enrollments": 23
    })
  print(tutorials)
  write_json_file(tutorials)
