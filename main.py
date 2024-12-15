# Display a background story for the character.
import os
#User inventory //  Need to append more items as they are purchased // Sell back items?
inventory_items = ["Wire Shark", "Reaver", "Aircrack-ng"]

#Loop through players inventory, display items on the screen
def inventory():
    num_list = 0
    for items in inventory_items:
        num_list +=1
        print(f"{num_list}.{items}")
        



def filler():
    pass
def filler():
    pass

os.system("cls")

print('''
In the bustling sprawl of Neon Haven, a city of towering skyscrapers and neon-lit alleyways, 
you grew up in the shadows of technology. Your father, a disgraced programmer framed for a cybercrime
he didn’t commit, left behind only an outdated laptop and a thirst for justice in your veins. You look
to avenge you father and family name.
''')

input(print("Press Any Key to Continue"))
os.system("cls")
# Main Player Menu

print('''
#####################
#  Main Menu        |
# 1. Inventory      |
# 2. Online Shop    |
# 3. Contracts      |
# 4. Exit           |
#####################
''')
choice = input(print("Please Choose an option: "))

if choice == "1":
    pass
elif choice == "2":
    pass
elif choice == "3":
    pass
elif choice == "4":
    pass

os.system("cls")

# Main Player Menu

print('''
#####################
#  Main Menu        |
# 1. Inventory      |
# 2. Online Shop    |
# 3. Contracts      |
# 4. Exit           |
#####################
''')
choice = input(print("Please Choose an option: "))

if choice == "1":
    pass
elif choice == "2":
    pass
elif choice == "3":
    pass
elif choice == "4":
    pass
os.system("cls")

# Create a menu for the user to see their current hacks, money, hardware
print(f'''
#####################
#  Inventory        |
# 1. Hacks          |
# 2. Hardware       |
# 3. Money          |
# 4. Exit           |
#####################
''')
choice = input(print("Please Choose an option: "))

if choice == "1":
    pass
elif choice == "2":
    pass
elif choice == "3":
    pass
elif choice == "4":
    pass
os.system("cls")



# Create a shopping menu for the player to purchase items and upgrades for the player
print(
    '''
##################################
#  Hacks R US!                   |
# 1. Wifi Hacks                  |
# 2. Network Hacks               |
# 3. System Hacks                |
# 4. Exit                        |
##################################

''')
choice = input(print("Please Choose an option: "))

if choice == "1":
    pass
elif choice == "2":
    pass
elif choice == "3":
    pass
elif choice == "4":
    pass

inventory()