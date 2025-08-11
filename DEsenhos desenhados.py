import turtle as t  # Importa a biblioteca turtle e a chama de "t"

# Desenha um quadrado
t.forward(100)      # Move 100 unidades para frente
t.left(90)          # Vira 90 graus à esquerda
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)

# Move para uma nova posição sem desenhar
t.penup()           # Levanta a caneta (não desenha)
t.left(180)         # Vira 180 graus
t.forward(-100)     # Move para trás (100 unidades)
t.pendown()         # Abaixa a caneta (volta a desenhar)

# Define a cor da caneta para vermelho
t.pencolor("red")

# Desenha um triângulo equilátero
t.left(90)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)

# Move para uma nova posição
t.penup()
t.left(120)
t.left(180)
t.forward(200)
t.pendown()

# Define a cor da caneta para azul
t.pencolor("blue")

# Desenha um retângulo
t.forward(100)
t.left(90)
t.forward(200)
t.left(90)
t.forward(100)
t.left(90)
t.forward(200)

# Move para nova posição e desenha um círculo rosa claro
t.penup()
t.forward(200)
t.pendown()
t.pencolor("#E8A2D9")  # Cor rosa claro

t.circle(100)  # Desenha um círculo com raio 100

# Move para uma nova posição e desenha dois círculos cinza claro
t.penup()
t.left(220)
t.forward(800)
t.left(50)
t.pendown()
t.pencolor("#C1B7B0")  # Cor cinza claro

t.circle(50)  # Primeiro círculo
t.penup()
t.forward(100)
t.pendown()
t.circle(50)  # Segundo círculo

# Desenha uma linha vertical para baixo
t.penup()
t.forward(-50)
t.left(90)
t.pendown()
t.forward(500)
