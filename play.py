from domain.character import Character
from domain.classes import Warrior, Mage, Cleric

if __name__ == "__main__":
    hero = Character("Aria", 100, 15)
    hero.take_damage(50)
    print(hero.health)

    warrior = Warrior("Bram")
    mage = Mage("Sylla")
    cleric = Cleric("Eldrin")


    warrior.describe()
    mage.describe()
    cleric.describe()

    warrior.attack(mage)
    mage.special_ability(warrior)
    cleric.healing_touch(mage)

    warrior.describe()
    mage.describe()
    cleric.describe()
