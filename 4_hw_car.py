class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year
    def start(self):
        print('Автомобиль заведен')
    def stop(self):
        print('Автомобиль заглушен')
    def pick_year(self):
        print(self.year)
    def pick_type(self):
        print(self.type)
    def pick_color(self):
        print(self.color)
