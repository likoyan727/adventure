import random

#welcome------------------------------

print("Welcome.")

#choose character and opponent--------

user_name = raw_input("What is your name? ")

#initial direction--------------------

direction1 = raw_input("Which direction do you want to go, " + user_name + "? N, S, E, or W? ")

while((direction1 != "N") and (direction1 != "n") and (direction1 != "S") and (direction1 != "s") and (direction1 != "E") and (direction1 != "e") and (direction1 != "W") and (direction1 != "w")):
   direction1 = raw_input("Enter a valid input. N, S, E, or W? ")

#variables for the anagrams

word1 = "inevitable"
temp_word1 = word1
anagram1 = ""
word2 = "golden"
temp_word2 = word2
anagram2 = ""
word3 = "unknown"
temp_word3 = word3
anagram3 = ""
word4 = "independence"
temp_word4 = word4
anagram4 = ""

#if direction N is chosen
if((direction1 == "N") or (direction1 == "n")):
    #scrambles word1 into an anagram
    h = 0
    while h < len(word1):
        temp_index = random.randrange(0,len(temp_word1))
        anagram1 += temp_word1[temp_index]
        temp_word1 = temp_word1[0:temp_index] + temp_word1[temp_index+1:]
        h += 1
    answer1 = raw_input("Guess the correct word from this anagram: " + anagram1 + " ")

    if(answer1 == word1):
        print("Good job!")
    else:
        print("Sorry, that's the wrong answer.")

#if direction S is chosen
elif((direction1 == "S") or (direction1 == "s")):
    #scrambles word2 into an anagram
    h = 0
    while h < len(word2):
        temp_index = random.randrange(0,len(temp_word2))
        anagram2 += temp_word2[temp_index]
        temp_word2 = temp_word2[0:temp_index] + temp_word2[temp_index+1:]
        h += 1
    answer2 = raw_input("Guess the correct word from this anagram: " + anagram2 + " ")

    if(answer2 == word2):
        print("Good job!")
    else:
        print("Sorry, that's the wrong answer.")

#if direction E is chosen
elif((direction1 == "E") or (direction1 == "e")):
    #scrambles word3 into an anagram
    h = 0
    while h < len(word3):
        temp_index = random.randrange(0,len(temp_word3))
        anagram3 += temp_word3[temp_index]
        temp_word3 = temp_word3[0:temp_index] + temp_word3[temp_index+1:]
        h += 1
    answer3 = raw_input("Guess the correct word from this anagram: " + anagram3 + " ")

    if(answer3 == word3):
        print("Good job!")
    else:
        print("Sorry, that's the wrong answer.")

#if direction W is chosen
elif((direction1 == "W") or (direction1 == "w")):
    #scrambles word4 into an anagram
    h = 0
    while h < len(word4):
        temp_index = random.randrange(0,len(temp_word4))
        anagram4 += temp_word4[temp_index]
        temp_word4 = temp_word4[0:temp_index] + temp_word4[temp_index+1:]
        h += 1
    answer4 = raw_input("Guess the correct word from this anagram: " + anagram4 + " ")

    if(answer4 == word4):
        print("Good job!")
    else:
        print("Sorry, that's the wrong answer.")

#second direction---------------------

direction2 = raw_input("Which direction do you want to go for your second step, " + user_name + "? N, S, E, or W? ")

while((direction2 != "N") and (direction2 != "n") and (direction2 != "S") and (direction2  != "s") and (direction2 != "E") and (direction2 != "e") and (direction2 != "W") and (direction2 != "w")):
   direction2 = raw_input("Enter a valid input. N, S, E, or W? ")

#checks if player died

if(direction2 == "N" or direction2 == "n"):
    death = False
else:
    death = True

#---puzzles---------------------------

if(death == False):
    print("Now you get to solve a puzzle")
#puzzle1 GUESSING GAME, if first direction was N
    if((direction1 == "N") or (direction1 == "n")):
        seven_dwarves = ["grumpy", "dopey", "doc", "happy", "bashful", "sneezy", "sleepy"]
        dwarf_input1 = raw_input("Name one of the seven dwarves: ")
        for x in seven_dwarves:
            if(dwarf_input1 == x):
                print(x)
                guess1 = True
                seven_dwarves.remove(x)
                break
            else:
                guess1 = False
        dwarf_input2 = raw_input("Name another dwarf: ")
        for y in seven_dwarves:
            if(dwarf_input2 == y):
                print(y)
                guess2 = True
                break
            else:
                guess2 = False
        if(guess1 == True and guess2 == True):
            print("You got them right!")
        else:
            print("Sorry, you got them wrong.")
#puzzle2 DICE, if first direction was S
    elif((direction1) == "S" or (direction1 == "s")):
        dice_roll = random.randrange(1,7)
        even_or_odd = raw_input("You rolled a die and got " + str(dice_roll) + ". Is this number even or odd? ")
        if(even_or_odd == "odd" and (dice_roll%2 != 0)) or (even_or_odd == "even" and (dice_roll%2 == 0)):
            print("You are smart!")
        else:
            print("Sorry, that's the wrong answer.")
#puzzle3 BACKWARDS, if first direction was E
    elif((direction1 == "E") or (direction1 == "e")):
        puzzle_word = "hornet"
        backwards_word = raw_input("Enter this word backwards: " + puzzle_word + " ")
        if(backwards_word == puzzle_word[::-1]):
            print("Good job!")
        else:
            print("The correct answer is actually " + puzzle_word[::-1])
#puzzle4 PRIME, if first direction was W
    else:
        prime = int(input("Enter a prime number: "))
        if(prime <= 1):
            print("That's incorrect.")
        else:
            is_prime = True
            i = 2
            while(i < prime):
                if(prime%i != 0):
                    is_prime = True
                else:
                    is_prime = False
                    break
                i += 1
            if(is_prime == True):
                print("That's correct!")
            else:
                print("That's incorrect.")
#end----------------------------------
    print("Congratulations, you made it out alive!")
else:
    print("Sorry, " + user_name + ", you died. Try again?")
