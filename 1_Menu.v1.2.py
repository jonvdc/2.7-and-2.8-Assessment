# Welcomes the user
# Gives the user options

import easygui


def menu():
    easygui.msgbox("Welcome to the Monster Card Storage Facility", "Welcome")

    options = easygui.buttonbox("Choose an option from below: ", "Menu",
                             choices=["Add Cards", "Search for Cards",
                                      "Delete Cards", "Print All Cards",
                                      "Exit"])

    return options


# Main routine
choice = menu()
easygui.msgbox(f"{choice} action succeeded")
