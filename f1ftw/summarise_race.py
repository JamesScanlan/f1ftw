import calculate_race_scores
from get_grand_prix_name import GetGrandPrixNameFromCommandLineArguments
from process_command_line_arguments import CommandLineArguments
import sys
import load_config

grand_prix_name = GetGrandPrixNameFromCommandLineArguments(default="Australian")
args=CommandLineArguments()
output_to_file = False
if len(args)>1:
    f=open(args[1], "w")
    original_output = sys.stdout
    sys.stdout = f
    output_to_file = True

config = load_config.ReadConfig()

if calculate_race_scores.ValidateConditions(grand_prix_name, config.current_year):
    calculate_race_scores.ProcessRaceScores(grand_prix_name, config.current_year)

if output_to_file:
    f.close()
    sys.stdout = original_output
    print(args[1] + " created")
