from get_grand_prix_name import GetGrandPrixNameFromCommandLineArguments
import load_config
import get_grand_prix_names

def FormatNumberDescriptor(number):
    if number == 1:
        return "st"
    if number == 2:
        return "nd"
    if number == 3:
        return "rd"
    if number > 3:
        return "th"
    return "Unknown"

def CalculateNumberOfRacesRemaining(race_name):
    config = load_config.ReadConfig()
    grand_prix_names = get_grand_prix_names.GetGrandPrixNames()
    counter = 0
    print_remaining_grand_prix = False
    remaining_races = ""
    for grand_prix_name in grand_prix_names:
        counter += 1
        if grand_prix_name == race_name:
            print("The " + race_name + " Grand Prix is the " + str(counter) + FormatNumberDescriptor(counter) + " race of the season.")
            print("In " + str(config.current_year) + " there are " + str(len(grand_prix_names)) + " races.")
            print("There are " + str(len(grand_prix_names) - counter) + " races remaining.")
            print_remaining_grand_prix = True
        if print_remaining_grand_prix == True:
            if grand_prix_name != race_name:
                remaining_races += grand_prix_name
                if counter < len(grand_prix_names):
                    remaining_races += ", "
    if print_remaining_grand_prix == True:
        print("The remaining races are: " + remaining_races)


if __name__ == "__main__":
    input_grand_prix_name = GetGrandPrixNameFromCommandLineArguments(default="All")
    if input_grand_prix_name != "All":
        CalculateNumberOfRacesRemaining(input_grand_prix_name)
