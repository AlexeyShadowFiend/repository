import random


class animal:


    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.tohunger = 0
        self.toeat = 0
        self.alive = True


    def to_partying(self):
        print('time to go for a walk')
        self.progress += 0.15
        self.gladness += 7
        self.tohunger += 3
    def to_sleep(self):
        print('I will sleep')
        self.gladness += 3
        self.tohunger += 3
        self.toeat -= 4
    def to_eat(self):
        print('You go to eat')
        self.gladness += 5
        self.progress -= 0.2
        self.tohunger -= 8
        self.toeat += 10



    def to_hunger(self):
        print('I want to eat')
        self.gladness += 5
        self.tohunger += 30


    def is_alive(self):
        if self.progress <- 0.5:
            print('Cast out......')
            self.alive = False
        elif self.tohunger <- 100:
            print('You are very hungry..')
            self.alive = False
        elif self.progress > 5:
            print('Passed externally...')
            self.alive = False



    def end_of_day(self):
        print(f'Progress = {self.progress}')
        print(f'Gladness = {self.gladness}')
        print(f'Eat = {self.toeat}')
        print(f'Hunger = {self.tohunger}')

    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " Life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 4)
        if live_cube == 1:
            self.to_partying()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_eat()
        elif live_cube == 4:
            self.to_hunger()
        self.end_of_day()
        self.is_alive()

cat = animal(name='Cat')
for day in range(365):
    if cat.alive == False:
        break
    cat.live(day)
