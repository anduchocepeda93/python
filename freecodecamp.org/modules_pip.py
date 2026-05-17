import useful_tools

# Example usage of the functions from useful_tools
dice = int(input("Enter the number of sides on the dice: "))
print(f"Rolling a {dice}-sided dice: {useful_tools.roll_dice(dice)}")

mls = int(input("Enter miles:"))
print(f"{mls} miles in feet:" f"{useful_tools.miles_to_feet(mls)}")

km = int(input("Enter kilometers:"))
print(f"{km} kilometers in meters:" f"{useful_tools.km_to_meters(km)}")

print(useful_tools.beatles)
