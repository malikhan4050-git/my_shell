import shlex

def parse_command(command):

    #Parse a command string into arguments.
    #Handle quotes and escaped characters.

    try :
        return shlex.split(command)
    except ValueError as e:
        print(f"Error parsing the command: {e}")
        return[]