import random

# Constants
feet_in_mile = 5280
meters_in_kilometer = 1000

# List of Beatles members
beatles = ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Star"]

# Function to get file extension
def get_file_ext(filename):
    return filename[filename.index(".") + 1:]

# Function to roll a dice
def roll_dice(num):
    return random.randint(1, num)
# Function to convert miles to feet
def miles_to_feet(miles):
    return miles * feet_in_mile
# Function to convert kilometers to meters
def km_to_meters(km):
    return km * meters_in_kilometer
