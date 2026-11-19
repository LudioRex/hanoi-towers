import os
import time
from hanoi_towers.stack import Stack
from hanoi_towers.bcolors import bcolors

clear = lambda: os.system('clear')


class HanoiTowers:
    """
    Hanoi Towers object that can run its own interaction menu or display
    a solution to itself.

        Attributes:
            Degree: int
                Number of blocks in the tower.
            
            MinMoves: int
                Minimum number of moves needed to solve the puzzle.
            
            CurrentMove: int
                Integer representing the number of moves made.
            
            Colors: list[str]
                List of ANSI escape sequences representing the colors
                of the blocks in the towers. White should not be a part
                of the colors.

            Collums: list[Stack]
                List of three stacks that each represent an individual
                collumns of the Hanoi Towers.
        
        Methods:
            run():
                Displays the towers and the user to solve the puzzle through input.

            solve_self(move_delay: float = 1):
                Displays the optimal solution to the towers with a certain delay
                between each move.
    """


    def __init__(self, degree: int, colors: list[str]=[bcolors.CYAN, bcolors.BLUE]) -> None:
        self.Degree: int = degree
        self.MinMoves: int = 2**degree - 1
        self.CurrentMove: int = 0
        self.Colors: list[str] = colors
        self.Colors.reverse()
        collumn1 = Stack([i for i in range(1, degree  + 1)])
        collumn2 = Stack([])
        collumn3 = Stack([])
        self.collumns: list[Stack] = [collumn1, collumn2, collumn3]
        

#---------------------------Display Logic--------------------------------


    def __display_upper_padding(self):
        """Displays two rows with empty collumns."""

        for i in range(2):
            print(' '*(self.Degree + 3), end='')
            print('\u2588', end='')
            print(' '*(self.Degree*2 + 3), end='')
            print('\u2588', end='')
            print(' '*(self.Degree*2 + 3), end='')
            print('\u2588')


    def __display_block(self, block_size: int):
        """
        Displays a single block with appropriate padding on either side.

            Arguments:
                block_size: int: The size of the block to be displayed.
        """
        if block_size == 0:
            color = bcolors.WHITE
        else:
            color = self.Colors[block_size % len(self.Colors)]

        print(' '*(self.Degree - block_size), end='')
        print(color + '\u2588'*(block_size*2 + 1) + bcolors.WHITE, end='')
        print(' '*(self.Degree - block_size), end='')


    def __display_row(self, row_num: int):
        """
        Displays a full row of the hanoi towers with its blocks or collumns.

            Arguments:
                row_num: int: The number of the row to be displayed.
        """

        row_bot = self.Degree - row_num        # Number of rows from the bottom.

        # Collumn 1.
        print(' '*3, end='')
        if row_bot <= self.collumns[0].count():
            self.__display_block(self.collumns[0][self.collumns[0].count() - row_bot])
        else:
            self.__display_block(0)
        print(' '*3, end='')

        # Collumn 2.
        if row_bot <= self.collumns[1].count():
            self.__display_block(self.collumns[1][self.collumns[1].count() - row_bot])
        else:
            self.__display_block(0)
        print(' '*3, end='')

        # Collumn 3.
        if row_bot <= self.collumns[2].count():
            self.__display_block(self.collumns[2][self.collumns[2].count() - row_bot])
        else:
            self.__display_block(0)
        print()


    def __display_towers(self):
        """Displays the whole towers."""

        print(f'{self.CurrentMove}/{self.MinMoves}')
        print()
        self.__display_upper_padding()
        for i in range(self.Degree):
            self.__display_row(i)


# ------------------------------Gameplay Logic------------------------------------


    def __is_legal_move(self, move_index: tuple[int]) -> bool:

        # Checking if the length is correct.
        if len(move_index) > 2:
            return False
        
        # Checking if all characters are valid.
        for i in range(2):
            if move_index[i] < 1 or move_index[i] > 3:
                return False
    
        moving_col: int = move_index[0] - 1
        target_col: int = move_index[1] - 1
    
        # Getting size of the involved blocks.
        moving_block = self.collumns[moving_col].peek()
        target_block = self.collumns[target_col].peek()

        # Checking if the sizes are appropriate.
        if target_block == 0:
            return True
        if moving_block > target_block:
            return False
        if moving_block == 0:
            return False
        return True


    def __move(self, move_index: tuple):

            if self.__is_legal_move(move_index):        # Check if the move is legal

                # Determine indices of collumns.
                moving_collumn: int = move_index[0] - 1
                target_collumn: int = move_index[1] - 1

                # Move the block.
                moving_block = self.collumns[moving_collumn].pop()
                self.collumns[target_collumn].push(moving_block)


                self.CurrentMove += 1       # Increase move counter
            else:
                print("That's an illegal move.")
                time.sleep(1)


    def __is_solved(self) -> bool:
        """Checks if this instance of the towers is solved."""

        solution = Stack([i for i in range(1, self.Degree  + 1)])
        if self.collumns[2] == solution:
            return True
        return False


    def run(self):
        """Run the puzzle for a human user."""

        while not self.__is_solved():       # Check if the towers are solved.   
            clear()
            self.__display_towers()
            movement: str = input()
            movement_index = (int(movement[0]), int(movement[1]))
            self.__move(movement_index)


        # Display last move.
        clear()
        self.__display_towers()
        time.sleep(1)


        # Display win screen.
        clear()
        print('Congrats! You won!')
        print(f'You completed the puzzle in {self.CurrentMove-self.MinMoves} moves above minimum.')


    def __solve__hanoi(self, degree: int, initial_collumn: int, target_collumn: int) -> list[tuple]:
        """
        Find the solution to any given Hanoi Towers puzzle.

            Arguments:

                degree: int
                    The number of blocks on the tower.
                
                initial_collumn: int
                    Integer representing the collumn in which the blocks are.

                target_collumn: int
                    Integer representing the collumn to which the blocks should move.
        """
        solution = []

        # Finding the open collumn.
        opencollumn: int = 0
        for i in range(1, 4):
            if i != initial_collumn and i != target_collumn:
                opencollumn = i
                break

        # Handling degree 1.
        if degree == 1:
            return [(initial_collumn, target_collumn)]
        
        # Handling higher degrees.
        else:
            solution += self.__solve__hanoi(degree - 1, initial_collumn, opencollumn)
            solution += [(initial_collumn, target_collumn)]
            solution += self.__solve__hanoi(degree - 1, opencollumn, target_collumn)
            return solution
        

    
    def solve_self(self, move_delay: int=1):
        """Display the solution to the towers with delay between each move."""
        solve = self.__solve__hanoi(self.Degree, 1, 3)      # Find solution.

        # Display the solution
        for move in solve:
            clear()
            self.__display_towers()
            self.__move(move)
            time.sleep(move_delay)

        # Show last move.
        clear()
        self.__display_towers()
        time.sleep(2)

        # Display final screen.
        clear()
        print(f'Towers were solved in {self.MinMoves} moves.')
