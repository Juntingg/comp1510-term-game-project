"""
ADD A DOCSTRING
"""
import random

from game import get_valid_user_input, get_valid_direction


def game_introduction():
    print("You are a warrior. It is said that within a forest lies a mysterious castle guarded\n"
          "by a dragon, protecting a treasure. Today, armed with your courage and sword, you\n"
          "arrive here. To win the game, you need to\n"
          " 1. level up your character to level 3.\n"
          " 2. find the key to open the castle gate.\n"
          " 3. defeat the dragon.\n"
          "---------------------------------------------------------------------------------------\n"
          "You will control the character's movement direction using the four keys:\n"
          " 1.'N' for north direction\n"
          " 2.'S' for south direction\n"
          " 3.'E' for east direction\n"
          " 4.'W' for west direction\n"
          "You can also input 'state' to check your character's attributes or 'help' to get instruction.\n"
          "---------------------------------------------------------------------------------------\n"
          "Many have ventured into this forest, only to return empty-handed or never return at all.\n"
          "But even in dire circumstances, an unwavering heart might bring you a miracle. So, adventurer,\n"
          "may your journey be successful!")

def make_board(rows, columns):
    events_choices = ["nothing", "mushroom", "mushroom", "wolf", "wolf", "wooden chest"]
    new_board = {}
    for row in range(rows):
        for column in range(columns):
            new_board[(row, column)] = random.choice(events_choices)
    # the right bottom corner of the game board must be a fixed value "castle"
    new_board[(rows - 1, columns - 1)] = "castle"
    new_board[(0, 0)] = "begin"
    hole_x, hole_y = 4, 4
    while (hole_x == 4 and hole_y == 4) or (hole_x == 0 and hole_y == 0):
        hole_x = random.randint(0, 4)
        hole_y = random.randint(0, 4)
    new_board[(hole_x, hole_y)] = "hole"
    return new_board



def check_reach_level_3(character):
    """

    :param character:
    :return:

    >>> my_char = {'Name': 'Bob', 'X-coordinate': 0, 'Y-coordinate': 0, 'HP': 10, 'Max HP': 10, 'EX': 0, 'Level': 2}
    >>> check_reach_level_3(my_char)
    False

    >>> my_char = {'Name': 'Joy', 'X-coordinate': 0, 'Y-coordinate': 0, 'HP': 10, 'Max HP': 10, 'EX': 0, 'Level': 3}
    >>> check_reach_level_3(my_char)
    True
    """
    return character["Level"] == 3


def describe_user_state(character):
    print(f"Your current location: ({character['X-coordinate']},{character['Y-coordinate']})")
    print(f"Name:{character['Name']} HP:{character['HP']}/{character['Max HP']} EX:{character['EX']} \
          Level:{character['Level']}")




def trigger_random_events(board, character):
    print("You move forward.")
    x_index = character["X-coordinate"]
    y_index = character["Y-coordinate"]

    if board[(x_index, y_index)] == "nothing":
        print("🍂 After a gust of wind passed by, the surroundings became even quieter. You decide to move forward.")
    elif board[(x_index, y_index)] == "mushroom":
        character["HP"] += 1
        print("🍄 You pick up a mushroom and eat it. You feel you are full of energy! HP + 1")
    elif board[(x_index, y_index)] == "wolf":
        character["HP"] -= 1
        print("🐺 A wolf attack you. HP - 1")
    elif board[(x_index, y_index)] == "traveled":
        print("👣 You notice faint footprints on the ground. You have been here not long ago.")
    elif board[(x_index, y_index)] == "hole":
        print("🕳️ Suddenly, you fall into a large hole. It's pitch black all around, and you can't see anything.\n"
              "It seems like you'll have to rely on your instincts to move forward now.")
        trigger_hole_event(character)
    elif board[(x_index, y_index)] == "castle" and not check_reach_level_3(character):
        print("A gruesome castle stands in front of you...\n"
              "🔒 But you have not get the key or reach level 3 to enter the castle. Please explore more!")
    else:
        character["EX"] += 1
        print("🌈 You find a wooden chest in a pile of soil! EX + 1")
    if board[(x_index, y_index)] != "castle":
        board[(x_index, y_index)] = "traveled"
    print(board)
def trigger_hole_event(character):
    distance = [40, 40]
    counter = 0
    while distance[0] != 0 or distance[1] != 0:
        input = get_valid_user_input()
        direction = get_valid_direction(character, input)
        counter += 1
        if counter == 40:
            print("It seems like you've been wandering around in the cave for too long, feeling exhausted.\n"
                  "Just as you were starting to feel a bit desperate, it's as if the gods heard your plea...\n"
                  "A mysterious force transports you out of the cave, leaving a key quietly resting in your hand.\n"
                  "Your unwavering persistence appears to have caught the attention of the divine.")
            break
        if distance[0] >= 80 or distance[0] <= -40 or distance[1] >= 80 or distance[1] <= -40:
            print("It seems like you are going too far? Maybe try the opposite direction...")
        if direction == "N":
            distance[0] -= 10
        elif direction == "E":
            distance[1] -= 10
        elif direction == "S":
            distance[0] += 10
        elif direction == "W":
            distance[1] += 10
        print("It's still pitch black. Keep moving forward...")
        print(distance)

    character["key"] = True
    print("Look what you've found! It seems to be a key... Could it be meant for opening the gates of the castle?\n"
          "Before you could ponder further, a mysterious force transports you out of the hole.")





