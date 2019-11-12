import sys

def set_output_to_file(file_handler):
    original_output = sys.stdout
    sys.stdout = file_handler
    return original_output

def set_output_to_console(original_output):
    sys.stdout = original_output