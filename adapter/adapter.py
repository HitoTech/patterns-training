from fancy_service import FancyNotifierService
from interfaces import Notifier


class FancyNotifierAdapter(Notifier):
    def __init__(self, notifier: FancyNotifierService):
        self.notifier = notifier

    def send(self, message: str) -> None:
        self.notifier.push_message_to_endpoint(message, 5)