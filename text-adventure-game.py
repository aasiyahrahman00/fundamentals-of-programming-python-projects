#  Creates and returns the game map containing all the rooms, descriptions, exits, items, traps and hints. The dictionary is wrapped in a function to ensure the rooms reset each time the player starts a new game.
def create_rooms():
    return {
        "Cozy Burrow": {
            "description": "The cozy burrow is warm but unstable. Loose dirt trembles above you as the tunnels continue to shake.",
            "exits": {"north": "Flower Garden", "west": "Veggie Garden", "east": "Twisty Tunnel"},
            "item": "Favourite Pillow",
            "item-text": "You look towards your teddies and favourite pillow as they start shaking. You can't lose your precious belongings! ",
            "trap": None,
            "hint_direction": "The burrow branches north, west and east...",
            "hint_item": "Cushy items may protect you from dangerous falls..."
        },

        "Flower Garden": {
            "description": "A summery warm fragrance of roses hits you before you enter the flower garden. The sun beams across your face, you look up and you notice a bird flying overhead near a patch of tulips.",
            "exits": {"south": "Cozy Burrow"},
            "item": "Stick",
            "item-text": "You look around and see a stick lying near the tulips, tangled between petals and fallen stems.",
            "trap": None,
            "hint_direction": "The only clear path leads south...",
            "hint_item": "Long items can help reach high places..."
        },

        "Veggie Garden": {
            "description": "Vibrant rows of vegetables glisten in the soil, but the garden feels suspiciously quiet. Something useful may be hidden among the roots.",
            "exits": {"east": "Cozy Burrow"},
            "item": "Thick Bundle of Roots",
            "item-text": "Thick roots twist through the soil, mixed in with broken stems and scraps of old plants.",
            "trap": "net",
            "hint_direction": "The garden path leads east...",
            "hint_item": "Thick roots may help stabilise structures..."
        },

        "Twisty Tunnel": {
            "description": "The burrow narrows, twisting and turning deeper underground. The air feels damp, and the walls are swallowed by darkness.",
            "exits": {"west": "Cozy Burrow", "south": "Magical Forest"},
            "item": "Glowy Mushroom",
            "item-text": "A faint blue glow comes from a mushroom near the wall, highlighting the surrounding damp stones and moss.",
            "trap": None,
            "hint_direction": "The tunnel splits west and south...",
            "hint_item": "Dark places need a light source..."
        },

        "Magical Forest": {
            "description": "Whispers of an ancient language surround you as you approach the magical forest. Chills roll down your back as it gets darker and darker till you can't see much at all.",
            "exits": {"north": "Twisty Tunnel", "south": "Ancient Oak Door"},
            "item": None,
            "item-text": "",
            "trap": "darkness",
            "hint_direction": "Escape the forest north or south...",
            "hint_item": "Something glowing may help here..."
        },

        "Ancient Oak Door": {
            "description": "As the forest thins you notice a huge aged door before you and you can smell the sweet, sweet, heavenly aroma of bananas. You push the door, its locked!",
            "exits": {"north": "Magical Forest"},
            "item": "Golden Key",
            "trap": None,
            "item-text": "",
            "hint_direction": "The way back is north...",
            "hint_item": "The key is too high to reach without a tool..."
        }

    }

rooms = create_rooms()


#  Displays the player's current location, remaining moves and inventory
def show_status(current_room, moves_left, inventory):
    print("\n---------------------------------- STATUS ----------------------------------")
    print(f"Location: {current_room}")
    print(f"Hops left: {moves_left}")
    if inventory:
        print("Items:", ", ".join(inventory))
    else:
        print("Items: Empty")


#  Displays the current room description and item text
def show_room(current_room, moves_left, inventory):
    room_info = rooms[current_room]

    print(f"\nLocation: {current_room}")
    print(room_info["description"])

    if current_room == "Ancient Oak Door":
        if "Stick" in inventory:
            print("Something golden glitters high above in a crow's nest. With your stick, you are able to reach it.")
        else:
            print("Something golden glitters high above in a crow's nest, beyond the reach of your paws.")

    elif room_info["item"] is not None:
        print(room_info["item-text"])


#  Shows all collected items in the player's inventory
def show_inventory(inventory):
    if not inventory:
        print("\nYour woven basket is empty!")
    else:
        print("\nYour woven basket contains: ")
        for item in inventory:
            print("-", item)


#  Handles player movement between connected rooms and reduces the remaining move count
def move_player(current_room, direction, moves_left):
    exits = rooms[current_room]["exits"]

    if direction in exits:
        #  Moves player to connected room
        new_room = exits[direction]
        moves_left -= 1

        if direction == "north":
            print("\nYou cautiously hop north...")
        elif direction == "east":
            print("\nYou squeeze through east...")
        elif direction == "west":
            print("\nYou head west, ears alert...")
        elif direction == "south":
            print("\nYou scurry south, it gets darker...")

        return new_room, moves_left

    else:
        print(f"\nYou try to hop {direction}... thud. A wall. Maybe not that way.")
        return current_room, moves_left


#  Allows the player to collect items and checks for special items needed to win the game
def take_item(current_room, inventory, moves_left, collected_rooms, requested_item):
    current_item = rooms[current_room]["item"]
    requested_item = requested_item.lower().strip()

    if current_item is None:
        if current_room in collected_rooms:
            print("\nYou already collected everything useful from here!")
        else:
            print("\nThere is nothing useful here!")
        return inventory, moves_left, False, collected_rooms

    if requested_item == "":
        print("\nWhat are you trying to take? Type the item name, like 'take stick'.")
        return inventory, moves_left, False, collected_rooms

    if requested_item not in current_item.lower():
        print(f"\n{requested_item.capitalize()} catches your eye, but you cannot take {requested_item} here.")
        return inventory, moves_left, False, collected_rooms

    if current_item == "Golden Key":
        if "Stick" in inventory:
            inventory.append("Golden Key")
            rooms[current_room]["item"] = None
            collected_rooms.append(current_room)

            print("\nUsing the Stick, you carefully push the Golden Key from the crow's nest. Thud. The heavy key lands beside you.")
            print("You quickly unlock the Ancient Oak Door as the whispers suddenly fall silent.")
            print("The huge door creaks open, revealing endless banana trees glowing in the moonlight.")

            print(r"""
             (\_/)      
             (•.•)     YAY!
             / >🍌

            BANANA PARADISE FOUND!
            """)

            print(f"\nYou escaped with {moves_left} moves remaining.")

            game_over = True

        else:
            print(rooms[current_room]["hint_item"])
            game_over = False

        return inventory, moves_left, game_over, collected_rooms

    else:
        inventory.append(current_item)
        rooms[current_room]["item"] = None
        collected_rooms.append(current_room)
        print(f"\nYou've added {current_item} to your woven basket.")

        if current_item == "Thick Bundle of Roots":
            moves_left += 5
            print("\nThe bundle of roots stabilises the burrow. You gain extra time.")

        game_over = False
        return inventory, moves_left, game_over, collected_rooms


#  Checks whether a room trap is triggered and gives penalties if the player does not have the protective items
def check_trap(current_room, inventory, moves_left, triggered_traps):
    if current_room in triggered_traps:
        return moves_left, triggered_traps

    if current_room == "Veggie Garden":
        if "Favourite Pillow" in inventory:
            print("Your Favourite Pillow cushions you from the hidden ditch trap.")
        else:
            print(
                "A hidden ditch covered with warm autumn leaves swallows you. You're trapped! Panicking, you dig your way out but lose time.")
            moves_left -= 3

        triggered_traps.append(current_room)

    elif current_room == "Magical Forest":
        if "Glowy Mushroom" in inventory:
            print("The Glowy Mushroom lights up your path revealing dense forest and thick mist swirling around you.")
        else:
            print(
                "You hop carefully into the Magical Forest but it's too dark. You stumble over a fallen tree and lose time.")
            moves_left -= 2

        triggered_traps.append(current_room)

    return moves_left, triggered_traps


#  Displays collapse warnings at specific move counts while also preventing duplicate warning messages
def check_collapse(moves_left, shown_warnings):
    if moves_left == 10 and 10 not in shown_warnings:
        print("\nThe tunnels shake harder. You need to hurry...")
        shown_warnings.append(10)

    if moves_left == 5 and 5 not in shown_warnings:
        print(
            "\nDirt falls from the ceiling, covering your fur. You hear parts of the burrow collapsing in the distance. Hurry...")
        shown_warnings.append(5)

    if moves_left == 1 and 1 not in shown_warnings:
        print("\nThe walls crack around you. One more delay could be fatal...")
        shown_warnings.append(1)


#  Checks if the player has run out of moves and displays losing message
def check_moves(moves_left):
    if moves_left <= 0:
        print("\nThe final rumble echoes behind you.")
        print("Your burrow collapses before you can unlock the Ancient Oak Door.")
        print(r"""
        (\_/)   💤
        ( x.x)     YOU LOSE!
        / > \>

        Your cozy home and banana dreams are lost...
        """)
        return True
    else:
        return False


#  Displays item and direction hints for the current room
def show_hints(current_room, hint_type):
    room = rooms[current_room]
    print("\n---------------------------------- HINT ------------------------------------")

    if hint_type == "direction":
        print("Direction hint:", room["hint_direction"])
    elif hint_type == "item":
        print("Item hint:", room["hint_item"])
    else:
        print("Type 'hint direction' or 'hint item'.")


#  Controls the main game loop, player input, game progression and replay system.
def main_game():
    #  Resets game data at the start of each new playthrough
    global rooms
    rooms = create_rooms()
    inventory = []
    collected_rooms = []
    triggered_traps = []
    shown_warnings = []
    current_room = "Cozy Burrow"
    moves_left = 20
    game_over = False

    while True:
        player_name = input("\nEnter your name: ").strip()

        if player_name == "":
            print("\nName cannot be empty!")
        elif player_name.isdigit():
            print("\nName cannot only contain numbers!")
        elif not any(char.isalpha() for char in player_name):
            print("\nName must contain at least one letter!")
        else:
            break

    print(r"""  
                           |)_|)
                         („• ֊ •„) 
                        |￣￣U  U￣￣￣￣￣￣￣￣￣|
                        |   THE BUNNY AND      |
                        |   THE GOLDEN KEY !   |
                        |                      |
                         ￣￣￣￣￣￣￣￣￣￣￣￣￣￣  """)

    print(f"\nWelcome, {player_name}!")

    print("\nSomewhere beyond the Ancient Oak Door, sweet banana trees are waiting.")
    print("To reach them, you must find the Golden Key before your burrow collapses.")
    print(f"You have {moves_left} moves before your home is lost forever.")
    print("Make sure to gather useful tools that will aid your journey.")

    print("\nYou wake from your afternoon nap and stretch your tiredness away in your cozy burrow.")
    print("A deep rumble shakes the tunnels. Your quest begins.")

    print("\n--------------------------------- COMMANDS ---------------------------------")
    print("Move:                    go north / go east / go south / go west")
    print("Shortcut:                n / e / s / w")
    print("Add To Woven Basket:     take (item you want to take)  e.g. 'take key' ")
    print("Others:                  inventory / look / hint direction / hint item / quit")

    while True:
        ready = input("\nAre you ready to begin (yes/no)? ").strip().lower()

        if ready == "yes":
            break
        elif ready == "no":
            print(f"\nTake your time {player_name}. The bananas are not going anywhere... probably.")
        else:
            print("\nPlease enter yes or no.")

    show_room(current_room, moves_left, inventory)

    while game_over == False:
        show_status(current_room, moves_left, inventory)

        command = input("\nWhat would you like to do? ").strip().lower()

        if command == "n":
            command = "go north"
        elif command == "e":
            command = "go east"
        elif command == "s":
            command = "go south"
        elif command == "w":
            command = "go west"

        if command.startswith("go"):
            parts = command.split()

            if len(parts) < 2:
                print("\nOops! I don't understand that command, type a direction like 'go north'.")

            else:
                direction = parts[1]
                old_room = current_room

                current_room, moves_left = move_player(current_room, direction, moves_left)

                if current_room != old_room:
                    moves_left, triggered_traps = check_trap(current_room, inventory, moves_left, triggered_traps)

                    if moves_left > 0:
                        show_room(current_room, moves_left, inventory)

        elif command.startswith("take"):
            requested_item = command[4:].strip()
            inventory, moves_left, game_over, collected_rooms = take_item(current_room, inventory, moves_left, collected_rooms, requested_item)
        elif command == "inventory":
            show_inventory(inventory)
        elif command == "look":
            show_room(current_room, moves_left, inventory)
        elif command.startswith("hint"):
            hint_type = command[4:].strip()
            show_hints(current_room, hint_type)
        elif command == "quit":
            print(
                "\nYour eyes slowly close, exhaustion wrapping its comforting arms around you as your body slowly gives in to rest. You abandon the quest with dreams of abundant banana trees surrounding you. Goodbye...")
            game_over = True
        else:
            print("\nOops! I don't understand that command. Try 'go north', 'hint direction' or 'take (item)'.")

        if game_over == False:
            check_collapse(moves_left, shown_warnings)
            if check_moves(moves_left):
                game_over = True


play_again = "yes"
while play_again == "yes":
    main_game()
    play_again = input("\nWould you like to play again (yes or no)? ").lower().strip()

    while play_again != "yes" and play_again != "no":
        play_again = input("Enter yes or no. ").lower().strip()

if play_again == "no":
    print("\nThank you for playing. Goodbye!")
