from calculate_best_qualifying import CalculateBestQualifying
from calculate_best_race import CalculateBestRace
from calculate_best_progression import CalculateBestProgression
from calculate_best_joker import CalculateBestJoker
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


print("\nQualifying\n==========")
CalculateBestQualifying(grand_prix_name, config.current_year)
print("\nRace\n====")
CalculateBestRace(grand_prix_name, config.current_year)
print("\nProgression\n===========")
CalculateBestProgression(grand_prix_name, config.current_year)
if config.current_year == 2017:
    print("\nJoker\n=====")
    CalculateBestJoker(grand_prix_name, config.current_year)

if output_to_file:
    f.close()
    sys.stdout = original_output
    print(args[1] + " created")
