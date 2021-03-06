import tkinter
import random
from tkinter.ttk import Progressbar
from tkinter import ttk
root=tkinter.Tk()
colours = ['Red','Blue','Green','Pink','Black', 
           'Yellow','Orange','White','Purple','Brown']
timeleft=60
score=0
def startGame(event):
    if timeleft==60:
        countdown()
    nextColour()

def nextColour():
    global score
    global timeleft

    if timeleft>0:
        e.focus_set()

        if e.get().lower()==colours[1].lower():
            score+=1
        e.delete(0,tkinter.END)

        random.shuffle(colours)

        label.config(fg=str(colours[1]),text=str(colours[0]))
        scoreLabel.config(text="Score:"+str(score))

def countdown():
    global timeleft

    if timeleft >0:
        timeleft-=1
        timeLabel.config(text="Time left:"+str(timeleft))
        bar['value']=100-timeleft*100/60
        if(timeleft <5):
            style.configure("black.Horizontal.TProgressbar", background='red')
        elif timeleft<10:
            style.configure("black.Horizontal.TProgressbar", background='yellow')
        else:
            style.configure("black.Horizontal.TProgressbar", background='green')

        timeLabel.after(1000,countdown)
    else:
        root.destroy()
        second=tkinter.Tk()
        second.title("Gameover")
        second.geometry("1350x700")
        GameOverLabel=tkinter.Label(text="Game Over",font=('Helvetica',30))
        GameScoreLabel=tkinter.Label(text="score is: "+str(score),font=('Helvetica',12))
        GameOverLabel.pack()
        GameScoreLabel.pack()
root.title("COLORGAME")
root.geometry("1350x700")

instructions = tkinter.Label(root, text = "Type in the colour"
                             "of the words, and not the word text!", 
                                      font = ('Helvetica', 12)) 
instructions.pack()
scoreLabel = tkinter.Label(root,text="Press enter to start",
                           font=('Helvetica',12))
scoreLabel.pack()

timeLabel = tkinter.Label(root,text = "Time left: "+ str(timeleft),
                          font=('Helvetica',12))
timeLabel.pack()

style = ttk.Style() 
style.theme_use('default') 
style.configure("black.Horizontal.TProgressbar", background='green')
bar = Progressbar(root,length=200,style='black.Horizontal.TProgressbar')
bar.pack()

label = tkinter.Label(root,font=('Helvetica',60))
label.pack()

e=tkinter.Entry(root)
root.bind('<Return>',startGame)
e.pack()
e.focus_set()
root.mainloop()
