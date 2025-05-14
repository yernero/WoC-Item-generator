import random

def generate_item():
    # Lists of possible characteristics for each item attribute
    item_types = ["Sword", "Spell Talisman", "Yao Art", "Beast Soul Talisman", "Mo Physique Technique"]
    power_levels = ["Uknown", "Bare", "Modest", "Mild", "Ample", "Strong", "Powerful", "Mighty", "Dominant", "Imperial", "Ultimate"]
    origins = ["Netherworld", "Kun Lun", "Tian Huan", "Nine Serenities", "Heavenly Court"]
    special_characteristics = ["Fire attribute", "Water attribute", "Wood attribute", "Metal attribute", "Earth attribute", "Yin attribute", "Yang attribute"]
    materials = ["Heavenly Jade", "Black Iron", "Spirit Wood", "Phoenix Feather", "Dragon Scale"]

    # Randomly select one characteristic from each list
    item_type = random.choice(item_types)
    power_level = random.choice(power_levels)
    origin = random.choice(origins)
    special_characteristic = random.choice(special_characteristics)
    material = random.choice(materials)

    # Construct the item name
    item_name = f"{power_level} {material} {item_type} of {origin} with {special_characteristic}"

    return item_name

# Parent class for weapon type items
class Weapon:
    def __init__(self, power_level, origin, material):
        self.power_level = power_level
        self.origin = origin
        self.material = material

# Child class for swords
class Sword(Weapon):
    def __init__(self, power_level, origin, material, special_characteristic):
        super().__init__(power_level, origin, material)
        self.special_characteristic = special_characteristic


# Parent class for Shen Power type items
class ShenPower:
    def __init__(self, power_level, origin):
        self.power_level = power_level
        self.origin = origin

# Child class for Spell Talisman, Yao Art and Mo Physique Technique
class SpellTalisman(ShenPower):
    def __init__(self, power_level, origin, special_characteristic):
        super().__init__(power_level, origin)
        self.special_characteristic = special_characteristic

class YaoArt(ShenPower):
    def __init__(self, power_level, origin, special_characteristic):
        super().__init__(power_level, origin)
        self.special_characteristic = special_characteristic

class MoPhysiqueTechnique(ShenPower):
    def __init__(self, power_level, origin, special_characteristic):
        super().__init__(power_level, origin)
        self.special_characteristic = special_characteristic


# Generate a few items
for _ in range(5):
    print(generate_item())


sword = Sword("Powerful", "Kun Lun", "Heavenly Jade", "Fire attribute")
#print(sword.power_level)  # Output: Powerful
#print(sword.material)  # Output: Heavenly Jade

spell_talisman = SpellTalisman("Mighty", "Netherworld", "Earth attribute")
#print(spell_talisman.power_level)  # Output: Mighty
#print(spell_talisman.special_characteristic)  # Output: Earth attribute
