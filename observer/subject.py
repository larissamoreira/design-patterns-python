class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        if not observer in self.observers:
            self.observers.append(observer)

    def detach(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)
    
    def notify(self, *args, **kwargs):
        for observer in self.observers:
            observer.update(*args, **kwargs)