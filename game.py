"""
Caroline Su
A01369603
"""
import random
from character import *
from battle import *
from event import *


def get_valid_user_input():
    direction_list = ["N", "S", "W", "E", "STATE", "HELP"]
    print("Enter your direction: ")
    while True:
        user_input = input("[Enter 'help' or a direction to move]: ").strip()
        if user_input.upper() in direction_list:
            return user_input.upper()
        # return "N", "S", "W", "E", "state", "help"
        else:
            print("❌ That is not a valid input, try again!")


def get_valid_direction(character, valid_input):
    if valid_input == "STATE":
        describe_user_state(character)
    elif valid_input == "HELP":
        print("---------------------------------------------------------------------------------------\n"
              "You will control the character's movement direction using the four keys:\n"
              " 1.'N' for north direction\n"
              " 2.'S' for south direction\n"
              " 3.'E' for east direction\n"
              " 4.'W' for west direction\n"
              "You can also input 'state' to check your character's attributes or 'help' to get instruction.\n"
              "---------------------------------------------------------------------------------------\n")
    else:
        return valid_input

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


# 🕌🗝️🔒🔓🚫🎉🍂🐍🐉🐻🦇🐗🫀😰😵😀😠👈👉


def movement_and_event(character, board, direction):
    move_character(character, direction)
    trigger_random_events(board, character)
    is_alive(character)
    upgrade_character_level(character)
    if there_is_an_attack():
        attack_battle(character)
        upgrade_character_level(character)


def is_arrived_castle(character, rows, columns):
    if character["X-coordinate"] == (rows - 1) and character["Y-coordinate"] == (columns - 1):
        return True


def boss_fight(character, rows, columns, board):
    while not is_arrived_castle(character, rows, columns):
        # if character have found the key
        valid_input = get_valid_user_input()

        if valid_input == "state":
            describe_user_state(character)
            movement_and_event(character, board, valid_input)
        else:
            # if the character is not at the boundary and the direction is valid
            if validate_move(board, character, valid_input):
                movement_and_event(character, board, valid_input)
                if not is_alive(character):
                    print("☠️ You gradually feel your vision blur...\n"
                          "eventually, you collapse due to excessive blood loss. Sorry, you die!")
                    return
            else:
                print("🚫 You have reached the edge of the forest. You cannot go further in this direction!")

    print("💢 Your arrival wake up the dragon!")
    fight_dragon(character)


def game():  # called from main
    game_introduction()
    rows = 5
    columns = 5
    board = make_board(rows, columns)
    character = make_character()
    reminder = False
    while True:
        if check_reach_level_3(character) and is_alive(character) and character["key"]:
            break
        valid_input = get_valid_user_input()
        get_valid_direction(character, valid_input)

        # if the character is not at the boundary and the direction is valid
        if validate_move(board, character, valid_input):
            movement_and_event(character, board, valid_input)
            if not is_alive(character):
                print("☠️ You gradually feel your vision blur...\n"
                      "eventually, you collapse due to excessive blood loss. Sorry, you die!")
                return
            # if character reach level 3 but have not found the key, remind him to find it
            if check_reach_level_3(character) and not character["key"] and not reminder:
                print("Now you are strong enough to defeat the dragon in the dark castle.\n"
                      "🗝️ But you have not find the key! Please go check around the forest!")
                reminder = True
                # character is at the boundary
        else:
            print("🚫 You have reached the edge of the forest. You cannot go further in this direction!")

    print("🐉 It is time for you to defeat the dragon in the dark castle and get the the treasure.\n")
    # boss fight
    boss_fight(character, rows, columns, board)


def main():
    pass


if __name__ == "__main__":
    game()
