"""
Caroline Su
A01369603
"""
import random


def is_alive(character):
    """
    Check if the character is alive

    Check if character's HP is reduced to 0

    :precondition: The 'character' parameter must be a dictionary containing 'HP' key
    :param character: A dictionary representing the character's attributes, including 'HP'
    :postcondition: Determines if the character is alive based on their HP
    :return: True if character's HP is greater than 0, otherwise False

    >>> new_character = {"X-coordinate": 1, "Y-coordinate": 1, "HP": 3}
    >>> is_alive(new_character)
    True

    >>> new_character = {"X-coordinate": 1, "Y-coordinate": 1, "HP": 0}
    >>> is_alive(new_character)
    False
    """
    return character["HP"] > 0


def there_is_an_attack():
    """
    Check if there is a random attack

    Simulate a random encounter with an enemy. It generates a random number between 1 and 5
    and returns True if the number is 1, indicating an attack. Otherwise, it returns False

    :postcondition: determine if a random foe appears
    :return: True if a random enemy appears, else False
    """
    attack = random.randint(1, 5)
    if attack == 1:
        return True


def dodge_enemy_attack():
    """
    Simulate dodging an enemy attack

    Randomly select an attack direction ("R" for right or "L" for left) by the enemy,
    and return the selected direction representing the enemy's attack direction

    :postcondition: Simulate a random selection of enemy attack direction ("R" or "L")
    :return: A string representing the direction of the enemy's attack ("R" for right or "L" for left)
    """
    enemy_attack = random.choice(["R", "L"])
    return enemy_attack


def ask_dodge_direction():
    """
    Prompt the user to choose a dodge direction (L or R) with a 50% chance to dodge the attack

    :postcondition: Prompt the user to choose direction until valid input is entered
    :return: A string representing the user's chosen dodge direction ('R' for right or 'L' for left)
    """
    print("Would you like to dodge to the right or to the left?(You have 50% chance to dodge the attack)")
    user_dodge = input("R for right 👉, L for left 👈. [Enter R or L]: ").strip().upper()
    while user_dodge not in ["L", "R"]:
        print("❌ That is not a valid input. Please try again!")
        user_dodge = input("R for right 👉, L for left 👈. [Enter R or L]: ").strip().upper()
    return user_dodge


def dodge_attack(character, reduced_hp, user_dodge):
    """
    Determine if the character dodge an enemy attack

    :precondition: The 'character' dictionary must contain the 'HP' key
    :precondition: 'reduced_hp' must be a positive integer representing the amount of HP reduced
    :precondition: 'user_dodge' must be a string with a value of 'L' or 'R'
    :param character: A dictionary representing the character's attributes, including 'HP'
    :param reduced_hp: An integer representing the amount of reduced HP if the dodge fails
    :param user_dodge: A string representing the user's chosen dodge direction ('L' or 'R')
    :postcondition: If the 'user_dodge' match the enemy attack direction, print a success
                    message. Otherwise, reduce the character's HP and prints a failure message
    """
    if user_dodge == dodge_enemy_attack():
        print("👍 Nice! You dodge the attack!")
    else:
        character["HP"] -= reduced_hp
        print(f"💥 Oh no! You did not dodge the attack! HP - {reduced_hp}")


def attack_battle(character):
    """
    Simulate a battle scenario where an enemy attack the character

    An enemy randomly appears and launches an attack on the character. The character
    is prompted to choose a dodge direction. If the dodge is successful, the character
    avoids damage; otherwise, HP is reduced by 2. After the attack, EX + 3.

    :precondition: The 'character' dictionary must be provided and must contain 'HP' and 'EX' keys
    :param character: A dictionary representing the character's attributes, including 'HP' and 'EX'
    :postcondition: Character is potentially losing HP and must gain EX
    """
    enemy = random.choice(["🦇 bat", "🐻 bear", "🐗 boar", "🐍 snake"])
    print(f"❗Suddenly! A {enemy} emerges and launches an attack on you!")
    user_dodge = ask_dodge_direction()
    dodge_attack(character, 2, user_dodge)
    character["EX"] += 3
    print("⚔️ You unleash a powerful strike and defeat the enemy! EX + 3")


def fight_dragon(character):
    """
    Simulate a battle between the character and a dragon

    Display a series of narrations describing the dragon's attacks and
    the character's attempts to dodge and strike.

    :precondition: The 'character' parameter must be a dictionary containing 'HP' key
    :param character: A dictionary representing the character's attributes, including 'HP'
    :postcondition: Simulate a battle scenario between the character and a dragon, print failure message
                    if the character die, or success message if the character defeat the dragon
    """
    narration_list = ["The dragon is furious and swiped at you with a mighty paw.",
                      "He lunges forward, its massive jaws opening wide as searing flames shoot forth.",
                      "The dragon's colossal wings beat forcefully, creating gusts of wind",
                      "The dragon roars at you!"]
    for count in range(3):
        print(narration_list[count])
        user_dodge = ask_dodge_direction()
        dodge_attack(character, 5, user_dodge)
        if not is_alive(character):
            print("☠️ Sorry, you die! You lose the game.")
            return
        print("⚔️ You gather all your focus and deliver a mighty strike aimed at the dragon.")
    print("You persistently battled and defeated the dragon. Finally, roaring in protest, "
          "the dragon fell.\nIn a secluded corner, you discovered the treasure. You win the game!🎉🎉🎉")
