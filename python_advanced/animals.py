class Animal_on_land:
    def say_hello(self):
        print("I'm animal on land")
    def running(self):
        print("I'm running here and there")

class Animal_on_sea:
    def say_hello(self):
        print("I'm animal on sea")

    def swimming(self):
        print("I'm swimming here and there")

class Guinea_pig(Animal_on_land, Animal_on_sea):
    pass

pig = Guinea_pig()
pig.say_hello()
pig.running()
pig.swimming()

