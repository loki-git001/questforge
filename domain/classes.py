from domain.character import Character


class Warrior(Character):
    def __init__(self, name: str) -> None:
        super().__init__(name, health=120, attack_power=18)

    def special_ability(self, target: Character) -> None:
        bonus = int(self.attack_power * 1.5)
        target.take_damage(bonus)
        print(f"{self.name} uses Cleave! {bonus} damage to {target.name}")


class Mage(Character):
    def __init__(self, name: str) -> None:
        super().__init__(name, health=80, attack_power=10)
        self.mana = 50

    def special_ability(self, target: Character) -> None:
        cost = 20
        if self.mana < cost:
            print(f"{self.name} doesn't have enough mana!")
            return
        self.mana -= cost
        damage = int(self.attack_power * 3)
        target.take_damage(damage)
        print(f"{self.name} casts Fireball! {damage} damage to {target.name}")


class Rogue(Character):
    def __init__(self, name: str) -> None:
        super().__init__(name, health=90, attack_power=14)

    def special_ability(self, target: Character) -> None:
        crit = self.attack_power * 2
        target.take_damage(crit)
        print(f"{self.name} lands a Backstab! {crit} critical damage to {target.name}")


class Cleric(Character):
    def __init__(self, name: str) -> None:
        super().__init__(name, health=100, attack_power=16)

    def healing_touch(self, target: Character) -> None:
        cost = 3
        if self.health < cost:
            print(f"not enough health to heal others")
            return
        self.take_damage(cost)
        heal_amount = cost * 2
        target.heal(heal_amount)
        print(
            f"{self.name} sacrifices {cost} HP to heal {target.name} for {heal_amount} HP!"
        )
