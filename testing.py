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
        #Test for comparision of cards

# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()