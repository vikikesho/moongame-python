class Card:
    def __init__(self, value) -> None:
        self.value = value
        pass

    def __str__(self) -> str:
        return str(self.value)