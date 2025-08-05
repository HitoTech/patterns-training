class ConfigManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigManager, cls).__new__(cls)
            cls._instance._config = {
                "env": "production",
                "timeout": 30,
                "debug": False
            }
        return cls._instance

    def get(self, key):
        return self._config.get(key)

    def set(self, key, value):
        self._config[key] = value