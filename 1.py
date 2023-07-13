print (" 🎰🎰 LET'S PLAY HANGMAN 🎰🎰 ")

import random

words_list = [ "apple" , "banana" , "kiwi" , "pineapple" , "watermelone" , "orange" , "peach" , "blueberry" , "strawberry" , "pear" , "cherry" ]

word = random.choice ( words_list )

right_chars = []
wrong_chars = []
mistakes = 0

while mistakes < 6 :
    correct = 0

    for i in range ( len ( word )) :
        if word [i] in right_chars :
            print ( word[i], end = " " )
            correct += 1
        else :
            print ( "_", end = " " )

    if correct == len ( word ) :
        break

    user_guess = input (" Please enter your guess : ")

    if len ( user_guess ) == 1 :
        if user_guess.lower () in word :
            right_chars.append ( user_guess )
            print (" ✔ good guess ✔ ")
        
        else :
            wrong_chars.append ( user_guess )
            mistakes += 1
            print (" ❌ try again ❌ ")
    
    else :
        print (" 😒 don't cheat, enter only one charecter 😒 ")
    
    print (" right charecters are : ", right_chars)
    print (" wrong charecters are : ", wrong_chars)
    print (" number of mistakes : ", mistakes)

if correct == len ( word ) : 
    print (" 🎉 YOU WIN 🎉 ")

elif mistakes == 6 :
    print (" 💀 GAME OVER 💀 ")
    print (" The word was : ", word)