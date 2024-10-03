#兌獎 #輸入 #還沒改
from tkinter import *
from tkinter import messagebox,ttk
import tkinter as tk
import tkinter.ttk as tt
from tkinter import IntVar



def printInfo():
     if (len(n1.get())==0 or len(n2.get())==0):
        messagebox.showwarning("warn!","開獎日、期別不可為空！！！")
     else:
        print(n1.get(),n2.get(),n3.get(),n4.get(),n5.get(),n6.get(),sep="\n")
        n1.set("")
        n2.set("")
        n3.set("")
        n4.set("")
        n5.set("")
        n6.set("")
        n7.set("")
        n8.set("")
def exist():
    n1.set("")
    n2.set("")
    n3.set("")
    n4.set("")
    n5.set("")
    n6.set("")
    n7.set("")
    n8.set("")


window = tk.Tk()
window.title("樂透了沒")

n1=StringVar()
n2=StringVar()
n3=StringVar()
n4=StringVar()
n5=StringVar()
n6=StringVar()
n7=StringVar()
n8=StringVar()


w=Canvas(window,width=600,height=700,background='#B8B8DC')
w.create_line(190,120,400,120,fill='#7373B9')
w.create_line(200,130,390,130,fill='#7373B9')
w.create_line(180,40,390,40,fill='#7373B9')
w.create_line(190,30,380,30,fill='#7373B9')
w.create_line(190,30,190,50,fill='#7373B9')
w.create_line(390,130,390,110,fill='#7373B9')
w.create_arc(208,162,158,112,fill='#7373B9')
w.create_arc(410,50,367,0,fill='#7373B9',start=180)
label = Label(window,text="樂透了沒",fg="#4F4FFF",bg='#FFABAB',width=8,
              font=("C:\Windows\Fonts\segoesc.ttf",35))
bnt1=Button(window,text="＃回主頁",fg='#0066FF',width=8,
            font=("C:\Windows\Fonts\segoesc.ttf",17)).place(x=450,y=630)
label3= Label(window,text="page 3",fg="black",bg='#B8B8DC',
              font=("C:\Windows\Fonts\segoesc.ttf",17)).place(x=270,y=630)

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

label1= Label(window,text="樂",fg="#484891",bg='#B8B8DC',
              font=("C:\Windows\Fonts\segoesc.ttf",28)).place(x=208,y=51)
label2= Label(window,text="透",fg="#484891",bg='#B8B8DC',
              font=("C:\Windows\Fonts\segoesc.ttf",28)).place(x=250,y=57)
label3= Label(window,text="了",fg="#484891",bg='#B8B8DC',
              font=("C:\Windows\Fonts\segoesc.ttf",28)).place(x=290,y=51)
label4= Label(window,text="沒",fg="#484891",bg='#B8B8DC',
              font=("C:\Windows\Fonts\segoesc.ttf",28)).place(x=330,y=57)
label5= Label(window,text="兌獎系統",fg="black",bg='#B8B8DC',
             width=8,font=("C:\Windows\Fonts\segoesc.ttf",20)).place(x=230,y=155)

label6=Label(window,text="種類",fg="black",bg='#D8D8EB',
             width=5,font=("C:\Windows\Fonts\segoesc.ttf",18)).place(x=151,y=195)
label5= Label(window,text="期別 :",fg="black",bg='#B8B8DC',
             width=5,font=("C:\Windows\Fonts\segoesc.ttf",18)).place(x=160,y=235)
e1=Entry(window,width=11,textvariable=n1).place(x=220,y=235)
label5= Label(window,text="ex:1111000045",fg="black",bg='#B8B8DC',
             font=("C:\Windows\Fonts\segoesc.ttf",12)).place(x=337,y=240)
label5= Label(window,text="開獎日 :",fg="black",bg='#B8B8DC',
             width=5,font=("C:\Windows\Fonts\segoesc.ttf",18)).place(x=151,y=275)
e2=Entry(window,width=11,textvariable=n2).place(x=220,y=275)
label5= Label(window,text="ex:2022/07/01",fg="black",bg='#B8B8DC',
             font=("C:\Windows\Fonts\segoesc.ttf",12)).place(x=337,y=280)
label5= Label(window,text="您的號碼 :",fg="black",bg='#B8B8DC',
             font=("C:\Windows\Fonts\segoesc.ttf",18)).place(x=145,y=310)
e3=Entry(window,width=6,textvariable=n3).place(x=178,y=355)
label5= Label(window,text="1 : ",fg="black",bg='#B8B8DC',
             font=("C:\Windows\Fonts\segoesc.ttf",18)).place(x=150,y=355)
e4=Entry(window,width=6,textvariable=n4).place(x=304,y=355)
label5= Label(window,text="2 : ",fg="black",bg='#B8B8DC',
             font=("C:\Windows\Fonts\segoesc.ttf",18)).place(x=270,y=355)
e5=Entry(window,width=6,textvariable=n5).place(x=304,y=405)
label5= Label(window,text="3 : ",fg="black",bg='#B8B8DC',
             font=("C:\Windows\Fonts\segoesc.ttf",18)).place(x=150,y=405)
e6=Entry(window,width=6,textvariable=n6).place(x=178,y=405)
label5= Label(window,text="4 : ",fg="black",bg='#B8B8DC',
             font=("C:\Windows\Fonts\segoesc.ttf",18)).place(x=270,y=405)
e7=Entry(window,width=6,textvariable=n7).place(x=304,y=455)
label5= Label(window,text="5 : ",fg="black",bg='#B8B8DC',
             font=("C:\Windows\Fonts\segoesc.ttf",18)).place(x=150,y=455)
e8=Entry(window,width=6,textvariable=n8).place(x=178,y=455)
label5= Label(window,text="6 : ",fg="black",bg='#B8B8DC',
             font=("C:\Windows\Fonts\segoesc.ttf",18)).place(x=270,y=455)
bnt2=Button(window,text="送出",fg='black',width=4,
            font=("C:\Windows\Fonts\segoesc.ttf",17),command=printInfo).place(x=170,y=525)
bnt2=Button(window,text="取消",fg='black',width=4,
            font=("C:\Windows\Fonts\segoesc.ttf",17),command=exist).place(x=290,y=525)

n1.set("")
n2.set("")
n3.set("")
n4.set("")
n5.set("")
n6.set("")
n7.set("")
n8.set("")




window.resizable(0,0)
w.pack()
window.mainloop()
