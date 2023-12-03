"""
Caroline Su
A01369603
"""


def make_character():
    """
    Make a new character with default value

    :postcondition: create a new character with preset attributes
    :return: a dictionary representing the character's default attributes

    >>> make_character()
    {'X-coordinate': 0, 'Y-coordinate': 0, 'HP': 10, 'Max HP': 10, 'EX': 0, 'Level': 1, 'key': False}
    """
    return {"X-coordinate": 0, "Y-coordinate": 0,
            "HP": 10, "Max HP": 10, "EX": 0, "Level": 1, "key": False}


def move_character(character, direction):
    """
    Update character X or Y coordinate

    Update the array that represent character's attributes and location according to the direction

    :precondition: character must be a dictionary
    :precondition: direction must be a letter of "S", "N", "W" or "E"
    :param character: a dictionary represent the character
    :param direction: a single character represent the direction
    :postcondition: update X or Y coordinate of the dictionary represent the character

    >>> new_char = {'X-coordinate': 3, 'Y-coordinate': 3, 'HP': 6, 'Max HP': 10, 'EX': 0, 'Level': 1, 'key': False}
    >>> new_direction = "E"
    >>> move_character(new_char, new_direction)
    >>> new_char
    {'X-coordinate': 4, 'Y-coordinate': 3, 'HP': 6, 'Max HP': 10, 'EX': 0, 'Level': 1, 'key': False}

    >>> new_char = {'X-coordinate': 2, 'Y-coordinate': 1, 'HP': 10, 'Max HP': 10, 'EX': 0, 'Level': 1, 'key': False}
    >>> new_direction = "S"
    >>> move_character(new_char, new_direction)
    >>> new_char
    {'X-coordinate': 2, 'Y-coordinate': 2, 'HP': 10, 'Max HP': 10, 'EX': 0, 'Level': 1, 'key': False}
    """
    if direction == "N":
        character["Y-coordinate"] -= 1
    elif direction == "S":
        character["Y-coordinate"] += 1
    elif direction == "E":
        character["X-coordinate"] += 1
    elif direction == "W":
        character["X-coordinate"] -= 1
    print(character["X-coordinate"], character["Y-coordinate"])


def is_arrived_castle(character, rows, columns):
    if character["X-coordinate"] == (rows - 1) and character["Y-coordinate"] == (columns - 1):
        return True


def upgrade_character_level(character):
    """
    Upgrade character

    Upgrade character and increase his HP if his EX value reach to a certain value

    :precondition: character must be a dictionary
    :param character: the dictionary represent the character
    :postcondition: update Level and HP attributes value of the character

    >>> new_char = {'X-coordinate': 2, 'Y-coordinate': 1, 'HP': 10, 'Max HP': 10, 'EX': 13, 'Level': 1, 'key': False}
    >>> upgrade_character_level(new_char)
    🎊 Congratulation! You are Level 2 now! You feel more powerful than before!
    Your courage has earned the recognition of the gods. You are now fully healed. Current HP: 15/15
    >>> new_char
    {'X-coordinate': 2, 'Y-coordinate': 1, 'HP': 15, 'Max HP': 15, 'EX': 3, 'Level': 2, 'key': False}

    >>> new_char = {'X-coordinate': 2, 'Y-coordinate': 1, 'HP': 10, 'Max HP': 10, 'EX': 20, 'Level': 2, 'key': False}
    >>> upgrade_character_level(new_char)
    🎊 Congratulation! You are Level 3 now! You feel more powerful than before!
    Your courage has earned the recognition of the gods. You are now fully healed. Current HP: 20/20
    >>> new_char
    {'X-coordinate': 2, 'Y-coordinate': 1, 'HP': 20, 'Max HP': 20, 'EX': 5, 'Level': 3, 'key': False}
    """
    if character["Level"] == 1 and character["EX"] >= 10:
        character["Level"] = 2
        character["HP"] = 15
        character["Max HP"] = 15
        character["EX"] -= 10
        print("🎊 Congratulation! You are Level 2 now! You feel more powerful than before!\n"
              "Your courage has earned the recognition of the gods. You are now fully healed. Current HP: 15/15")

    if character["Level"] == 2 and character["EX"] >= 15:
        character["Level"] = 3
        character["HP"] = 20
        character["Max HP"] = 20
        character["EX"] -= 15
        print("🎊 Congratulation! You are Level 3 now! You feel more powerful than before!\n"
              "Your courage has earned the recognition of the gods. You are now fully healed. Current HP: 20/20"
              )
