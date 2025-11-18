import random

# Conpnets of cards
SUITS = ['♢','♣','♡','♠']
RANKS = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

deck = [] # Blank Deck

G_score = 0 # round score


#TODO:Make this in to a class and have a function that returns the deck size
def make_deck():
    # Combines Suits and Ranks to make a list of complete cards and then shuffle a 6 pack deck.
    for _ in range(6):
        for suit in SUITS:
            for rank in RANKS:
                deck.append((f"{rank}{suit}"))
    random.shuffle(deck)    

class DrawCards:
    def __init__(self,deck):
        self.deck = deck
    
    def draw(self, n): # draw n cards from the deck and remove them
        drawn = []    
        for _ in range(n):
            if not self.deck:
                break # no more cards
            drawn.append(self.deck.pop())
        return drawn
        

class Player():
    def __init__(self,name):
        self.name = name
        self.hand = []

    def draw_from_shoe(self, shoe, n):
        self.hand.extend(shoe.draw(n))


if __name__ == "__main__":
    make_deck()
    shoe = DrawCards(deck)

    print("Deck:", len(deck))
    print("Draw 4:", shoe.draw(4))
    print(len(deck))

    player = Player(input("Whats your name?: "))
    player.draw_from_shoe(shoe, 2)
    print(f"{player}'s hand: {player.hand}")
    print(len(deck))

