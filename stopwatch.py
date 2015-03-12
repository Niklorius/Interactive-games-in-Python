"Stopwatch: the game"
# To be ran in codeskulptor.

# define global variables
import simplegui

on_state = False
time = 0
match = 0
stop_trials = 0

score_string = "Score: " + str(match) + "/" + str(stop_trials)


def print_score():
    
    score_string = "Score: " + str(match) + "/" + str(stop_trials)
    return score_string


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    A = t / 600
    
    B = t / 100 % 6
    
    C = t / 10 % 10
    D = t % 10
    
    #computing A and B
    
    
    return str(A) + ":" + str(B) + str(C) + "." + str(D) 
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_button():
    stop_watch.start()
    global on_state
    on_state = True
    
def stop_button():
    stop_watch.stop()
    
    global match, stop_trials, on_state
    
    if on_state == True and time % 10 == 0:
        match = match + 1
        stop_trials = stop_trials + 1
        
    elif on_state == True and time % 10 != 0:
        stop_trials = stop_trials + 1
        
    on_state = False
    
def reset_button():    
    global time, match, stop_trials
    time = 0
    match = 0
    stop_trials = 0
    stop_watch.stop()
    
    
# define event handler for timer with 0.1 sec interval
def tick():
    global time
    time += 1
# define draw handler
def draw(canvasio):
    global score_string
    canvasio.draw_text(format(time), [100, 250], 100, 'Red')
    canvasio.draw_text(print_score(), [250, 100], 50, 'White')
    
# create frame
stopwatchframe = simplegui.create_frame('Stopwatch Da Game', 500, 500)


# register event handlers
stopwatchframe.add_button('Start', start_button, 100)
stopwatchframe.add_button('Stop', stop_button, 100)
stopwatchframe.add_button('Reset', reset_button, 100)
stopwatchframe.set_draw_handler(draw)
stop_watch = simplegui.create_timer(100, tick)

# start frame
stopwatchframe.start()

