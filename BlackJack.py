import random

# Conpnets of cards
SUITS = ['♢','♣','♡','♠']
RANKS = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
FACE = ['J','Q','K']


class Shoe:
    def __init__(self, num_packs=6):
        self.cards = []
        for _ in range(num_packs):
            for suit in SUITS:
                for rank in RANKS:
                    self.cards.append(f"{rank}{suit}")
        random.shuffle(self.cards)

    def draw(self, n): # draw n cards from the deck and remove them
        drawn = []    
        for _ in range(n):
            if not self.cards:
                break # no more cards
            drawn.append(self.cards.pop())
        return drawn
    
    def size(self):
        return len(self.cards)

        
class Player:
    def __init__(self, name, shoe):
        self.name = name
        self.hand = []
        self.shoe = shoe
        

    def p_draw(self, n):
        if self.shoe:
            self.hand.extend(self.shoe.draw(n))
        else:
            raise ValueError("Player has no shoe assigned to draw from")
        
    def p_score(self):
        return Score(self.hand).get_score()
        
#TODO: Make a score function that will get the hand score of the hand and the bankers score 
class Score:
    def __init__(self,hand):
        self.hand = hand

    def get_score(self):
        total = 0
        aces = 0 

        for card in self.hand: # Strips cards of Suits
            value = card[:-1]

            if value == "A": #Count Aces separately 
                aces += 1
            elif value in FACE:
                total += 10
            else:
                total += int(value)
        
        # Aces can be 11 as long as the hand dosnt bust, 1 if it will
        for _ in range(aces):
            if total + 11 <= 21:
                total += 11
            else:
                total += 1

        return total

class Dealer:
    def __init__(self, name, shoe):
        self.name = name
        self.hand = []
        self.shoe = shoe

    def dealer_draw(self, n):
        if self.shoe:
            self.hand.extend(self.shoe.draw(n))
        else:
            raise ValueError("Player has no shoe assigned to draw from")
        
    def dealer_score(self):
        return Score(self.hand).get_score()
        


if __name__ == "__main__":
    shoe = Shoe()
    print("Shoe size:", shoe.size())
    # print("Draw 4:", shoe.draw(4))
    # print("Deck after draw:", shoe.size())
   
    player = Player(input("Whats your name?: "), shoe)
    dealer = Dealer("Dealer", shoe)
    player.p_draw(2)
    dealer.dealer_draw(2)
    
    print(f"{player.name}'s hand: {player.hand}")
    print(f"{dealer.name}'s hand: [??, {dealer.hand[0]}]")
    print(shoe.size())
    
    print(player.p_score())
    print(dealer.dealer_score())
  

