#python3 summarise_race.py Hungarian ~/Documents/Code/Python/f1ftw/hungarian_summary.txt

import calculate_race_scores
import calculate_race_wins
import calculate_best
import calculate_running_totals
from get_grand_prix_name import get_grand_prix_name_from_command_line_arguments
from process_command_line_arguments import CommandLineArguments
import sys
import load_config
import titler
import calculate_number_of_races_remaining_in_season

def get_file_name_from_command_line_argument():
    args = CommandLineArguments()
    if len(args)>1:
        return args[1]
    else:
        return None

def open_file(filename):
    f = open(filename, "w")
    return f

def set_output_to_file(file_handler):
    original_output = sys.stdout
    sys.stdout = file_handler
    return original_output

def set_output_to_console(original_output):
    sys.stdout = original_output

def close_file(f):
    f.close()

def calc_scores(grand_prix_name, current_year):
    if calculate_race_scores.validate_conditions(grand_prix_name, current_year):
        calculate_race_scores.process_race_scores(grand_prix_name, current_year)

def calc_race_wins(current_year):
    calculate_race_wins.calculate_race_wins(current_year)
    wins = calculate_race_wins.calculate_total_race_wins(config.current_year)
    calculate_race_wins.display_race_win_totals(wins)

if __name__== "__main__":
    grand_prix_name = get_grand_prix_name_from_command_line_arguments(default = "Australian")
    output_filename = get_file_name_from_command_line_argument()
    config = load_config.read_config()

    file_handler = open_file(output_filename)

    original_output = set_output_to_file(file_handler)
    titler.Title("Scores for " + grand_prix_name + " Grand Prix")
    calc_scores(grand_prix_name, config.current_year)
    print("\n\n")
    titler.Title("Running Totals")
    calc_race_wins(config.current_year)

    print("\n\n")
    titler.Title("Best Scores for Race")
    calculate_best.calculate_best(grand_prix_name, config.current_year)

    print("\n\n")
    titler.Title("Running Totals")
    calculate_running_totals.calculate_running_totals(config.current_year, False)

    print("\n\n")
    titler.Title("Remaining Races")
    calculate_number_of_races_remaining_in_season.calculate_number_of_races_remaining(grand_prix_name)

    close_file(file_handler)

    set_output_to_console(original_output)

    print(output_filename + " created")
