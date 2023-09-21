from abc import ABC, abstractmethod

class Battery(ABC):
    def __init__(self, lastServiceDate):
        self.lastServiceDate = lastServiceDate

    @abstractmethod
    def needs_service(self):
        pass