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
    return new_board


def make_character(name):
    return {f"Name": {name}, "X-coordinate": 0, "Y-coordinate": 0,
            "HP": 10, "Max HP": 10, "EX": 0}




def get_user_choice():

    direction_list = [(1, "north"), (2, "south"), (3, "west"), (4, "east")]
    print("Choose a direction you want to go,", direction_list)
    if True:
        user_input = int(input("Enter a number(1-4): "))
        if user_input in range(1, 5):
            direction = direction_list[user_input - 1][1]
            return direction


def game(): # called from main
    rows = 5
    columns = 5
    board = make_board(rows, columns)
    character = make_character("Player name")
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
