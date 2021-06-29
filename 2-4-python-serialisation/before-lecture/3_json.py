"""
JSON

JavaScript Object Notation (JSON) is a serialisation format with its origins in the Javascript language. However, in recent times it has become a universal standard used by many languages and tools for storing data.

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
  pass

def write_json_file(data):
  pass

if __name__ == "__main__":
  pass