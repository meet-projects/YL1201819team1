import tkinter as tk
import turtle 
from tkinter import *
import sys
import time
import pygame
pygame.mixer.init() 
pygame.mixer.music.load("SpongeBob.mp3")
pygame.mixer.music.play(-1,0.0)


turtle.tracer(0.0)
turtle.speed(100)
turtle.penup()
turtle.goto(turtle.pos()[0] + 45 ,turtle.pos()[1] + 240)
turtle.pendown()
BG = "boop.gif"
turtle.bgpic("boop.gif")
turtle.register_shape("SpongebobBack.gif")
food = turtle.clone()
food.penup()
food.pensize(30)
food.goto(1080,720)
writer = turtle.clone()
Spongebob = turtle.clone()
turtle.register_shape("Spongebob.gif")
turtle.register_shape("pita.gif")
turtle.register_shape("lefa.gif")
Spongebob.shape("Spongebob.gif")
turtle.register_shape("egg.gif")
turtle.register_shape("falafel1.gif")
turtle.register_shape("chips.gif")
turtle.register_shape("tomato.gif")
turtle.register_shape("hummus.gif")
turtle.register_shape("pickle.gif")
turtle.register_shape("shawrma2.gif")
turtle.register_shape("waterbottleanimation.gif")
turtle.register_shape("cocaCola.gif")
Spongebob.penup()
Spongebob.goto(10,-320)

def hide(x):
    x.pack_forget()
def hide_me(event):
    event.widget.pack_forget()


window = Tk()

frame = Frame(window)
frame.pack()

def close_window (): 
    window.destroy()


def Shawerma():
    Shawerma = turtle.clone()
    Shawerma.goto(Shawerma.pos()[0]+200,Shawerma.pos()[1]-550)
    Shawerma.pensize(50)
    Shawerma.shape("shawrma2.gif")



def Falafel():
    Falafel= turtle.clone()
    Falafel.goto(Falafel.pos()[0]+5,Falafel.pos()[1]-470)
    Falafel.pensize(50)
    Falafel.shape("falafel1.gif")


def Humous():
    Humous= turtle.clone()
    Humous.goto(Humous.pos()[0]+5,Humous.pos()[1]-470)
    Humous.pensize(50)
    Humous.shape("hummus.gif")


def Egg():
    Egg= turtle.clone()
    Egg.goto(Egg.pos()[0]+5,Egg.pos()[1]-470)
    Egg.pensize(50)
    Egg.shape("egg.gif")

    
def Chips():
    Chips= turtle.clone()
    Chips.goto(Chips.pos()[0]+5,Chips.pos()[1]-470)
    Chips.pensize(50)
    Chips.shape("chips.gif")


def Tomato():
    Tomato= turtle.clone()
    Tomato.goto(Tomato.pos()[0]+5,Tomato.pos()[1]-470)
    Tomato.pensize(50)
    Tomato.shape("tomato.gif")




def Pickle():
    Pickle= turtle.clone()
    Pickle.goto(Pickle.pos()[0]+5,Pickle.pos()[1]-470)
    Pickle.pensize(50)
    Pickle.shape("pickle.gif")


def Cola():
    Cola= turtle.clone()
    Cola.goto(Cola.pos()[0]-200,Cola.pos()[1]-470)
    Cola.pensize(50)
    Cola.shape("cocaCola.gif")









def ShawermaFinish():
    ShawermaFinish= turtle.clone()
    ShawermaFinish.hideturtle()
    turtle.clearscreen()
    ShawermaFinish.penup()
    turtle.bgpic("finaleshawarma.gif")
    ShawermaFinish.goto(ShawermaFinish.pos()[0]+20,ShawermaFinish.pos()[1]-110)





def FalafelFinish():
    falafelFinish= turtle.clone()

    turtle.clearscreen()
    turtle.bgpic("finalfalafel.gif")
    falafelFinish.goto(falafelFinish.pos()[0]+20,falafelFinish.pos()[1]-110)










def buy():
    frame = tk.Tk()
    writer.clear()
    shawerma = tk.Button(frame,
                    text="Shawerma",
                    fg="green",
                    command= Shawerma)
    shawerma.pack()
    
    falafel= tk.Button(frame,
                    text="Falafel",
                    fg="green",
                    command= Falafel)
    falafel.pack()

    egg = tk.Button(frame,
                    text="Egg",
                    fg="green",
                    command= Egg)
    egg.pack()
    humous = tk.Button(frame,
                    text="Humous",
                    fg="green",
                    command= Humous)
    humous.pack()

    tomato = tk.Button(frame,
                    text="Tomato",
                    fg="red",
                    command= Tomato)
    tomato.pack()

    chips = tk.Button(frame,
                    text="Chips",
                    fg="yellow",
                    command= Chips)
    chips.pack()

    cola = tk.Button(frame,
                    text="Cola",
                    fg="Red",
                    command= Cola)
    cola.pack()





    shawermaFinish = tk.Button(frame,
                    text="ShawermaFinish",
                    fg="blue",
                    command= ShawermaFinish)
    shawermaFinish.pack()

    falafelFinish = tk.Button(frame,
                    text="FalafelFinish",
                    fg="blue",
                    command=FalafelFinish)
    falafelFinish.pack()




   

turtle.setup(1080,720)


s = turtle.getscreen()
Dir_X = 0

def MoveRight():
    Spongebob.goto(Spongebob.pos()[0] + 40,Spongebob.pos()[1])
    Dir_X = 1
def MoveLeft():
    Spongebob.goto(Spongebob.pos()[0] - 40,Spongebob.pos()[1])
    Dir_X = 2
def MoveUp():
    Spongebob.goto(Spongebob.pos()[0],Spongebob.pos()[1]+ 40)
    Dir_Y = 1
def MoveDown():
    Spongebob.goto(Spongebob.pos()[0],Spongebob.pos()[1] - 40)
    Dir_Y = 2
def pos():
    print(Spongebob.pos())


def firstScreen():
    global BG
    if BG == ("boop.gif"):
        if Spongebob.pos() == (50,-240):
            BG = 'inside.gif'
            turtle.bgpic("inside.gif")
            Spongebob.shape("SpongebobBack.gif")
            writer.write("Welcome", align = "center", font = ("Arial",30,"normal"))
        elif Spongebob.pos()[1] == -240:
            Spongebob.goto(Spongebob.pos()[0],Spongebob.pos()[1] - 40)

        if Spongebob.pos()[1]  == -320:
            Spongebob.goto(Spongebob.pos()[0], Spongebob.pos()[1] + 40)

        if Spongebob.pos()[0]  == -550:
            Spongebob.goto(Spongebob.pos()[0] + 40, Spongebob.pos()[1])
        if Spongebob.pos()[0]  == 530:
            Spongebob.goto(Spongebob.pos()[0] - 40, Spongebob.pos()[1] )



def secondScreen():
    global BG
    if BG == ("inside.gif"):
        if Spongebob.pos() == (330,-120): #or Spongebob.pos() == (330,-40) or Spongebob.pos() == (320,-40):
            Spongebob.hideturtle()
            writer.clear()
            turtle.penup()
            BG = "SHAWRMA2.gif"
            turtle.bgpic("SHAWRMA2.gif")
            buy()
        if Spongebob.pos()[0]  == -550:
            Spongebob.goto(Spongebob.pos()[0] + 40, Spongebob.pos()[1])
        if Spongebob.pos()[0]  == 530:
            Spongebob.goto(Spongebob.pos()[0] - 40, Spongebob.pos()[1] )
        if Spongebob.pos()[1]  == -320:
            Spongebob.goto(Spongebob.pos()[0], Spongebob.pos()[1] + 40)
        if Spongebob.pos()[1] == -120:
            Spongebob.goto(Spongebob.pos()[0], Spongebob.pos()[1] - 40)



   


def Movement():
    s.onkeypress(MoveRight, "d")
    s.onkeypress(MoveLeft, "a")
    s.onkeypress(MoveUp, "w")
    s.onkeypress(MoveDown, "s")
    s.onkeypress(pos, "p")
    s.listen()



while True:
    Movement()
    firstScreen()
    secondScreen()
    time.sleep(0.05)
    turtle.update()
    

window.mainloop()

