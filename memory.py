# implementation of card game - Memory

import simplegui
import random
turns_label = ""
lst = []
exposed = []
state = 0
show_cards = []
turns = 0
# helper function to initialize globals
def new_game():
    global lst,turns, exposed,show_cards, state
    state = 0
    show_cards = []
    turns = 0
    lst = []
    exposed = []
    lst = range(0,8,1)
    lst.extend(range(0,8,1))
    random.shuffle(lst)
    turns_label = "Turns = "+str(turns)
    label.set_text(turns_label)
    for idx in range(0,len(lst)):
        exposed.append(False)

     
# define event handlers
def mouseclick(pos):
    global lst, exposed, state, show_cards, turns,turns_label
    click_pos = list(pos)
    card_no = click_pos[0] // 50
    
    if exposed[card_no] == False:
        exposed[card_no] = True
        show_cards.append(card_no)
        # add game state logic here
        if state == 0:
            state = 1
        elif state == 1:
            turns += 1
            turns_label = "Turns = "+str(turns)
            label.set_text(turns_label)
            state = 2
        else:
            if(lst[show_cards[0]] != lst[show_cards[1]]):
                exposed[show_cards[0]] = False
                exposed[show_cards[1]] = False
            
            show_cards.pop(0)
            show_cards.pop(0)
            exposed[show_cards[0]] = True
            state = 1
        
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global lst, exposed,turns
    pos = [25,60]
    idx = 0
    for num in lst:
        if(exposed[idx] == True):
            canvas.draw_text(str(lst[idx]), [pos[0]-10,pos[1]], 36, "White")
        else:
            canvas.draw_polygon([[pos[0]-25, pos[1]-60], [pos[0]+25, pos[1]-60], [pos[0]+25, pos[1]+40], [pos[0]-25, pos[1]+40]], 5,"Black",'Green')
        idx += 1
        pos[0]+=50
        


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game)
turns_label = "Turns = "+str(turns)
label = frame.add_label(turns_label)
label.set_text(turns_label)

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric