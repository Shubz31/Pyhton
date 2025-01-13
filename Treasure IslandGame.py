print('''
      
      IIIIIIII  IIIIIII  IIIIIIIIII IIIIIIIIII IIIIIIII          IIIIIIIIII IIIIIIIII II             II       III      II IIIIIIII
      II        II    II II         II         II      II            II     II        II            II II     II II    II II      II
      II        IIIIIII  IIIIIIII   IIIIIIII   II       II           II     IIIIIIIII II           II   II    II  II   II II       II
      II   IIII II II    II         II         II       II           II            II II          IIIIIIIII   II   II  II II       II 
      II    II  II  II   II         II         II      II            II            II II         II       II  II    II II II      II 
      IIIIIIII  II   II  IIIIIIIIII IIIIIIIIII IIIIIIII          IIIIIIIIII IIIIIIIII IIIIIIIII II         II II     IIII IIIIIIII
''')
print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right". \n').lower()
if choice1 == "left":
    choice2 = input('You came to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim cross. \n').lower()
    if choice2 == "wait":
        choice3 = input("You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
        if choice3 == "blue":
            print("Congrajulations! You entered the correct door, you have won the game and the treasure is yours.")
        elif choice3 == "yellow":
            print("You entered the room of beasts and got killed. Game Over!")
        elif choice3 == "red":
            print("You entered a room full of fire. Game Over!")
    else:
        print("You were eaten by crocodiles. Game Over!")
else:
    print("You fell into a hole. Game Over!")
          