from model.car import Car
from engine.capulet_engine import CapuletEngine
from battery.spindler_battery import SpindlerBattery


class Calliope(Car):
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.engine = CapuletEngine
        self.battery = SpindlerBattery
        self.engine.last_service_mileage = last_service_mileage
        self.engine.current_mileage = current_mileage
        self.battery.current_date = current_date
        self.battery.last_service_date = last_service_date
