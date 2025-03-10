import load_config
from load_grands_prix_meta_data import read_grands_prix_meta_data
import text_padding
import text_file_writer
from process_command_line_arguments import CommandLineArgumentsProcessor
import console_output_redirector

def display_races(current_year):
    races = sorted(read_grands_prix_meta_data(current_year), key = lambda Race: Race.start_date)
    for race in races:
        print(text_padding.pad_right(race.name,25)+ "(" + str(race.start_date) + " to " + str(race.end_date) + ")")

if __name__== "__main__":
    output_file_name = CommandLineArgumentsProcessor().get_argument(0)
    config = load_config.read_config()

    if output_file_name != None:
        file_handler = text_file_writer.open_file(output_file_name)
        original_output = console_output_redirector.set_output_to_file(file_handler)

    display_races(config.current_year)

    if output_file_name != None:
        text_file_writer.close_file(file_handler)
        console_output_redirector.set_output_to_console(original_output)
        print(output_file_name + ' created.')