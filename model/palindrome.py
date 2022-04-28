from model.car import Car
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery


class Palindrome(Car):
    def __init__(self, last_service_date, warning_light_is_on):
        self.engine = SternmanEngine
        self.battery = SpindlerBattery
        self.engine.warning_light_is_on = warning_light_is_on
        self.battery.last_service_date = last_service_date
