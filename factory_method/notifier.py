from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def send(self, message: str):
        pass

class BasicNotifier(Notifier):
    def send(self, message: str):
        print(f"Console: {message}")

class EmailNotifier(Notifier):
    def send(self, message: str):
        print(f"Email: {message}")

class SlackNotifier(Notifier):
    def send(self, message: str):
        print(f"Slack: {message}")