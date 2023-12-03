"""
Caroline Su
A01369603
"""
import random
import character
import battle
import event


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


def validate_move(board, my_character, direction):
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
    Run the game
    """
    # initiate the game configuration
    game_introduction()
    rows = 5
    columns = 5
    board = make_board(rows, columns)
    my_character = character.make_character()
    key_reminder = False
    dragon_reminder = False
    while True:
        if (event.check_reach_level_3(my_character) and battle.is_alive(my_character)
                and my_character["key"] and character.is_arrived_castle(my_character, rows, columns)):
            break
        valid_input = event.get_valid_user_input()
        valid_direction = event.get_valid_direction(my_character, valid_input)
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
        print("💢 Your arrival wake up the dragon!")
        battle.fight_dragon(my_character)


def main():
    game()


if __name__ == "__main__":
    main()
