from process_command_line_arguments import CommandLineArguments

def get_grand_prix_name_from_command_line_arguments(default):
    args = CommandLineArguments()
    if len(args)>0:
        return args[0]
    else:
        return default
