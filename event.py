"""
Caroline Su
A01369603
"""


def get_valid_user_input():
    direction_list = ["N", "S", "W", "E", "STATE", "HELP"]
    while True:
        user_input = input("[Enter 'help' or a direction to move]: ").strip()
        if user_input.upper() in direction_list:
            return user_input.upper()
        # return "N", "S", "W", "E", "state", "help"
        else:
            print("❌ That is not a valid input, try again!")


def get_valid_direction(character, valid_input):
    while valid_input in ["STATE", "HELP"]:
        if valid_input == "STATE":
            describe_user_state(character)
        else:
            print("---------------------------------------------------------------------------------------\n"
                  "You will control the character's movement direction using the four keys:\n"
                  " 1.'N' for north direction\n"
                  " 2.'S' for south direction\n"
                  " 3.'E' for east direction\n"
                  " 4.'W' for west direction\n"
                  "You can also input 'state' to check your character's attributes or 'help' to get instruction.\n"
                  "---------------------------------------------------------------------------------------\n")
        valid_input = get_valid_user_input()
    return valid_input


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
    print(f"HP:{character['HP']}/{character['Max HP']} EX:{character['EX']} \
          Level:{character['Level']}")


def trigger_random_events(board, character):
    print("You move forward.")
    x_index = character["X-coordinate"]
    y_index = character["Y-coordinate"]

    if board[(x_index, y_index)] == "nothing":
        print("🍂 After a gust of wind passed by, the surroundings became even quieter. Nothing happened.")
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
    elif board[(x_index, y_index)] == "wooden chest":
        character["EX"] += 1
        print("🌈 You find a wooden chest in a pile of soil! EX + 1")
    if board[(x_index, y_index)] != "castle":
        board[(x_index, y_index)] = "traveled"
    print(board)


def hole_movement(distance, user_input):
    if ((distance[0] >= 80 and user_input == "S") or (distance[0] <= -40 and user_input == "N")
            or (distance[1] >= 80 and user_input == "W") or (distance[1] <= -40) and user_input == "E"):
        print("It seems like you are going too far? Maybe try the opposite direction...")
    if user_input == "N":
        distance[0] -= 10
    elif user_input == "E":
        distance[1] -= 10
    elif user_input == "S":
        distance[0] += 10
    elif user_input == "W":
        distance[1] += 10
    print("It's still pitch black. Keep moving forward...")
    print(distance)


def trigger_hole_event(character):
    distance = [40, 40]
    counter = 0
    while distance[0] != 0 or distance[1] != 0:
        user_input = get_valid_user_input()
        valid_input = get_valid_direction(character, user_input)
        if valid_input in ["S", "N", "W", "E"]:
            counter += 1
            if counter == 20:
                print("You feel a little uncomfortable, and the darkness makes you feel disoriented.\n"
                      "But you have no choice but to move forward...")
            if counter == 40:
                print("It seems like you've been wandering around in the cave for too long, feeling exhausted.\n"
                      "Just as you were starting to feel a bit desperate, it's as if the gods heard your plea...\n"
                      "A mysterious force transports you out of the cave, leaving a key quietly resting in your hand.\n"
                      "Your unwavering persistence appears to have caught the attention of the divine.\n"
                      "After a burst of white light, there is something lied in your hand.")
                break
            hole_movement(distance, valid_input)

    character["key"] = True
    print("Look what you've gotten! It seems to be a key... Could it be meant for opening the gates of the castle?\n"
          "Before you could ponder further, a mysterious force transports you out of the hole."
          "Please continue to explore the forest...")
