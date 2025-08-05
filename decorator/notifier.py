from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def send(self, message:str):
        pass

class BasicNotifier(Notifier):
    def send(self, message:str):
        print(message)

class EmailDecorator(Notifier):
    def __init__(self, notifier: Notifier):
        self.notifier = notifier

    def send(self, message:str):
        self.notifier.send(message)
        print(f"Sending email with message: {message}")

class SlackDecorator(Notifier):
    def __init__(self, notifier: Notifier):
        self.notifier = notifier

    def send(self, message:str):
        self.notifier.send(message)
        print(f"Sending slack with message: {message}")