class Pokemon:
    def __init__(self, element: str, name: str, health: float, attack: float, defence: float):
        self.element = element
        self.name = name
        self.health = health
        self.attack = attack
        self.defence = defence


def calc_damage(attacker: Pokemon, defender: Pokemon):
    effect = 1
    if attacker.element == "fire" and defender.element == "water":
        effect = 0.5
    elif attacker.element == "water" and defender.element == "fire":
        effect = 2
    elif attacker.element == "water" and defender.element == "grass":
        effect = 0.5
    elif attacker.element == "water" and defender.element == "electric":
        effect = 0.5
    elif attacker.element == "water" and defender.element == "water":
        effect = 1
    elif attacker.element == "grass" and defender.element == "water":
        effect = 2

    50 * (attacker.attack/defender.defence) * effect


stoffer = Pokemon("water", "Stoffer", 1200, 100, 200)
ofenlurf = Pokemon("fire", "Ofenlurf", 500, 225, 125)
uindeer = Pokemon("grass", "Uindeer", 350, 75, 350)
rencare = Pokemon("electric", "Rencare", 600, 60, 200)




result = calc_damage(stoffer,uindeer)
