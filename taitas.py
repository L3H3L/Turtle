import turtle



teki = turtle.Turtle()
teki.speed(50)
ablak= turtle.Screen()
ablak.setup(1300,700)
teki.pencolor("pink")
ism= 0
#meret = 0.5
meret= turtle.numinput("meret", "Add meg a virág méretét!")

teki.fillcolor("pink")
teki.begin_fill()
while ism !=4:
    teki.circle(100*meret,180)
    teki.rt(90)
    ism = ism + 1
teki.end_fill()
teki.pu()

teki.bk(100*meret)
teki.pd()
teki.fillcolor("yellow")
teki.begin_fill()
teki.circle(100*meret,360)
teki.pu()
teki.lt(90)
teki.fd(10*meret)

teki.end_fill()
teki.pu()
teki.pensize(10)
teki.rt(180)
teki.fd(111*meret)
teki.pd()
teki.pencolor("green")
teki.fd(100*meret)
teki.lt(135)
teki.fd(45*meret)
teki.lt(180)
teki.fd(45*meret)
teki.lt(45)
teki.fd(100*meret)

teki.lt(90)
#teki.pencolor("coral4)")
teki.fillcolor("coral4")
teki.begin_fill()
teki.fd(690)
teki.lt(180)
teki.fd(1285)
teki.lt(90)
teki.fd(185)
teki.lt(90)
teki.fd(1285)
teki.lt(90)
teki.fd(185)
teki.end_fill()

teki.pencolor("red")
teki.fillcolor("red")
teki.begin_fill()
teki.lt(45)
teki.fd(400)
teki.lt(90)
teki.fd(400)
teki.rt(45)
teki.bk(565.7)
teki.end_fill()


print(f"Hello {name}, how are you?")









print("kész")
turtle.done()
