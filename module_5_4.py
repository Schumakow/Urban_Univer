lass House:
    pass
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return   super().__new__(cls)


    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        '''new_floor - номер этажа(int), на который нужно приехать'''
        for i in range(1, new_floor):
            print(i)
        if self.number_of_floors < new_floor or new_floor < 1:
            print('Такого этажа не существует')
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"
    def __eq__(self, other):
        '''__eq__(self, other) - должен возвращать True, если количество этажей одинаковое у self и у other.'''
        return self.number_of_floors == other.number_of_floors
    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floor
    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors
    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors
    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors
    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors
    def __add__(self, value):
        new_value = self.number_of_floors + value
        print(f'метод add! {self.name}')
        # return new_value

    def __radd__(self, other):
        new_value = value + self.number_of_floors
        return new_value
    def __iadd__(self, other):
        self.number_of_floors += value
        return self.number_of_floors

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
#
h2 = House('ЖК Акация', 20)
print(House.houses_history)

h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

del h2
del h1

print(House.houses_history)
