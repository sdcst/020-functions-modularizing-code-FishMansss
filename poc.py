import random

def showCard(rank):
    print("                            ")
    print("  __________ ")
    print(f" |        {rank} |               ")
    print(" |          |               ")
    print(" |          |               ")
    print(" |    1     |               ")
    print(" |          |               ")
    print(f" |{rank}         |               ")
    print(" |__________|                         ")

for i in range(20):
    card1 = random.randint(1,13)
    if card1 == 1:
        card1 = "A"
    elif card1 == 10:
        card1 = "T"
    
    showCard(card1)
