from domain.character import Character

def run_special_round(attacker: Character, defender: Character):
    """Works for ANY Character subclass — this is polymorphism in action."""
    attacker.special_ability(defender)


def total_party_damage(party: list[Character], target: Character):
    for attacker in party:
        attacker.attack(target)
        print(f"{target.name} HP: {target.health}")
        