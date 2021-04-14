#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck():
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """

    deck = []
    half_one =[]
    half_two = []
    def __init__(self, suite, ranks):
        self.suite = suite
        self.ranks = ranks
        print("Deck initialized!")

    def create_deck(self):
        for s in self.suite:
            for r in self.ranks:
                self.deck.append(s+r)
        print("Deck created!")
        # print(self.deck)

    def shuffle(self):
        shuffle(self.deck)
        print("Deck has been shuffled!")

    def split(self):
        self.half_one = self.deck[:26]
        self.half_two = self.deck[26:]
        print("Deck has been splitted:")
        print("Deck 1: " + str(self.half_one))
        print("Deck 2: " + str(self.half_two))

    def show(self):
        print(self.deck)
         

class Hand():
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''

    def __init__(self, cards):
        self.cards = cards

    def add(self, card):
        self.cards.append(card)

    def remove(self, card):
        self.cards.remove(card)

class Player(Hand):
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def check(self):
        return len(self.hand.cards)

    def play(self, index):
        card_played = self.hand.cards[index]
        card_played_stripped = card_played[1:]
        if card_played_stripped == "J":
            card_played_stripped = 11
        elif card_played_stripped == "Q":
            card_played_stripped = 12
        elif card_played_stripped == "K":
            card_played_stripped = 13
        elif card_played_stripped == "A":
            card_played_stripped = 14
        else:
            card_played_stripped = int(card_played_stripped)
        return card_played_stripped, card_played

######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

deck = Deck(SUITE,RANKS)
deck.create_deck()
deck.shuffle()

deck.split()

hand1 = Hand(deck.half_one)
hand2 = Hand(deck.half_two)

tom = Player("Tom", hand1)
michal = Player("Michal", hand2)

def game(player1, player2):
    try:
        card_drawn_tom = tom.play(0)
        card_drawn_michal = michal.play(0)
        print(card_drawn_tom)
        print(card_drawn_michal)     
    except IndexError:
        print("Someone is out of cards!")
        if tom.check() > michal.check():
            print("And it is Michal! Tom WON!")
            return False  
        else:
            print("And it is Tom! Michal WON!")
            return False  

    if card_drawn_tom[0] > card_drawn_michal[0]:
        print(f"Tom has drawn {card_drawn_tom[1]} which is bigger than {card_drawn_michal[1]} and therefore he won this round!")
        tom.hand.add(card_drawn_michal[1])
        michal.hand.remove(card_drawn_michal[1])
        tom.hand.remove(card_drawn_tom[1])
        tom.hand.add(card_drawn_tom[1])

        if tom.check() == 0:
            print("No cards left, Michal won!")
            return False
    elif card_drawn_tom[0] < card_drawn_michal[0]:
        print(f"Michal has drawn {card_drawn_michal[1]} which is bigger than {card_drawn_tom[1]} and therefore he won this round!")
        michal.hand.add(card_drawn_tom[1])
        tom.hand.remove(card_drawn_tom[1])
        michal.hand.remove(card_drawn_michal[1])
        michal.hand.add(card_drawn_michal[1])
        if michal.check() == 0:
            print("No cards left, Tom won!")
            return False
    else:
        print("WAR!")

        try:
            card_drawn_tom = tom.play(3)
            card_drawn_michal = michal.play(3)
            print(card_drawn_tom)
            print(card_drawn_michal)     
        except IndexError:
            print("Someone is out of cards!")
            if tom.check() > michal.check():
                print("And it is Michal! Tom WON!")
                return False  
            else:
                print("And it is Tom! Michal WON!")
                return False        
        print(tom.hand.cards)
        print(michal.hand.cards)
        if card_drawn_tom[0] > card_drawn_michal[0]:
            print(f"Tom has drawn {card_drawn_tom[1]} which is bigger than {card_drawn_michal[1]} and therefore he won this round!")
            tom.hand.add(card_drawn_michal[1])
            michal.hand.remove(card_drawn_michal[1])
            tom.hand.add(card_drawn_tom[1])
            tom.hand.remove(card_drawn_tom[1])
            print(tom.hand.cards)
            print(michal.hand.cards)
            for i in range(0,3):
                tom.hand.add(michal.hand.cards[i])
            for i in range(0,3):    
                michal.hand.remove(michal.hand.cards[0])
            for i in range(0,3):    
                tom.hand.add(tom.hand.cards[i])
            for i in range(0,3):    
                tom.hand.remove(tom.hand.cards[0])
            
            if tom.check() == 0:
                print("No cards left, Michal won!")
                return False

        elif card_drawn_tom[0] < card_drawn_michal[0]:
            print(f"Michal has drawn {card_drawn_michal[1]} which is bigger than {card_drawn_tom[1]} and therefore he won this round!")
            michal.hand.add(card_drawn_tom[1])
            tom.hand.remove(card_drawn_tom[1])
            michal.hand.add(card_drawn_michal[1])
            michal.hand.remove(card_drawn_michal[1])
            print(tom.hand.cards)
            print(michal.hand.cards)
            for i in range(0,3):
                michal.hand.add(tom.hand.cards[i])
            for i in range(0,3):    
                tom.hand.remove(tom.hand.cards[0])
            for i in range(0,3):    
                michal.hand.add(michal.hand.cards[i])
            for i in range(0,3):    
                michal.hand.remove(michal.hand.cards[0])
                    
            if michal.check() == 0:
                print("No cards left, Tom won!")
                return False

        else:
            print("DOUBLE WAR! GAME ENDED, NEITHER WON!")
            return False

while True:
    hra = game(tom, michal)
    if hra == False:
        break
# Use the 3 classes along with some logic to play a game of war!
