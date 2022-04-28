from model.car import Car
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery


class Rorschach(Car):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        self.engine = WilloughbyEngine
        self.battery = NubbinBattery
        self.engine.last_service_mileage = last_service_mileage
        self.engine.current_mileage = current_mileage
        self.battery.last_service_date = last_service_date