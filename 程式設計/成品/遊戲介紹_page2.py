from tkinter import *
from tkinter import messagebox,ttk
import tkinter as tk
import tkinter.ttk as tt

#page2
def play_info():
       
        def back():
                window.destroy()
        def show_test():
                import def測試
                def測試.show()
        def big_info():
                return"""從01~49中任選6個號碼進行投\n注。將隨機開出六個號碼加一
        個特別號。如果有三個以上(含\n三個號碼)對中當期開出之六個
        號碼(特別號只適用於貳獎、肆\n獎、陸獎和柒獎)即為中獎，可
        依規定兌領獎金。"""

        def super_info():
            return"""從第1個選號區中的01~38 號碼\n中任選6個號碼，並從第2個選
        號區中的01~08的號碼中任選1\n個號碼進行投注。將隨機從第\n1區開出六個號碼和第2區開出
        一個號碼。如對中當期第1區\n開出之任一個獎號和第2區也對
        中當期第2區開出之獎號即為中\n獎(普獎)，可依規定兌領獎金。"""

        def t539_info():
            return"""從01~39的號碼中任選5個號碼\n進行投注。將隨機開出五個中
        獎號碼，如有二個以上（含二\n個號碼）對中當期開出之五個
        號碼，即為中獎，並可依規定\n兌領獎金。"""

        def show_1():
                a=comboExample.get()
                if a=="大樂透":
                        lab1 = Label(window,text="大樂透介紹",fg="black",bg='#FFABAB',
                             width=10,font=18).place(x=215,y=290)
                        lab2=Label(window,text=big_info(),justify="left",anchor="ne",fg="black",bg='#FFABAB',
                             width=24,height=50,font=15).place(x=151,y=322)
                        lab3=Label(window,text="每注售價:50元",fg="black",bg='#FFABAB',
                             width=25,font=16).place(x=150,y=525)
                        lab4=Label(window,text="開獎時間:星期二、星期五",fg="black",bg='#FFABAB',
                             width=25,font=16).place(x=150,y=575)
                if a=="威力彩":
                        lab1 = Label(window,text="威力彩介紹",fg="black",bg='#FFABAB',
                             width=10,font=18).place(x=215,y=290)
                        lab2=Label(window,text=super_info(),justify="left",anchor="n",fg="black",bg='#FFABAB',
                                width=24,height=10,font=15).place(x=151,y=322)
                        lab3=Label(window,text="每注售價:100元",fg="black",bg='#FFABAB',
                             width=25,font=16).place(x=150,y=525)
                        lab4=Label(window,text="開獎時間:星期一、星期四",fg="black",bg='#FFABAB',
                             width=25,font=16).place(x=150,y=575)
                if a=="今彩539":
                        lab1 = Label(window,text="今彩539介紹",fg="black",bg='#FFABAB',
                             width=10,font=18).place(x=215,y=290)
                        lab2=Label(window,text=t539_info(),justify="left",anchor="ne",fg="black",bg='#FFABAB',
                             width=24,height=10,font=16).place(x=151,y=322)
                        lab3=Label(window,text="每注售價:50元",fg="black",bg='#FFABAB',
                             width=25,font=16).place(x=150,y=525)
                        lab4=Label(window,text="開獎時間:星期一至星期六",fg="black",bg='#FFABAB',
                             width=25,font=16).place(x=150,y=575)
                        
        window = tk.Tk()
        window.title("樂透了沒")
        w=Canvas(window,width=600,height=700,background='#FFABAB')
        w.create_line(190,120,400,120,fill='#FF3B3B')
        w.create_line(200,130,390,130,fill='#FF3B3B')
        w.create_line(180,40,390,40,fill='#FF3B3B')
        w.create_line(190,30,380,30,fill='#FF3B3B')
        w.create_line(190,30,190,50,fill='#FF3B3B')
        w.create_line(390,130,390,110,fill='#FF3B3B')
        w.create_arc(208,162,158,112,fill='#FF3B3B')
        w.create_arc(410,50,367,0,fill='#FF3B3B',start=180)
        lab1 = Label(window,text="請選擇彩券種類：",fg="black",bg='#FFABAB',width=15,font=("C:\Windows\Fonts\segoesc.ttf",15)).place(x=208,y=170)
        bnt1=Button(window,text="＃上一頁",fg='#0066FF',width=8,font=17,command=back).place(x=450,y=630)

        std=("大樂透", "威力彩","今彩539")
        comboExample = tt.Combobox(window,values=std,width=20,height=25,font=17)
        comboExample.place(x=185,y=210) 
        comboExample.current(0)
              
        
        w.create_polygon([120,210,150,250,90,250],fill='#8C8CFF',outline='#8C8CFF')
        w.create_polygon([120,330,150,370,90,370],fill='#FFABAB',outline='#8C8CFF')
        w.create_polygon([120,450,150,490,90,490],fill='#8C8CFF',outline='#8C8CFF')
        w.create_polygon([450,210,480,250,420,250],fill='#8C8CFF',outline='#8C8CFF')
        w.create_polygon([450,330,480,370,420,370],fill='#FFABAB',outline='#8C8CFF')
        w.create_polygon([450,450,480,490,420,490],fill='#8C8CFF',outline='#8C8CFF')

        lab2 = Button(window,text='確定',font=("C:\Windows\Fonts\segoesc.ttf",15),command=show_1).place(x=255,y=250) #確定

        label1= Label(window,text="樂",fg="#000085",bg='#E8C9FF',
               font=("C:\Windows\Fonts\segoesc.ttf",28)).place(x=208,y=51)

        label2= Label(window,text="透",fg="#000085",bg='#E8C9FF',
               font=("C:\Windows\Fonts\segoesc.ttf",28)).place(x=250,y=57)

        label2= Label(window,text="了",fg="#000085",bg='#E8C9FF',
               font=("C:\Windows\Fonts\segoesc.ttf",28)).place(x=290,y=51)

        label2= Label(window,text="沒",fg="#000085",bg='#E8C9FF',
               font=("C:\Windows\Fonts\segoesc.ttf",28)).place(x=330,y=57)

        w.pack()
        window.resizable(0,0)
        window.mainloop()

play_info()










