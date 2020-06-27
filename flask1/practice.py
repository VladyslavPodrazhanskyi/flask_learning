class Dog():
    def __init__(self, name, age, breed='poodle'):
        self.name = name
        self.age = age
        self.breed = breed
        self.speed = 20

    def run(self):
        print("I'm running")

    def speed_up(self, val):
        self.speed += val


d = Dog('Bobik', 5)

print(d.speed)
print(d.name)
print(d.breed)
print(d.__dict__)