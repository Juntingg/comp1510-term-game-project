"""
Caroline Su
A01369603
"""
import random


# health/happiness/hit points and/or other meaningful measurable
# attributes, a level, and abilities


def make_board(rows, columns):
    events_choices = ["nothing", "nothing", "mushroom", "wolf", "wooden chest"]
    new_board = {}
    for row in range(rows):
        for column in range(columns):
            new_board[(row, column)] = random.choice(events_choices)

    new_board[(0, 0)] = ""
    return new_board


def make_character(name):
    return {f"Name": {name}, "X-coordinate": 0, "Y-coordinate": 0,
            "HP": 10, "Max HP": 10, "EX": 0}


def check_random_events(board, character):
    print("You look around.")
    x_index = character["X-coordinate"]
    y_index = character["Y-coordinate"]
    if board[(x_index, y_index)] == "nothing":
        print("After a gust of wind passed by, the surroundings became even quieter. You decide to move forward.")
    elif board[(x_index, y_index)] == "mushroom":
        character["HP"] += 1
        print("You pick up a mushroom and eat it. You feel you are full of energy! HP + 1")
    elif board[(x_index, y_index)] == "wolf":
        character["HP"] -= 1
        print("A wolf attack you. HP - 1")
    else:
        character["EX"] += 2
        print("You find a wooden chest in a pile of soil! EX + 2")


def get_valid_user_input():
    input_list = {"1": "N", "2": "S", "3": "W", "4": "E", "state": "state"}
    print('Choose a direction you want to go, [(1, "north"), (2, "south"), (3, "west"), (4, "east")]')
    print('Or type in "state" to see your character states.')
    while True:
        user_input = input("Enter 'state' or a number(1-4): ").strip()
        if user_input in input_list.keys():
            valid_input = input_list[user_input]
            return valid_input
        else:
            print("❌ That is not a valid input, try again!")


def game(): # called from main
    rows = 5
    columns = 5
    board = make_board(rows, columns)
    character = make_character("Player name")
    check_random_events(board, character)

    get_valid_user_input()
# achieved_goal = False
# while not achieved_goal:
# // Tell the user where they are
# describe_current_location(board, character)
# direction = get_user_choice( )
# valid_move = validate_move(board, character, direction)
# if valid_move:
# move_character(character)
# describe_current_location(board, character)
# there_is_a_challenge = check_for_challenges()
# if there_is_a_challenge:
# execute_challenge_protocol(character)
# if character_has_leveled():
# execute_glow_up_protocol()
# achieved_goal = check_if_goal_attained(board, character)
# else:
# // Tell the user they can’t go in that direction
# // Print end of game stuff like congratulations or sorry you died


def main():
    pass


if __name__ == "__main__":
    game()
