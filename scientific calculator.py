#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pygame


# In[2]:


pip install pyaudio


# In[3]:


pip install speechrecognition


# In[1]:


# importing the required libraries
from tkinter import *
import math
import tkinter.messagebox
from pygame import mixer

import speech_recognition


# In[4]:


# setting thwe window layout
root = Tk() 
root.geometry('500x500')
root.title('Scientific Calculator')
root.iconbitmap('C:\\Users\\hp\\Downloads\\text-logo.ico')

mixer.init()
# logics
def pi():
    if display.get()=='0':
        display.delete(0,END)
        pos = len(display.get())
        display.insert(pos, str(math.pi))

def fact():
    try:
        fac= float(display.get())
        fac= math.factorial(fac)
        display.delete(0,END)
        display.insert(0,str(fac))
    except exception:
        tkinter.messagebox.showerror('error')

def sin():
    try:
        si= float(display.get())
        si= math.sin(si)
        display.delete(0,END)
        display.insert(0,si)
    except exception:
        tkinter.messgaebox.error('error')
        
        
def cos():
    try:
        co= float(display.get())
        co= math.cos(co)
        display.delete(0,END)
        display.insert(0,co)
    except exception:
        tkinter.messgaebox.error('error')        
        
def tan():
    try:
        ta= float(display.get())
        ta= math.tan(ta)
        display.delete(0,END)
        display.insert(0,ta)
    except exception:
        tkinter.messgaebox.error('error')  
        
def butn1():
    if display.get()=='0':
        display.delete(0,END)

    pos = len(display.get())
    display.insert(pos,'1')
        
def butn2():
    if display.get()=='0':
        display.delete(0,END)

    pos = len(display.get())
    display.insert(pos,'2')        
        
def butn3():
    if display.get()=='0':
        display.delete(0,END)

    pos = len(display.get())
    display.insert(pos,'3')        
        
def add():
    pos=len(display.get())
    display.insert(pos,'+')

# for frame 2
def ep():
    if display.get()=='0':
        display.delete(0,END)
        pos = len(display.get())
        display.insert(pos, str(math.e))
            
        
def sqrt():
    try:
        sq=float(display.get())
        sq=math.sqrt(sq)
        display.delete(0,END)
        display.insert(0,sq)
    except exception:
        tkinter.messagebox.error('error')
        
def sin1():
    try:
        asp=float(display.get())
        asp=math.asin(asp)
        display.delete(0,END)
        display.insert(0,asp)
    except exception:
        tkinter.messagebox.error('error')
        
def cos1():
    try:
        acp=float(display.get())
        acp=math.acos(acp)
        display.delete(0,END)
        display.insert(0,acp)
    except exception:
        tkinter.messagebox.error('error')
        
def tan1():
    try:
        atp=float(display.get())
        atp=math.asin(atp)
        display.delete(0,END)
        display.insert(0,atp)
    except exception:
        tkinter.messagebox.error('error')
        
def butn4():
    if display.get()=='0':
        display.delete(0,END)

    pos = len(display.get())
    display.insert(pos,'4') 
    
def butn5():
    if display.get()=='0':
        display.delete(0,END)

    pos = len(display.get())
    display.insert(pos,'5') 
    
def butn6():
    if display.get()=='0':
        display.delete(0,END)

    pos = len(display.get())
    display.insert(pos,'6') 
    
def sub():
    pos=len(display.get())
    display.insert(pos,'-')
    
#for frame 3
def rad():
    try:
        ra=float(display.get())
        ra=math.radians(ra)
        display.delete(0,END)
        display.insert(0,ra)
    except exception:
        tkinter.messagebox.error('error')
        
def roud():
    try:
        rod=float(display.get())
        rod= round(rod)
        display.delete(0,END)
        display.insert(0,rod)
    except exception:
        tkinter.messagebox.error('error')
        
def log():
    try:
        lo=float(display.get())
        lo=math.log10(lo)
        display.delete(0,END)
        display.insert(0,str(lo))
    except exception:
        tkinter.messagebox.error('error')
        
def logn():
    try:
        lm=float(display.get())
        lm=math.log(lm)
        display.delete(0,END)
        display.insert(0,str(lm))
    except exception:
        tkinter.messagebox.error('error')
        
def pow():
    if display.get()=='0':
        display.delete(0,END)
        pos=len(display.get())
        display.insert(pos,'**')
        

        
def butn7():
    if display.get()=='0':
        display.delete(0,END)

    pos = len(display.get())
    display.insert(pos,'7') 
    
def butn8():
    if display.get()=='0':
        display.delete(0,END)

    pos = len(display.get())
    display.insert(pos,'8') 
    
def butn9():
    if display.get()=='0':
        display.delete(0,END)

    pos = len(display.get())
    display.insert(pos,'9') 
    
def mul():
    pos=len(display.get())
    display.insert(pos,'*')

    
# for frame 4

def perc():
    pos=len(display.get())
    display.insert(pos,'%')
    
def obrc():
    pos=len(display.get())
    display.insert(pos,'(')
    
def cbrc():
    pos=len(display.get())
    display.insert(pos,')') 
    
def decimal():
    pos=len(display.get())
    display.insert(pos,'.')
    
def eq():
    try:
        eql=display.get()
        eql=eval(eql)
        display.delete(0,END)
        display.insert(0,eql)
    except exception:
        tkinter.messagebox.error("error")
        
def butn0():
    if display.get()=='0':
        display.delete(0,END)

    pos = len(display.get())
    display.insert(pos,'0')
    
def bksp():
    pos=len(display.get())
    disp=str(display.get())
    if disp=='':
        display.insert(0,'0')
    elif disp==' ':
        display.insert(0,'0')
    elif disp=='0':
        pass
    else:
        display.delete(0,END)
        display.insert(0,disp[0:pos-1])
        
    
    
def cl():
    pos=len(display.get())
    display.delete(0,END)
    display.insert(pos,'0')
    
def div():
    pos=len(display.get())
    display.insert(pos,'/')
#voice recognition

def add(a,b):
    return a+b
def sub(a,b):
    return a-b

def mul(a, b):
    return a * b
def div(a, b):
    return a / b

operations={'ADD':add,'ADDITION':add,'SUM':add,'PLUS':add,
            'SUBTRACTION':sub , 'DIFFERENCE':sub , 'MINUS':sub , 'SUBTRACT':sub,
            'PRODUCT': mul, 'MULTIPLICATION': mul,'MULTIPLY': mul,
            'DIVISION': div, 'DIV': div, 'DIVIDE': div }


def findNumbers(t):
    l=[]
    for num in t:
        try:
            l.append(int(num))
        except ValueError:
            pass
    return l


def audio():
    mixer.music.load('C:\\Users\\hp\\Downloads\\harsh python\\music1.mp3')
    mixer.music.play()
    sr = speech_recognition.Recognizer()
    with speech_recognition.Microphone()as m:
        try:
            sr.adjust_for_ambient_noise(m,duration=0.2)
            voice=sr.listen(m)
            text=sr.recognize_google(voice)

            mixer.music.load('C:\\Users\\hp\\Downloads\\harsh python\\music2.mp3')
            mixer.music.play()
            text_list=text.split(' ')
            for word in text_list:
                if word.upper() in operations.keys():
                    l=findNumbers(text_list)
                    result=operations[word.upper()](l[0],l[1]) #mul(5.0,6.0)
                    display.delete(0,END)
                    display.insert(0,int(result))

                else:
                    pass


        except:
            pass

    
# Adding the entry box and customizing it according
display= Entry(root , font= 'Ariel', fg='black', bg="light green", bd = 5, justify= RIGHT)
display.insert(0, "0")
display.pack(expand = True, fill=BOTH, side= TOP)

micImage=PhotoImage(file='C:\\Users\\hp\\Downloads\\harsh python\\microphone.png',master=root)
micButton = Button(root,image=micImage, bd=0, bg='dodgerblue3',command=audio, activebackground='dodgerblue3')
micButton.pack(expand=True, fill=BOTH)

# adding the button

# make the frame 1
row1 = Frame(root, bg='#000000')
row1.pack(expand= True, fill=BOTH)
# adding the button to frame 1
pi_butn=Button(row1,text='π',font='segoe 18',relief=RIDGE,fg="white",command= pi,bg="black").pack(expand= True , fill=BOTH, side=LEFT)
fact_butn=Button(row1,text='x!',font='segoe 18',relief=RIDGE,fg="white",command= fact ,bg="black").pack(expand= True , fill=BOTH, side=LEFT)
sin_butn=Button(row1,text='Sin',font='segoe 18',relief=RIDGE,fg="white", command = sin, bg="black").pack(expand= True , fill=BOTH, side=LEFT)
cos_butn=Button(row1,text='Cos',font='segoe 18',relief=RIDGE, fg="white",command= cos, bg="black").pack(expand= True , fill=BOTH, side=LEFT)
tan_butn=Button(row1,text='Tan',font='segoe 18',relief=RIDGE,fg="white",command= tan, bg="black").pack(expand= True , fill=BOTH, side=LEFT)
butn_1=Button(row1,text=1,font='segoe 18',relief=RIDGE,fg="white", command= butn1 ,bg="black").pack(expand= True , fill=BOTH, side=LEFT)
butn_2=Button(row1,text=2,font='segoe 18',relief=RIDGE, fg="white",command= butn2, bg="black").pack(expand= True , fill=BOTH, side=LEFT)
butn_3=Button(row1,text=3,font='segoe 18',relief=RIDGE,fg="white",command= butn3, bg="black").pack(expand= True , fill=BOTH, side=LEFT)
butn_add=Button(row1,text='+',font='segoe 18',relief=RIDGE,fg="white", command= add, bg="black").pack(expand= True , fill=BOTH, side=LEFT)


# make the frame 2
row2 = Frame(root, bg='#000000')
row2.pack(expand= True, fill=BOTH)
# adding the button to frame 1
butn_exp=Button(row2,text='e',font='segoe 18',relief=RIDGE, fg="white",command= ep, bg="black").pack(expand= True , fill=BOTH, side=LEFT)
root_butn=Button(row2,text='x',font='segoe 18',relief=RIDGE, fg="white",command= sqrt, bg="black").pack(expand= True , fill=BOTH, side=LEFT)
sin1_butn=Button(row2,text='Sin-1',font='segoe 18',relief=RIDGE,fg="white",command= sin1, bg="black").pack(expand= True , fill=BOTH, side=LEFT)
cos1_butn=Button(row2,text='Cos-1',font='segoe 18',relief=RIDGE,fg="white",command=cos1 ,bg="black").pack(expand= True , fill=BOTH, side=LEFT)
tan1_butn=Button(row2,text='Tan-1',font='segoe 18',relief=RIDGE,fg="white",command=tan1 ,bg="black").pack(expand= True , fill=BOTH, side=LEFT)
butn_4=Button(row2,text=4,font='segoe 18',relief=RIDGE,fg="white",command= butn4, bg="black").pack(expand= True , fill=BOTH, side=LEFT)
butn_5=Button(row2,text=5,font='segoe 18',relief=RIDGE,fg="white",command= butn5, bg="black").pack(expand= True , fill=BOTH, side=LEFT)
butn_6=Button(row2,text=6,font='segoe 18',relief=RIDGE,fg="white",command= butn6, bg="black").pack(expand= True , fill=BOTH, side=LEFT)
butn_sub=Button(row2,text='-',font='segoe 18',relief=RIDGE,fg="white",command=sub, bg="black").pack(expand= True , fill=BOTH, side=LEFT)


#make the frame 3
row3 = Frame(root, bg='#000000')
row3.pack(expand= True, fill=BOTH)
# adding the button to frame 1
rd_butn=Button(row3,text='Rad',font='segoe 18',relief=RIDGE,fg="white",command=rad, bg="black").pack(expand= True , fill=BOTH, side=LEFT)
round_butn=Button(row3,text='Round',font='segoe 18',relief=RIDGE,fg="white",command=roud, bg="black").pack(expand= True , fill=BOTH, side=LEFT)
ln_butn=Button(row3,text='ln',font='segoe 18',relief=RIDGE,fg="white",command=logn, bg="black").pack(expand= True , fill=BOTH, side=LEFT)
log_butn=Button(row3,text='log',font='segoe 18',relief=RIDGE,fg="white", command=log, bg="black").pack(expand= True , fill=BOTH, side=LEFT)
xy_butn=Button(row3,text='x^y',font='segoe 18',relief=RIDGE,fg="white",command=pow, bg="black").pack(expand= True , fill=BOTH, side=LEFT)
butn_7=Button(row3,text=7,font='segoe 18',relief=RIDGE,fg="white",command=butn7, bg="black").pack(expand= True , fill=BOTH, side=LEFT)
butn_8=Button(row3,text=8,font='segoe 18',relief=RIDGE,fg="white",command=butn8,bg="black").pack(expand= True , fill=BOTH, side=LEFT)
butn_9=Button(row3,text=9,font='segoe 18',relief=RIDGE, fg="white",command=butn9, bg="black").pack(expand= True , fill=BOTH, side=LEFT)
butn_mul=Button(row3,text='*',font='segoe 18',relief=RIDGE,fg="white",command=mul, bg="black").pack(expand= True , fill=BOTH, side=LEFT)


#make the frame 4
row4 = Frame(root, bg='#000000')
row4.pack(expand= True, fill=BOTH)
# adding the button to frame 1
per_butn=Button(row4,text='%',font='segoe 18',relief=RIDGE, fg="white",command=perc, bg="black").pack(expand= True , fill=BOTH, side=LEFT)
brc1_butn=Button(row4,text='(',font='segoe 18',relief=RIDGE,fg="white",command=obrc, bg="black").pack(expand= True , fill=BOTH, side=LEFT)
brc2_butn=Button(row4,text=')',font='segoe 18',relief=RIDGE, fg="white",command=cbrc, bg="black").pack(expand= True , fill=BOTH, side=LEFT)
butn_dec=Button(row4,text='.',font='segoe 18',relief=RIDGE, fg="white",command=decimal, bg="black").pack(expand= True , fill=BOTH, side=LEFT)
butn_clr=Button(row4,text='C',font='segoe 18',relief=RIDGE,fg="white",command=cl, bg="black").pack(expand= True , fill=BOTH, side=LEFT)
butn_backspace=Button(row4,text='Bkspc',font='segoe 18',relief=RIDGE,fg="white",command=bksp, bg="black").pack(expand= True , fill=BOTH, side=LEFT)
butn_zero=Button(row4,text='0',font='segoe 18',relief=RIDGE, fg="white",command=butn0, bg="black").pack(expand= True , fill=BOTH, side=LEFT)
butn_equal=Button(row4,text='=',font='segoe 18',relief=RIDGE,fg="white",command= eq, bg="red").pack(expand= True , fill=BOTH, side=LEFT)
butn_div=Button(row4,text="/",font='segoe 18',relief=RIDGE,fg="white",command=div, bg="black").pack(expand= True , fill=BOTH, side=LEFT)
                
#terminating the window
root.mainloop()


# In[ ]:





# In[ ]:




