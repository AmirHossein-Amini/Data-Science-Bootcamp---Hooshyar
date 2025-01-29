# Variables
actions_list = ["add", "edit", "delete", "show", "help", "finalize"]


command_args = {
        "add": 3,
        "edit": 4,
        "delete": 2,
        "show": 1,
        "help": 1,
        "finalize": 1
    }


shopping_cart = []

# Function Definitions
def validate_command(command):
    """Validate the command and number of arguments."""
    act = command[0]
    if act in actions_list:
        if len(command) != command_args[act]:
            print("Invalid number of arguments for {0} command. \
Please type 'help' for more information.".format(act))
            return False
        else:
            return True
    else:
         print("Unknown command! Please enter again: ")
         return False


def validate_int(arg):
    """Validate if the argument can be cast to an integer."""
    try:
        user_input = int(arg)
        if user_input <= 0:
            print("Please enter a positive integer.")
            return False
        else:
            return user_input
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return False


def show_help():
    """Shows a guideline of program"""
    print("Commands")
    print("1. Add item: add <item> <count>")
    print("2. Edit item: edit <item number> <new item> <count>")
    print("3. Delete item: delete <item number>")
    print("4. Show list: show")
    print("5. Show help: help")
    print("6. Finalize list: finalize")


def add(item, count):
    """Add an item to the shopping list"""
    item_entry = {
        "item": item,
        "count": count
    }
    shopping_cart.append(item_entry)
    print("{1} unit(s) of {0} added to the shopping list"\
          .format(item, count))


def edit(number, item, count):
    """Edit an item from shopping list"""
    try:
        if len(shopping_cart) < 1:
            print("Nothing in shopping list to edit.\
Add an item first!")
        else:
            index = number - 1
            shopping_cart[index] = {"item": item, "count": count}
            print("Item {0} has been edited to {1} with {2} units"\
                .format(number, item, count))
    except IndexError:
        print("The shopping list has only {0} number of items"\
              .format(len(shopping_cart)))


def delete(number):
    """Delete an item from the list"""
    try:
        if len(shopping_cart) < 1:
                print("Nothing in shopping list to delete. \
Add an item first!")
        else:
            index = number -1
            shopping_cart.pop(index)
            print("Item {0} has been deleted from shopping list"\
                  .format(number))
    except IndexError:
        print("The shopping list has only {0} number of items"\
              .format(len(shopping_cart)))


def show_list():
    """Show all items in the list"""
    if len(shopping_cart) < 1:
            print("Shopping list is empty.")
    else:
        for (index, cart) in enumerate(shopping_cart):
            print("{0}. {1} - {2} units".\
                format((index+1), cart["item"], cart["count"]))


def finalize():
    """Finalize the shopping cart, there can be no changes afterward"""
    print("Shopping list finalized. No further changes can be made.")
    actions_list.pop(0)
    actions_list.pop(0)
    actions_list.pop(0)
    actions_list.pop(2)


# Main Program Logic 
def main():
    print("Welcome to the Shopping List Program!\n")
    show_help()
    # main program logic loop
    while True:
        command = input("\n>: ").lower().split()
        act = command[0]
        if not validate_command(command):
            continue
        if act == "help":
            show_help()
        elif act == "add":
            if not validate_int(command[2]):
                continue
            else:
                arg1 = command[1].title()
                arg2 = validate_int(command[2])
                add(arg1, arg2)
        elif act == "edit":
            if not validate_int(command[1]) or not validate_int(command[3]):
                continue
            else:
                arg1 = validate_int(command[1])
                arg2 = command[2].title()
                arg3 = validate_int(command[3])
                edit(arg1, arg2, arg3)
        elif act == "delete":
            if not validate_int(command[1]):
                continue
            else:
                arg1 = validate_int(command[1])
                delete(arg1)
        elif act == "show":
            show_list()
        elif act == "finalize":
            finalize()


# Entry Point Check
if __name__ == "__main__":
    main()