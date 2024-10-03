#首頁
from tkinter import *
from tkinter import messagebox,ttk
import tkinter as tk
import tkinter.ttk as tt
import requests
import bs4
import tkinter

def playinfo_page():
    import 遊戲介紹_page2
def recentinfo_page():
    import 近一個月中獎_page2
def winningsystem_page():
    import 對獎系統_page2
window = Tk()
window.title("樂透了沒")
w=Canvas(window,width=600,height=700,background='#FFDDAA')
w.create_line(190,120,400,120,fill='#FF8800')
w.create_line(200,130,390,130,fill='#FF8800')
w.create_line(180,40,390,40,fill='#FF8800')
w.create_line(190,30,380,30,fill='#FF8800')
w.create_line(190,30,190,50,fill='#FF8800')
w.create_line(390,130,390,110,fill='#FF8800')
w.create_arc(208,162,158,112,fill='#FF8800')
w.create_arc(410,50,367,0,fill='#FF8800',start=180)

w.create_oval(90,210,140,260,fill='#FF8888',outline='#FF8888')
w.create_oval(90,325,140,375,outline='#FF8888')
w.create_oval(90,436,140,486,fill='#FF8888',outline='#FF8888')
w.create_oval(450,210,500,260,fill='#FF8888',outline='#FF8888')
w.create_oval(450,325,500,375,outline='#FF8888')
w.create_oval(450,436,500,486,fill='#FF8888',outline='#FF8888')




bnt1=Button(window,text="彩券介紹",fg='black',
            font=("C:\Windows\Fonts\segoesc.ttf",28),command=playinfo_page).place(x=220,y=220)

bnt1=Button(window,text="近一個月開獎號碼",fg='black',
            font=("C:\Windows\Fonts\segoesc.ttf",28),command=recentinfo_page).place(x=165,y=330)

bnt1=Button(window,text="對獎系統",fg='black',
            font=("C:\Windows\Fonts\segoesc.ttf",28),command=winningsystem_page).place(x=220,y=440)

bnt1=Button(window,text="＃回主頁",fg='#0066FF',width=8,
            font=("C:\Windows\Fonts\segoesc.ttf",17)).place(x=450,y=630)


label1= Label(window,text="樂",fg="#FF5511",bg='#FFDDAA',
               font=("C:\Windows\Fonts\segoesc.ttf",33)).place(x=210,y=50)

label2= Label(window,text="透",fg="#FF5511",bg='#FFDDAA',
               font=("C:\Windows\Fonts\segoesc.ttf",33)).place(x=250,y=56)

label2= Label(window,text="了",fg="#FF5511",bg='#FFDDAA',
               font=("C:\Windows\Fonts\segoesc.ttf",33)).place(x=290,y=50)

label2= Label(window,text="沒",fg="#FF5511",bg='#FFDDAA',
               font=("C:\Windows\Fonts\segoesc.ttf",33)).place(x=330,y=56)

label3= Label(window,text="page 1",fg="black",bg='#FFDDAA',
               font=("C:\Windows\Fonts\segoesc.ttf",17)).place(x=270,y=630)



w.pack()
window.resizable(0,0)
window.mainloop()
