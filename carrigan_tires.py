from tires.tires import Tires
import numpy as np

class CarriganTires(Tires):
    def __init__(self, tires_condition):
        self.tires_condition = tires_condition

    def tires_need_service(self):
        return np.max(self.tires_condition) > 0.9