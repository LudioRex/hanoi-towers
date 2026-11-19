import time
import os
clear = lambda: os.system('clear')

class Menu:
    """
    Creates an interactive menu.

        Attributes:
            Options: list[str]
                List of the options that should be displayed in
                the menu.

        Methods:
            run() -> int:
                Displays the menu and loops until valid user
                input. Returns the index of the option selected
                by the user.
    """

    def __init__(self, options: list[str]) -> None:
        self.Options = options

    
    def run(self) -> int:
        correct_input = False
        selected_option = ''
        while(not correct_input):
            correct_input = True
            for i in range(len(self.Options)):
                print(f"{self.Options[i]} ({i + 1})")

            selected_option = input()

            if not selected_option.isnumeric():
                clear()
                print('Please input a correct option number.')
                time.sleep(2)
                correct_input = False
            elif int(selected_option) <= 0 or int(selected_option) > len(self.Options):
                clear()
                print('Please input a correct option number.')
                time.sleep(2)
                correct_input = False

        return int(selected_option) - 1
