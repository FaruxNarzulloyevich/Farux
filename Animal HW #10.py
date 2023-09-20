class Animal:

    def __init__(self,animal):
        self.animal = animal


class Dog(Animal):

    def __init__(self,animal):
        super().__init__(animal)

    def make_sound(self,make_sound):
        self.make_sound = 'wouwou'

    def listen_sound(self,animal):
            return animal.make_sound


print(Animal.dog(make_sound))