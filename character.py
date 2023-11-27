"""
Caroline Su
A01369603
"""


def make_character():
    """

    :param name:
    :return:

    >>> make_character()
    {'X-coordinate': 0, 'Y-coordinate': 0, 'HP': 10, 'Max HP': 10, 'EX': 0, 'Level': 1, 'key': False}
    """
    return {"X-coordinate": 0, "Y-coordinate": 0,
            "HP": 10, "Max HP": 10, "EX": 0, "Level": 1, "key": False}


def move_character(character, direction):
    if direction == "N":
        character["Y-coordinate"] -= 1
    elif direction == "S":
        character["Y-coordinate"] += 1
    elif direction == "E":
        character["X-coordinate"] += 1
    elif direction == "W":
        character["X-coordinate"] -= 1


def upgrade_character_level(character):
    if character["Level"] == 1 and character["EX"] >= 10:
        character["Level"] = 2
        character["HP"] = 15
        character["Max HP"] = 15
        character["EX"] -= 10
        print("🎊 Congratulation! You are Level 2 now! You feel more powerful than before!\n"
              "Your courage has earned the recognition of the gods. You are now fully healed. Current HP: 15/15")

    if character["Level"] == 2 and character["EX"] >= 15:
        character["Level"] = 3
        character["HP"] = 15
        character["Max HP"] = 20
        character["EX"] -= 15
        print("🎊 Congratulation! You are Level 3 now! You feel more powerful than before!\n"
              "Your courage has earned the recognition of the gods. You are now fully healed. Current HP: 20/20"
              )







