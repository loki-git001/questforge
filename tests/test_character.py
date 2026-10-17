from domain.character import Character
from domain.classes import Warrior, Mage, Rogue, Cleric


def test_warrior_initialization():
    warrior = Warrior("Bram")

    assert warrior.name == "Bram"
    assert warrior.health == 120
    assert warrior.attack_power == 18
    assert warrior.is_alive is True


def test_warrior_cleave():
    warrior = Warrior("Bram")
    target = Character("Goblin", 100, 5)

    warrior.special_ability(target)

    # 18 attack power * 1.5 = 27 damage
    assert target.health == 73


def test_mage_initialization():
    mage = Mage("Sylla")

    assert mage.name == "Sylla"
    assert mage.health == 80
    assert mage.attack_power == 10
    assert mage.mana == 50


def test_mage_fireball():
    mage = Mage("Sylla")
    target = Character("Goblin", 100, 5)

    mage.special_ability(target)

    assert target.health == 70
    assert mage.mana == 30
    assert mage.health == 80


def test_mage_cannot_cast_without_enough_mana(capsys):
    mage = Mage("Sylla")
    target = Character("Goblin", 100, 5)

    mage.mana = 10
    mage.special_ability(target)

    assert target.health == 100
    assert mage.mana == 10

    output = capsys.readouterr().out
    assert "Sylla doesn't have enough mana!" in output


def test_rogue_initialization():
    rogue = Rogue("Shadow")

    assert rogue.name == "Shadow"
    assert rogue.health == 90
    assert rogue.attack_power == 14


def test_rogue_backstab():
    rogue = Rogue("Shadow")
    target = Character("Goblin", 100, 5)

    rogue.special_ability(target)

    # 14 attack power * 2 = 28 critical damage
    assert target.health == 72


def test_cleric_initialization():
    cleric = Cleric("Eldrin")

    assert cleric.name == "Eldrin"
    assert cleric.health == 100
    assert cleric.attack_power == 16


def test_cleric_healing_touch():
    cleric = Cleric("Eldrin")
    target = Character("Bram", 100, 18)

    target.take_damage(30)
    cleric.healing_touch(target)

    # Target starts at 70 HP and receives 6 HP.
    assert target.health == 76

    # Cleric sacrifices 3 HP.
    assert cleric.health == 97


def test_cleric_cannot_heal_with_insufficient_health(capsys):
    cleric = Cleric("Eldrin")
    target = Character("Bram", 100, 18)

    cleric.take_damage(98)
    target.take_damage(30)

    cleric.healing_touch(target)

    assert cleric.health == 2
    assert target.health == 70

    output = capsys.readouterr().out
    assert "not enough health to heal others" in output
