from domain.classes import Warrior, Mage, Rogue, Cleric
from domain.battle import total_party_damage

if __name__ == "__main__":
    party = [Warrior("Bram"), Mage("Sylla"), Cleric("Eldrin"), Rogue("Kade")]
    dummy = Warrior("Training Dummy")

    print("=" * 50)
    print("BEFORE BATTLE")
    for member in party:
        member.describe()

    print("TARGET")
    dummy.describe()

    total_party_damage(party, dummy)

    print("=" * 50)
    print("AFTER BATTLE")
    for member in party:
        member.describe()

    print("TARGET")
    dummy.describe()
