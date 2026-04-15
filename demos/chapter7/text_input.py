import os

def getCurrentDirectory():
    current_directory = os.path.dirname(os.path.realpath(__file__))
    return current_directory