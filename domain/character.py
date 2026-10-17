class Character:
    def __init__(self, name: str, health: int, attack_power: int) -> None:
        self.name = name
        self.__max_health = max(0, health)
        self._health = max(0, self.__max_health)
        self.attack_power = attack_power

    @property
    def health(self) -> int:
        return self._health

    @property
    def is_alive(self) -> bool:
        return self._health > 0

    def take_damage(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("Damage can't be less than 0")
        self._health = max(0, self._health - amount)

    def describe(self) -> None:
        print(f"{self.name} has {self.health} HP and {self.attack_power} ATK")

    def attack(self, target: "Character") -> None:
        if not self.is_alive:
            return
        target.take_damage(self.attack_power)
        print(f"{self.name} attacks {target.name} for {self.attack_power} damage!")

    def heal(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("Heal amount can't be less than 0")
        self._health = min(self._health + amount, self.__max_health)
