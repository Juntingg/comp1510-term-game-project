"""
Caroline Su
A01369603
"""
import random


def make_board(rows, columns):
    events_choices = ["nothing", "nothing", "mushroom", "wolf", "wooden chest"]
    new_board = {}
    for row in range(rows):
        for column in range(columns):
            new_board[(row, column)] = random.choice(events_choices)
    # the right bottom corner of the game board must be a fixed value "castle"
    new_board[(rows - 1, columns - 1)] = "castle"
    new_board[(0, 0)] = "begin"
    hole_x, hole_y = 4, 4
    while hole_x == 4 and hole_y == 4:
        hole_x = random.randint(0, 4)
        hole_y = random.randint(0, 4)
    new_board[(hole_x, hole_y)] = "hole"
    return new_board


def make_character(name):
    """

    :param name:
    :return:

    >>> make_character("Bob")
    {'Name': 'Bob', 'X-coordinate': 0, 'Y-coordinate': 0, 'HP': 10, 'Max HP': 10, 'EX': 0, 'Level': 1}

    >>> make_character("Caroline")
    {'Name': 'Caroline', 'X-coordinate': 0, 'Y-coordinate': 0, 'HP': 10, 'Max HP': 10, 'EX': 0, 'Level': 1}
    """
    return {"Name": name, "X-coordinate": 0, "Y-coordinate": 0,
            "HP": 10, "Max HP": 10, "EX": 0, "Level": 1, "key": False}


def trigger_random_events(board, character):
    print("You look around.")
    x_index = character["X-coordinate"]
    y_index = character["Y-coordinate"]
    if not check_reach_level_3(character):
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
            print("Suddenly, you fall into a large hole. It's pitch black all around, and you can't see anything.\n"
                  "It seems like you'll have to rely on your instincts to move forward now.")
            trigger_hole_event(character)
        elif board[(x_index, y_index)] == "castle":
            print("A gruesome castle stands in front of you...\n"
                  "🔒 But you have not get the key or reach level 3 to enter the castle. Please explore more!")
        else:
            character["EX"] += 2
            print("🌈 You find a wooden chest in a pile of soil! EX + 2")
        board[(x_index, y_index)] = "traveled"


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


def is_alive(character):
    return character["HP"] > 0


def trigger_hole_event(character):

    distance = [40, 40]
    counter = 0
    while distance[0] != 0 and distance[1] != 0:
        direction = get_valid_user_input()
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

    character["key"] = True
    print("Look what you've found! It seems to be a key... Could it be meant for opening the gates of the castle?\n"
          "Before you could ponder further, a mysterious force transports you out of the hole.")


def get_valid_user_input():
    input_list = {"1": "N", "2": "S", "3": "W", "4": "E", "state": "state"}
    print('Choose a direction you want to go, [(1, "north"), (2, "south"), (3, "west"), (4, "east")]\n'
          'Or type in "state" to see your character states.')
    while True:
        user_input = input("[Enter 'state' or a number(1-4)]: ").strip()
        if user_input in input_list.keys():
            valid_input = input_list[user_input]
            return valid_input
        # return "N", "S", "W", "E"
        else:
            print("❌ That is not a valid input, try again!")


def validate_move(board, character, direction):
    x_max_coordinator = max((key[0]) for key in board.keys())
    y_max_coordinator = max((key[1]) for key in board.keys())
    if character["X-coordinate"] == x_max_coordinator and direction == "E":
        return False
    elif character["X-coordinate"] == 0 and direction == "W":
        return False
    elif character["Y-coordinate"] == 0 and direction == "N":

        return False
    elif character["Y-coordinate"] == y_max_coordinator and direction == "S":
        return False
    return True


def move_character(character, direction):
    if direction == "N":
        character["Y-coordinate"] -= 1
    elif direction == "S":
        character["Y-coordinate"] += 1
    elif direction == "E":
        character["X-coordinate"] += 1
    elif direction == "W":
        character["X-coordinate"] -= 1


def there_is_an_attack():
    attack = random.randint(1, 5)
    if attack == 1:
        return True


def dodge_enemy_attack():
    enemy_attack = random.choice(["R", "L"])
    return enemy_attack

# 🕌🗝️🔒🔓🚫🎉🍂🐍🐉🐻🦇🐗🫀😰😵😀😠👈👉


def attack_battle(character):
    enemy = random.choice(["🦇 bat", "🐻 bear", "🐗 boar", "🐍 snake"])
    print(f"❗Be careful! A {enemy} emerges and launches an attack on you!")
    print("Would you like to dodge to the right or to the left?(You have 50% chance to dodge the attack)")
    user_dodge = input("R for right 👉, L for left 👈. [Enter R or L]: ")
    if user_dodge.strip().upper()[0] == dodge_enemy_attack():
        print("👍 Nice! You dodge the attack!")
    else:
        character["HP"] -= 2
        print("💥 Oh no! You did not dodge the attack! HP - 2")

    character["EX"] += 3
    print("⚔️ You unleash a powerful strike and defeat the enemy! EX + 3")


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


def describe_user_state(character):
    print(f"Your current location: ({character['X-coordinate']},{character['Y-coordinate']})")
    print(f"Name:{character['Name']} HP:{character['HP']}/{character['Max HP']} EX:{character['EX']}")


def is_arrived_castle(character, rows, columns):
    if character["X-coordinate"] == rows and character["Y-coordinate"] == columns:
        return True


def dodge_dragon(character):
    print("Would you like to dodge to the right or to the left?(You have 50% chance to dodge the attack)")
    user_dodge = input("R for right 👉, L for left 👈. [Enter R or L]: ")
    user_dodge = user_dodge.strip().upper()
    while user_dodge not in ["L", "R"]:
        print("That is not a valid input. Please try again!")
        user_dodge = input("R for right, L for left. [Enter R or L]: ")
    if user_dodge == dodge_enemy_attack():
        print("Nice! You dodge the attack!")
    else:
        character["HP"] -= 5
        print("Oh no! You did not dodge the attack! HP - 5")


def fight_dragon(character):
    narration_list = ["The dragon is furious and swiped at you with a mighty paw.",
                      "He lunges forward, its massive jaws opening wide as searing flames shoot forth.",
                      "The dragon's colossal wings beat forcefully, creating gusts of wind",
                      "The dragon roars at you!"]
    for count in range(3):
        print(narration_list[count])
        dodge_dragon(character)
        if not is_alive(character):
            print("☠️ Sorry, you die! You lose the game.")
            return
        print("⚔️ You gather all your focus and deliver a mighty strike aimed at the dragon.")
    print("You persistently battled and defeated the dragon. Finally, roaring in protest, "
          "the dragon fell.\n" + "In a secluded corner, you discovered the treasure. 🎉🎉🎉")


def movement_and_event(character, board, direction):
    move_character(character, direction)
    trigger_random_events(board, character)
    is_alive(character)
    upgrade_character_level(character)
    if there_is_an_attack():
        attack_battle(character)
        upgrade_character_level(character)



def game():  # called from main
    rows = 5
    columns = 5
    board = make_board(rows, columns)
    character = make_character("Caroline")
    reminder = False
    while not check_reach_level_3(character) and is_alive(character) and not character["key"]:
        valid_input = get_valid_user_input()

        if valid_input == "state":
            describe_user_state(character)
        else:
            # if the character is not at the boundary and the direction is valid
            if validate_move(board, character, valid_input):
                movement_and_event(character, board, valid_input)
                if not is_alive(character):
                    print("☠️ the reduing hp ..")
                    return
                # if character reach level 3 but have not found the key, remind him to find it
                if check_reach_level_3(character) and character["key"] and not reminder:
                    print("It is time for you to defeat the dragon in the dark castle and get the the treasure.\n"
                          "But you have not find the key! Please go check around the forest!")
                    reminder = True
                    # character is at the boundary
            else:
                print("🚫 You have reached the edge of the forest. You cannot go further in this direction!")

    print("It is time for you to defeat the dragon in the dark castle and get the the treasure.\n")
    # if character["key"]:
    #     print("And you have already find the key in a hole! You can go the the castle now!")
    # else:
    #     print("But you have not find the key! Please go check around the forest!")
    while not is_arrived_castle(character, rows, columns):
        # if character have found the key
        valid_input = get_valid_user_input()

        if valid_input == "state":
            describe_user_state(character)
            if not is_alive(character):
                print("☠️ the reduing hp ..")
                return
        else:
            # if the character is not at the boundary and the direction is valid
            if validate_move(board, character, valid_input):
                movement_and_event(character, board, valid_input)
            else:
                print("🚫 You have reached the edge of the forest. You cannot go further in this direction!")

    print("💢 Your arrival wake up the dragon!")
    fight_dragon(character)





def main():
    pass


if __name__ == "__main__":
    game()
