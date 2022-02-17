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

for i in p1Deck:
    print("P1 - " + i[0])

print(len(p1Deck))
print(len(p2Deck))