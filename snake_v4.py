import turtle
import time
import keyboard
import random

#hide the turtle and give it the fastest drawing speed
turtle.hideturtle()
turtle.speed(0)

def drawsquare(x, y, size, colour):
    turtle.color("black", colour)
    #Reset turtle position without drawing
    turtle.penup()
    turtle.goto((x * size)-(size / 2), (y * size)+(size / 2))
    turtle.pendown()
    turtle.begin_fill()
    turtle.goto((x * size)+(size / 2), (y * size)+(size / 2))
    turtle.goto((x * size)+(size / 2), (y * size)-(size / 2))
    turtle.goto((x * size)-(size / 2), (y * size)-(size / 2))
    turtle.goto((x * size)-(size / 2), (y * size)+(size / 2))
    turtle.end_fill()

def drawarena(length, height, size):
    turtle.penup()
    turtle.goto(0-(length * size)+(size/2), 0+(height * size)-(size/2))
    turtle.pendown()
    turtle.goto(0+(length * size)-(size/2), 0+(height * size)-(size/2))
    turtle.goto(0+(length * size)-(size/2), 0-(height * size)+(size/2))
    turtle.goto(0-(length * size)+(size/2), 0-(height * size)+(size/2))
    turtle.goto(0-(length * size)+(size/2), 0+(height * size)-(size/2))

#NEW GAME
while True:
    #Defining variables and stuff
    snakeposX = 0
    snakeposY = 0
    arenalength = 4
    arenaheight = 4
    snakelength = 3
    repeat = snakelength
    snakedirection = 90
    scale = 30
    snakehistoryX = [-2, -1, 0]
    snakehistoryY = [0, 0, 0]
    snakehistorymerged = []
    snakedead = 0
    foodXY = 0

    #set the food
    foodX = random.randint(-arenalength + 1, arenalength - 1)
    foodY = random.randint(-arenaheight + 1, arenaheight - 1)
    print("Made new food")

    #PROGRAM STARTS
    while snakedead == 0:
        timeout = time.time() + 1/(1+(snakelength/30))
    
        #COMPUTING PART

        while not time.time() > timeout:
            #check for movement
            if keyboard.is_pressed("up"):
                snakedirection = 0
            elif keyboard.is_pressed("right"):
                snakedirection = 90
            elif keyboard.is_pressed("down"):
                snakedirection = 180
            elif keyboard.is_pressed("left"):
                snakedirection = -90

        #move in the direction the snake is facing
        if snakedirection == 0:
            snakeposY = snakeposY + 1
        elif snakedirection == 90:
            snakeposX = snakeposX + 1
        elif snakedirection == 180:
            snakeposY = snakeposY - 1
        elif snakedirection == -90:
           snakeposX = snakeposX - 1

        #merge snakehistory lists
        repeat = 0
        #refresh list
        snakehistorymerged.clear()
        while repeat <= snakelength - 1:
            snakehistorymerged.append(str(snakehistoryX[repeat]) + str(snakehistoryY[repeat]))
            repeat = repeat + 1

        #check if the snake ate food
        if snakehistoryX[snakelength-1] == foodX and snakehistoryY[snakelength-1] == foodY:
            snakelength = snakelength + 1
            #set the food
            foodX = random.randint(-arenalength + 1, arenalength - 1)
            foodY = random.randint(-arenaheight + 1, arenaheight - 1)
            print("Made new food")

            #merge foodX and foodY
            foodXY = str(foodX) + str(foodY)
            print("FoodXY:",foodXY)
            #give the food a new random position
            while foodXY in snakehistorymerged:
                foodX = random.randint(-arenalength + 1, arenalength - 1)
                foodY = random.randint(-arenaheight + 1, arenaheight - 1)
                foodXY = str(foodX) + str(foodY)
                print("Made new food cause old food spawned inside snake")
                print("Food:",foodX,",",foodY)
                
                #abort
                if keyboard.is_pressed("s"):
                    turtle.done()

        #update snakes latest position
        snakehistoryX.append(snakeposX)
        snakehistoryY.append(snakeposY)
    
        #keeps the snakehistory lists the same length as the snake
        if len(snakehistoryX) > snakelength:
            del snakehistoryX[0]
            del snakehistoryY[0]

        #console checks
        print("----------------One frame has passed----------------")
        print("Snake length:",snakelength)
        print("Snake Direction:",snakedirection)
        print("Snake's X history:",snakehistoryX)
        print("Snake's Y history:",snakehistoryY)
        print("Snake's history merged:",snakehistorymerged)
        print("Food:",foodX,",",foodY)
        print("")

        #check if snake ran into itself
        if not len(snakehistorymerged) == len(set(snakehistorymerged)):
            snakedead = 1
            print("----------------SNAKE DIED----------------")
            print("----------------GAME OVER----------------")

        #check if snake ran out of bounds
        if snakehistoryX[snakelength-1] >= arenalength or snakehistoryX[snakelength-1] <= -arenalength or snakehistoryY[snakelength-1] >= arenaheight or snakehistoryY[snakelength-1] <= -arenaheight:
            snakedead = 1
            print("----------------SNAKE DIED----------------")
            print("----------------GAME OVER----------------")

        #DRAWING PART
        turtle.clear()
        #even faster drawing
        turtle.tracer(0, 0)

        #draw arena
        drawarena(arenalength, arenaheight, scale)

        #Draw the food
        drawsquare(foodX, foodY, scale, "red")

        #draw the snake
        repeat = snakelength
        while repeat >= 0:
            drawsquare(snakehistoryX[repeat-1], snakehistoryY[repeat-1], scale, "green")
            repeat = repeat - 1

        #update screen to show all drawings
        turtle.update()

    print("----------------Press space to play again----------------")
    keyboard.wait("space")
    #checks if the player got the snake to maximum length
    if snakelength >= (arenaheight * 2) - 1 * (arenalength * 2) - 1:
        #increases the arena size
        arenaheight = arenaheight + 4
        arenalength = arenalength + 4