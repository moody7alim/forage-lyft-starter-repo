from datetime import datetime

from engine.willoughby_engine import WilloughbyEngine
from battery.spindler_battery import SpindlerBattery


class Glissade(WilloughbyEngine, SpindlerBattery):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        WilloughbyEngine.__init__(self, current_mileage, last_service_mileage)
        SpindlerBattery.__init__(self, last_service_date)
    def needs_service(self):
        if  self.engine_should_be_serviced() or self.battery_should_be_serviced():
            return True
        else:
            return False
