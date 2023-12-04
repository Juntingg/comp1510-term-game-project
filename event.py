"""
Caroline Su
A01369603
"""


def get_valid_user_input():
    """
    Get valid user input

    Prompt the user to enter a direction ('N', 'S', 'W', 'E') or other request ('STATE', 'HELP', 'HINT')

    :postcondition: Keep prompting the user for input until user enter a valid input
    :return: A string representing a valid direction ('N', 'S', 'W', 'E') or other request('STATE', 'HELP', 'HINT')
    """
    direction_list = ["N", "S", "W", "E", "STATE", "HELP", "HINT"]
    while True:
        user_input = input("[Enter 'help' or a direction to move]: ").strip()
        if user_input.upper() in direction_list:
            return user_input.upper()
        # return "N", "S", "W", "E", "state", "help"
        else:
            print("❌ That is not a valid input, try again!")


def get_valid_direction(character):
    """
    Get a valid direction for character movement.

    While the 'valid_input' is a game state ('STATE', 'HELP', 'HINT'),
    displays corresponding information. Keeps asking for input until
    user enter a valid direction.

    :precondition: The 'character' parameter must be a dictionary containing 'hole' key
    :precondition: The 'valid_input' parameter must be a string representing a valid game
                   request or direction
    :param character: A dictionary representing the character's attributes, including 'hole'
    :postcondition: Display corresponding message and prompt the user to enter a valid direction

    :return: A string representing a valid direction for character movement ('N', 'S', 'W', 'E').
    """
    valid_input = get_valid_user_input()
    while valid_input in ["STATE", "HELP", "HINT"]:
        if valid_input == "STATE":
            describe_user_state(character)
        elif valid_input == "HINT":
            print("Please check out the location:", character["hole"])
        else:
            print("---------------------------------------------------------------------------------------\n"
                  "You will control the character's movement direction using the four keys:\n"
                  " 1.'N' for north direction\n"
                  " 2.'S' for south direction\n"
                  " 3.'E' for east direction\n"
                  " 4.'W' for west direction\n"
                  "You can also input 'state' to check your character's attributes or 'help' to get instruction.\n"
                  "Tell you quietly: you can type 'hint' if you couldn't find the key!\n"
                  "---------------------------------------------------------------------------------------")
        valid_input = get_valid_user_input()
    return valid_input


def check_reach_level_3(character):
    """
    Check if the character has reached Level 3.

    :precondition: The 'character' parameter must be a dictionary containing 'Level' key
    :param character: A dictionary representing the character's attributes, including 'Level'
    :postcondition: Checks if the character's level is 3
    :return: True if the character's level is 3, else False

    >>> my_char = {'Name': 'Bob', 'X-coordinate': 0, 'Y-coordinate': 0, 'HP': 10, 'Max HP': 10, 'EX': 0, 'Level': 2}
    >>> check_reach_level_3(my_char)
    False

    >>> my_char = {'Name': 'Joy', 'X-coordinate': 0, 'Y-coordinate': 0, 'HP': 10, 'Max HP': 10, 'EX': 0, 'Level': 3}
    >>> check_reach_level_3(my_char)
    True
    """
    return character["Level"] == 3


def describe_user_state(character):
    """
    Display the current state of the user

    :precondition: The 'character' parameter must be a dictionary containing keys:
                   'X-coordinate', 'Y-coordinate', 'HP', 'Max HP', 'EX', 'Level'
    :param character: A dictionary representing the character's attributes
    :postcondition: Display the character's current location, HP, maximum HP, EX points, and level

    >>> my_char = {'Name': 'Bob', 'X-coordinate': 3, 'Y-coordinate': 4, 'HP': 15, 'Max HP': 20, 'EX': 30, 'Level': 3}
    >>> describe_user_state(my_char)
    Your current location: (3,4)
    HP:15/20 EX:30 Level:3

    >>> my_char = {'Name': 'Joy', 'X-coordinate': 2, 'Y-coordinate': 2, 'HP': 5, 'Max HP': 15, 'EX': 3, 'Level': 2}
    >>> describe_user_state(my_char)
    Your current location: (2,2)
    HP:5/15 EX:3 Level:2
    """
    print(f"Your current location: ({character['X-coordinate']},{character['Y-coordinate']})\n"
          f"HP:{character['HP']}/{character['Max HP']} EX:{character['EX']} "
          f"Level:{character['Level']}")


def trigger_random_events(board, character):
    """
    Trigger a random event

    Trigger a random event based on the location character has reached and print corresponding message

    :precondition: The 'board' parameter must be a dictionary where keys are coordinate tuples (x, y)
                   and values represent events at those coordinates.
    :precondition: The 'character' parameter must be a dictionary containing "HP" attribute
    :param board: A dictionary representing the game board with coordinates as keys and events as values.
    :param character: A dictionary representing the character's attributes.
    :postcondition: Display message based on the triggered event and update the character's attributes
    """
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
    # print(board)


def hole_movement(distance, user_input):
    """
    Simulate movement within a hole based on user input

    Move the character within a pitch-black hole based on the user's directional input,
    and display warning message if the user is going too far in one direction

    :precondition: The 'distance' parameter must be a list containing two integer elements representing
                   the distance moved along the x-axis and y-axis
    :precondition: The 'user_input' parameter must be a string of "N", "E", "S", or "W"
    :param distance: A list representing the distance moved along the x and y axes within the hole
    :param user_input: A string representing the user's directional input ("N", "E", "S", "W")
    :postcondition: Update the distance based on the user's input Displays a warning message
                    if the user is going too far in one direction

    >>> test_distance = [20, -10]
    >>> hole_movement(test_distance, "N")
    It's still pitch black. Keep moving forward...
    >>> test_distance
    [10, -10]

    >>> test_distance = [60, 60]
    >>> hole_movement(test_distance, "S")
    It seems like you are going too far? Maybe try the opposite direction...
    It's still pitch black. Keep moving forward...
    >>> test_distance
    [70, 60]
    """
    if ((distance[0] >= 60 and user_input == "S") or (distance[0] <= -30 and user_input == "N")
            or (distance[1] >= 60 and user_input == "W") or (distance[1] <= -30) and user_input == "E"):
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
    # print(distance)


def trigger_hole_event(character):
    """
    Simulate events when the character falls into a hole

    Initiate a scenario where the character falls into a hole and must navigate through darkness.
    The character makes directional movements based on user valid inputs. After a certain number
    of movements, special events occur, and the character obtains a key.

    :precondition: The 'character' parameter must be a dictionary containing "key" attribute
    :param character: A dictionary representing the character's attributes
    :postcondition: character's key attribute will have a boolean value of True
    """
    distance = [30, 30]
    counter = 0
    while distance[0] != 0 or distance[1] != 0:
        get_valid_user_input()
        valid_input = get_valid_direction(character)
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
