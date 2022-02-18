import random
#This is the protoype of the war game to run on console. - JS

# Below, I started the deck. I figured the best way to program it would be a list of tuples, with the key being the card designation
# and the value being the value of the card (1-13 per suit) - JS

officialDeck = [
    # Hearts
    ('A-H', 1), ('2-H', 2), ('3-H', 3), ('4-H', 4), ('5-H', 5), ('6-H', 6), ('7-H', 7), ('8-H', 8), ('9-H', 9), ('10-H', 10), ('J-H', 11), 
    ('Q-H', 12), ('K-H', 13),
    # Spades
    ('A-S', 1), ('2-S', 2), ('3-S', 3), ('4-S', 4), ('5-S', 5), ('6-S', 6), ('7-S', 7), ('8-S', 8), ('9-S', 9), ('10-S', 10), ('J-S', 11), 
    ('Q-S', 12), ('K-S', 13),
    # Diamonds
    ('A-D', 1), ('2-D', 2), ('3-D', 3), ('4-D', 4), ('5-D', 5), ('6-D', 6), ('7-D', 7), ('8-D', 8), ('9-D', 9), ('10-D', 10), ('J-D', 11), 
    ('Q-D', 12), ('K-D', 13),
    # Clubs
    ('A-C', 1), ('2-C', 2), ('3-C', 3), ('4-C', 4), ('5-C', 5), ('6-C', 6), ('7-C', 7), ('8-C', 8), ('9-C', 9), ('10-C', 10), ('J-C', 11), 
    ('Q-C', 12), ('K-C', 13)
]


# Part 1 - Shuffle
# Below is the function to shuffle the deck, and then cut the deck and deal to each player

def shuffle(deck):
    funcDeck = [] # empty deck that will be used to rebuild the official deck
    for i in deck:
        funcDeck.append(i) # this rebuilds the offical deck. 
    shuffledDeck = [] # empty deck that will be filled through this funciton
    while len(funcDeck) != 0: # While cards are still in the original deck
        cardsRemaining = len(funcDeck) # Number of cards still in the original deck
        chosenCard = random.randint(0, cardsRemaining - 1) # Choose a random card in original deck
        shuffledDeck.append(funcDeck.pop(chosenCard)) #puts the chosen card in the shuffled deck
    return shuffledDeck

def splitDeck(shuffledDeck): #This splits the shuffled deck in 2 and returns 2 decks for 2 players
    half = len(shuffledDeck)//2
    return shuffledDeck[:half], shuffledDeck[half:]

shuffledDeck = shuffle(officialDeck) #shuffles the original deck
p1Deck, p2Deck = splitDeck(shuffledDeck)


def compareFun(p1Card, p2Card, currentPot, p1Deck, p2Deck):
    print("P1 Card: " + str(p1Card))
    print("P2 Card: " + str(p2Card))
    if p1Card[1] > p2Card[1]: #if player one has the bigger card, he gets the pot
        winner = "p1"
    elif p1Card[1] < p2Card[1]: #if player two has the bigger card, he gets the pot
        winner = "p2"        
    elif p1Card[1] == p2Card[1]: # If the cards have the samve value, draw 4 more cards and the 4th card drawn will be checked
            try:
                for i in range(0, 3):
                    currentPot.append(p1Deck.pop(0))
                    currentPot.append(p2Deck.pop(0))
                    p1Card2 = p1Deck.pop(0)
                    p2Card2 = p2Deck.pop(0)
                    currentPot.extend((p1Card2, p2Card2))
                    winner, currentPot = compareFun(p1Card2, p2Card2, currentPot, p1Deck, p2Deck)
            except:
                print("running exception")
                if p1Card[1] > p2Card[1]:  # if player one has the bigger card, he gets the pot
                    winner = "p1"
                elif p1Card[1] < p2Card[1]:  # if player two has the bigger card, he gets the pot
                    winner = "p2"
    return winner, currentPot
            


def playGame(p1, p2):
    count = 0
    if count > 100000:
        print("This game has ended in a draw!!!")
        return
    p1len = len(p1)
    p2len = len(p2)
    while p1len != 0 or p2len != 0: # established the endgame rules for War, where one player needs the whole deck to win
        if len(p2) == 0:
            print("Player 1 has won!")
            break
        elif len(p1) == 0:
            print("Player 2 has won!")
            break
        count += 1
        print("Player 1 Deck Size: " + str(len(p1)))
        print("Player 2 Deck Size: " + str(len(p2)))
        print(count)
        currentPot = [] # Sets up an empty list at the beginning of each round for the cards that will be used in that round
        p1Card = p1.pop(0) #These two variables grab the "top" cards from each deck
        p2Card = p2.pop(0)
        currentPot.extend((p1Card, p2Card))
        winner, currentPot = compareFun(p1Card, p2Card, currentPot, p1, p2)
        if winner == "p1":
            for i in range(0, len(currentPot)):
               p1.append(currentPot[i])
        else:
            for i in range(0, len(currentPot)):
               p2.append(currentPot[i])
        p1len = len(p1)
        p2len = len(p2)

playGame(p1Deck, p2Deck)