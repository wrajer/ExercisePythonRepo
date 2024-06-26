class Weapon:
    def __init__(self, name: str, type: str, damage: int, value: int) -> None:
        self.name = name
        self.type = type
        self.damage = damage
        self.value = value


iron_sword = Weapon("Iron sword", "sharp", 10, 100)
short_bow = Weapon("Short bow", "ranged", 7, 100)
fists = Weapon("Fists", "blunt", 2, 50)
