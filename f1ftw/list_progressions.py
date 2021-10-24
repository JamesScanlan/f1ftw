import get_grand_prix_names
import load_config
import datetime
import calculate_best_progression

if __name__== "__main__":
    config = load_config.read_config()
    active_year = config.current_year
    grand_prix_names = get_grand_prix_names.get_grand_prix_names(datetime.date.today(), active_year)

    for grand_prix_name in grand_prix_names:
        print("\n\n" + grand_prix_name)
        calculate_best_progression.calculate_best_progression(grand_prix_name, active_year)