from random import *
class Card:
    def __init__(self,suit,value,points):
        self.name=value+" of "+suit
        self.points=points
        self.inDeck=True #boolean that shows if card is in deck
    def drawCard(self):
        self.inDeck=False
    def insertCard(self):
        self.inDeck=True
    
class Deck:
    deck=[] #empty deck, to be initialized
    values=["Ace","King","Queen","Jack","10","9","8","7","6","5","4","3","2"]
    points=[4,3,2,1,0,0,0,0,0,0,0,0,0]
    suits=["Spades","Hearts","Diamonds","Clubs"]
    """Deck class: each card has name and index.
        spades: 0-12
        hearts: 13-25
        diamonds: 26-38
        clubs: 39-51
    """
    def __init__(self):
        for suit in Deck.suits:
            for x in range(len(Deck.values)):
                Deck.deck.append(Card(suit, Deck.values[x],Deck.points[x]))
    def print(self):
        for x in range(52):
            if Deck.deck[x].inDeck:
                print(Deck.deck[x].printCard())
    
    def draw(self):
        pos=randint(0,51)
        while(not(Deck.deck[pos].inDeck)): #loops until selects non-empty card
              pos=randint(0,51)
        Deck.deck[pos].drawCard()
        return (Deck.deck[pos]) #returns Card object

    def reset(self):
        for card in Deck.deck:
            card.insertCard()
        print("Deck Reshuffled")

    def is_empty(self):
        for card in Deck.deck:
            if card.inDeck:
                return False
        return True

class Hand: #a hand is 13 cards, 1 player
    hand=[]
    def __init__(self,myD):
        for x in range(13):
            Hand.hand.append(myD.draw())
    def sort(self):
        Hand.hand=sorted(Hand.hand, key=lambda card: card[1])
    def displayHand(self):
        for card in Hand.hand:
            print(card)

class Table:
    def __init__(self,myD):
        pass
        
myD=Deck()
#myD.print()
for x in range(52):
    myD.draw()
print(myD.is_empty())
myD.reset()
"""hand=Hand(myD)
hand.displayHand()
hand.sort()
hand.displayHand()
"""
