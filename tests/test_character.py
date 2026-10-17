from domain.character import Character


def test_healing_cannot_exceed_max_health():
    hero = Character("Aria", 100, 15)

    hero.take_damage(50)  # HP becomes 50
    hero.heal(1000)  # Attempt to heal far beyond max HP

    assert hero.health == 100
