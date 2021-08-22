from abc import ABC
from exceptions import LowFuelError, NotEnoughFuel


CONSUMPTION = 10   # liter/ 100km


class Vehicle(ABC):
    weight = 0
    started = False
    fuel = 0
    fuel_consumption = 0

    def __init__(self, weight=0, fuel=0, fuel_consumption=0):
        weight = self.weight
        fuel = self.fuel
        fuel_consumption = self.fuel_consumption

    def start(self):
        if self.started == False:
            if self.fuel > 0:
                self.started = True
                return 'W-w-w-w-zh-zh'
            else:
                raise NotEnoughFuel('Not Fuel!')

    def move(self, distance):
        use_up = distance / CONSUMPTION
        if use_up <= self.fuel:
            self.start()
            self.fuel -= use_up
            return 'Zhzhhzzhhzhz'
        raise NotEnoughFuel('Not Fuel!')