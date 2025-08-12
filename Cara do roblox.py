import turtle as t

t.speed(10)
t.hideturtle()

# Função para desenhar o olho com pálpebra inclinada
def desenhar_olho(x, y):
    # Pupila
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.pensize(35)
    t.pencolor("black")
    t.circle(18)

    # Brilho
    t.pensize(4)
    t.pencolor("white")
    t.penup()
    t.goto(x + 8, y + 20)
    t.pendown()
    t.circle(2)

    # Pálpebra superior (mais inclinada)
    t.pencolor("black")
    t.pensize(5)
    t.penup()
    t.goto(x - 28, y + 32)
    t.setheading(10)  # ângulo mais agressivo
    t.pendown()
    t.forward(56)

# Função para desenhar a boca fina e inclinada
def desenhar_boca():
    t.penup()
    t.goto(-35, -65)
    t.setheading(5)  # leve inclinação pra direita
    t.pendown()
    t.pensize(3)
    t.pencolor("black")
    t.forward(70)  # linha reta
    t.setheading(-60)
    t.circle(35, 50)  # curvinha no canto

# Desenhar olhos
desenhar_olho(-65, 0)  # esquerdo
desenhar_olho(35, 0)   # direito

# Desenhar boca
desenhar_boca()

t.done()
