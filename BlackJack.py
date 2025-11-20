import random

# Conpnets of cards
SUITS = ['♢','♣','♡','♠']
RANKS = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

deck = [] # Blank Deck

G_score = 0 # round score


class Deck:
    def __init__(self, num_packs=6):
        self.cards = []
        for _ in range(num_packs):
            for suit in SUITS:
                for rank in RANKS:
                    self.cards.append(f"{rank}{suit}")
        random.shuffle(self.cards)

    def size(self):
        return len(self.cards)


class DrawCards:
    def __init__(self,deck):
        self.deck = deck
    
    def draw(self, n): # draw n cards from the deck and remove them
        drawn = []    
        for _ in range(n):
            if not self.deck:
                break # no more cards
            drawn.append(self.deck.cards.pop())
        return drawn
        
#TODO: add a def to add players to the game and there names 
class Player():
    def __init__(self, name, shoe):
        self.name = name
        self.hand = []
        self.shoe = shoe

    def p_draw(self, n):
        if self.shoe:
            self.hand.extend(self.shoe.draw(n))
        else:
            raise ValueError("Player has no shoe assigned to draw from")


if __name__ == "__main__":
    deck = Deck()
    shoe = DrawCards(deck)
    print("Deck size:", deck.size())
    print("Draw 4:", shoe.draw(4))
    print("Deck after draw:", deck.size())
   
    player = Player(input("Whats your name?: "), shoe)
    player.p_draw(5)
    print(f"{player.name}'s hand: {player.hand}")
    print(deck.size())

