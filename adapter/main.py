from adapter import FancyNotifierAdapter
from fancy_service import FancyNotifierService

notifier = FancyNotifierService()
adapter = FancyNotifierAdapter(notifier)

adapter.send("Major Tom to Ground Control")