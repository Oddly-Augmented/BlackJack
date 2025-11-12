import random

SUITS = ['♢','♣','♡','♠']
RANKS = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
deck = []

# Combines Suits and Ranks to make a list of complete cards and then shuffle the deck.
def make_deck():
    for suit in SUITS:
        for rank in RANKS:
            deck.append((f"{rank}{suit}"))
    random.shuffle(deck)    

# Outputs one card from the deck and removes it so it can't be drawn again
def get_card():
    if not deck:
        print("Deck is empty")
        return None
    card = deck.pop()  
    print(card)
    return card


if __name__ == "__main__":
    print()
    make_deck()
    get_card()

    print(deck)
    print(len(deck))
