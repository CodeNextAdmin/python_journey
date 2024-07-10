# Journey Challenge:
# Create your own survival story by being creative in your story telling and create ways of surviving your simulation!
# Input at least 10 key-value pairs in your new dictionary and have more than 2 tool to help you survive!
# Make sure the conditions match with the bad and good decision making behind the template!

# BONUS: Create a functions within the program to make it more efficient and clean!


# dictionary for the tools
options = {
  "headphones": "A",
  "lighter": "B",
  "flashlight": "C",
  "batteries": "D"
}

print("Welcome to the journey simulator to choose options to win and escape! \n")
print("------------------------------------------------------------------------")
print("You're currently stuck in the woods and you need to find a way out.") 
print("It is raining heavy and you need to find a way to get out of the woods.") 
print("You see a house in the distance and you. What tool will you choose to get out of the woods? \n")


values = options.values()

# Get all key-value pairs
items = options.items()

# Print each key-value pair
for key, value in items:
  print(f"{value}: {key}")


print("Choose your option")
userChoices = input("Insert the letters you want to choose with no spaces but with a comma between each letter: ")
userList = list(userChoices.split(','))

# create a variable that holds on to the correct amount of tools needed to win the game
correctItems = 2

# each condition where if the right items aren't chosen, you describe the reason why you need it
if "C" not in userList:
  print("You need batteries to start up something\n")
if "D" not in userList:
  print("You need a tool to see at night\n")

# condition where you will the right choices were there BUT there are other options that were chosen
if "C" and "D" in userList:
  print("You have chosen the right tools to get out of the woods BUT too many items! \n")
  # nested condition where you will win the game if you have the right tools 
  if len(userList) == correctItems:
    print("You have chosen the right tools to get out of the woods! \n")
    print("======= YOU WON =======")
else:
  print("You have chosen the wrong tools to get out of the woods, try again! \n")
