// JavaScript version of the Console War Game.
// CU CSP

function createOfficialDeck() {
    const theDECK = [
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
    return theDECK
}

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
    var deckOne = deck;
    var deckTwo = deckOne.splice(26,26);
    return [deckOne, deckTwo];
};

function compareFunc(p1Card, p2Card, currentPot, p1Deck, p2Deck) {
    var p1FuncCard = p1Card[0][1]
	assignCardInfo(p1Card, 'p1');
    var p2FuncCard = p2Card[0][1]
	assignCardInfo(p2Card, 'p2');
    if (p1FuncCard > p2FuncCard) {
        var winner = "p1";
        return [winner, currentPot, p1Deck, p2Deck];
    } else if (p1FuncCard < p2FuncCard) {
        var winner = "p2";
        return [winner, currentPot, p1Deck, p2Deck];
    } else if (p1FuncCard == p2FuncCard) {
        if (p1Deck.length >= 5 && p2Deck.length >= 5){
            for (i = 0; i < 3; i++) {
                currentPot.push(p1Deck.splice(0,1));
                currentPot.push(p2Deck.splice(0,1));
            }
            var test1 = p1Deck.length
            var test2 = p2Deck.length
            var p1Card2 = p1Deck.slice(0,1);
            var p2Card2 = p2Deck.slice(0,1);
            var test1 = p1Deck.length
            var test2 = p2Deck.length
            p1Deck = p1Deck.slice(1, (p1Deck.length));
            p2Deck = p2Deck.slice(1, (p2Deck.length));
            currentPot.push(p1Card2);
            currentPot.push(p2Card2);
            var result = compareFunc(p1Card2, p2Card2, currentPot, p1Deck, p2Deck);
        } else {
            if (p1Deck.length > p2Deck.length) {
                var shorterListLen = p2Deck.length;
            } else {
                var shorterListLen = p1Deck.length;
            }
            if (shorterListLen == 0) {
                if (p1Deck.length > p2Deck.length) {
                    var winner = "p1";
                    return [winner, currentPot, p1Deck, p2Deck]
                } else {
                    var winner = "p2";
                    return [winner, currentPot, p1Deck, p2Deck]
                }
            } else if (shorterListLen == 1) {
                var p1Card2 = p1Deck.slice(0,1);
                var p2Card2 = p2Deck.slice(0,1);
                currentPot.push(p1Card2);
                currentPot.push(p2Card2);
                p1Deck = p1Deck.slice(1, p1Deck.length)
                p2Deck = p2Deck.slice(1, p2Deck.length)
                var result = compareFunc(p1Card2, p2Card2, currentPot, p1Deck, p2Deck);
            } else {
                for (i = 0; i < shorterListLen-1; i++) {
                    currentPot.push(p1Deck.splice(0,1));
                    currentPot.push(p2Deck.splice(0,1));
                }
                var p1Card2 = p1Deck.slice(0,1);
                var p2Card2 = p2Deck.slice(0,1);
                currentPot.push(p1Card2);
                currentPot.push(p2Card2);
                var result = compareFunc(p1Card2, p2Card2, currentPot, p1Deck, p2Deck);
            }
        }
    }
    var winner = result[0];
    var currentPot = result[1];
    var finalP1Deck = result[2];
    var finalP2Deck = result[3];
    return [winner, currentPot, finalP1Deck, finalP2Deck];
}

function slowPlay(p1Deck, p2Deck){
		
}


function playGame(p1Deck, p2Deck) {
    var count = 0;

    //Skipping doing the player names for now. Am going to figure this part out w/ the html.
    //Same thing with the game speed section.
    while (p1Deck.length != 0 || p2Deck.length != 0) {
        if (count >= 5000) {
            console.log("This game has ended in a draw!!!");
            return;
        }
        if (p2Deck.length == 0) {
            console.log("Player One has won the game!!!");
            return;
        } else if (p1Deck.length == 0) {
            console.log("Player Two has won the game!!!");
            return;
        }
		
        count = count + 1;
		
        var currentPot = [];
        var p1Card = p1Deck.slice(0, 1);
        p1Deck = p1Deck.slice(1, (p1Deck.length));
		
        var p2Card = p2Deck.slice(0, 1);
        p2Deck = p2Deck.slice(1, (p2Deck.length));
		
        currentPot.push(p1Card);
        currentPot.push(p2Card);
		
        var result = compareFunc(p1Card, p2Card, currentPot, p1Deck, p2Deck);
        var winner = result[0];
		
        currentPot = result[1];
		
        p1Deck = result[2];
        p2Deck = result[3];
		
        //currentPot = shuffleDeck(currentPot);
        if (winner == "p1") {
            for (i = 0; i < currentPot.length; i++) {
                p1Deck.push(currentPot[i][0]);
            }
        } else {
            for (i = 0; i < currentPot.length; i++) {
                p2Deck.push(currentPot[i][0]);
            }
        }
    }
}

function setupGame() {
	var officialDeck = createOfficialDeck();
	var shuffDeck = shuffleDeck(officialDeck);
	var sDecks = splitDecks(shuffDeck);
	var playerOneDeck = sDecks[0];	
	var playerTwoDeck = sDecks[1];
	assignDeckImageLocation(playerOneDeck);
	assignDeckImageLocation(playerTwoDeck);
	playGame(playerOneDeck, playerTwoDeck);
}

// FRONT END FUNCTIONS

// Gives card name and image to player hand div container
function assignCardInfo(card, id){
	document.getElementById(id + 'Hand').style.visibility = 'visible';
	document.getElementById(id + 'CurrentCard').src=assignCardImageLocation(card);
	document.getElementById(id + 'CardName').innerHTML = assignCardImageName(card);
}

// Gives card image file location
function assignCardImageLocation(card){
	var cardName = card[0][0];
	var cardImageLocation = './static/images/' + cardName + '.jpg';
	return cardImageLocation;
}

// Gives card image name		
function assignCardImageName(card){
	var cardName = card[0][0];
	var cardValue = card[0][1];
	var suit = cardName[cardName.length - 1];
	if (suit == 'C'){
		suit = 'Clubs';
	} else if (suit == 'D'){
		suit = 'Diamonds';
	} else if (suit == 'H'){
		suit = 'Hearts';
	} else if (suit == 'S'){
		suit = 'Spades';
	} else {
		suit = 'Error: No card suit detected.';
	}
	
	if ((cardValue > 1) && (cardValue < 11)){
		cardValue = cardValue.toString();
	} else if (cardValue == 1){
		cardValue = 'Ace';
	} else if (cardValue == 11){
		cardValue = 'Jack';
	} else if (cardValue == 12){
		cardValue = 'Queen';
	} else if (cardValue == 13){
		cardValue = 'King';
	} else {
		cardValue = 'Error: No card value detected.';
	}
	var imageName = cardValue + ' of ' + suit;
	return imageName;
}

// Gives deck image file location -- yet to implement
function assignDeckImageLocation(deck){
	var deckSize = Object.keys(deck).length;
	var filePath = './static/images/';
	if (deckSize == 0) {
		filePath = filePath + 'emptyDeck.jpg';
	} else if ((deckSize >= 1) && (deckSize <= 9)){
		filePath = filePath + 'deck1-9.jpg';
	} else if ((deckSize >= 10) && (deckSize <= 18)){
		filePath = filePath + 'deck10-18.jpg';
	} else if ((deckSize >= 19) && (deckSize <= 27)){
		filePath = filePath + 'deck19-27.jpg';
	} else if ((deckSize >= 28) && (deckSize <= 36)){
		filePath = filePath + 'deck28-36.jpg';
	} else if ((deckSize >= 37) && (deckSize <= 45)){
		filePath = filePath + 'deck37-45.jpg';
	} else {
		filePath = filePath + 'deck46-54.jpg';
	}
	return filePath	
}

// Chages display of game control buttons
function alterPlayButtons(){
	document.getElementById('playButton').style.visibility = 'hidden';
	document.getElementById('nextButton').style.visibility = 'visible';
	document.getElementById('fastForwardButton').style.visibility = 'visible';
}


document.getElementById('p1DeckImage').src='./static/images/deck46-54.jpg';
document.getElementById('p2DeckImage').src='./static/images/deck46-54.jpg';


//function createPlayerNames() {
//	console.log(document.getElementById('playerNameTextBox').value);
//}


document.querySelector('#restartGame')
	.addEventListener('click', function(){
	window.location=('index.html');
	document.getElementById('p1Hand').style.visibility = 'hidden';
	document.getElementById('p2Hand').style.visibility = 'hidden';
});
document.querySelector('#gitSource')
	.addEventListener('click', function(){
	window.open('https://github.com/rodu4835/CSPB_3308_Team_3');
});
document.querySelector('#about')
	.addEventListener('click', function(){
	window.location=('devInfo.html');
});

document.querySelector('#playButton')
	.addEventListener('click', function(){
	alterPlayButtons();
	setupGame();
});

//document.querySelector('#playerNameTextBox')
//	.addEventListener('keyup', function(){
//	createPlayerNames();
//});
	










