#!/usr/bin/python3

from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1.creature import HealCapability, TransformCapability

class BattleStrategy(ABC):

    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

class NormalStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> bool:
        if not self.is_valid(creature):
            raise ValueError(f"Invalid Creature '{creature.name}' for this normal strategy")
        print(creature.attack())

class DefensiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise ValueError(f"Invalid Creature '{creature.name}' for this defensive strategy")
        print(creature.attack())
        if isinstance(creature, HealCapability):
            print(creature.heal())

class AggressiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise ValueError(f"Invalid Creature '{creature.name}' for this aggressive strategy")
        if isinstance(creature, TransformCapability):
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())
