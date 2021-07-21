# CardGame
CardGame where the winner is the player that draws the card with the highest value.

The cardGame class includes the following methods:

--The constructor method, which is responsible for the creation and filling of a list of 52 elements, which are themselves tuples of 2 integers. This list of tuples contains the characteristics of each of the 52 cards. For each of them, we store separately an integer indicating the value (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, the last 4 values being those Jack, Queen, King and Ace), and another integer indicating the suit of the card (i.e. 0,1,2,3 for Hearts, Diamonds, Clubs and Spades). In such a list, the element (11,2) therefore designates the jack of clubs, and the completed list will look like: [(2, 0), (3.0), (3.0), (4 , 0), ..... (12.3), (13.3), (14.3)]

--The card_name() method which returns, in the form of a string, the identity of any card for which it has been given the descriptor tuple as an argument. For example, the instruction: print game.card_name ((14, 3)) should cause the display of: Ace of spades

--The shuffling method () which shuffles the cards. This method is therefore used to shuffle the elements of the list containing the cards, regardless of the number.

--The draw() method which does the following: When this method is invoked, a card is removed from the game. The tuple containing its value and color is returned to the calling program. We always take the first card of the list. If this method is invoked when there are no cards left in the list, then the special object None is returned to the calling program.


After creating the cardGame class with all the above methods, we want to try if our program works, so we play the following game:

We define two players A and B. We instantiate two sets of cards (one for each player) and we shuffle them. Then, using a loop, we draw a card from each of the two decks 52 times and we compare their values. If the first of the two has the higher value, we add a point to player A. If the opposite situation arises, we add a point to player B. If the two values are equal, we have a draw (we do not add any points to any player). At the end of the loop, we compare the counts of A and B to determine the winner.


Example:

Player A vs Player B:

3 of Clubs * 6 of Hearts ==> Points : 0 * 1

2 of Spades * 3 of Spades ==> Points : 0 * 2

ace of Diamond * 7 of Clubs ==> Points : 1 * 2

…

king of Hearts * 4 of Diamond ==> Points : 24 * 27

ace of Clubs * 10 of Spades ==> Points : 25 * 27

Player A has 25 points, Player B has 27.

Winner : Player B
