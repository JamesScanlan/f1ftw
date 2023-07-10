import load_race_results
from get_grand_prix_name import get_grand_prix_name_from_command_line_arguments
import get_grand_prix_names
import load_config


if __name__ == "__main__":
    config = load_config.read_config()

    grand_prix_name = get_grand_prix_name_from_command_line_arguments(default = "All")
    
    if grand_prix_name != "All":
        results = load_race_results.read_race_results(grand_prix_name, config.current_year)

        positions = []
        for qualifying_result in results.qualifying_results:
            positions.append(qualifying_result.position)

        positions = sorted(positions)
        analysed_results = {}
        for position in positions:
            if position not in analysed_results:
                analysed_results[position] = 1
            else:
                analysed_results[position] += 1

        print(analysed_results)

        for analysed_result in analysed_results:
            if analysed_results[analysed_result] > 1:
                # print(analysed_result, analysed_results[analysed_result])
                for qualifying_result in results.qualifying_results:
                    if qualifying_result.position == analysed_result:
                        print(qualifying_result.driver.person_name)            
        # print(qualifying_result.driver.person_name, qualifying_result.position)
