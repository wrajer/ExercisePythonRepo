import os

os.system("")  # if console not show colors


class HealthBar:

    symbol_remaining: str = "▮"
    symbol_lost: str = "_"
    barrier: str = "|"

    colors = dict = {
        "red": "\033[91m",
        "purple": "\033[91m",
        "green": "\033[92m",
        "default": "\033[0m",
    }

    def __init__(
        self, entity, length: int = 20, is_colored: bool = True, color: str = "Default"
    ) -> None:  # jesli ma __to jest to metoda prywatna
        self.entity = entity
        self.length = length

        self.max_value = entity.health_max
        self.current_value = entity.health

        self.is_colored = is_colored
        self.color = (
            self.colors.get(color) or self.colors["default"]
        )  # to jest w sumie jak definicja set/get, do psrawdzenia ktore wywołanie jest lepsze pierwsz czy drugie

    def test():
        return "test return"

    def update(self) -> None:
        self.current_value = self.entity.health

    def draw(self) -> None:
        remaining_bars = round(self.current_value / self.max_value * self.length)
        lost_bars = self.length - remaining_bars
        print(
            f"{self.entity.name}'s HEALTH:{self.entity.health}' / '{self.entity.health_max}"
        )
        print(f"{self.color if self.is_colored else ''}")
        print(
            f"{self.barrier}{self.symbol_remaining*remaining_bars}{self.symbol_lost*lost_bars}{self.barrier}"
        )
        print(f"{self.colors['default']}")
