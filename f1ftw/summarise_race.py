#python3 summarise_race.py Hungarian ~/Documents/Code/Python/f1ftw/hungarian_summary.txt

import calculate_race_scores
import calculate_race_wins
import calculate_best
import calculate_running_totals
from get_grand_prix_name import GetGrandPrixNameFromCommandLineArguments
from process_command_line_arguments import CommandLineArguments
import sys
import load_config
import titler

def GetFileNameFromCommandLineArgument():
    args=CommandLineArguments()
    if len(args)>1:
        return args[1]
    else:
        return None

def OpenFile(filename):
    f = open(filename, "w")
    return f

def SetOutputToFile(file_handler):
    original_output = sys.stdout
    sys.stdout = file_handler
    return original_output

def SetOutputToConsole(original_output):
    sys.stdout = original_output

def CloseFile(f):
    f.close()

def CalcScores(grand_prix_name, current_year):
    if calculate_race_scores.ValidateConditions(grand_prix_name, current_year):
        calculate_race_scores.ProcessRaceScores(grand_prix_name, current_year)

def CalcRaceWins(current_year):
    calculate_race_wins.CalculateRaceWins(current_year)
    wins = calculate_race_wins.CalculateTotalRaceWins(config.current_year)
    calculate_race_wins.DisplayRaceWinTotals(wins)

if __name__== "__main__":
    grand_prix_name = GetGrandPrixNameFromCommandLineArguments(default="Australian")
    output_filename = GetFileNameFromCommandLineArgument()
    config = load_config.ReadConfig()

    file_handler = OpenFile(output_filename)

    original_output = SetOutputToFile(file_handler)
    titler.Title("Scores for " + grand_prix_name + " Grand Prix")
    CalcScores(grand_prix_name, config.current_year)
    print("\n\n")
    titler.Title("Running Totals")
    CalcRaceWins(config.current_year)

    print("\n\n")
    titler.Title("Best Scores for Race")
    calculate_best.CalculateBest(grand_prix_name, config.current_year)

    print("\n\n")
    titler.Title("Running Totals")
    calculate_running_totals.CalculateRunningTotals(config.current_year, False)

    CloseFile(file_handler)

    SetOutputToConsole(original_output)

    print(output_filename + " created")
