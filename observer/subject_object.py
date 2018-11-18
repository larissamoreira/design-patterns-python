from subject import Subject

class WeatherData(Subject):
    def __init__(self, temp, humidity, pressure):
        self.temp = temp
        self.humidity = humidity
        self.pressure = pressure
        self.observers = []
    
    def get_temp():
        return self.temp

    def get_humidity():
        return self.humidity

    def get_pressure():
        return self.pressure

    def set_temp(self, temp):
        self.temp = temp
        self.notify('update temperature', temp=temp)
    
    def set_humidity(self, humidity):
        self.humidity = humidity
        self.notify('update humidity', humidity=humidity)

    def set_pressure(self, pressure):
        self.pressure = pressure
        self.notify('update pressure', pressure=pressure)

    def attach(self, observer):
        if not observer in self.observers:
            self.observers.append(observer)

    def detach(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify(self, *args, **kwargs):
        for observer in self.observers:
            observer.update(*args, **kwargs)