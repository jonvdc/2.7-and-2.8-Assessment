statistics = ["Strength", "Speed", "Stealth", "Cunning"]
card_storage = {}

# Enter name of the card
card_name = input("Please enter your chosen Monster Card name: ").title()

# Loop for the
# card statistics to make code shorter
for stat in statistics:

    # Asks user to enter a card stat
    number = int(input(f"What is {card_name}'s level of {stat}? \n"
                       f"Enter as a number between 1 and 25 \n"))

    # Adds stats to dictionary
    card_storage[stat] = number

# Output results
print("The new monster card is: \n\n"
      f"{card_name}: \n"
      f"{card_storage}")
