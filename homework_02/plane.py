"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel,fuel_consumption)
        self.cargo = 0
        self.max_cargo = max_cargo

    def load_cargo(self, cargo_weight):
        if self.cargo + cargo_weight <= self.max_cargo:
            self.cargo += cargo_weight
        else:
            raise CargoOverload()

    def remove_all_cargo(self):
        removed_cargo = self.cargo
        self.cargo = 0
        return removed_cargo