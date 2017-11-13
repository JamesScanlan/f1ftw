from calculate_best_qualifying import CalculateBestQualifying
from calculate_best_race import CalculateBestRace
from calculate_best_progression import CalculateBestProgression
from calculate_best_joker import CalculateBestJoker
from get_grand_prix_name import GetGrandPrixNameFromCommandLineArguments
from process_command_line_arguments import CommandLineArguments
import sys

grand_prix_name = GetGrandPrixNameFromCommandLineArguments(default="Australian")
args=CommandLineArguments()
output_to_file = False
if len(args)>1:
    f=open(args[1], "w")
    original_output = sys.stdout
    sys.stdout = f
    output_to_file = True

print("\nQualifying\n==========")
CalculateBestQualifying(grand_prix_name)
print("\nRace\n====")
CalculateBestRace(grand_prix_name)
print("\nProgression\n===========")
CalculateBestProgression(grand_prix_name)
print("\nJoker\n=====")
CalculateBestJoker(grand_prix_name)

if output_to_file:
    f.close()
    sys.stdout = original_output
    print(args[1] + " created")
