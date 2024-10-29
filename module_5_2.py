
class House:
    pass
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

building_one = House('ЖК LEVEL МИЧУРИНСКИЙ', 42)
building_one.go_to(33)



h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
