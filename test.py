import turtle

# Ablak beállítása
screen = turtle.Screen()
screen.bgcolor("white")
#screen.tracer(0)  # Gyorsabb rajzolás érdekében
t = turtle.Turtle()
#t.hideturtle() ---------------------------------
t.shape("turtle")
t.setheading(90)
t.speed(1)
t.pensize(2)

# Pozicionálás (hogy ne középen kezdje)
t.penup()
t.goto(-100, 0)
t.pendown()
"""
# Színes ív rajzolása
t.pencolor("darkred")
t.setheading(90)     # Felfelé nézzen a kezdéshez
t.circle(-100, 180)  # Negatív sugárral jobbra kanyarodik (így lesz boltív)

def rajzolj_ivet(sugar, fok, szin):
    t.penup()     # Kezdőpont beállítása
    t.setheading(90)  # Felfelé nézzen
    t.pendown()
    t.pencolor(szin)
    t.circle(-sugar, fok) # Ív rajzolása

"""

def Négyzet(szin):
    t.pencolor(szin)
    for _ in range(4):
        t.forward(50)
        t.right(90)

Négyzet("black")
# A teknős elrejtése a végén
#screen.update()
print("Kész az ív!")
turtle.done()