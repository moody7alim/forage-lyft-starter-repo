from battery import Battery
class NubbinBattery():
    def __init__(self, last_service_date):
        super().__init__(last_service_date)

    def battery_should_be_serviced(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < self.current_date or self.engine_should_be_serviced():
            return True
        else:
            return False
        

