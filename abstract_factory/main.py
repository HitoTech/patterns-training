from abstract_factory.mac_widgets import MacFactory
from abstract_factory.win_widgets import WinFactory
from app import paint

import platform

if platform.system() == "Darwin":
    factory = MacFactory()
else:
    factory = WinFactory()

print(f"Detected OS: {platform.system()}")

paint(factory)