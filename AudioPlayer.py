import tkinter as tk
from pygame import mixer as m
from pygame import time as t
from tkinter import filedialog, messagebox
import os
from sys import exit as kill

    
    
# Mixer ###################
m.init()
m.music.set_volume(0.5)
###########################

# Tkinter setup ###########
root = tk.Tk()
volume = tk.DoubleVar()


def file():
    file.count = 0
    file.audio = filedialog.askdirectory(title = "Choose the folder of music")
    m.music.load(file.audio + f"/{os.listdir(file.audio)[file.count]}")
def specificaudio():
     file.audio = filedialog.askopenfilename(title = "Pick your audio file")
     m.music.load(file.audio)
def startwithnextitem():
    try:
        file.count += 1
        for i in range(len(os.listdir(file.audio))):
            file.items = f"/{os.listdir(file.audio)[file.count]}"
            m.music.load(file.audio + file.items)
        m.music.play()
    except:
         print("No audio left to play. (Pressing start will play the last heard audio)")  
         tk.messagebox.showwarning("Uh oh", "No audio left to play. (Pressing start will play the last heard audio)")
def start():
     try:
        m.music.play()
     except:
        print("No audio loaded.")
        tk.messagebox.showwarning("Uh oh", "No audio loaded.")  
def pause():
    m.music.pause()
def unpause():
    m.music.unpause()
def volume_set():
    m.music.set_volume(volume.get())
def loop():
    m.music.play(-1)
def quit():
    kill()

# GUI
root.title("audio Player")
root.configure(bg="black")
root.minsize(250,125)
root.maxsize(250,125)
root.geometry("250x125+500+250")


choosefolder = tk.Button(text ="Choose folder", command = file, bg="grey", fg="white")
choosefolder.place(x=0,y=0)

choosespecific = tk.Button(text = "Choose specific audio", command = specificaudio, bg="grey", fg="white")
choosespecific.place(x=84,y=0)

volumeslider = tk.Scale( root, from_ = 0, to = 1, resolution = 0.01, orient = tk.HORIZONTAL, variable =  volume, bg="grey", fg="white", activebackground="grey")
volumeslider.place(x=144,y=83)

volumeset = tk.Button(text ="Set Volume", command = volume_set, bg="grey", fg="white")
volumeset.place(x=179.5,y=57)

start = tk.Button(text ="Start/Restart", command = start, bg="grey", fg="white")
start.place(x=0,y=25)

startwithnextitem = tk.Button(text = "Next", command = startwithnextitem, bg="grey", fg="white")
startwithnextitem.place(x=75,y=25)

pause = tk.Button(text ="Pause", command = pause, bg="grey", fg="white")
pause.place(x=0,y=50)

unpause = tk.Button(text ="Unpause", command = unpause, bg="grey", fg="white")
unpause.place(x=0,y=75)

loop = tk.Button(text = "Loop (restarts audio)", command = loop, bg="grey", fg="white")
loop.place(x=0,y=100)

quit = tk.Button(text="Quit",command=quit,bg="grey", fg="white")
quit.place(x=218,y=0)

root.mainloop()