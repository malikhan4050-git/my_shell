import sys
import prompt
import shutil

def main():
    while True:
        command = prompt.get_user_input()
        command = command.strip()
        
        if command == "":
            continue
        
        if command == "exit":
            print("Goodbye!")
            sys.exit(0)
        elif command.startswith("show "):
            msg = command[5:]
            print(msg)
        elif command.startswith("type "):
            cmd = command[5:].strip()
            builtinTypes = ["exit", "type", "show"]

            if cmd in builtinTypes:
                print(f"{cmd} is a shell builtin.")
            else:
                path = shutil.which(cmd)
                if path:
                    print(f"{cmd} is a {path}")
                else:
                    print(f"{cmd} is not found, sorry!")
        else:
            print(f"{command}: command not found")

if __name__ == "__main__":
    main()