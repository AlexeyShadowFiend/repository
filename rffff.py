import random


class Student:


    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 15
        self.tohunger = 0
        self.toeat = 0
        self.alive = True


    def to_study(self):
        print('I had a snack and went to school')
        self.progress += 0.15
        self.gladness -= 3
        self.money -= 10
        self.tohunger += 5
        self.toeat = 4
    def to_sleep(self):
        print('I will sleep')
        self.gladness += 3
    def to_chill(self):
        print('I had a snack and went for a walk')
        self.gladness += 5
        self.progress -= 0.2
        self.money -= 5
        self.tohunger += 3.5
        self.toeat += 3

    def to_eat(self):
        print('I go to eat')
        self.tohunger += 3.5
        self.tohunger = 0
        self.toeat += 15




    def is_alive(self):
        if self.progress <- 0.5:
            print('Cast out......')
            self.alive = False
        elif self.gladness <= 0:
            print('Depression..')
            self.alive = False
        elif self.progress > 5:
            print('Passed externally...')
            self.alive = False
        elif self.money <- 0:
            print('You not have money,so you go to work and you got an award')
            self.gladness += -5
            self.progress -= 0.2
            self.money += 100




    def end_of_day(self):
        print(f'Progress = {self.progress}')
        print(f'Gladness = {self.gladness}')
        print(f'Money = {self.money}')
        print(f'Satiety = {self.toeat}')
        print(f'Hunger = {self.tohunger}')

    def live(self, day):
        day = "Day " + str(day) + " of" + self.name + " Life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 4)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_eat()
        elif live_cube == 4:
            self.to_chill()
        self.end_of_day()
        self.is_alive()


nick = Student(name='Nick')
for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)
