import get_grand_prix_names
import calculate_best_qualifying
import load_config


def calculate_best_season(active_year):
    qualifying = {}
    for grand_prix in get_grand_prix_names.get_all_grand_prix_for_season(active_year):
        print(grand_prix)
        results = calculate_best_qualifying.generate_results(grand_prix, active_year)
        for result in results:
            if result.driver not in qualifying:
                qualifying[result.driver.person_name.full_name()] = 1
            else:
                qualifying[result.driver.person_name.full_name()] += 1
            break

    #{k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
    qualifying = sorted(qualifying.items(), key=lambda item: item[1])
    print(qualifying)

if __name__ == "__main__":
    config = load_config.read_config()
    calculate_best_season(config.current_year)