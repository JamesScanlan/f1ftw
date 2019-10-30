from calculate_best_qualifying import calculate_best_qualifying
from calculate_best_race import calculate_best_race
from calculate_best_progression import calculate_best_progression
from calculate_best_joker import calculate_best_joker
from get_grand_prix_name import get_grand_prix_name_from_command_line_arguments
from process_command_line_arguments import CommandLineArguments
import sys
import load_config

def calculate_best(grand_prix_name, current_year):
    print("\nQualifying\n==========")
    calculate_best_qualifying(grand_prix_name, current_year)
    print("\nRace\n====")
    calculate_best_race(grand_prix_name, current_year)
    print("\nProgression\n===========")
    calculate_best_progression(grand_prix_name, current_year)
    if current_year == 2017:
        print("\nJoker\n=====")
        calculate_best_joker(grand_prix_name, current_year)

def read_additional_command_line_argument():
    args = CommandLineArguments()
    if len(args)>1:
        return args[1]
    return None

def open_file(filename):
    f = open(filename, "w")
    return f

def redirect_console_ouput_to_file(file_handle):
    original_output = sys.stdout
    sys.stdout = file_handle
    return original_output

def close_file(file_handle, original_output):
    file_handle.close()
    sys.stdout = original_output

if __name__== "__main__":
    grand_prix_name = get_grand_prix_name_from_command_line_arguments(default="Australian")
    config = load_config.read_config()
    output_filename = read_additional_command_line_argument()
    file_handle = None
    original_output = None
    if output_filename != None:
        file_handle = open_file(output_filename)
        original_output = redirect_console_ouput_to_file(file_handle)

    calculate_best(grand_prix_name, config.current_year)

    if file_handle != None:
        close_file(file_handle, original_output)
        print(output_filename + " created")
