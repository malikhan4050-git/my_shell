import sys
import prompt
import shutil
import subprocess
import os

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
        
        elif command.startswith("kill "):
            process_name = command[5:].strip()
            try:
                os.system(f"taskkill /f /im {process_name}.exe")
                print(f"Closed all processes name {process_name}.exe")
            except Exception as e:
                print(f"Error killing the process {process_name} : {e}")
        
        elif command == "pwd":
            dir = os.getcwd()
            print(f"The current working directory is : {dir}")
        
        elif command.startswith("cd "):
            path = command[3:].strip()
            try:
                os.chdir(path)
            except FileNotFoundError:
                print(f"cd : {path} : no such file or directory")
            except NotADirectoryError:
                print(f"cd : {path} : Not a directory")
            except Exception as e:
                print(f"cd : {path} : {e}")
        
        else:
            path = shutil.which(command)
            if path:
                try:
                    subprocess.Popen(command, shell=True)
                except Exception as e:
                    print(f"Error executing the command: {e}")
            else:
                print(f"{command} not found, sorry!")

if __name__ == "__main__":
    main()