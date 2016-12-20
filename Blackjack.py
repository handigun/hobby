# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
message = "Hit or Stand ?"
score = 0
player_pos = [20,400]
dealer_pos = [20,200]
# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}



# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    global in_play
    def __init__(self):
        self.card_list = []
        self.s = ""
        self.value = 0# create Hand object

    def __str__(self):
        self.s = ""
        for card in self.card_list: # return a string representation of a hand
            self.s += str(card) + " "
        return "Hand Contains "+self.s

    def add_card(self, card):
        self.card_list.append(card)	# add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        self.value = 0
        for card in self.card_list:
            self.value += VALUES[card.rank]
        
        for card in self.card_list:
            if(card.rank == 'A'):
                if( self.value+10 <= 21):
                    return self.value + 10
        return self.value
   
    def draw(self, canvas, pos):
        pos[0] = 20
        # draw a hand on the canvas, use the draw method for cards
        if self == player_hand:
            for card in self.card_list:
                card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(card.rank), 
                        CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(card.suit))
                canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
                pos[0] += 80
        else:
            if in_play == True:
                pos[0] = 20
                card_loc = (CARD_BACK_CENTER[0],CARD_BACK_CENTER[1])
                canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE, [pos[0] + CARD_BACK_CENTER[0], pos[1] + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
                pos[0] += 80
                for i in range(1,len(self.card_list)):
                    card = self.card_list[i]
                    card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(card.rank), 
                            CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(card.suit))
                    canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
                    pos[0] += 80            
            else:
                pos[0] = 20
                for card in self.card_list:
                    card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(card.rank), 
                            CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(card.suit))
                    canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
                    pos[0] += 80

        
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.s = ""
        self.cards = []	
        for suit in SUITS:
            for rank in RANKS:
                card = Card(suit, rank)
                self.cards.append(card)

    def shuffle(self):
        # shuffle the deck 
        # use random.shuffle()
        random.shuffle(self.cards) 

    def deal_card(self):
        # deal a card object from the deck
        card = self.cards[-1]
        self.cards.remove(card)
        return card
        
    
    def __str__(self):
        # return a string representing the deck
        for card in self.cards:
            self.s += str(card)+" "
        return "Deck Contains "+self.s

d = Deck()
player_hand = Hand()
dealer_hand = Hand()

#define event handlers for buttons
def deal():
    global outcome, in_play,message,player_hand,dealer_hand, d, score
    message = "Hit or Stand?"
    outcome = ""
    if in_play:
        score -= 1
        outcome ="You lose"
        message = "New Deal?"
    
    d = Deck()
    player_hand = Hand()
    dealer_hand = Hand()
    d.shuffle()          
    player_hand.add_card(d.deal_card())
    
    dealer_hand.add_card(d.deal_card()) 
    
    player_hand.add_card(d.deal_card())
    
    dealer_hand.add_card(d.deal_card())
    message = "Hit or Stand?" 
    in_play = True
   

def hit():
    global in_play, outcome, score, message
    # replace with your code below
    # if the hand is in play, hit the player
    # if busted, assign a message to outcome, update in_play and score
    if(player_hand.get_value() >=21):
        in_play = False
    else:
        player_hand.add_card(d.deal_card())
        if(player_hand.get_value() == 21):
            in_play = False
            outcome = "You Win"
            message = "New Deal?"
            score += 1
        elif(player_hand.get_value() > 21):
            in_play = False
            outcome = "Busted"
            message = "New Deal?"
            score -= 1
        else:
            in_play = True
        
def stand():
    global in_play, outcome, score, message
    in_play = False
    while(dealer_hand.get_value() < 17):
        dealer_hand.add_card(d.deal_card())
    
    if(dealer_hand.get_value() > 21):
        outcome = "You Win"
        message = "New Deal?"
        score += 1
    else:
        if(dealer_hand.get_value() >= player_hand.get_value()):
            outcome = "You Lose"
            score -= 1
            message = "New Deal?"
        else:
            outcome = "You Win"
            message = "New Deal?"
            score += 1

# draw handler    
def draw(canvas):
    global score, outcome
    canvas.draw_text("BLACKJACK", (225 , 50), 32, "BLACK")
    canvas.draw_text("PLAYER:", (20 , 350), 24, "WHITE")
    canvas.draw_text("DEALER:", (20 , 150), 24, "WHITE")
    canvas.draw_text(message, (150 , 350), 24, "WHITE")
    canvas.draw_text(outcome, (300 , 100), 24, "WHITE")
    
    s = "SCORE: "+str(score)
    canvas.draw_text(s, (450 , 75), 24, "WHITE")
    player_hand.draw(canvas, player_pos)
    
    
    dealer_hand.draw(canvas, dealer_pos)
        
        
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric