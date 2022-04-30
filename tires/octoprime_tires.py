from tires.tires import Tires
import numpy as np

class OctoprimeTires(Tires):
    def __init__(self, tires_condition):
        self.tires_condition = tires_condition

    def tires_need_service(self):
        return np.sum(self.tires_condition) > 3
