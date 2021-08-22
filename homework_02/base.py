from abc import ABC

from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):

    def __init__(self, weight=0, fuel=0, fuel_consumption=0):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError('Low Fuel!')

    def move(self, distance):
        fuel_amount = distance * self.fuel_consumption
        if fuel_amount <= self.fuel:
            self.start()
            self.fuel -= fuel_amount
            return
        raise NotEnoughFuel('Not Fuel!')
