from decorator.notifier import EmailDecorator, SlackDecorator
from notifier import BasicNotifier

# Console
notifier = BasicNotifier()
notifier.send("This is an SOS to the World")

# Email
notifier = EmailDecorator(BasicNotifier())
notifier.send("This is an SOS to the World")

# Slack
notifier = SlackDecorator(BasicNotifier())
notifier.send("This is an SOS to the World")

# Multi channel
notifier = SlackDecorator(EmailDecorator(BasicNotifier()))
notifier.send("This is an SOS to the World")