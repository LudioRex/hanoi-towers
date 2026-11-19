from typing import TypeVar, Generic

T = TypeVar("T")

class Stack(Generic[T]):
    """
    Represents a last in/fist out type of stack.

        Attributes:
            sl : list
                List containing all the items in the stack.
        
        Methods:
            peek():
                Returns the item at the top of the stack.

            push(item):
                Adds item at the top of the stack.

            pop():
                Returns and removes the item at the top of the stack.

            count():
                Returns the number of items in the stack.
    """

    def __init__(self, stack_lst: list[T]) -> None:
        stack_lst.reverse()
        self.sl: list[T] = stack_lst       # sl stands for stack list.

    def __str__(self) -> str:
        reversed_lst: list = [self.sl[i] for i in range(self.count() - 1, -1, -1)]
        return str(reversed_lst)
    
    def __getitem__(self, key: int):
        if self.sl == []:
            return 0
        reversed_lst: list = [self.sl[i] for i in range(self.count() - 1, -1, -1)]
        return reversed_lst[key]
    

    def __eq__(self, value) -> bool:
        return self.sl == value.sl
    

    def __ne__(self, value: object) -> bool:
        return self.sl != value.sl

    def peek(self) -> T:
        """Returns the item at the top of the stack."""
        if self.sl == []:
            return 0
        return self.sl[-1]
    
    def push(self, item) -> None:
        """Adds a new item to the top of the stack."""
        self.sl.append(item)

    def pop(self) -> T:
        """Returns and removes the item at the top of the stack."""
        return self.sl.pop()
    
    def count(self) -> int:
        """Returns the number of items in the stack."""
        return len(self.sl)