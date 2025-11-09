from typing import Dict


class Faction:
    maximum_amount = 200
    Fruits = ("apples", "oranges", "bananas", "strawberries")

    def __init__(self, name: str, apples: int, oranges: int, bananas: int, strawberries: int) -> None:
        self.name = name
        self.fruits: Dict[str, int] = {
            "apples": apples,
            "oranges": oranges,
            "bananas": bananas,
            "strawberries": strawberries
        }

        for fruit, amount in self.fruits.items():
            if not isinstance(amount, int):
                raise TypeError(f"{fruit} amount must be an integer")
            if amount < 0 or amount > Faction.maximum_amount:
                raise ValueError(
                    f"{fruit} amount must be between 0 and {Faction.maximum_amount}")

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError(f"{name} must be a string")
        name = name.strip()
        if not name:
            raise ValueError("name can not be empty")
        self._name = name

    def __repr__(self):
        return (
            f"Faction name is {self.name}, "
            f"oranges amount = {self.fruits['oranges']}, "
            f"bananas amount = {self.fruits['bananas']}, "
            f"strawberries amount = {self.fruits['strawberries']}"
        )


war_kingdom = Faction("war_kingdom", 80, 40, 100, 200)
print(war_kingdom)

# validated the fruits
