import unittest
import ConsoleWarTest as cwt

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

class TextprocTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_split(self):
        shuffledDeck = cwt.shuffle(officialDeck)  # shuffles the original deck
        p1Deck, p2Deck = cwt.splitDeck(shuffledDeck)
        if len(p1Deck) != 26 & len(p2Deck) != 26:
            raise ValueError("The deck splitting did not work!")
        else:
            print("The Deck splitting has worked!")

    def test_checks(self):
        for i in range (0, 1000):
            try:
                shuffledDeck = cwt.shuffle(officialDeck)  # shuffles the original deck
                p1Deck, p2Deck = cwt.splitDeck(shuffledDeck)
                cwt.playGame(p1Deck, p2Deck)
            except:
                raise ValueError("The counter does not work")
        print("The checks do not exceed 1000")

    def test_comparison(self):
        # Initializing variables for test
        p1Card, p2Card, currentPot, p1Deck, p2Deck = [0,0], [0,0], [], [], []
        
        # iterating through the different values of cards Ace(1) - King(13)
        for i in range(1,14):
            # checks to see if number is odd or even and sets the p1 or p2 card to that value
            # This allows the check to test both case: p1Card is greater and p2Card is greater
            if i%2==1:
                p1Card[1] = i
            else:
                p2Card[1] = i
            
            # running the compareFun function with the set values for p1Card and p2Card, plus the empty place holding variables
            result = cwt.compareFun(p1Card, p2Card, currentPot, p1Deck, p2Deck)
            
            # Asserts that the result is p1 when p1Card is infact greater or the opposite when p2Card is greater
            if p1Card[1] > p2Card[1]:
                self.assertEqual(result[0], 'p1')
            else:
                self.assertEqual(result[0], 'p2')

    
# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()
