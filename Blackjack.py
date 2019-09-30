import random
from IPython.display import clear_output

class Dealer():
    def __init__(self):
        self.hand = []
        self.punkty = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'Walet':10 ,'Dama':10,'Król':10,'As':11}
    def ask(self):
        decision = input("\nHit or Stand? 'h' or 's'").upper()
        if decision == 'H':
            return 'Hit'
        else:
            return 'Stand'
        
    def sum_point(self):
        pass
    
    def show_card(self):
        print('\nKarta Dilera:', self.hand[1])
        return f'Karta dilera: {self.hand[1:]}'
    def show_cards(self):
        print('\nKarty Dilera:', self.hand)

    
    def check(self):
        x=0
        suma=0
        for i in self.hand:
            suma += self.punkty[self.hand[x]]
            x+=1
        return suma
        
    
    
class Deck():
    def __init__(self):
        self.karty = {'2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9','10':'10','11':'Walet','12':'Dama','13':'Król','14':'As'}
        
    
    def pick_card(self):
        index = str(random.choice([2,3,4,5,6,7,8,9,10,11,12,13,14]))
        card = self.karty[index]
        return card
        pass
    
    
class Player():
    
    def __init__(self):
        
        self.funds = int(input('How much funds? '))
        self.bet = 0
        self.hand = []
        self.punkty = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'Walet':10 ,'Dama':10,'Król':10,'As':11}
        
    def show_cards(self):
        print('\nKarty gracza:', self.hand)
        return f'Karty gracza: {self.hand}'
    
    def check(self):
        x=0
        suma=0
        for i in self.hand:
            suma += self.punkty[self.hand[x]]
            x+=1
        return suma
            
        
        
        
    
while True:
    
#print('Welcome to Blackjack')
#name = input('What is your name? ')
#print('\n Welcome ', name, '! \n')
    Gambler = Player()
    Cards = Deck()
    Master = Dealer()

# kto najblizej 21 wygrywa
    while True:
        clear_output()
        Gambler.hand=[]
        Master.hand=[]
        print('You have', Gambler.funds,'$ avaiable')
    
        Gambler.bet = int(input('How much You bet?'))
        
    # zapytaj jaka sume ma gracz i ile stawia ############
    
    # wylosuj dwie karty dla gracza
        Gambler.hand.append(Cards.pick_card())
        Gambler.hand.append(Cards.pick_card())
    # wylosuj dwie karty dla dilera
        Master.hand.append(Cards.pick_card())
        Master.hand.append(Cards.pick_card())
    # pokaz DWIE karty gracza i JEDNA karte dilera
        Master.show_card()
        Gambler.show_cards()
    # ask to hit another card or stand
        if Master.ask() == 'Hit':
            Gambler.hand.append(Cards.pick_card())
            Gambler.show_cards()
            if Master.ask() == 'Hit':
                Gambler.hand.append(Cards.pick_card())
                Gambler.show_cards()
            Master.show_cards() # pokazuje druga karte (teraz widac obie)
            if Master.check() <= 16 and Gambler.check() < 21:
                Master.hand.append(Cards.pick_card())
                print('Karty Dilera po dobraniu:')
                Master.show_cards()
        
    # sprawdz czy przekroczono sume 21 pkt u gracza, jesli tak to koniec gry i przegrana gracza i odjac zalozone pieniadze
        if Gambler.check() > 21:
            print("\nPRZEGRANA!\nSuma przekroczyła 21 pkt\nTracisz", Gambler.bet,'$')
            Gambler.funds -= Gambler.bet
        elif Master.check() > 21:
            Master.show_cards()
            print('\nWYGRANA! Diler przekroczyl 21')
            Gambler.funds += Gambler.bet
        elif Gambler.check() > Master.check():
            Master.show_cards()
            print('\nWYGRANA!')
            Gambler.funds += Gambler.bet
        elif Gambler.check() <= Master.check():
            Master.show_cards()
            print("\nPRZEGRANA!\nDiler miał wiecej pkt\nTracisz", Gambler.bet,'$')
            Gambler.funds -= Gambler.bet
            
        
        #napisac ile  kasy w sumie teraz po wygranej lub przegranej
        
    # czy chce grac jeszcze raz
        if input("Want to play again? 'y' or 'n'") == 'y':
            continue
        else:
            print('You end game with',Gambler.funds,'$')
            break
              
    break
    
    # Sprawdz sume kart dilera, jesli 16 lub mniej to wylosowac kolejna karte
    # Sprawdz kto jest blizej 21 pkt i oglos wygranego
    # spytac czy chce grac jeszcze raz

