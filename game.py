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
            "HP": 10, "Max HP": 10, "EX": 0, "Level": 1}


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


def check_reach_level_3(character):
    return character["Level"] == 3


def is_alive(character):
    return character["HP"] == 3


def get_valid_user_input():
    input_list = {"1": "N", "2": "S", "3": "W", "4": "E", "state": "state"}
    print('Choose a direction you want to go, [(1, "north"), (2, "south"), (3, "west"), (4, "east")]')
    print('Or type in "state" to see your character states.')
    while True:
        user_input = input("[Enter 'state' or a number(1-4)]: ").strip()
        if user_input in input_list.keys():
            valid_input = input_list[user_input]
            return valid_input
        else:
            print("❌ That is not a valid input, try again!")


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


def dodge_attack():
    enemy_attack = random.choice(["R", "L"])
    return enemy_attack


# def enemy_dodge_attack():
#     enemy_dodge = random.randint(1, 4)
#     if enemy_dodge == 1:
#         return True

def attack_battle(character):
    enemy = random.choice(["bat", "bear", "boar", "snake"])
    print(f"Be careful! A {enemy} emerges and launches an attack on you!")
    print("Would you like to dodge to the right or to the left?(You have 50% chance to dodge the attack)")
    user_dodge = input("R for right, L for left. [Enter R or L]: ")
    if user_dodge.strip().upper()[0] == dodge_attack():
        print("Nice! You dodge the attack!")
    else:
        character["HP"] -= 2
        print("Oh no! You did not dodge the attack! HP - 2")

    character["EX"] += 4
    print("You unleash a powerful strike and defeat the enemy! EX + 4")





def describe_user_state(character):
    return f"Name:${character['Name']} HP:${character['HP']}/${'Max HP'} EX:${character['EX']}"


def game(): # called from main
    rows = 5
    columns = 5
    board = make_board(rows, columns)
    character = make_character("Caroline")

    while not check_reach_level_3(character) and is_alive(character):
        valid_input = get_valid_user_input()
        if valid_input == "state":
            print(describe_user_state(character))
        else:
            move_character(character, valid_input)
            check_random_events(board, character)
            if there_is_an_attack():
                attack_battle()


    if not is_alive(character):
        print("Sorry, you die! You lose the game.")
    else:




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
