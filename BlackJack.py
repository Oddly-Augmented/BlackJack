import random
import json

# Compnets of cards
SUITS = ['♢','♣','♡','♠']
RANKS = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
FACE = ['J','Q','K']

class Colors:
     RESET = '\033[0m'
     RED = '\033[31m'
     GREEN = '\033[32m'

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
    
    def clear_p_hand(self):
        self.hand.clear()
        
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

        return int(total)
#TODO: Idd like to add a list of names for the Dealer like "Dealer {Random name}"
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
    
    def clear_d_hand(self):
        self.hand.clear()
        


class Stats:
#Make/generate a json file to hold and store stats like Win/Loss, games played, and ties. 
    def __init__(self, path = "BlackJack_Stats.json"):
        self.stats_file = path
        self.data = self.load_stats()
    def load_stats(self):
        try:
            with open(self.stats_file, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {"games_played": 0, "games_won": 0, "games_lost": 0, "games_tied": 0}
    
    def save_stats(self):
        with open(self.stats_file, "w") as f:
            json.dump(self.data, f)

    def record_win(self):
        self.data["games_played"] += 1
        self.data["games_won"] += 1
        self.save_stats()
    def record_loss(self):
        self.data["games_played"] += 1
        self.data["games_lost"] += 1
        self.save_stats()
    def record_tie(self):
        self.data["games_played"] += 1
        self.data["games_tied"] += 1
        self.save_stats()



#TODO: I dont know if I can get to this but it would be fun to implement a betting system for the game and win/lose condishions for it. Like get $1000 and win or $0 and you lose. 

if __name__ == "__main__":
    shoe = Shoe() ### Make the deck
    stats = Stats()
    print("Welcome to BlackJack simulator")
    
    player = Player(input("Whats your name?: ").strip(), shoe)
    dealer = Dealer("Dealer", shoe)

    # Game Loop
    while True:
        game_choice = input("Would you like to play (y/n) or see stats (s): ").strip().lower()
        if game_choice == "n":
            print("Thanks for playing!")
            break
        elif game_choice == "s":
            stats.load_stats()
            print(f"Games Played: {stats.data['games_played']}, Won: {stats.data['games_won']}, Lost: {stats.data['games_lost']}, Tied: {stats.data['games_tied']}")
        elif game_choice == "y":
            
            player.clear_p_hand()
            dealer.clear_d_hand()
            player.p_draw(2)
            dealer.dealer_draw(2)

            print(f"\n{player.name}'s Hand: {player.hand} Score: {player.p_score()}")
            print("\nDealer must stand on 17 and draw to 16")
            print(f"\n{dealer.name}'s Hand: [??, {dealer.hand[0]}]")

            while True: 
                # Game loop for player, hit or stand till 21 or bust.
                if player.p_score() > 21:
                    print("You Bust!")
                    break
                choice = input("\nHit or Stand: (h/s): ").strip().lower()
                if choice == "h":
                    player.p_draw(1)
                    print(f"\n{player.name}'s Hand: {player.hand} Score: {player.p_score()}")
                elif choice == "s":
                    break
                else:
                    print("\nPlease type 'h' or 's'.")

            # Dealer play "Dealer must stand on 17 and draw to 16"
            if player.p_score() <= 21:
                print(f"\n{dealer.name}'s \nHand: {dealer.hand} Score: {dealer.dealer_score()}")
                while dealer.dealer_score() <17:
                    dealer.dealer_draw(1)
                    print(f"\n{dealer.name}'s Hits \nHand: {dealer.hand} Score: {dealer.dealer_score()}")

            p_final = player.p_score()
            d_final = dealer.dealer_score()
            # Get final scores and who wins
            print(f"\nFinal Scores: \n{player.name}: {p_final}\n{dealer.name}: {d_final}")

            if p_final > 21:
                stats.record_loss()
                print(f"{Colors.RED}{player.name} busts {dealer.name} WINS!{Colors.RESET}")
            elif d_final > 21:
                stats.record_win()
                print(f"{Colors.GREEN}{dealer.name} busts {player.name} WINS!{Colors.RESET}")
            elif p_final > d_final:
                stats.record_win()
                print(f"{Colors.GREEN}{player.name} WINS!{Colors.RESET}")
            elif d_final > p_final:
                stats.record_loss()
                print(f"{Colors.RED}{dealer.name} WINS!{Colors.RESET}")
            else:
                stats.record_tie()
                print("Tie")
        else:
            print("Please type 'y' or 'n' or 's'.")
        

