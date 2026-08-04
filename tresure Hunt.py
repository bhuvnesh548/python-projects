#tresure Hunt 
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 


direction = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right"\n')

if direction.lower() == "right":
  print("You were attacked and eaten by a wild dingo. Game Over.")
elif direction.lower() == "left":
  lake = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n')
  if lake.lower() == "swim":
    print("You get captivated by the songs of sirens and lured down to the lake and drown. Game Over.")
  else:
    doors = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
    if doors.lower() == "blue":
      print("You enter a room of of puppies. You are immobilized by cuteness. You win their love, but lose the treasure. Game Over.")
    elif doors.lower() == "yellow":
      print("You found the treasure! You Win!")
    elif doors.lower() == "red":
      print("You enter a room full of doors to other rooms and cannot escape. Game Over.")
    else: 
      print("You chose a door that doesn't exist. Game Over.")
