# Import the necessary modules.
import os
import json

# Define the constants.
ROOM_TYPES = ["Single", "Double", "Suite"]

# Create the database.
database = {}

# Load the data from the file.
if os.path.exists("hotel.json"):
    with open("hotel.json", "r") as file:
        database = json.load(file)

# Get the user input.
room_type = input("What type of room do you need? ")
number_of_rooms = int(input("How many rooms do you need? "))

# Check if the room type is available.
if room_type not in ROOM_TYPES:
    print("Sorry, we don't have that type of room.")
    exit()

# Check if there are enough rooms available.
if number_of_rooms > database[room_type]:
    print("Sorry, we don't have enough rooms of that type.")
    exit()

# Update the database.
database[room_type] -= number_of_rooms

# Save the data to the file.
with open("hotel.json", "w") as file:
    json.dump(database, file)

# Print the confirmation message.
print("Your reservation has been confirmed.")
