#第二頁彩卷選單
import tkinter
import tkinter as tk
from tkinter import *
import tkinter.ttk as tt
from  tkinter import ttk
import requests,bs4,re,datetime
from tkinter import messagebox,ttk

def winning_info():
        def big():
                import 大樂透對獎
        def super():
                import 威力彩對獎
        def today():
                import 今彩539對獎
        def back():
                window4.destroy()
        
        window4 = tk.Tk()
        window4.title("樂透了沒")

        w=Canvas(window4,width=600,height=700,bg="#B8B8DC")
        w.create_line(190,120,400,120,fill='#7373B9')
        w.create_line(200,130,390,130,fill='#7373B9')
        w.create_line(180,40,390,40,fill='#7373B9')
        w.create_line(190,30,380,30,fill='#7373B9')
        w.create_line(190,30,190,50,fill='#7373B9')
        w.create_line(390,130,390,110,fill='#7373B9')
        w.create_arc(208,162,158,112,fill='#7373B9')
        w.create_arc(410,50,367,0,fill='#7373B9',start=180)
        bnt1=Button(window4,text="＃上一頁",fg='#0066FF',width=8,
            font=("C:\Windows\Fonts\segoesc.ttf",17),command=back).place(x=450,y=650)
        label3= Label(window4,text="page 2",fg="black",bg='#B8B8DC',
              font=("C:\Windows\Fonts\segoesc.ttf",17)).place(x=260,y=650)

        w.create_polygon([120,220,140,250,100,250],fill='#AE57A4',outline='#AE57A4')
        w.create_polygon([120,280,140,250,100,250],fill='#AE57A4',outline='#AE57A4')
        w.create_polygon([120,340,140,370,100,370],fill='#AE57A4',outline='#AE57A4')
        w.create_polygon([120,400,140,370,100,370],fill='#AE57A4',outline='#AE57A4')
        w.create_polygon([120,460,140,490,100,490],fill='#AE57A4',outline='#AE57A4')
        w.create_polygon([120,520,140,490,100,490],fill='#AE57A4',outline='#AE57A4')
        w.create_polygon([450,220,470,250,430,250],fill='#AE57A4',outline='#AE57A4')
        w.create_polygon([450,280,470,250,430,250],fill='#AE57A4',outline='#AE57A4')
        w.create_polygon([450,340,470,370,430,370],fill='#AE57A4',outline='#AE57A4')
        w.create_polygon([450,400,470,370,430,370],fill='#AE57A4',outline='#AE57A4')
        w.create_polygon([450,460,470,490,430,490],fill='#AE57A4',outline='#AE57A4')
        w.create_polygon([450,520,470,490,430,490],fill='#AE57A4',outline='#AE57A4')

        label1= Label(window4,text="樂",fg="#484891",bg='#B8B8DC',
              font=("C:\Windows\Fonts\segoesc.ttf",28)).place(x=208,y=51)
        label2= Label(window4,text="透",fg="#484891",bg='#B8B8DC',
              font=("C:\Windows\Fonts\segoesc.ttf",28)).place(x=250,y=57)
        label3= Label(window4,text="了",fg="#484891",bg='#B8B8DC',
              font=("C:\Windows\Fonts\segoesc.ttf",28)).place(x=290,y=51)
        label4= Label(window4,text="沒",fg="#484891",bg='#B8B8DC',
              font=("C:\Windows\Fonts\segoesc.ttf",28)).place(x=330,y=57)
        label5= Label(window4,text="對獎系統",fg="black",bg='#B8B8DC',
             width=14,font=("C:\Windows\Fonts\segoesc.ttf",24)).place(x=162,y=155)
        bnt1=Button(window4,text="大樂透",fg="black",width=8,
            font=("C:\Windows\Fonts\segoesc.ttf",28),command=big).place(x=205,y=250)
        bnt1=Button(window4,text="威力彩",fg="black",width=8,
            font=("C:\Windows\Fonts\segoesc.ttf",28),command=super).place(x=205,y=350)
        bnt1=Button(window4,text="今彩539",fg="black",width=8,
            font=("C:\Windows\Fonts\segoesc.ttf",28),command=today).place(x=205,y=450)
        w.pack()
        window4.resizable(0,0)
        window4.mainloop()

winning_info()

