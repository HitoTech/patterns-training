from observer.displays import ConsoleDisplay, MobileDisplay, AlertDisplay
from observer.weather_station import WeatherStation

weather_station = WeatherStation()
console_display = ConsoleDisplay()
mobile_display = MobileDisplay()
alert_display = AlertDisplay()

weather_station.attach(console_display)
weather_station.attach(mobile_display)
weather_station.attach(alert_display)

weather_station.set_temperature(23.5)
weather_station.set_temperature(0)
weather_station.set_temperature(77.7)

weather_station.detach(mobile_display)

weather_station.set_temperature(50)