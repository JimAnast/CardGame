import random
class CardGame():
    def __init__(self):
       deck = []
       for self.suit in range(4):
           for self.value in range(2, 15):
               new_tuple = tuple((self.value, self.suit))
               deck.append(new_tuple)
       self.deck = deck


    def card_name(card_tuple):
        value = card_tuple[0]
        suit = card_tuple[1]


        if value == 11:
            rank = "Jack"
        elif value == 12:
            rank = "Queen"
        elif value == 13:
            rank = "King"
        elif value == 14:
            rank = "Ace"

        if suit == 0:
            name_suit = "Hearts"
        elif suit == 1:
            name_suit = "Diamonds"
        elif suit == 2:
            name_suit = "Clubs"
        else:
            name_suit = "Spades"

        if value in range(11, 15):
            return (str(rank) + " of " + str(name_suit))
        else:
            return (str(value) + " of " + str(name_suit))

    def shuffle(self):
        random.shuffle(self.deck)
        return self.deck

    def draw(self):
        if len(self.deck) ==0:
            return None
        card_drawn = self.deck.pop()
        return card_drawn


if __name__ == '__main__':
    print("Player A vs Player B:")
    deck1= CardGame()
    deck2= CardGame()
    CardGame.shuffle(deck1)
    CardGame.shuffle(deck2)
    i=0
    countA=0
    countB=0
    while i <52:
        card1 = CardGame.draw(deck1)
        card2 = CardGame.draw(deck2)
        if card1[0] > card2[0]:
            countA += 1
        elif card1[0] < card2[0]:
            countB += 1

        print(CardGame.card_name(card1), "*", CardGame.card_name(card2), "==> Points:", str(countA), "*",
              str(countB))
        i +=1
    print("Player A has ", countA, " points, Player B has ", countB, " points.")
    if countA > countB:
        print("Winner: Player A")
    elif countA < countB:
        print("Winner: Player B")
    else:
        print("The game is a draw.")






