
from email.mime import image
from glob import glob
import socket
from tkinter import *
from  threading import Thread
from turtle import title
from PIL import ImageTk, Image
import random

screen_width = None
screen_height = None

SERVER = None
PORT = None
IP_ADDRESS = None


canvas1 = None
canvas2 = None

playerName = None
nameEntry = None
nameWindow = None
gameWindow = None
leftBoxes = []
rightBoxes = []
playerType = None
dice = None
rollButton = None
finishLine = None



def saveName():
    global SERVER
    global playerName
    global nameWindow
    global nameEntry

    playerName = nameEntry.get()
    nameEntry.delete(0,END)
    nameWindow.destroy()

    SERVER.send(playerName.encode())

    
    playerWindow()

def playerWindow():
    global gameWindow
    global canvas2
    global screen_width
    global screen_height
    global dice
    global rollButton
    
    gameWindow = Tk()
    gameWindow.title("Ludo Game Screen")
    gameWindow.attributes("-fullscreen",True)

    screen_width=gameWindow.winfo_screenwidth()
    screen_height=gameWindow.winfo_screenheight()

    bg=ImageTk.PhotoImage(file="./assets/background.png")

    canvas2 = Canvas(gameWindow,width=500,height=500)
    canvas2.pack(fill="both",expand=True)
    canvas2.create_image(0,0,image=bg,anchor="nw")
    canvas2.create_text(screen_width/2,screen_height/5,text="Ludo Game",font={"Chalkboard SE",80},fill="white")

    createLeftBoard()
    createRightBoard()
    finishBox()

    rollButton = Button(gameWindow,text="ROLL THE DICE",fg = "black",font={"Chalkboard SE",80},width=20,height=5,command=rollingDice())
    rollButton.place(x=screen_width/2-85,y=screen_height/2+250)

    dice = canvas2.create_text(screen_width/2-40,screen_height/2+100,text="\u2680",font=("Chalkboard SE",200),fill="white")

    

    gameWindow.resizable(True,True)



    gameWindow.mainloop()

def rollingDice():
    # https://graphemica.com/characters/tags/dice
    dicePick= ["/u2680","/u2681","/u2682","/u2683","/u2684","/u2685"]
    randomDice=random(dicePick)

def createLeftBoard():
    global gameWindow
    global leftBoxes
    global screen_height
    global screen_width

    xpos = 20
    for i in range(0,11):
        if i == 0:
            boxLabel = Label(gameWindow,font={"Chalkboard SE",80},bg="red",width=2,height=1,borderwidth=0)

            boxLabel.place(x=xpos,y=screen_height/2-150)


            leftBoxes.append(boxLabel)
            xpos+=30
        
        else:
            boxLabel = Label(gameWindow,font={"Chalkboard SE",80},bg="white",width=2,height=2,borderwidth=0)

            boxLabel.place(x=xpos,y=screen_height/2-150)


            leftBoxes.append(boxLabel)
            xpos+=75

def createRightBoard():
    global gameWindow
    global rightBoxes
    global screen_height
    global screen_width

    xpos = 1100
    for i in range(0,11):
        if i == 10:
            boxLabel = Label(gameWindow,font={"Chalkboard SE",80},bg="blue",width=2,height=1,borderwidth=0)

            boxLabel.place(x=xpos,y=screen_height/2-150)


            rightBoxes.append(boxLabel)
            xpos+=30
        else:
            boxLabel = Label(gameWindow,font={"Chalkboard SE",80},bg="white",width=2,height=2,borderwidth=0)

            boxLabel.place(x=xpos,y=screen_height/2-150)


            rightBoxes.append(boxLabel)
            xpos+=75


def finishBox():
    global gameWindow
    global screen_height
    global screen_width
    global finishLine

    finishLine = Label(gameWindow,font={"Chalkboard SE",80},bg="green",width=8,height=4,borderwidth=0,text="Home")
    finishLine.place(x=screen_width/2-70,y=screen_height/2-150)


#Teacher write code here for askPlayerName()
def askPlayerName():
    global playerName
    global nameEntry
    global nameWindow 
    global canvas1 
    global  screen_height
    global screen_width

    nameWindow = Tk()
    nameWindow.title("Ludo Masters")
    nameWindow.attributes("-fullscreen",True)

    screen_width = nameWindow.winfo_screenwidth()
    screen_height=nameWindow.winfo_screenheight()

    bg=ImageTk.PhotoImage(file="./assets/background.png")

    canvas1 = Canvas(nameWindow,width=500,height=500)
    canvas1.pack(fill="both",expand=True)
    canvas1.create_image(0,0,image=bg,anchor="nw")
    canvas1.create_text(screen_width/2,screen_height/5,text="ENTER NAME",font={"Chalkboard SE",80},fill="white")

    nameEntry=Entry(nameWindow,width=25,justify="center",font={"Chalkboard SE",90},bg="white")
    nameEntry.place(x=screen_width/2-100,y=screen_height/3)    

    button= Button(nameWindow,text="save",font={"Chalkboard SE",90},bg="yellow",command=saveName)
    button.place(x=screen_width/2-30,y=screen_height/2)

    nameWindow.resizable(True,True)



    nameWindow.mainloop()


def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    PORT  = 8000
    IP_ADDRESS = '127.0.0.1'

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))


    # Creating First Window
    askPlayerName()




setup()
