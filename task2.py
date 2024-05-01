"""
Task 2:
Create a program to play a number guessing game
There should be a function:
title()
displays instructions and how to play

game()
plays the games
"""
import random
import os 
import math
import time
os.system('cls')
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

def game():
    total = 0
    
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
##cards
    print("\n\n         hit '1' or stand '2'")
    choice = input()
    if choice == 1:
        card1 = random.randint(1,13)
        if card1 == 1:
            print("Ace")
        if card1 == 2:
            print("2")
        if card1 == 3:
            print("3")
        if card1 == 4:
            print("4")
        if card1 == 5:
            print("5")
        if card1 == 6:
            print("6")
        if card1 == 7:
            print("7")
        if card1 == 8:
            print("8")
        if card1 == 9:
            print("9")
        if card1 == 10:
            print("10")
        if card1 == 11:
            print("Jack")
        if card1 == 12:
            print("Queen")
        if card1 == 13:
            print("King")
    print("                            ")
    print("  __________ ")
    print(f" |       {card1}  |               ")
    print(" |          |               ")
    print(" |          |               ")
    print(f" |    {card1}      |               ")
    print(" |          |               ")
    print(f" |{card1}          |               ")
    print(" |__________|                         ")
    input()
game()