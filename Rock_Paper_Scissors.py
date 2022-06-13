#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
while True:
    possible_options = ["R", "P", "S"]
    user_option = input("Pick an option as listed (R for 'rock', P for 'paper', S for 'scissors'): \n")
    print('*'*100)         
    
    computer_option = random.choice(possible_options)
    print(f"\nYou chose {user_option}, computer chose {computer_option}.\n")
    
    if user_option.upper() == computer_option:
        print(f"You picked same option as the computer. You both picked {user_option}. It's a tie!")
        print('*'*100) 
    elif user_option.upper() == "R" or "r":
        if computer_option == "S" or "s":                
            print("Rock (R) smashes scissors (S)! You win!")
            print('*'*100) 
        else:
            print("Paper covers rock! You lose.")
            print('*'*100) 
    elif user_option.upper() == "P" or "p":
        if computer_option == "R":            
            print("Paper (P) covers rock (R)! You win!")
            print('*'*100) 
        else:
            print("Scissors (S) cuts paper (P)! You lose.")
            print('*'*100) 
    elif user_option.upper() == "S" or "s":
        if computer_option == "P" or "p":
            print("Scissors (S) cuts paper (P)! You win!")
            print('*'*100) 
        else:
            print("Rock (R) smashes scissors (S)! You lose.") 
            print('*'*100)    
    
    play_again = input("You want to play again? (y/n): ")
    if play_again.lower() != "y":
        print("\nAwesome! Thanks for playing!" )
        print('*'*100)
        break


# In[ ]:




