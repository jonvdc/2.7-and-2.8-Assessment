"""Add card v1.2
Makes sure the user enters a
number in the correct range so none of those
pesky errors come up
-J.VDC"""

import easygui

statistics = ["Strength", "Speed", "Stealth", "Cunning"]

card_storage = {}

# Enter name of the card
card_name = easygui.enterbox("Enter your Monster's name: ")

# Loop for the
# card statistics to make code shorter
for stat in statistics:

    # Another loop so the user is
    # forced to input an integer
    while True:

        try:
            # Asks user to enter a card stat
            number = int(easygui.enterbox(f"What is {card_name}'s level of {stat}? \n"
                                          f"Enter as a number between 1 and 25 \n",
                                          f"{stat}"))

            # If entered stat is bigger than 25
            # return an error message and
            # a chance to try again
            if number > 25:
                easygui.msgbox("The number you entered is too big. "
                               "Please try again",
                               "Error: Number too big")

            # The same but if lower than 1
            elif number < 1:
                easygui.msgbox("The number you entered is too small. "
                               "Please try again",
                               "Error: Number too small")

            # If user enters stat correctly
            else:
                break

        # If user tries entering
        # a letter instead
        except ValueError:
            easygui.msgbox("No letters please. Please enter a number")

    # Adds stats to dictionary
    card_storage[stat] = number

# Final product
easygui.msgbox("Your new card is: \n\n"
               f"{card_name} \n\n"
               f"{card_storage}")
