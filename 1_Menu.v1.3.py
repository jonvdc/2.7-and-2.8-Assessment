import easygui


# Adding a new card function
def add():
    pass


# Searching the cards functions
def search():
    pass


# Delete a card functions
def delete():
    pass


# Printing all the cards function
def printing():
    pass


# Loop to end code on user input
while True:

    # Asking user what they want to do with the monster cards
    options = easygui.buttonbox("What would you like to do?: \n",
                                "Menu",
                                choices=["Add", "Search", "Delete", "Print", "Exit"])

    # Add card branch
    if options == "Add":
        add()

    # Search for cards branch
    elif options == "Search":
        search()

    # Delete card branch
    elif options == "Delete":
        delete()

    # Print all cards branch
    elif options == "Print":
        printing()

    # Exit for user
    elif options == "Exit":

        # Goodbye message
        easygui.msgbox("Thank you for using the Monster Card Storage Facility", "Exit")
        break
