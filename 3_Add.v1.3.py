"""Function tiiiiiiime
I hate using them but they're necessary
-J.VDC"""

import easygui


# Function for joinning dictionary's
def joinning(dic):
    message = ""

    # Joinning the dictionary inputted
    for key, value in dic.items():
        message = f"{key}:\n"

        # Formatting dictionary inside dictionary
        for key2, value2 in value.items():
            message += f"- {key2}: {value2} \n"

    return message


# Function for adding a new Monster Card
def add():

    # Variable setting
    attributes = ["Strength", "Speed", "Stealth", "Cunning"]
    ability_level = {}
    new_card = {}

    # Asking user to enter monster card name with character checker
    card_name = ("Please enter the card name")

    # Loop for the 4 attributes
    for item in attributes:
        # Asking user to enter how much strength card has
        number = easygui.integerbox(f"What is {card_name}'s level of {item}? \n"
                                    f"(Number between 1 and 25) \n",
                                    f"{item}", upperbound=25,
                                    lowerbound=1)

        # Adding items and number to as the ability
        ability_level[item] = number

    # Adding ability's and monster card name to a new dictionary
    new_card[card_name] = ability_level

    # Joinning code for monster cards dictionary
    new_card_formatted = joinning(new_card)

    # Output results and asking if correct results
    answer = easygui.buttonbox("The new Monster Card is: \n\n"
                               f"{new_card_formatted} \n\n"
                               f"Is this new Monster Card correct?",
                               choices=["Yes", "No"])

    # User enters yes
    if answer == "Yes":

        easygui.msgbox("Great! This New Card was added", "New Card Added")
        monster_cards.update(new_card)

    # User enters no
    elif answer == "No":
        easygui.msgbox("So sorry. Lets make some changes!",
                       "New Card incorrect")


# All monster cards
monster_cards = {}

# Calling on add new card function
add()

# Printing card for testing
print(monster_cards)
