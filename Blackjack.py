import random
from IPython.display import clear_output

class Dealer():
    def __init__(self):
        self.hand = []
        self.points = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'Jack':10 ,'Queen':10,'King':10,'Ace':11}
    def ask(self):
        decision = input("\nHit or Stand? 'h' or 's' ").upper()
        if decision == 'H':
            return 'Hit'
        else:
            return 'Stand'
    
    def show_card(self):
        print("\nDealer's card:", self.hand[1])
    def show_cards(self):
        print("\nDealer's Hand:", self.hand)

    def check(self):
        suma=0
        for i in self.hand:
            suma += self.points[i]
        return suma
        
    
class Deck():
    def __init__(self):
        self.karty = {'2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9','10':'10','11':'Jack','12':'Queen','13':'King','14':'Ace'}  
    
    def pick_card(self):
        index = str(random.choice([2,3,4,5,6,7,8,9,10,11,12,13,14]))
        card = self.karty[index]
        return card
    
    
class Player():
    
    def __init__(self):
        
        self.funds = int(input('How much funds? '))
        self.bet = 0
        self.hand = []
        self.points = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'Jack':10 ,'Queen':10,'King':10,'Ace':11}
        
    def show_cards(self):
        print("\nPlayer's hand:", self.hand)
        
    def check(self):
        suma=0
        for i in self.hand:
            suma += self.points[i]
        return suma
            
          
    
while True:
    
    print('Welcome to Blackjack')
    player = Player()
    deck = Deck()
    dealer = Dealer()

    while True:
        clear_output()
        player.hand=[]
        dealer.hand=[]
        print('You have', player.funds,'$ avaiable')
        player.bet = int(input('How much You bet?'))
        player.hand.append(deck.pick_card())
        player.hand.append(deck.pick_card())
        dealer.hand.append(deck.pick_card())
        dealer.hand.append(deck.pick_card())
        dealer.show_card()
        player.show_cards()
        show_hand = False
    # ask to hit another card or stand
        if dealer.ask() == 'Hit':
            player.hand.append(deck.pick_card())
            dealer.show_card()
            player.show_cards()
            if player.check() < 21 and dealer.ask() == 'Hit':
                player.hand.append(deck.pick_card())
                dealer.show_card()
                player.show_cards()
            if dealer.check() <= 16 and player.check() < 21:
                dealer.hand.append(deck.pick_card())
                print("\nDealer's hand after picking another card:")
                dealer.show_cards()
                show_hand = True
        
        if player.check() > 21:
            print("\nYOU LOST!    Sum of your points exceeded 21\n\n YOU LOSE:", player.bet,'$\n')
            player.funds -= player.bet
        elif dealer.check() > 21:
            if show_hand == False:
                dealer.show_cards()
            print('\nYOU WON!    Dealer had more than 21 points\n\n YOU GAIN:', player.bet, '$\n')
            player.funds += player.bet
        elif player.check() > dealer.check():
            if show_hand == False:
                dealer.show_cards()
            print('\nYOU WON!    You had more points\n\n YOU GAIN:', player.bet, '$\n')
            player.funds += player.bet
        elif player.check() <= dealer.check():
            if show_hand == False:
                dealer.show_cards()
            print("\nYOU LOST!    Dealer had more points\n\nYOU LOSE:", player.bet,'$\n')
            player.funds -= player.bet
            
            
        if input("Want to play again? 'y' or 'n' ") == 'y':
            continue
        else:
            print('You end game with',player.funds,'$')
            break
              
    break




