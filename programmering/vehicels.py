class Monster:
    def __init__(self, name: str, health : int, attack_power: int):
        self.name = name
        self.health = health
        self.attack_power = attack_power


    def attack(self, target):

        print(self.name, "attackerar" , target)

    def take_damage(self, damage):
        self.health -= damage

    def life(self):
        if self.health > 1:
            print ("dead")
        else:
            print("it's alive")



class zombie(Monster):
    def __init__(self, name, health, attack_power, attack: int):
        super().__init__(name, health, attack_power)
        self.attack = attack


class dragon(Monster):
    def __init__(self, name, health, attack_power, fire_damage: int):
        super().__init__(name, health, attack_power)
        self.fire_damage = fire_damage
        print(self.name, self.health, self.attack_power)


class vampire(Monster):
    def __init__(self, name, health, attack_power, suck_blood):
        super().__init__(name, health, attack_power)
        self.suck_blood = suck_blood

dragon_1 = dragon("goonster" ,269, 42)

zombie_1 = zombie("goondead" ,100, 12)

vampire_1 = vampire("goonlord" ,1000 , 420)

dragon_1.attack("goonlord")

dragon_1.take_damage("42")

dragon_1.life()



