"""Add card v1.0
The add component of the assessment
Uses generic and boring print statements
[ Be glad I'm not lazy enough to put this into
the final program ;) ]
By J.VDC"""

# Asking user to enter monster card name
card_name = input("Please enter the name of the card: ").title()

# Asks user to enter the card statistics consisting of
# Strength, Speed, Stealth, Cunning
strength = int(input(f"Please add {card_name}'s strength statistic\n"
                     f"Enter as a number between 1 and 25: "))

speed = int(input(f"\nPlease add {card_name}'s speed statistic \n"
                  f"Enter as a number between 1 and 25: "))

stealth = int(input(f"\nPlease add {card_name}'s stealth statistic \n"
                    f"Enter as a number between 1 and 25: "))

cunning = int(input(f"\nPlease add {card_name}'s cunning statistic \n"
                    f"Enter as a number between 1 and 25: \n"))

# Prints result to user
print("\nHere is your card: \n\n"
      f"{card_name}: \n\n"
      f"Strength: {strength} \n"
      f"Speed: {speed} \n"
      f"Stealth: {stealth} \n"
      f"Cunning: {cunning}")
