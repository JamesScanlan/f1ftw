import load_race_results
from get_grand_prix_name import get_grand_prix_name_from_command_line_arguments
import get_grand_prix_names
import load_config

def do_calculation(grand_prix_name, active_year):
    print(grand_prix_name)
    results = load_race_results.read_race_results(grand_prix_name, active_year)
    load_race_results.validate_race_results(results)


if __name__ == "__main__":
    config = load_config.read_config()

    grand_prix_name = get_grand_prix_name_from_command_line_arguments(default = "All")
    if grand_prix_name != "All":
        do_calculation(grand_prix_name, config.current_year)
    else:
        grand_prix_names = get_grand_prix_names.get_grand_prix_names()
        for grand_prix_name in grand_prix_names:
            DoCalculation(grand_prix_name,config.current_year)
