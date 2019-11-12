from calculate_best_qualifying import calculate_best_qualifying
from calculate_best_race import calculate_best_race
from calculate_best_progression import calculate_best_progression
from calculate_best_joker import calculate_best_joker
from get_grand_prix_name import get_grand_prix_name_from_command_line_arguments
from process_command_line_arguments import CommandLineArguments
import sys
import load_config
import console_output_redirector
import text_file_writer

def generate_best(grand_prix_name, current_year):
    print("\nQualifying\n==========")
    calculate_best_qualifying(grand_prix_name, current_year)
    print("\nRace\n====")
    calculate_best_race(grand_prix_name, current_year)
    print("\nProgression\n===========")
    calculate_best_progression(grand_prix_name, current_year)
    if current_year == 2017:
        print("\nJoker\n=====")
        calculate_best_joker(grand_prix_name, current_year)


def calculate_output(output_file_name, grand_prix_name, current_year):
    file_handler = None
    original_output = None

    if output_filename != None:
        file_handler = text_file_writer.open_file(output_file_name)
        original_output = console_output_redirector.set_output_to_file(file_handler)

    calculate_best(grand_prix_name, config.current_year)

    if file_handler != None:
        text_file_writer.close_file(file_handler)
        console_output_redirector.set_output_to_console(original_output)
        print(output_filename + " created")


def read_additional_command_line_argument():
    args = CommandLineArguments()
    if len(args)>1:
        return args[1]
    return None

if __name__== "__main__":
    grand_prix_name = get_grand_prix_name_from_command_line_arguments(default = "Australian")
    config = load_config.read_config()
    output_file_name = read_additional_command_line_argument()
    calculate_output(output_file_name, grand_prix_name, config.current_year)
