from hanoi_towers.hanoiTowers import HanoiTowers
from hanoi_towers.hanoiTowers import clear
from hanoi_towers.bcolors import bcolors
from hanoi_towers.menu import Menu
import time


class GameControl:
    """
    Controls the  Hanoi Towers game.

        Attributes:
            ColorScheme: list[str]
                List of strings representing the currently selected
                color scheme

            Custom_CS: list[str]
                List of strings representing the user's custom color
                scheme.

        Methods:
            run_main_menu():
                Displays the main menu and handles user input to call
                relevant methods.
    """
    DEFAULT_CS = [bcolors.CYAN, bcolors.BLUE]       # CS stands for Color Scheme.
    REVERSE_CS = [bcolors.BLUE, bcolors.CYAN]
    XMAS_CS = [bcolors.GREEN, bcolors.RED]
    DEFAULT_CS_LST = [DEFAULT_CS, REVERSE_CS, XMAS_CS]
    

    def __init__(self) -> None:
        self.ColorScheme = self.DEFAULT_CS
        self.Custom_CS = []

    def run_main_menu(self):
        """Displays the main menu and handles user input."""

        clear()

        # Run the menu.
        main_menu = Menu(['Play', 'Computer Solve', 'Block Colors', 'Help'])
        selected_option = main_menu.run()

        clear()

        # Handle user input.
        if selected_option in [0, 1]:       # Create towers object if necesary.
            block_num = ''

            while not block_num.isnumeric():
                block_num = input('How many blocks do you want?')

                if not block_num.isnumeric:
                    clear()
                    print('Please input a positive integer.')
                    time.sleep(2)

            block_num = int(block_num)

            if block_num > 20:
                print('High amounts of blocks may not display well.')

            towers = HanoiTowers(block_num, colors=self.ColorScheme)
        

        # Switch depending on input.
        if selected_option == 0:
            towers.run()
            time.sleep(2)
            self.run_main_menu()

        elif selected_option == 1:
            time_delay = input('Do you want to set time delay? (Y/N)').lower()

            if time_delay == 'y':
                delay = float(input('What should be the delay?'))
                towers.solve_self(delay)
                self.run_main_menu()

            else:
                towers.solve_self()
                self.run_main_menu()

        elif selected_option == 2:
            self.__run_color_menu()

        elif selected_option == 3:
            self.__run_help_screen()


    def __run_color_menu(self):
        """Allows the user to set the desired color theme."""

        # Run color scheme menu.
        menu1 = Menu(['Default', 'Reverse', 'Xmas', 'New Color Scheme'])
        selected_option = menu1.run()

        # Run color scheme creation menu.
        if selected_option == 3:
            self.Custom_CS = []
            clear()

            colors_str = ['Red', 'Green', 'Yellow', 'Blue', 'Purple', 'Cyan', 'Done']
            colors_lst = [f'\033[9{i + 1}m'for i in range(7)]


            menu2 = Menu([colors_lst[i] + colors_str[i] for i in range(7)])
            selected_option = 0

            while selected_option != 6:
                clear()
                selected_option = menu2.run()

                if selected_option != 6:        # Don't append color for "Done" option.
                    self.Custom_CS.append(colors_lst[selected_option])

            if self.Custom_CS == []:        # Handle blank input error.
                self.ColorScheme = self.DEFAULT_CS
            else:
                self.ColorScheme = self.Custom_CS

        else:
            self.ColorScheme = self.DEFAULT_CS_LST[selected_option]

        self.run_main_menu()



    def __run_help_screen(self):
        """Displays the help screen."""
        print(bcolors.BLUE + 'HELP:')
        print()
        print(bcolors.CYAN + 'What are Hanoi Towers?')
        print(bcolors.WHITE +
            '''
            Hanoi Towers are a puzzle game. The game consists of three collumns
            where you can place blocks. The game starts with a set number of blocks
            on the first collumn and the goal is to move them all to the last one.
            There is one catch though: you can't place blocks on top of smaller ones.
            '''
            )
        print()
        print(bcolors.CYAN + 'How hard is it?')
        print(bcolors.WHITE +
            '''
            The minimum number of moves needed to solve the puzzle grows exponetially
            with the number of blocks. So while solving a set of towers with 3 blocks
            requires 7 moves, solving a set with 10 block requires 1023 moves.
            '''
            )
        print()
        print(bcolors.CYAN + 'How do I play the game?')
        print(bcolors.WHITE +
            '''
            In the main menu, select the "Play" option. Once you select the number of
            blocks you want, the game starts. Move the blocks by entering the numbers
            of the collumns. Something like "13" would move the top block of collumn 1
            to collumn 3.
            '''
            )
        print()
        print(bcolors.CYAN + 'What is "Computer Solve"?')
        print(bcolors.WHITE +
            '''
            Solving big towers is pretty long. If you don't want to go through the hassle
            yourself, select "Computer Solve" and you'll get a nice animation of the
            optimal solution to the puzzle. By default, there is a 1 second delay between
            each move, but you can change it to whatever you like when prompted. This is
            important if you want to see a big set of towers be solved fast, or else you
            could have to wait minutes or even hours.
            '''
            )
        print()
        print(bcolors.CYAN + 'How do I change the block colors?')
        print(bcolors.WHITE +
            '''
            If you want to change the colors of the blocks, choose the "Block Colors" option
            in the main menu. You can choose from one of the preset color schemes or you can
            create your own. To create your own color scheme, select the "New Color Scheme"
            option. You'll be prompted to select colors, you can select however many you want,
            but if you pick more colors than the number of blocks you play with you will not
            see them displayed. The order in which you choose the colors is the order they will
            be displayed and if you choose less colors than blocks the color scheme will loop.
            You can only have one saved custom color scheme so be careful if you try to create a new one.
            '''
            )
        input()
        self.run_main_menu()
