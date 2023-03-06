from get_grand_prix_name import get_grand_prix_name_from_command_line_arguments
import load_config
import get_grand_prix_names

def format_number_descriptor(number):
    if number == 1:
        return "st"
    if number == 2:
        return "nd"
    if number == 3:
        return "rd"
    if number > 3:
        return "th"
    return "Unknown"

def calculate_number_of_races_remaining(race_name):
    config = load_config.read_config()
    grand_prix_names = get_grand_prix_names.get_all_grand_prix_for_season(config.current_year)
    counter = 0
    print_remaining_grand_prix = False
    remaining_races = ""
    for grand_prix_name in grand_prix_names:
        counter += 1
        if grand_prix_name == race_name:
            print("The " + race_name + " Grand Prix is the " + str(counter) + format_number_descriptor(counter) + " race of the season.")
            print("In " + str(config.current_year) + " there are " + str(len(grand_prix_names)) + " races.")
            print("There are " + str(len(grand_prix_names) - counter) + " races remaining.")
            print_remaining_grand_prix = True
            if len(grand_prix_names) == counter:
                print_remaining_grand_prix = False

        if print_remaining_grand_prix == True:
            if grand_prix_name != race_name:
                remaining_races += grand_prix_name
                if counter < len(grand_prix_names):
                    remaining_races += ", "
    if print_remaining_grand_prix == True:
        if ',' in remaining_races: 
            print("The remaining races are: " + remaining_races)
        else:
            print("The remaining race is: " + remaining_races)


if __name__ == "__main__":
    input_grand_prix_name = get_grand_prix_name_from_command_line_arguments(default = "All")
    if input_grand_prix_name != "All":
        calculate_number_of_races_remaining(input_grand_prix_name)
