import time


def print_pause(msg):
    print(msg)
    time.sleep(1)


print_pause("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
print_pause("Rumor has it that a wicked fairie is somewhere around here, and has been terrifying the nearby village.")
print_pause("Enter 1 to knock on the door of the house.")
print_pause("Enter 2 to peer into the cave.")


while True:
    choice = input("What would you like to do?")
    time.sleep(1)
    print("(Please enter 1 or 2).")
    if choice == "1":
        print("You face a monster who kills you instantly")
        break
    elif choice == "2":
        print("You live on")
        break
