from process_command_line_arguments import CommandLineArguments

def GetGrandPrixNameFromCommandLineArguments(default):
    args=CommandLineArguments()
    if len(args)>0:
        return args[0]
    else:
        return default
