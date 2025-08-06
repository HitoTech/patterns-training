from observer.interfaces import Subject, Observer


class WeatherStation(Subject):
    def __init__(self):
        self._observers = []
        self._temperature = None

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self._temperature)

    def set_temperature(self, temperature: float):
        self._temperature = temperature
        self.notify()