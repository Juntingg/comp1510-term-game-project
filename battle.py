"""
ADD A DOCSTRING
"""
import random


def is_alive(character):
    """
    Check if the character is alive

    Check if character's HP is reduced to 0

    :param character: a dictionary representing character
    :postcondition: determine if character is alive
    :return: True is character HP is greater than 0 else False

    >>> new_character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 3}
    >>> is_alive(new_character)
    True

    >>> new_character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 0}
    >>> is_alive(new_character)
    False
    """
    return character["HP"] > 0


def there_is_an_attack():
    attack = random.randint(1, 5)
    if attack == 1:
        return True


def dodge_enemy_attack():
    enemy_attack = random.choice(["R", "L"])
    return enemy_attack


def dodge_attack(character, reduced_hp):
    print("Would you like to dodge to the right or to the left?(You have 50% chance to dodge the attack)")
    user_dodge = input("R for right 👉, L for left 👈. [Enter R or L]: ").strip().upper()
    while user_dodge not in ["L", "R"]:
        print("That is not a valid input. Please try again!")
        user_dodge = input("R for right, L for left. [Enter R or L]: ").strip().upper()
    if user_dodge == dodge_enemy_attack():
        print("👍 Nice! You dodge the attack!")
    else:
        character["HP"] -= reduced_hp
        print(f"💥 Oh no! You did not dodge the attack! HP - {reduced_hp}")


def attack_battle(character):
    enemy = random.choice(["🦇 bat", "🐻 bear", "🐗 boar", "🐍 snake"])
    print(f"❗Suddenly! A {enemy} emerges and launches an attack on you!")
    dodge_attack(character, 2)
    character["EX"] += 3
    print("⚔️ You unleash a powerful strike and defeat the enemy! EX + 3")


def fight_dragon(character):
    narration_list = ["The dragon is furious and swiped at you with a mighty paw.",
                      "He lunges forward, its massive jaws opening wide as searing flames shoot forth.",
                      "The dragon's colossal wings beat forcefully, creating gusts of wind",
                      "The dragon roars at you!"]
    for count in range(3):
        print(narration_list[count])
        dodge_attack(character, 5)
        if not is_alive(character):
            print("☠️ Sorry, you die! You lose the game.")
            return
        print("⚔️ You gather all your focus and deliver a mighty strike aimed at the dragon.")
    print("You persistently battled and defeated the dragon. Finally, roaring in protest, "
          "the dragon fell.\nIn a secluded corner, you discovered the treasure. You win the game!🎉🎉🎉")
