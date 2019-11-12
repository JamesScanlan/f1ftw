import sys

def open_file(filename):
    f = open(filename, "w")
    return f

def close_file(f):
    f.close()