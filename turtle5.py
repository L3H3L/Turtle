import turtle, random

print("A nyertes:", random.randint(1,19))

teki = turtle.Turtle()

ablak = turtle.Screen()
ablak.setup(1300, 700)
"""
a = 200
ism = 0
while ism != 10:
    teki.rt(90)
    teki.circle(a, -90)
    teki.pu()
    teki.goto(0, 0)
    teki.lt(180)
    teki.pd()
    a = a-20
    ism = ism + 1
"""
#szökőkút

teki.lt(90)
for a in range(1, 7):
    teki.circle(-30*a, 90)
    teki.circle(-30*a, -90)
    teki.circle(30*a, 90)
    teki.circle(30*a, -90)
