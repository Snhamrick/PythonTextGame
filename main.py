#Seth Hamrick

def show_intro():   #function call for menu prompt
    print('Welcome to Race for Potion')
    print('Your friend James has been poisoned by a Wicked Witch,', end=' ')
    print('you have travelled to the Witch Manor in hopes of saving James.')
    print('Collect 9 items to brew potion antidote and save James or suffer the wraith of the Witch')
    print()
    print('Movement Commands: \"Move North\", \"Move South\", \"Move East\", \"Move West\"')
    print('To add item to inventory: \"Collect\"')
    print()


def show_status(location, inventory): #function call to show current status
    print('Current Room:', location)
    print('Inventory:', inventory)

def collect_item(inventory, item): #function call to collect item from room, not duplicating item in inventory
    if item not in inventory:
        inventory.append(item)
        return inventory


def main(): #begin main loop of game
    rooms = {
    'Eery Entrance': {'North': 'Library', 'East': 'Tea Room', 'West': 'Basement'},
    'Basement' : {'East': 'Eery Entrance', 'item': 'Clay'},
    'Tea Room' : {'North': 'Cats Room', 'West': 'Eery Entrance', 'item': 'Honey'},
    'Cats Room': {'North': 'Bedroom', 'West': 'Library', 'South': 'Tea Room', 'item': 'Black Cat Hair'},
    'Library' : {'North': 'Witch Den', 'East': 'Cats Room', 'West': 'Great Dining Room', 'South': 'Eery Entrance', 'item': 'Incantation'},
    'Great Dining Room': {'North': 'Kitchen', 'East': 'Library', 'item': 'Orange Peel'},
    'Kitchen' : {'North': 'Broom Closet', 'East': 'Witch Den', 'South': 'Great Dining Room', 'item': 'Ginseng Root'},
    'Witch Den' : {'East': 'Bedroom', 'West': 'Kitchen', 'South': 'Library', 'item': 'Wicked Witch'},
    'Bedroom' : {'North': 'Potion Room', 'West': 'Witch Den', 'South': 'Cats Room', 'item': 'Eucalyptus'},
    'Potion Room' : {'West': 'Broom Closet', 'South': 'Bedroom', 'item' : 'Werewolf fur'},
    'Broom Closet' : {'East': 'Potion Room', 'South': 'Kitchen', 'item' : 'Cobweb'}, }

    location = 'Eery Entrance' #set start room as Eery Entrance
    inventory = []
    show_intro()


    while location != 'Witch Den':
        if len(inventory) == 9: #add exit if player collects all items
            print('Congratulations, you have collected all ingredients, now you can brew the potion to save James!!!')
            print('You rush home to brew the antidote for James!')
            break
        show_status(location, inventory)
        action = input('What would you like to do?').strip().split() #turn input into a list
        print()
        if action[0] == 'Collect':
            if 'item' in rooms[location].keys():
                item = rooms[location]['item']
                collect_item(inventory, item)
                print('You have added {} to the inventory.'.format(item))
                print()
            else:
                print('There is no item in this room.')
                print()
        elif action[0] == 'Move':
            if action[1] in rooms[location].keys():
                location = rooms[location][action[1]]
                if 'item' in rooms[location].keys():
                    print('You see the', rooms[location]['item'], 'in the', location)
                    print()
            else:
                print('There is no door in that direction.')
                print()
        else:
            print('Invalid command, please enter valid command. Make sure all words are capitalized!')
            print()
    if location == 'Witch Den':
        print('You have encountered the Wicked Witch!!!!')
        print('Tehehehehehe, now you are trapped here forever!!!')
        print('The witch has trapped you, you were not able to brew the potion antidote for James.....')
        print('Thanks for playing, feel free to try again!')




main()
