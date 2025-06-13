from enum import Enum
from random import choice

class Direction(Enum):
    UP    = 1
    DOWN  = 2
    LEFT  = 3
    RIGHT = 4


class Snake:
    def __init__(self, \
                 ScreenWidth: int = 10, \
                 ScreenHeight: int = 10, \
                 SnakeX: int = 0, \
                 SnakeY: int = 0, \
                 snakeMarker: str = "#", \
                 foodMarker: str = "*", \
                 spaceMarker: str = " ", \
                 strictMode: bool = False) -> None:
        """
        Initialize the Snake game.

        :param ScreenWidth: (int, optional) Width of the game screen. Defaults to 10.
        :param ScreenHeight: (int, optional) Height of the game screen. Defaults to 10.
        :param SnakeX: (int, optional) Initial X position of the snake's head. Defaults to 0.
        :param SnakeY: (int, optional) Initial Y position of the snake's head. Defaults to 0.
        :param snakeMarker: (str, optional) Character representing the snake. Defaults to "#".
        :param foodMarker: (str, optional) Character representing the food. Defaults to "*".
        :param spaceMarker: (str, optional) Character representing empty space. Defaults to " ".
        :param strictMode: (bool, optional) If True, raises an error when the snake overlaps itself. Defaults to False.
        """
        self.marker: list[str] = [snakeMarker, foodMarker, spaceMarker]
        self.screen: list[list[str]] = [[self.marker[2] for _ in range(ScreenWidth)] for _ in range(ScreenHeight)]
        self.screen[SnakeY][SnakeX] = self.marker[0]
        # snake header's X and Y always at the last element of the list 
        self.snake: list[tuple[int, int]] = [(SnakeX, SnakeY)]
        self.food: list[tuple[int, int]] = []
        self.length = 1
        self.strict = strictMode

    def __updateScreen(self) -> None:
        for y in range(len(self.screen)):
            for x in range(len(self.screen[y])): self.screen[y][x] = self.marker[2]
        
        for x, y in self.snake: self.screen[y][x] = self.marker[0]
        for x, y in self.food: self.screen[y][x] = self.marker[1]
    
    def __hasDuplicate(self, lst: list):
        return len(lst) != len(set(lst))
    
    def restart(self, SnakeX: int = 0, SnakeY: int = 0) -> None:
        """
        Restart the game.

        :param SnakeX: (int, optional) Initial X position of the snake's head. Defaults to 0.
        :param SnakeY: (int, optional) Initial Y position of the snake's head. Defaults to 0.
        """
        self.snake = [(SnakeX, SnakeY)]
        self.food = []
        self.__updateScreen()

    def generateFood(self, FoodX: int, FoodY: int) -> None:
        """
        Generate food at the given position.

        :param FoodX: Food's X position.
        :param FoodY: Food's Y position.
        """
        self.food.append((FoodX, FoodY))
        self.__updateScreen()

    def move(self, direction: Direction) -> bool:
        """
        Move the snake to the given direction.

        :param direction: (Direction(Enum), recommend) Move the snake.
        :return ateFood: (bool) Return True if the snake ate the food, else return False.
        """
        # get the snake's header's X position and Y position
        x, y = self.snake[-1]
        if   direction == Direction.UP:    y -= 1
        elif direction == Direction.DOWN:  y += 1
        elif direction == Direction.LEFT:  x -= 1
        elif direction == Direction.RIGHT: x += 1
        
        if x < 0 or x >= len(self.screen[0]) or y < 0 or y >= len(self.screen):
            raise IndexError('Snake moved out of bounds')
        
        if self.strict and self.__hasDuplicate(self.snake):
            raise IndexError('The position of Snake is repeated.')
        
        # if the snake ate the food, then the snake will grow
        ateFood = self.screen[y][x] == self.marker[1]

        if ateFood:
            self.snake.append((x, y))
            self.food.pop(self.food.index((x, y)))
            self.length += 1
        else:
            # remove the tail of the snake
            self.screen[self.snake[0][1]][self.snake[0][0]] = self.marker[2]
            self.snake.pop(0)
            self.snake.append((x, y))

        # update the snake's position
        self.__updateScreen()
        return ateFood

    def printScreen(self) -> None:
        """
        Print the game screen.
        """
        for row in self.screen:
            print(' '.join(row))

    @staticmethod
    def example() -> None:
        import os
        import time
        import keyboard
        from random import randint

        clearScreen = lambda: os.system('cls' if os.name == 'nt' else 'clear')

        snake = Snake(ScreenWidth=20, ScreenHeight=20, spaceMarker="-")
        snake.generateFood(5, 5)
       
        direction = Direction.RIGHT

        while True:
            clearScreen()
            snake.printScreen()
            time.sleep(0.15)

            direction =      Direction.UP    if keyboard.is_pressed('w') or keyboard.is_pressed('up')    \
                        else Direction.DOWN  if keyboard.is_pressed('s') or keyboard.is_pressed('down')  \
                        else Direction.LEFT  if keyboard.is_pressed('a') or keyboard.is_pressed('left')  \
                        else Direction.RIGHT if keyboard.is_pressed('d') or keyboard.is_pressed('right') \
                        else direction

            try:
                if snake.move(direction): snake.generateFood(randint(3, 16), randint(3, 16))
            except IndexError as e: 
                print(f"Game Over! Because {e}")
                break
        
        print(f"Your score: {snake.length - 1}")
        keyboard.press("Enter")
        input()
        if input("Try again? [Y/n]> ").lower() == "y":
            Snake.example()
