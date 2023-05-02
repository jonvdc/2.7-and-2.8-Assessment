# Welcomes the user
# Gives the user options

import easygui

while True:

    easygui.msgbox("Welcome to this site", "Welcome")

    menu = easygui.buttonbox("Choose an option from below: ", "Menu",
                             choices=["Add Cards", "Search for Cards",
                                      "Delete Cards", "Print All Cards",
                                      "Exit"])

    if menu == "Add Cards":
        easygui.msgbox("Add Cards action succeeded")

    elif menu == "Search for Cards":
        easygui.msgbox("Change Search for Cards action succeeded")

    elif menu == "Delete Cards":
        easygui.msgbox("Delete Cards action succeeded")

    elif menu == "Print All Cards":
        easygui.msgbox("Print All Cards action succeeded")

    elif menu == "Exit":
        break
