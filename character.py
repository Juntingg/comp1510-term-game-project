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

    :precondition: character must be a dictionary with 'X-coordinate' and 'Y-coordinate' keys
    :precondition: direction must be a letter of "S", "N", "W" or "E"
    :param character: a dictionary representing the character
    :param direction: a single uppercase character representing the direction
    :postcondition: update X or Y coordinate of the dictionary representing the character
                    according to the specific direction

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


def is_arrived_castle(character, rows, columns):
    """
    Check if the character has arrived at the castle based on its coordinates

    :precondition: The 'character' parameter must be a dictionary with 'X-coordinate' and 'Y-coordinate' keys.
    :precondition: 'rows' and 'columns' must be positive integers representing the dimensions of the grid.
    :param character: A dictionary representing the character's position with 'X-coordinate' and 'Y-coordinate'
    :param rows: An integer representing the total number of rows in the grid
    :param columns: An integer representing the total number of columns in the grid
    :postcondition: Return True if the character's position matches the bottom-right corner of the grid,
                    otherwise return False
    :return: A boolean value indicating whether the character has arrived at the castle

    >>> is_arrived_castle({"X-coordinate": 4, "Y-coordinate": 4}, 5, 5)
    True
    >>> is_arrived_castle({"X-coordinate": 2, "Y-coordinate": 4}, 5, 5)
    False
    """
    return character["X-coordinate"] == (rows - 1) and character["Y-coordinate"] == (columns - 1)


def upgrade_character_level(character):
    """
    Update character level

    Update the character's level and attributes based on experience points (EX).

    :precondition: The 'character' parameter must be a dictionary containing 'Level' and 'EX' keys
    :param character: A dictionary representing the character's attributes
    :postcondition: Updates the 'character' dictionary based on the experience points (EX):

    >>> new_char = {"Level": 1, "EX": 12, "HP": 10, "Max HP": 10}
    >>> upgrade_character_level(new_char)
    🎊 Congratulation! You are Level 2 now! You feel more powerful than before!
    Your courage has earned the recognition of the gods. You are now fully healed. Current HP: 15/15
    >>> new_char
    {'Level': 2, 'EX': 2, 'HP': 15, 'Max HP': 15}
    >>> new_char = {"Level": 2, "EX": 20, "HP": 15, "Max HP": 15}
    >>> upgrade_character_level(new_char)
    🎊 Congratulation! You are Level 3 now! You feel more powerful than before!
    Your courage has earned the recognition of the gods. You are now fully healed. Current HP: 20/20
    >>> new_char
    {'Level': 3, 'EX': 5, 'HP': 20, 'Max HP': 20}
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
