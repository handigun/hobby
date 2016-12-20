# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    if(direction == 'Right'):
        x = random.randrange(1,5)
    else:
        x = -(random.randrange(1,5))
    y = -(random.randrange(1,3))
    ball_vel = [x,y]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    paddle1_pos = [HALF_PAD_WIDTH, HEIGHT/2]
    paddle2_pos = [WIDTH - HALF_PAD_WIDTH, HEIGHT/2]
    paddle1_vel = [0,0]
    paddle2_vel = [0,0]
    spawn_ball('Right')
    
def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    if(ball_pos[1] < BALL_RADIUS):
        ball_vel[1] = -ball_vel[1]
    elif(ball_pos[1] > HEIGHT-BALL_RADIUS):
        ball_vel[1] = -ball_vel[1]
    elif(ball_pos[0]<PAD_WIDTH+BALL_RADIUS):
        if ball_pos[1]> paddle1_pos[1]-HALF_PAD_HEIGHT and ball_pos[1] < paddle1_pos[1]+HALF_PAD_HEIGHT:
            ball_vel[0] = -ball_vel[0] * 1.1
        else:
            score2 += 1
            spawn_ball('Right')
            
    elif(ball_pos[0]>WIDTH-(PAD_WIDTH+BALL_RADIUS)):
        if ball_pos[1]> paddle2_pos[1]-HALF_PAD_HEIGHT and ball_pos[1] < paddle2_pos[1]+HALF_PAD_HEIGHT:
            ball_vel[0] = -ball_vel[0] * 1.1
        else:
            score1 += 1
            spawn_ball('Left')
    # draw ball
    c.draw_circle(ball_pos,BALL_RADIUS,1, "White","White")
    # update paddle's vertical position, keep paddle on the screen
    
    paddle1_pos[1] += paddle1_vel[1]
    if(paddle1_pos[1]+HALF_PAD_HEIGHT > HEIGHT):
        paddle1_pos[1] = HEIGHT - HALF_PAD_HEIGHT
    if(paddle1_pos[1]-HALF_PAD_HEIGHT < 0):
        paddle1_pos[1] = HALF_PAD_HEIGHT
    paddle2_pos[1] += paddle2_vel[1]
    if(paddle2_pos[1]+HALF_PAD_HEIGHT > HEIGHT):
        paddle2_pos[1] = HEIGHT - HALF_PAD_HEIGHT
    if(paddle2_pos[1]-HALF_PAD_HEIGHT < 0):
        paddle2_pos[1] = HALF_PAD_HEIGHT
    # draw paddles
    c.draw_line([paddle1_pos[0],paddle1_pos[1]+HALF_PAD_HEIGHT],[paddle1_pos[0],paddle1_pos[1]-HALF_PAD_HEIGHT],PAD_WIDTH,'White')
    c.draw_line([paddle2_pos[0],paddle2_pos[1]+HALF_PAD_HEIGHT],[paddle2_pos[0],paddle2_pos[1]-HALF_PAD_HEIGHT],PAD_WIDTH,'White')
    # draw scores
    c.draw_text(str(score1), (225, 50), 36, 'Red')
    c.draw_text(str(score2), (375, 50), 36, 'Red')
def keydown(key):
    global paddle1_vel, paddle2_vel
    if(key == simplegui.KEY_MAP['up']):
        paddle2_vel[1]-=3
    elif(key == simplegui.KEY_MAP['down']):
        paddle2_vel[1]+=3
    elif(key == simplegui.KEY_MAP['w']):
        paddle1_vel[1]-=3
    elif(key == simplegui.KEY_MAP['s']):
        paddle1_vel[1]+=3
    pass
def keyup(key):
    global paddle1_vel, paddle2_vel
    if(key == simplegui.KEY_MAP['up']):
        paddle2_vel[1]=0
    elif(key == simplegui.KEY_MAP['down']):
        paddle2_vel[1]=0
    elif(key == simplegui.KEY_MAP['w']):
        paddle1_vel[1]=0
    elif(key == simplegui.KEY_MAP['s']):
        paddle1_vel[1]=0
    pass

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button1 = frame.add_button('Restart', new_game,100)

# start frame
new_game()
frame.start()
