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

# Generate a few items
for _ in range(5):
    print(generate_item())
