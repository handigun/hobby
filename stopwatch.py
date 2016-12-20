# template for "Stopwatch: The Game"
import simplegui
# define global variables
time = 0
interval = 100
tries = 0
wins = 0
is_stop = False


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    a = t // 600
    b = ((t // 10)%60)//10
    c = ((t // 10)%60)%10
    d = t % 10
    str1 = str(a)+":"+str(b)+str(c)+"."+str(d)
    return str1    


# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global is_stop
    is_stop = False
    timer.start()

def stop():
    global is_stop
    if( is_stop == False):
        is_stop = True
        timer.stop()
        check_win()
  
def reset():
    global time, tries, wins, is_stop
    is_stop = False
    timer.stop()
    time = 0
    tries = 0
    wins = 0
    
def check_win():
    global time, tries, wins
    tries = tries+1
    if((time % 10) == 0):
        wins = wins+1
    
    
# define event handler for timer with 0.1 sec interval
def tick():
    global time
    time = time + 1
    

# define draw handler
def draw(canvas):
    global time, tries, wins
    str1 = str(wins)+"/"+str(tries)
    canvas.draw_text(str1,[225,36], 36, "Green")
    canvas.draw_text(str(format(time)), [110,110],36,"Red")
    
# create frame
frame = simplegui.create_frame("StopWatch",300,200)
timer = simplegui.create_timer(interval, tick)

# register event handlers
button1 = frame.add_button('Start', start,100)
button2 = frame.add_button('Stop', stop,100)
button3 = frame.add_button('Reset', reset,100)
frame.set_draw_handler(draw)

# start frame
frame.start()



# Please remember to review the grading rubric
