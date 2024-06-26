from weapon import fists  # nie importuje klasy ale sam bron
from health_bar import HealthBar


class Character:

    race = "Human"  # class-lavel variables, for all instanses

    def __init__(
        self, name: str, health: int
    ) -> None:  # magic method, uruchamiana zawsze gdy jest nowy object
        self.name = name  # object level variable
        self.health = health
        self.health_max = health

        self.weapon = fists  # deafoult wepon

    def attact(self, target) -> None:
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)
        target.health_bar.update()


class Hero(Character):  # dzidziczy po Charakterze, wszystko dziedziczy

    def __init__(self, name: str, health: int) -> None:
        super().__init__(name=name, health=health)  # dziedziczone
        self.default_weapon = self.weapon
        self.health_bar = HealthBar(self, color="green")

    def equip(self, weapon) -> None:
        self.wepon = weapon
        print(f"{self.wepon} equipped a(n) {self.weapon.name}")

    def drop(self) -> None:
        print(f"{self.name} dropped a(n) {self.weapon.name}")
        self.weapon = self.defailt_weapon


class Enemy(Character):  # dzidziczy po Charakterze, wszystko dziedziczy

    def __init__(self, name: str, health: int, weapon) -> None:
        super().__init__(name=name, health=health)
        self.wepon = weapon
        self.health_bar = HealthBar(self, color="red")
