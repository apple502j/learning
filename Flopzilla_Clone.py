import random

Values= "A23456789TJQK"
Suits= "shcd"

class Card:
    def __init__(self, Value, Suit):         
        self.Value = Value                    #(string)Value of card, Can Be A,2,3,4,5,6,7,8,9,T,J,Q,K
        self.Suit = Suit                      #(string) Suit of card, Can Be h, d, c or s
        
class Player:
    def __init__(self, Position, isDealer, holeCard):
        self.Position = Position             #(integer)Position of the player wrt Dealer
        self.isDealer = isDealer             #(boolean) True if player is dealer
        self.holeCard = holeCard             #(Card) Player's holding
        
class Board:
    def __init__(self, run):                 #A list of 5 cards from Deck
        self.run = run
                           
Deck = []                                    #list of objects of class Card
for i in Values:                             #Initializing cards to Deck
    for j in Suits:
        Deck.append(Card(i, j))
            
num_players = int(input("Enter nuber of players (2-10): "))

if num_players in range(2,11):               #Dealing?
    iters = 0
    while iters < num_players:
        index = random.randint(0, 52)
        print(Deck[index].Value + Deck[index].Suit)
        iters += 1
else:
    print("Number of players either less than 2 or greater than 10!!")
