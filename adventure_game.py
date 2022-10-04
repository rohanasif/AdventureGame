import time
import random

monster = random.choice(["fairy", "troll", "ogre"])


def print_pause(msg):
    print(msg)
    time.sleep(1)


def repeat():
    play_again = input("Would you like to play again?"
                       " Enter 'y' for yes or 'n' for no: ")
    if play_again.lower() == "y":
        initial_setup()
        main_loop()

    elif play_again.lower() == "n":
        print("Thank you for playing")

    else:
        print("Please enter either 'y' or 'n'")


def initial_setup():
    print_pause("You find yourself standing in an open field,"
                " filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a wicked " + monster +
                " is somewhere around here, and has been"
                " terrifying the nearby village.")
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")


def main_loop():
    while True:
        print_pause("What would you like to do?")
        print_pause("(Please enter 1 or 2).")
        choice = input()
        if choice == "1":
            print("The " + monster + " kills you! You lose!")
            repeat()
            break
        elif choice == "2":
            print("You win")
            repeat()
            break


initial_setup()
main_loop()
