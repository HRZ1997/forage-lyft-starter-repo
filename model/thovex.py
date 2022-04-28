from model.car import Car
from engine.capulet_engine import CapuletEngine
from battery.nubbin_battery import NubbinBattery


class Thovex(Car):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        self.engine = CapuletEngine
        self.battery = NubbinBattery
        self.engine.last_service_mileage = last_service_mileage
        self.engine.current_mileage = current_mileage
        self.battery.last_service_date = last_service_date
