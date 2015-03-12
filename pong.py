# Implementation of classic arcade game Pong
#Need codeskulptor to run this game
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

score1 = 0
score2 = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    
    # Set launch direction of ball, do 4 and 3 for vel
    if direction:
        ball_vel = [3, -3]
    else:
        ball_vel = [-3, -3]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    global LEFT, RIGHT
    spawn_ball(random.choice([LEFT, RIGHT]))
    paddle1_pos = [HALF_PAD_WIDTH, HEIGHT/2]
    paddle2_pos = [WIDTH - HALF_PAD_WIDTH, HEIGHT/2]
    paddle1_vel = 0
    paddle2_vel = 0
    score1 = 0
    score2 = 0
    
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global LEFT, RIGHT
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    

    
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # reflect the ball on walls
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= (HEIGHT-1) - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    
    # reflect the ball on paddle1
    
    if paddle1_pos[1] <= ball_pos[1] <= paddle1_pos[1]+PAD_HEIGHT and ball_pos[0] <= PAD_WIDTH + BALL_RADIUS:
        ball_vel[0] = -ball_vel[0]*1.1
        
        
    # Respawn the ball when touching left gutter    
    elif ball_pos[0] <= (PAD_WIDTH + BALL_RADIUS):
        
        score2 += 1
        spawn_ball(RIGHT)    
        
        
    # reflect the ball on paddle2
    if paddle2_pos[1] <= ball_pos[1] <= paddle2_pos[1]+PAD_HEIGHT and ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS -1:
        ball_vel[0] = -ball_vel[0]*1.1    
    
    
    # Respawn the ball when touching right gutter
    elif ball_pos[0] >= ((WIDTH-1) - PAD_WIDTH - BALL_RADIUS):
        score1 += 1
        spawn_ball(LEFT)
   
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, 'White', 'White')
    
    # update paddle's vertical position, keep paddle on the screen
    
    if HEIGHT - PAD_HEIGHT +7 >= (paddle1_pos[1] + paddle1_vel) >= 0:
        paddle1_pos[1] += paddle1_vel
    
    if HEIGHT - PAD_HEIGHT +7 >= (paddle2_pos[1] + paddle2_vel) >= 0:
        paddle2_pos[1] += paddle2_vel
    
    
    # draw paddle1
          
    canvas.draw_line(paddle1_pos, [paddle1_pos[0], paddle1_pos[1]+PAD_HEIGHT], PAD_WIDTH, 'White')
    # draw paddle2
          
    canvas.draw_line(paddle2_pos, [paddle2_pos[0], paddle2_pos[1]+PAD_HEIGHT], PAD_WIDTH, 'White')    
    
    # draw scores
    canvas.draw_text(str(score1), [WIDTH/4, HEIGHT/4], 50, 'Red')
    canvas.draw_text(str(score2), [WIDTH*3/4-25, HEIGHT/4], 50, 'Blue')
    
def keydown(key):
    global paddle1_vel, paddle2_vel, paddle1_pos, paddle2_pos

    # paddle 1
    
   
    if key == simplegui.KEY_MAP["w"]:
       paddle1_vel = -8
    
    if key == simplegui.KEY_MAP["s"]:
       paddle1_vel = 8
    
    
        
    # paddle 2
    
    
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -8
    
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 8
    
   
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    paddle1_vel = 0
    paddle2_vel = 0
    
def restart():
    
    new_game()

    
    
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Restart', restart, 80)

# start frame
new_game()
frame.start()
