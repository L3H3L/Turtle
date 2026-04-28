import turtle, random

teki = turtle.Turtle()
ablak = turtle.Screen()
ablak.setup(1300, 700)

#körív rajzolása circle (sugár, szög)
#sugár és szög is lehet negatív

ism = 0
while ism != 4:
    teki.circle(100, 180)
    teki.rt(90)
    ism = ism + 1
teki.pu()
teki.goto(-600, 0)
teki.pd()

#félkörívek egymás mellett

teki.rt(90)
for a in range(6):
    teki.circle(100, -180)
    teki.rt(180)
#félkörívek egymás mellett felcserélve
teki.rt(90)
for a in range(6):
    teki.circle(-60, -180)
    teki.circle(60, 180)

# 4. alakzat
teki.lt(90)
for a in range(2):
    teki.circle(-100, 180)
    teki.rt(90)
    teki.circle(100, 180)
    teki.rt(90)