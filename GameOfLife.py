import turtle as t
import random as r

# function to group consecutive characters
def group(arr):
    substr_lengths = []
    count = 1
    current_num = arr[0]
    for num in arr[1:]:
        if num == current_num:
            count += 1
        else:
            substr_lengths.append(count)
            count = 1
            current_num = num
    substr_lengths.append(count)
    return substr_lengths, arr[0]

# drawing a line of pixels
def draw_line(seq, flag, start_x, start_y): # turtle dir ->
    t.goto(start_x, start_y)
    t.begin_fill()
    for val in seq:
        if flag == 1: # black square
            t.goto(start_x, start_y-sq_scale)
            start_x += sq_scale*val
            t.goto(start_x, start_y-sq_scale)
            t.goto(start_x, start_y)
            flag -= 1
        else: # white square
            start_x += sq_scale*val
            t.goto(start_x,start_y)
            flag +=1
    t.end_fill()

# generating a new generation + drawing
def next_gen(old_gen, start_y):
    new_gen = list(map(lambda _: [0]*width, range(height)))
    for x in range(1, width-1):
        for y in range(1, height-1):
            neighbors = old_gen[y-1][x-1]+old_gen[y-1][x]+old_gen[y-1][x+1] \
            + old_gen[y][x-1] + old_gen[y][x+1] \
            + old_gen[y+1][x-1]+old_gen[y+1][x]+old_gen[y+1][x+1]
            if neighbors < 2 or neighbors > 3:
                new_gen[y][x] = 0
            elif neighbors == 3:
                new_gen[y][x] = 1
            elif neighbors == 2:
                new_gen[y][x] = old_gen[y][x]
        
        # symb_flag is the color of the first pixel in the line
        gen_grouped, symb_flag = group(old_gen[x])
        draw_line(gen_grouped, symb_flag, start_pos_x, start_y)
        start_y -= sq_scale
    return new_gen

# constants
sq_scale = 14
width = 100
height = 100
start_pos_x = -width*sq_scale//2 # left upper corner x
start_pos_y = height*sq_scale//2 # left upper corner y

# turtle settings
t.up()
t.speed(100)
t.tracer(0)
t.screensize(3000,3000)
t.hideturtle()

# random generation
gen = [[r.randint(0,1) for _ in range(width)] for _ in range(height)]

# inf loop to refresh canvas
while True:
    gen = next_gen(gen, start_pos_y)
    t.update()
    t.clear()
