def turn_right():
    turn_left()
    turn_left()
    turn_left()

# debugging infinite loop
while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear(): # always right is clear, turn right and move
        turn_right()
        move()
    elif front_is_clear():   # if right is not clear and front is clear: move
        move()
    else:             # if both is not clear, turn left
        turn_left()