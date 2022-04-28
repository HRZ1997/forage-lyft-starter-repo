from model.serviceable import Serviceable

class Car(Serviceable):
    def __init__(self, Engine, Battery):
        self.engine = Engine
        self.battery = Battery

    def needs_service(self):
        if self.battery.battery_needs_service() or self.engine.engine_needs_service():
            return True
        else:
            return False
