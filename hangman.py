import random

WORDLIST = ["Fever", "Breathless", "Antisocial", "Virus", "Die", "Disease", "Contagious", "Cough", "Lockdown", "China", "Wuhan", "Global", "Circuit Breaker", "Lawrence Wong", "Masks"]
wordlist = [word.upper() for word in WORDLIST]

WORDLIST2 = ["Love Lockdown", "SICKO MODE",
             "Made in China", "Stayin Alive", 
            "Great Indoors", "I will survive"]
wordlist2 = [word.upper() for word in WORDLIST2]

print ("Welcome to Quarantine Hangwoman! \nGuess the correct phrase to avoid death. \n")

x=0
while x<6:
    choice = input ("Would you like to guess a quarantine word or song? \n")
    choice = str(choice.upper())
    if choice == "SONG":
        word = random.choice(wordlist2)
        break
    elif choice == "WORD":
        word = random.choice(wordlist)
        break
    elif choice == "Q":
        exit()

    else:
        print("\nPlease try again and type in either 'Word' or 'Song'\n\nIf you do not want to play the game, type 'Q'. You have " + str(5-x) + " tries remaining.")
        x+=1

if x ==6:
    exit()

def hangman(word):
    wrong = 0
    stages = [
              "________         ",
              "|        |       ",
              "|        -       ",
              "|       '0'      ",
              "|       /|\      ",
              "|        +       ",
              "|       / \      ",
              "|                ",
              ]
    remaining_letters = list (word)
    board = ["_"] * len(word)
    space = " "
        
    if space in remaining_letters:
        for i in range(len( remaining_letters)):
            if remaining_letters[i]== space:
                berry = remaining_letters.index (space)
                board [berry]= space
                remaining_letters[berry] = '$'
    

    win = False
   

    print ((" ".join(board)))
    
    while wrong < len(stages) - 1:

        print ("\n")
        msg = "Guess a letter or a word. Type Q to quit \n"
        char1 = input (msg)
        char = char1.upper()
                
        if char in remaining_letters and len(char)==1:
            print (char + " is correct. Keep going!")
            for i in range (len(remaining_letters)):
                            if remaining_letters[i]== char:
                                guess = remaining_letters.index(char)
                                board [guess]=char
                                remaining_letters[guess] = '$'
                                
        elif char == word and len(char) > 1:
            remaining_letters == "$"
            print ("You win! The word is:")
            print (word)
            win = True
            break

        elif char == "Q":
            quit()
            
        
        else:
            wrong +=1
            b=wrong+1
            print (char + " is incorrect")
            print ("You have " + str(8 - b) + " chances left")
        print ((" ".join(board)))
        e=wrong+1
        print("\n".join(stages[0:e]))
        
        if "_" not in board:
            print ("You win!")
            print (" ".join(board))
            win = True
            break
    if not win:
        print ("You died! The word was {}.".format(word))


hangman(word)

