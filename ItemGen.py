def generate_artifact_name():
    print("Welcome to the artifact name generator based on the 'World of Cultivation' universe!")

    # Ask the user to input levels for various elements and powers
    sword_level = int(input("Please enter a level for sword scripture power (0-10): "))
    spell_level = int(input("Please enter a level for spell talisman power (0-10): "))
    yao_level = int(input("Please enter a level for Yao arts power (0-10): "))
    beast_level = int(input("Please enter a level for beast soul talisman power (0-10): "))
    mo_level = int(input("Please enter a level for Mo physique technique power (0-10): "))

    # Assign each level a specific term
    level_terms = {0: "Null", 1: "Bare", 2: "Modest", 3: "Mild", 4: "Ample", 
                   5: "Strong", 6: "Powerful", 7: "Mighty", 8: "Dominant", 
                   9: "Imperial", 10: "Ultimate"}

    # Generate the artifact name
    artifact_name = f"{level_terms[sword_level]} Sword, {level_terms[spell_level]} Spell, {level_terms[yao_level]} Yao, {level_terms[beast_level]} Beast, {level_terms[mo_level]} Mo"

    print("The generated artifact name is:", artifact_name)

generate_artifact_name()
