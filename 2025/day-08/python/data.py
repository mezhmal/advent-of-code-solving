import os

current_directory = os.path.dirname(__file__)

def readFile(filename):
  with open(os.path.join(current_directory, '..', 'data', filename)) as f:
    return f.readlines()
