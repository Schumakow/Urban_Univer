
class House:
    pass
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        '''new_floor - номер этажа(int), на который нужно приехать'''
        for i in range(1, new_floor):
            print(i)
        if self.number_of_floors < new_floor or new_floor < 1):
            print('Такого этажа не существует')


building_one = House('ЖК LEVEL МИЧУРИНСКИЙ', 42)
building_one.go_to(33)

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
