# Клас Subject (Суб'єкт)
class TemperatureSensor:
    def __init__(self):
        self._temperature = 0
        self._observers = []

    def get_temperature(self):
        return self._temperature

    def set_temperature(self, temperature):
        self._temperature = temperature
        self.notify_observers()

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature)


# Клас Observer (Спостерігач)
class TemperatureDisplay:
    def update(self, temperature):
        print(f"Temperature Display: {temperature} degrees Celsius")


class TemperatureLogger:
    def update(self, temperature):
        print(f"Temperature Logger: Logging {temperature} degrees Celsius")


if __name__ == "__main__":
    # Створення екземплярів класів
    temperature_sensor = TemperatureSensor()
    display_observer = TemperatureDisplay()
    logger_observer = TemperatureLogger()

    # Додавання спостерігачів до сенсора
    temperature_sensor.add_observer(display_observer)
    temperature_sensor.add_observer(logger_observer)

    # Зміна температури і сповіщення спостерігачів
    temperature_sensor.set_temperature(25)
    temperature_sensor.set_temperature(30)
