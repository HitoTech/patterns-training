from unittest import case

from notifier import *

def create_notifier(channel: str) -> Notifier:
    match channel:
        case "email":
            return EmailNotifier()
        case "slack":
            return SlackNotifier()
        case _:
            return BasicNotifier()