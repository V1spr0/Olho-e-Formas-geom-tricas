import turtle as t
#definindo a velocidade 
t.speed(100)

#Fazendo a pupila

t.width(40)
t.circle(20)
t.width(1)
t.pencolor("white")

t.penup()
t.left(90)
t.forward(30)
t.left(-90)
t.forward(15)
t.pendown()

#Fazendo a luz da pupila

t.width(5)
t.circle(2)
t.width(1)

t.penup()
t.left(90)
t.forward(33)
t.left(90)
t.pendown()

#fazendo o olho

t.pencolor("black")
t.width(5)
t.forward(100)
t.left(180)
t.forward(130)
t.left(320)
t.forward(20)
t.width(4)
t.forward(10)
t.width(3)
t.forward(10)
t.width(2)
t.forward(10)
t.width(1)
t.forward(10)

t.penup()
t.left(180)
t.forward(60)
t.left(40)
t.forward(100)
t.pendown()


t.left(50)
t.width(5)
t.forward(30)
t.width(4)
t.forward(20)
t.width(3)
t.forward(20)
t.left(130)
t.forward(150)
t.left(30)
t.forward(40)
t.left(240)

t.penup()
t.forward(50)
t.left(-90)
t.pendown()

t.pencolor("white")
t.width(55)
t.forward(130)
t.width(3)

t.penup()
t.forward(60)
t.left(-90)
t.forward(110)
t.left(-90)
t.pendown()

t.pencolor("black")
t.forward(170)
