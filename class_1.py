class House():
    """
    Класс: описание дома
    """
    def __init__(self, street, number_home):
        """свойства дома"""
        self.street = street        #какие будут свойства у нашего класса
        self.number_home =  number_home
        # self.auto = auto
        # self.your_level = your_level
        self.age = 10
        self.year = 2022

    def build(self):
        """
        метод строит дом
        """
        print("Дом на улице " + self.street + " под номером " + str(self.number_home) + " построен!")

    # def parking(self):
    #     """
    #     парковка дома
    #     """
    #     print(f"Your " + self.auto + " already here!")
    #
    # def level(self):
    #     """этаж"""
    #     print("Твой этаж " + str(self.your_level) +  "." + " Приятного отдохнуть!")

    def age_of_house(self, year):
        """возраст дома"""
        print("Возраст дома: ")
        self.year -= self.age


class ProspectHouse(House):
    """Класс - наследник"""
    def __init__(self, prospect, number_house):
        super().__init__(self, number_house)
        self.prospect = prospect         #Наше собственное свойство

PrHouse = ProspectHouse("Проспект Сталлоне", 10)
print(PrHouse.prospect)