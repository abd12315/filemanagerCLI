import os
from datetime import datetime

class user_in:
    def __init__(self, dtyp="", date="", strtup="", sys_date=""):
        self.dtyp = dtyp
        self.date = date
        self.strtup = strtup
        self.sys_date = sys_date
        self.valid_commands = ["list", "cd", "md", "rd", "help", "play", "pass"]

    def prestartup(self):
        os.system("cls" if os.name == "nt" else "clear")  # Clear screen for Windows/Linux
        os.system("date")  # Simulate DOS-like prompt

    def cln(self):
        if self.dtyp == "list":
            for item in os.listdir():
                self.date = datetime.now()
                print(f"{item}\t{self.date}")
        elif self.dtyp == "help":
            Help(dtyp="help").help()
        elif self.dtyp.startswith("play "):
            filename = self.dtyp.split(" ", 1)[1]
            if os.path.exists(filename):
                Play_Audio(filename).play()
            else:
                print("File not found.")
        elif self.dtyp.startswith("cd "):
            target = self.dtyp.split(" ", 1)[1]
            try:
                os.chdir(target)
            except FileNotFoundError:
                print("Directory not found.")
        elif self.dtyp.startswith("pass"):
            if len(self.dtyp.split(" ", 1)) < 2:
                print("No target specified for pass command.")
                return
            target = self.dtyp.split(" ", 1)[1]
            try:
                with open("SecretFile.txt") as password_file:
                    secretPassword = password_file.read().strip()
                print('Enter your password.')
                typedPassword = input()
                if typedPassword == secretPassword:
                    print("Access granted")
                else:
                    print("Access Denied")
            except FileNotFoundError:
                print("SecretFile.txt not found.")
        elif self.dtyp in self.valid_commands:
            print(f"Command '{self.dtyp}' recognized, but not implemented yet.")
        else:
            print("Invalid command. Please try again or type 'help'.")

    def retry(self):
        base_path = os.path.abspath(os.path.dirname(__file__))  # Location of this script
        while True:
            current_path = os.getcwd()
            prompt_label = "sys" if current_path == base_path else os.path.basename(current_path)

            self.dtyp = input(f"{prompt_label} >> ").strip()
            if self.dtyp.lower() == "exit":
                print("Exiting PROGMAN...")
                break
            self.cln()

class Help(user_in):
    def __init__(self, dtyp="", date="", strtup="", sys_date=""):
        super().__init__(dtyp, date, strtup, sys_date)
        self.uinhlp = ""

    def help(self):
        help_file = {
            "list": "Enlist files available in current working directory",
            "cd": "Change the directory whether inside or outside of the directory",
            "md": "Make a new folder or directory",
            "rd": "Remove the current file or directory",
            "play": "Play the audio file using ffplay that plays mp3 song within CLI",
            "pass": "pass through password via admin privileges or just a default user profile"
        }

        self.uinhlp = input("You've reached the Help Section. Type any command for detailed info: ")
        found = False
        for key, value in help_file.items():
            if self.uinhlp in key or self.uinhlp in value:
                print(f"{key} - {value}")
                found = True
        if not found:
            print("No match found.")

class Play_Audio(user_in):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def play(self):
        print(f"Playing: {self.filename}")
        os.system(f'ffplay -nodisp -autoexit "{self.filename}"')

# Main execution
uin = user_in()
uin.prestartup()
uin.retry()
