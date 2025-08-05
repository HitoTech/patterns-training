from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class LightCommand(Command, ABC):
    def __init__(self, light):
        self.light = light

class LightOnCommand(LightCommand):
    def execute(self):
        self.light.on()
        print("Light's on :D")

class LightOffCommand(LightCommand):
    def execute(self):
        self.light.off()
        print("Light's off :(")