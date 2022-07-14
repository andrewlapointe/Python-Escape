from game.display import Display

class Game:

    def __init__(self) -> None:
        self.name = None
        self.gamePosition = 0

    def events() -> None:
        pass

    def startGame(self) -> None:
        self.name = input("Who are you? \nMy name is...")
        Display.displayString(f"Hello {self.name}")
        