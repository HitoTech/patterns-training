from factory import create_notifier

channels = ["email", "slack", "sms"]

for channel in channels:
    notifier = create_notifier(channel)
    notifier.send(f"Test message via {channel}")