class Zombie:

    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, plant):
        plant.health = plant.health - self.damage
        return plant.health

    def take_damage(self, amount):
        self.health = self.health - amount
        return self.health

    def move(self, distance):
        distance = distance - 1
        return distance



class Plant:

    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, zombie):
        zombie.health = zombie.health - self.damage
        return zombie.health

    def take_damage(self, amount):
        self.health -= amount
        return self.health

turn = 1

plant1 = Plant("Peashooter", 100, 15)
plant2 = Plant("Raul", 50, 50)

zombie1 = Zombie("Mark", 150, 25)
distance = 1

while True:

    print(f"""
[Game Info]

Turn no.{turn}

Plants:
    Plant 1: {plant1.name}
        {plant1.name} health: {plant1.health}
    Plant 2: {plant2.name}
        {plant1.name} health: {plant2.health}

Zombies:
    Zombie 1: {zombie1.name}
        {zombie1.name} health: {zombie1.health}
        distance from plant = {distance}
    
""")

    if distance == 0:
        plant2.attack
        zombie1.take_damage(plant2.damage)
        plant1.take_damage(zombie1.damage)
        plant2.take_damage(zombie1.damage)
    elif distance > 0:
        plant2.attack(zombie1)
        plant1.attack(zombie1)
        distance = distance - 1



    if plant1.health and plant2.health <= 0:
        print("All plants are dead")
        print("Zombies won")
        break
    elif zombie1.health <= 0:
        print("Plants won")
        print(f"Final Zombie Health: {zombie1.health}")
        break

    turn = turn + 1
