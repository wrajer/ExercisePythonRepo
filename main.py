from character import Hero, Enemy
from weapon import short_bow


hero = Hero("antos", 100)
enemy = Enemy("Egon", 90, short_bow)

while hero.health > 0 and enemy.health > 0:
    hero.attact(enemy)
    enemy.attact(hero)

    hero.health_bar.draw()
    enemy.health_bar.draw()
    # print(f"Health of {hero.name}: {hero.health}")
    # print(f"Health of {enemy.name}: {enemy.health}")

    input()

print(f"End Game - winner below")
hero.health_bar.draw()
enemy.health_bar.draw()
