"""
Task 2:
Create a program to play a number guessing game
There should be a function:
title()
displays instructions and how to play

game()
plays the games
"""
##imports
import random
import os 
import time
##setup
os.system('cls')


##shuffle animation
def shuffle():    
    os.system('cls')
    time.sleep(1)
    print("The Dealer shuffles the deck")
    time.sleep(1)
    os.system('cls')
    print("The Dealer shuffles the deck.")
    time.sleep(1)
    os.system('cls')
    print("The Dealer shuffles the deck..")
    time.sleep(1)
    os.system('cls')
    print("The Dealer shuffles the deck...")
    time.sleep(1)
    os.system('cls')
##title
def title():
    print("----------------------------BLACK JAX---------------------------------")
    print("--------------------------Press 'ENTER' to continue-------------------")
    input()
    os.system('cls')
    print("----------------------------BLACK JAX---------------------------------")
    time.sleep(1)
    print("your goal is to get as close as you can to 21 without going over it...")
    time.sleep(1)
    print("you can hit (grab another card) or stand (let the dealer play)")
    print("Dealer always cheques your pot and you pay a premium for betting...")
    print("--------------------------Press 'ENTER' to continue-------------------")
    input()
##drawing a card phase
def draw():
    global total
    total = 0
    while total < 22:
        
        print("\n\n         hit '1' or stand '2'")
        x = input()
        if x=="2":
               
            if total <21 and total >16:
                os.system('cls')
                print("Close enough..")  
                input()
            if total < 17:
                os.system('cls')
                print("probbably not Close enough..")  
                input()
        if x=="1":
            card = random.randint(1,13)
            if card == 11:
                card = "J"
            if card ==12:
                card = "Q"
            if card ==13:
                card = "K"
            print("                            ")
            print("  __________ ")
            print(f" |         {card}|               ")
            print(" |          |               ")
            print(" |          |               ")
            print(f" |    {card}     |               ")
            print(" |          |               ")
            print(f" |{card}         |               ")
            print(" |__________|                         ")
            if card == "J" or card == "Q" or card == "K":
                    card = 10
            total = total + card
            print(f"\n\n         Total:{total}")
            if total == 21:
                os.system('cls')
                print("black jax!!")
                input()
    else:
        os.system('cls')
        print("Bust")
        input()
        exit

#title()
#shuffle()
draw()

if total > 21:
     os.system('cls')
     print("prolly a loss")