from domain.character import Character

if __name__ == "__main__":
    hero = Character("Aria", 100, 15)
    hero.take_damage(50)
    print(hero.health)
