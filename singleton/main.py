from singleton import ConfigManager

configManager = ConfigManager()
key = configManager.get("env")
print(key)

a = ConfigManager()
b = ConfigManager()
print(a is b)

a.set("debug", True)
print(b.get("debug"))