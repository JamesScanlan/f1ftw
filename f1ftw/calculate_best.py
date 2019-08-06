from calculate_best_qualifying import CalculateBestQualifying
from calculate_best_race import CalculateBestRace
from calculate_best_progression import CalculateBestProgression
from calculate_best_joker import CalculateBestJoker
from get_grand_prix_name import GetGrandPrixNameFromCommandLineArguments
from process_command_line_arguments import CommandLineArguments
import sys
import load_config

def CalculateBest(grand_prix_name, current_year):
    print("\nQualifying\n==========")
    CalculateBestQualifying(grand_prix_name, current_year)
    print("\nRace\n====")
    CalculateBestRace(grand_prix_name, current_year)
    print("\nProgression\n===========")
    CalculateBestProgression(grand_prix_name, current_year)
    if current_year == 2017:
        print("\nJoker\n=====")
        CalculateBestJoker(grand_prix_name, current_year)

def ReadAdditionalCommandLineArgument():
    args = CommandLineArguments()
    if len(args)>1:
        return args[1]
    return None

def OpenFile(filename):
    f=open(filename, "w")
    return f

def RedirectConsoleOuputToFile(file_handle):
    original_output = sys.stdout
    sys.stdout = file_handle
    return original_output

def CloseFile(file_handle, original_output):
    file_handle.close()
    sys.stdout = original_output

if __name__== "__main__":
    grand_prix_name = GetGrandPrixNameFromCommandLineArguments(default="Australian")
    config = load_config.ReadConfig()
    output_filename = ReadAdditionalCommandLineArgument()
    file_handle = None
    original_output = None
    if output_filename != None:
        file_handle = OpenFile(output_filename)
        original_output = RedirectConsoleOuputToFile(file_handle)

    CalculateBest(grand_prix_name, config.current_year)

    if file_handle != None:
        CloseFile(file_handle, original_output)
        print(output_filename + " created")
