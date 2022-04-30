from model.serviceable import Serviceable

class Car(Serviceable):
    def __init__(self, Engine, Battery, Tires):
        self.engine = Engine
        self.battery = Battery
        self.tires = Tires

    def needs_service(self):
        if self.battery.battery_needs_service() or self.engine.engine_needs_service() or self.tires.tires_need_service():
            return True
        else:
            return False
