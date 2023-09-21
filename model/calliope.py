from datetime import datetime

from engine.capulet_engine import CapuletEngine
from battery.spindler_battery import SpindlerBattery



class Calliope(CapuletEngine, SpindlerBattery):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        CapuletEngine.__init__(self, current_mileage, last_service_mileage)
        SpindlerBattery.__init__(self, last_service_date)
    def needs_service(self):
        if self.battery_should_be_serviced() or self.engine_should_be_serviced():
            return True
        else:
            return False
