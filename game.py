"""
Caroline Su
A01369603
"""
import random
import character
import battle
import event


def game_introduction():
    """
    Introduce the game to the player

    :postcondition: Print the game introduction and instructions to the player
    """
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


def make_board(rows, columns, my_character):
    """
    Create a new game board

    Create a board with the given number of rows and columns. Each cell is assigned
    a random event from a predefined set of choices. The bottom-right corner is set as "castle",
    the top-left corner as "begin", and a random cell (excluding corners) as "hole"

    :precondition: 'rows' and 'columns' must be positive integers
    :precondition: The 'my_character' dictionary must be provided and contain valid character attributes
    :param rows: The number of rows in the board
    :param columns: The number of columns in the board
    :param my_character: A dictionary representing the character's attributes
    :postcondition: Generate a board with specified dimensions, assigns events to cells, places "castle",
                    "begin", and "hole" events at fixed locations, and updates the 'my_character' dictionary
                    with the location of the hole
    :return: A dictionary representing the generated game board
    """
    events_choices = ["nothing", "mushroom", "mushroom", "wolf", "wolf", "wooden chest"]
    new_board = {}
    for row in range(rows):
        for column in range(columns):
            new_board[(row, column)] = random.choice(events_choices)
    # the right bottom corner of the game board must be a fixed value "castle"
    new_board[(rows - 1, columns - 1)] = "castle"
    new_board[(0, 0)] = "begin"
    hole_x, hole_y = rows - 1, columns - 1
    while (hole_x == (rows - 1) and hole_y == (columns - 1)) or (hole_x == 0 and hole_y == 0):
        hole_x = random.randint(0, (rows - 1))
        hole_y = random.randint(0, (columns - 1))
    new_board[(hole_x, hole_y)] = "hole"
    my_character["hole"] = (hole_x, hole_y)
    return new_board


def validate_move(board, my_character, direction):
    """
    Validate character's movement

    Checks if the movement in the given direction is within the boundaries of the board

    :precondition: 'board' must contain coordinates as keys representing the game board
    :precondition: 'my_character' must contain 'X-coordinate' and 'Y-coordinate' keys with valid integer values
    :precondition: 'direction' parameter must be a string with a value of 'N', 'S', 'E', or 'W'.
    :param board: A dictionary representing the game board with coordinates as keys
    :param my_character: A dictionary representing the character's attributes
    :param direction: A string representing the direction ('N', 'S', 'E', or 'W')
    :postcondition: Check if the character's movement in the specified direction is within the board's boundaries
    :return: True if the move is valid, otherwise False

    >>> my_board = {(0, 0): 'A', (1, 0): 'B', (0, 1): 'C', (1, 1): 'D'}
    >>> my_char = {"X-coordinate": 0, "Y-coordinate": 0}
    >>> validate_move(my_board, my_char, 'N')
    False
    >>> validate_move(my_board, my_char, 'E')
    True
    """
    x_max_coordinator = max((key[0]) for key in board.keys())
    y_max_coordinator = max((key[1]) for key in board.keys())
    if my_character["X-coordinate"] == x_max_coordinator and direction == "E":
        return False
    elif my_character["X-coordinate"] == 0 and direction == "W":
        return False
    elif my_character["Y-coordinate"] == 0 and direction == "N":

        return False
    elif my_character["Y-coordinate"] == y_max_coordinator and direction == "S":
        return False
    return True


def game():  # called from main
    """
    Start a new game
    """
    # initiate the game configuration
    game_introduction()
    my_character = character.make_character()
    rows = 7
    columns = 7
    board = make_board(rows, columns, my_character)
    key_reminder = False
    dragon_reminder = False
    while True:
        if (event.check_reach_level_3(my_character) and battle.is_alive(my_character)
                and my_character["key"] and character.is_arrived_castle(my_character, rows, columns)):
            break
        valid_direction = event.get_valid_direction(my_character)
        # if the character is not at the boundary and the direction is valid
        if validate_move(board, my_character, valid_direction):
            character.move_character(my_character, valid_direction)
            event.trigger_random_events(board, my_character)
            battle.is_alive(my_character)
            character.upgrade_character_level(my_character)
            if battle.there_is_an_attack():
                battle.attack_battle(my_character)

            if not battle.is_alive(my_character):
                print("☠️ You gradually feel your vision blur...\n"
                      "eventually, you collapse due to excessive blood loss. Sorry, you die!")
                return
            character.upgrade_character_level(my_character)
            # if character reach level 3 but have not found the key, remind him to find it
            if event.check_reach_level_3(my_character) and not my_character["key"] and not key_reminder:
                print("Now you are strong enough to defeat the dragon in the dark castle.\n"
                      "🗝️ But you have not find the key! Please go check around the forest!")
                key_reminder = True
            if event.check_reach_level_3(my_character) and my_character["key"] and not dragon_reminder:
                print("🐉 It is time for you to defeat the dragon in the dark castle and get the the treasure.\n"
                      "Please go to the south east corner of the forest!")
                dragon_reminder = True
        # character is at the boundary
        else:
            print("🚫 You have reached the edge of the forest. You cannot go further in this direction!")

    # boss fight
    if character.is_arrived_castle(my_character, rows, columns):
        print("💢 🐉 🔥Your arrival wake up the dragon!")
        battle.fight_dragon(my_character)


def main():
    """
    Run the game
    """
    game()


if __name__ == "__main__":
    """
    Run the main function
    """
    main()
