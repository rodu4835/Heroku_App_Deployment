// JavaScript version of the Console War Game.
// CU CSP

const officialDeck = [
    // Hearts
    ['A-H', 1], ['2-H', 2], ['3-H', 3], ['4-H', 4], ['5-H', 5], ['6-H', 6], ['7-H', 7], ['8-H', 8], ['9-H', 9], ['10-H', 10], ['J-H', 11], 
    ['Q-H', 12], ['K-H', 13],
    // Spades
    ['A-S', 1], ['2-S', 2], ['3-S', 3], ['4-S', 4], ['5-S', 5], ['6-S', 6], ['7-S', 7], ['8-S', 8], ['9-S', 9], ['10-S', 10], ['J-S', 11], 
    ['Q-S', 12], ['K-S', 13],
    // Diamonds
    ['A-D', 1], ['2-D', 2], ['3-D', 3], ['4-D', 4], ['5-D', 5], ['6-D', 6], ['7-D', 7], ['8-D', 8], ['9-D', 9], ['10-D', 10], ['J-D', 11], 
    ['Q-D', 12], ['K-D', 13],
    // Clubs
    ['A-C', 1], ['2-C', 2], ['3-C', 3], ['4-C', 4], ['5-C', 5], ['6-C', 6], ['7-C', 7], ['8-C', 8], ['9-C', 9], ['10-C', 10], ['J-C', 11], 
    ['Q-C', 12], ['K-C', 13]
];

//console.log(officialDeck [0] [0]);

function shuffleDeck(deck) {
    var funcDeck = deck;
    var shuffledDeck = [];
    while (funcDeck.length != 0) {
        var rand = Math.floor(Math.random() * funcDeck.length);
        shuffledDeck.push(funcDeck[rand]);
        funcDeck.splice(rand, 1);
    };
    return shuffledDeck
};

function splitDecks(deck) {
    const deckOne = deck;
    const deckTwo = deckOne.splice(26,26);
    return [deckOne, deckTwo];
};

const shuffDeck = shuffleDeck(officialDeck)
const sDecks = splitDecks(shuffDeck)
var playerOneDeck = sDecks[0]
var playerTwoDeck = sDecks[1]

for (i = 0; i < playerOneDeck.length; i++) {
    console.log(i + " - " +  playerOneDeck[i]);
    console.log(i + " - " + playerTwoDeck[i])
}
console.log(playerOneDeck.length);

