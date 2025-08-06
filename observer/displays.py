from observer.interfaces import Observer


class ConsoleDisplay(Observer):
    def update(self, temperature: float) -> None:
        print(f"New temperature is {temperature}")

class MobileDisplay(Observer):
    def update(self, temperature: float) -> None:
        print(f"New mobile temp is {temperature}")

class AlertDisplay(Observer):
    def update(self, temperature: float) -> None:
        if temperature > 40:
            print("ALERT! Temperature is above 40")