from random import *
class Deck:
    deck=[] #empty deck, to be initialized
    hasCard=[] #list of booleans, indicates if associated card is in deck
    values=["Ace","King","Queen","Jack","10","9","8","7","6","5","4","3","2"]
    suits=["Spades","Hearts","Diamonds","Clubs"]
    """Deck class: each card has name and index.
        spades: 0-12
        hearts: 13-25
        diamonds: 26-38
        clubs: 39-51
    """
    def __init__(self):
        for suit in Deck.suits:
            for value in Deck.values:
                card=value+" of "+suit
                Deck.deck.append(card)

        for x in range(52):
            Deck.hasCard.append(True)
            
    def print(self):
        for x in range(52):
            if Deck.hasCard[x]:
                print(Deck.deck[x])
                
    def in_deck(self,pos):
        return Deck.hasCard[pos]
    
    def draw(self):
        pos=randint(0,51)
        while(not(Deck.in_deck(self,pos))): #loops until selects non-empty card
              pos=randint(0,51)
        Deck.hasCard[pos]=False
        return (Deck.deck[pos],pos) #tuple that identifies index of card

    def reset(self):
        print("Reshuffling deck")
        for x in range(len(Deck.hasCard)):
            Deck.hasCard[x]=True
            
    def is_empty(self):
        for x in Deck.hasCard:
            if x==True:
                return False
        return True

class Hand:
    hand=[]
    def __init__(self,myD):
        for x in range(13):
            Hand.hand.append(myD.draw())
    def sort(self):
        Hand.hand=sorted(Hand.hand, key=lambda card: card[1])
    def displayHand(self):
        for card in Hand.hand:
            print(card)
        
myD=Deck()
#myD.print()
hand=Hand(myD)
hand.displayHand()
hand.sort()
hand.displayHand()

