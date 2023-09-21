from datetime import datetime

from engine.sternman_engine import SternmanEngine
from battery.nubbin_battery import NubbinBattery


class Palindrome(SternmanEngine, NubbinBattery):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        SternmanEngine.__init__(self, current_mileage, last_service_mileage)
        NubbinBattery.__init__(self, last_service_date)

    def needs_service(self):
        if self.engine_should_be_serviced() or self.battery_should_be_serviced():
            return True
        else:
            return False
