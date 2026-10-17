import pytest

from domain.character import Character


def test_character_initialization():
    character = Character("Aria", 100, 15) 

    assert character.name == "Aria"
    assert character.health == 100
    assert character.attack_power == 15
    assert character.is_alive is True


def test_character_takes_damage():
    character = Character("Aria", 100, 15)

    character.take_damage(30)

    assert character.health == 70


def test_character_health_cannot_go_below_zero():
    character = Character("Aria", 100, 15)

    character.take_damage(150)

    assert character.health == 0
    assert character.is_alive is False


def test_negative_damage_raises_error():
    character = Character("Aria", 100, 15)

    with pytest.raises(ValueError, match="Damage can't be less than 0"):
        character.take_damage(-10)


def test_character_heals():
    character = Character("Aria", 100, 15)

    character.take_damage(40)
    character.heal(20)

    assert character.health == 80


def test_healing_cannot_exceed_max_health():
    character = Character("Aria", 100, 15)

    character.take_damage(10)
    character.heal(50)

    assert character.health == 100


def test_negative_healing_raises_error():
    character = Character("Aria", 100, 15)

    with pytest.raises(ValueError, match="Heal amount can't be less than 0"):
        character.heal(-5)


def test_character_attack():
    attacker = Character("Aria", 100, 15)
    target = Character("Goblin", 50, 5)

    attacker.attack(target)

    assert target.health == 35


def test_dead_character_cannot_attack(capsys):
    attacker = Character("Aria", 100, 15)
    target = Character("Goblin", 50, 5)

    attacker.take_damage(100)
    attacker.attack(target)

    assert target.health == 50
    assert capsys.readouterr().out == ""


def test_describe_prints_character_information(capsys):
    character = Character("Aria", 100, 15)

    character.describe()

    output = capsys.readouterr().out

    assert output == "Aria has 100 HP and 15 ATK\n"
