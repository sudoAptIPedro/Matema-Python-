from turtle import *
"""

CREATE YOUR VIRUS ANIMATION!!!
by: sudoAptIPedro

"""

#input dos dados nas variaveis:
a = int(input("Digite um valor para a primeira coordenada: "))
b = int(input("Digite um valor para a segunda coordenada: "))
c = str(input("Digite uma cor de fundo: "))
d = str(input("Digite uma cor de caneta: "))
e = int(input("Digite uma altura: "))

#create function for animation with turtle:
def createAnimation(x, y, z, w, k):
    bgcolor(z)
    speed(0)
    pencolor(w)
    penup()
    goto(0,k)
    pendown()
    #loop
    while True:
        forward(x)
        right(y)
        x+=3
        y+=1

#final 

#output 
createAnimation(a, b, c, d, e)
print(createAnimation(a, b, c, d, e))
