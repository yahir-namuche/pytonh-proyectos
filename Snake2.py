import turtle
import time
import random

posponer=0.1
#marcador
Score=0
High_Score=0

#Configuracion de la ventana
wn= turtle.Screen()
wn.title("Juego de Snake")
wn.bgcolor("black")
wn.setup(width=600,height=600)
wn.tracer(0)
#segmentos
segmentos=[]

#cabeza serpiente
cabeza=turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("dark green")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction="stop"

#comida
comida=turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)
#texto
texto=turtle.Turtle()
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Score:0     High Score:0",align="center",font=("courier",24,"normal"))

#funciones
def arriba():
    cabeza.direction="up"
def abajo():
    cabeza.direction="down"
def derecha():
    cabeza.direction="right"
def izquierda():
    cabeza.direction="left"
def mov():
    if cabeza.direction == "up" :
        y= cabeza.ycor()
        cabeza.sety(y+20)
    if cabeza.direction == "down" :
        y= cabeza.ycor()
        cabeza.sety(y-20)
    if cabeza.direction == "left" :
        x= cabeza.xcor()
        cabeza.setx(x-20)
    if cabeza.direction == "right" :
        x= cabeza.xcor()
        cabeza.setx(x+20)

#teclado
wn.listen()
wn.onkeypress(arriba,"Up")
wn.onkeypress(abajo,"Down")
wn.onkeypress(derecha,"Right")
wn.onkeypress(izquierda,"Left")

while True:
    wn.update()
    #coliciones bordes
    if cabeza.xcor()>280 or cabeza .xcor() <-280 or cabeza .ycor()>270 or cabeza. ycor() < -270:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction="stop"
        #esconder segmento
        for segmento in segmentos:
            segmento.goto(1000,1000)
        #limpiar lista de segmentos
        segmentos.clear()

        #resetear marcador
        texto.clear()
        Score=0
        texto.write("Score: {}     High Score:{}".format(Score , High_Score),
            align="center",font=("courier",24,"normal"))
 
    #colisiones de comida
    if cabeza.distance(comida)<20:
        random.randint(-280,280)
        x=random.randint(-280,280)
        y=random.randint(-280,280)
        comida.goto(x,y)

        nuevo_segmento=turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("green")
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)
        #aumentar marcador
        Score += 10

        if Score > High_Score:
            High_Score = Score
        
        texto.clear()
        texto.write("Score: {}     High Score:{}".format(Score,High_Score),
        align="center",font=("courier",24,"normal"))



    #mover segmentos
    totalseg = len(segmentos)
    for index in range(totalseg -1,0,-1 ):
        x=segmentos[index-1].xcor()
        y=segmentos[index-1].ycor()
        segmentos[index].goto(x,y)
    if totalseg >0:
        x=cabeza.xcor()
        y=cabeza.ycor()
        segmentos[0].goto(x,y)

    mov()

    #coliciones con el cuerpo
    for segmento in segmentos:
        if segmento.distance(cabeza)<20:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction="stop"
            #sconder los segmentos
            for segmento in segmentos:
                segmento.goto(1000,1000)
                
            segmentos.clear()


    time.sleep(posponer)