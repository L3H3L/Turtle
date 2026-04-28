import turtle

#teknős elnevezése
buci = turtle.Turtle()

#ablak elnevezése
ablak = turtle.Screen()

#ablak méretének megadása
ablak.setup(1300,700)

#háttérszín megváltoztatása
turtle.bgcolor("beige")

#teknős mozgatása

#teknős sebessége
buci.speed(0)

#előre megy (forward-bk)
buci.bk(50)

#jobbra a fordulás(rt)
buci.rt(60)
buci.fd(100)

#balra fordulás (lt)
buci.lt(60)
buci.fd(100)

#adott koordinátára megy(goto)
buci.goto(-500,300)

#ceruza felemelése penup(pu)
buci.pu()
buci.goto(500,-300)

#ceruza letevése pendown(pd)
buci.pd()

buci.pencolor("blue")
buci.bk(300)

#szín megadási módjának megváltoztatása
turtle.colormode(255)
buci.pencolor(250, 150, 200)
buci.bk(300)

buci.pu()
buci.goto(-300,0)

#kitöltési szín megadása
buci.fillcolor(20, 190, 125)

#kör rajzolása
buci.circle(100)

buci.end_fill()

buci.end_fill()

#rajzok letörlése
ablak.reset()

print("Kész az ív!")
turtle.done()