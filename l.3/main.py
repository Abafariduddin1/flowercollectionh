import pgzrun
import random

WIDTH = 500
HEIGHT = 500
TITLE = "Flower collecting"

gameover = False
score = 0 

def over():
    global gameover
    gameover = True

bee = Actor("beebee.png")
flower = Actor("flowert.png")
bee.pos = 200, 200

def moving():
    k = random.randint(0, 500)
    l = random.randint(0, 500)
    flower.pos = k, l

def draw():
    screen.blit("grassplain.png", (0, 0))
    bee.draw()
    flower.draw()
    screen.draw.text(f"Score: {score}", (10, 10), fontsize=40, color="white")
    
    if gameover:
        screen.draw.text(f"Time's up! Your score is {score}", center=(250,250),fontsize=50, color="red")

def update():
    global score
    if not gameover:  
        if keyboard.left:
            bee.x -= 10 
        elif keyboard.right:
            bee.x += 10
        elif keyboard.down:
            bee.y += 10 
        elif keyboard.up:
            bee.y -= 10
        if bee.colliderect(flower):
            moving()
            score += 1  

clock.schedule(over, 60) 
pgzrun.go()
