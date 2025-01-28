# 1. Libraries
import random
import copy


# 2. Constant Variables
# 2.1 base map of the D&D game
BASE_MAP = [[" ","_"," ","_"," ","_"," ","_"," ","_"," "],
            ["|","_","|","_","|","_","|","_","|","_","|"],
            ["|","_","|","_","|","_","|","_","|","_","|"],
            ["|","_","|","_","|","_","|","_","|","_","|"],
            ["|","_","|","_","|","_","|","_","|","_","|"],
            ["|","_","|","_","|","_","|","_","|","_","|"]]

# 2.2 base moves
BASE_MOVES = ['right', 'left', 'up', 'down']


# 3. Function Definitions
def initial_position():
    """Generate a random initial position for an entity."""
    position = {
    "row": random.randrange(1, 6),
    "column": random.randrange(1, 11, 2)
}
    return position


def modify_map(position):
    """Return a modified game map showing the player's position."""
    game_map = copy.deepcopy(BASE_MAP)
    game_map[position["row"]][position["column"]] = "x"
    return game_map


def show_board(game_map):
    """Display the game map."""
    for row in game_map:
        for cell in row:
            print(cell, end="")
        print()


def show_location(position):
    """Show the player's current location as room coordinates."""
    location = {
        "row": position["row"],
        "column": (position["column"] + 1) // 2
    }
    print("You are in room: ({0},{1})".format \
         (location["row"],location["column"]))


def filter_moves(position):
    """Return a list of valid moves based on the player's position."""
    moves = copy.deepcopy(BASE_MOVES)
    if position["row"] == 1:
        moves.remove("up")
    if position["row"] == 5:
        moves.remove("down")
    if position["column"] == 1:
        moves.remove("left")
    if position["column"] == 9:
        moves.remove("right")
    return moves


def change_position(direction,entity_position):
    """Update an entity's position based on the direction."""
    if direction == "up":
        entity_position["row"] -= 1
    elif direction == "down":
        entity_position["row"] += 1
    elif direction == "right":
        entity_position["column"] += 2
    elif direction == "left":
        entity_position["column"] -= 2
    return entity_position


# 4. Main Program Logic 
def main():
    print("Welcome to the Dungeon & Dragon")
    #if input
    # initialize player, dragon and dungeon positions
    player_position = initial_position()
    dungeon_position = initial_position()
    while dungeon_position["row"] == player_position["row"] and \
        dungeon_position["column"] == player_position["column"]:
        dungeon_position = initial_position()
    dragon_position = initial_position()
    while (dragon_position["row"] == player_position["row"] and \
        dragon_position["column"] == player_position["column"]) or \
        (dragon_position["row"] == dungeon_position["row"] and \
        dragon_position["column"] == dungeon_position["column"]) :
        dragon_position = initial_position()

    # main game loop
    while True:
        show_board(modify_map(player_position))
        show_location(player_position)
        print("You can move in {0} directions" \
              .format(filter_moves(player_position)))
        

        direction = input("Please enter your move: ").lower()
        if direction not in filter_moves(player_position):
            print("\nUnacceptable move! Please enter again...")
            continue


        player_position = change_position(direction,player_position)
        if player_position == dungeon_position:
            print("\nCongratulations, You have scaped the dungeon safely!")
            break
        elif player_position == dragon_position:
            print("\nThe Dragon has caught you! You are dead!")
            break


# 5. Entry Point Check
if __name__ == "__main__":
    main()