import tkinter as tk
from  tkinter import ttk
from tkinter import*
from tkinter import filedialog
from PIL import Image
import pyttsx3
import os

root=Tk()
root.title("text to speech")
root.geometry("900x600")
root.resizable(False,False)
root.configure(bg="#305065")

engine = pyttsx3.init()
def speaknow():
    text = text_area.get(1.0,END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')
    def setvoice():
        if(gender == 'MALE'):
            engine.setProperty('voice',voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice',voices[1].id)
            engine.say(text)
            engine.runAndWait()
    if(text):
        if(speed=="Fast"):
            engine.setProperty('rate',250)
            setvoice()
        elif(speed=="Normal"):
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()
def download():
     text = text_area.get(1.0,END)
     gender = gender_combobox.get()
     speed = speed_combobox.get()
     voices = engine.getProperty('voices')
     def setvoice():
        if(gender == 'MALE'):
            engine.setProperty('voice',voices[0].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()
        else:
            engine.setProperty('voice',voices[1].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()
     if(text):
        if(speed=="Fast"):
            engine.setProperty('rate',250)
            setvoice()
        elif(speed=="Normal"):
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()
    


#top frame
Top_frame=Frame(root,bg="white",width=1100,height=150)
Top_frame.place(x=0,y=0)

Logo1=PhotoImage(file='speaker.png')
Label(Top_frame,image=Logo1,bg="white").place(x=-10,y=-50)

Label(Top_frame,text="TEXT TO SPEECH",font=("algerian",55),bg="white",fg="black").place(x=280,y=30)


####
text_area=Text(root,font=("algerian",20),bg="white",relief=GROOVE,wrap=WORD)
text_area.place(x=10,y=230,width=500,height=280)

Label(root,text="VOICE",font="algerian 15 bold",bg="#305065",fg="white").place(x=580,y=220)
Label(root,text="SPEED",font="algerian 15 bold",bg="#305065",fg="white").place(x=780,y=220)




gender_combobox= ttk.Combobox(root,values=['MALE','FEMALE'],font="algerian",state='r',width=10)
gender_combobox.place(x=550,y=250)
gender_combobox.set('MALE')


speed_combobox= ttk.Combobox(root,values=['FAST','NORMAL','SLOW'],font="algerian",state='r',width=10)
speed_combobox.place(x=730,y=250)
speed_combobox.set('NORMAL')



btn=Button(root,text="SPEAK",command=speaknow,width=10,font="algerian 14",bg="white")
btn.place(x=550,y=350)

btn=Button(root,text="Download",command=download,width=10,font="algerian 14",bg="white")
btn.place(x=730,y=350)


root.mainloop()
