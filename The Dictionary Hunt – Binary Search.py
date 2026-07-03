"""You are in a library with a physical English dictionary. You need to find the word "Ephemeral". Instead of starting from the first page, you open the dictionary in the middle. If the middle page starts with the letter M, you know that E comes before M, so you search only the left half of the dictionary. You repeat this process until you find the word."""
# Dictionary Hunt

dict = {
    "A": "Apple",
    "B": "Ball",
    "C": "Cat",
    "D": "Dog",
    "E": "Ephemeral",
    "F": "Fish",
    "G": "Goat"
}

key = input("Enter the letter to search: ")

if key in dict:
    print("Word Found:", dict[key])
else:
    print("Word not found.")
