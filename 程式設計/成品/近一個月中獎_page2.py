#近一個月

from tkinter import *
from tkinter import messagebox,ttk
import tkinter as tk
import tkinter.ttk as tt
import requests
import bs4
import tkinter
def recent_lotto():
    def back():
        window3.destroy()
    def show_lotto():
        a=comboExample1.get()
        #大樂透
        #得到字典(鍵:期別 值0:開獎日 值1:兌獎截止日 值2~8:中獎號碼(由小到大) 值9:特別號)
        if a =="大樂透":
            url="https://www.taiwanlottery.com.tw/Lotto/Lotto649/history.aspx"
            a=requests.get(url)
            b=bs4.BeautifulSoup(a.text,"lxml")

            dict_value=[]
            dict_key=[]
            win=tkinter.Tk()
            win.title("大樂透")
            tree=ttk.Treeview(win,show='headings')#表格
            for x in range(0,50):
                if b.find(id=("Lotto649Control_history_dlQuery_No1_"+str(x)))==None:
                    break
                else:
                    w=[]
                    k=[]
                    k.append(b.find(id=("Lotto649Control_history_dlQuery_L649_DrawTerm_"+str(x))).text)
                    w.append(b.find(id=("Lotto649Control_history_dlQuery_L649_DDate_"+str(x))).text)
                    w.append(b.find(id=("Lotto649Control_history_dlQuery_L649_EDate_"+str(x))).text)
                    for y in range(1,7):
                        w.append(b.find(id=("Lotto649Control_history_dlQuery_No"+str(y)+"_"+str(x))).text)
                    w.append(b.find(id=("Lotto649Control_history_dlQuery_SNo_"+str(x))).text)
                    dict_value.append(w)
                    tree["columns"]=("期別","開獎日","兌獎日期","中獎號碼","特別號")
                    tree.column("期別",width=100)   #表示列,不顯示
                    tree.column("開獎日",width=100)
                    tree.column("兌獎日期",width=100)
                    tree.column("中獎號碼",width=150)
                    tree.column("特別號",width=100)

                    tree.heading("期別",text="期別")  #顯示錶頭
                    tree.heading("開獎日",text="開獎日")
                    tree.heading("兌獎日期",text="兌獎日期")
                    tree.heading("中獎號碼",text="中獎號碼")
                    tree.heading("特別號",text="特別號")
                    tree.insert("",1,values=(k[0],w[0],w[1],w[2:8],w[8])) #插入資料
    
            tree.pack()
            win.resizable(0,0)
            win.mainloop()
        #今彩539
        #得到字典(鍵:期別 值0:開獎日 值1:兌獎截止日 值2~7:中獎號碼)
        if a=="今彩539":
            url="https://www.taiwanlottery.com.tw/Lotto/Dailycash/history.aspx"
            a=requests.get(url)
            b=bs4.BeautifulSoup(a.text,"lxml")

            dict_value=[]
            dict_key=[]
            win=tkinter.Tk()
            win.title("今彩539")
            tree=ttk.Treeview(win,show='headings')#表格
            for x in range(0,50):
                if b.find(id=("D539Control_history1_dlQuery_D539_DrawTerm_"+str(x)))==None:
                    break
                else:
                    m=[]
                    n=[]
                    n.append(b.find(id=("D539Control_history1_dlQuery_D539_DrawTerm_"+str(x))).text)
                    m.append(b.find(id=("D539Control_history1_dlQuery_D539_DDate_"+str(x))).text)
                    m.append(b.find(id=("D539Control_history1_dlQuery_D539_EDate_"+str(x))).text)
                    for y in range(1,6):
                        m.append(b.find(id=("D539Control_history1_dlQuery_No"+str(y)+"_"+str(x))).text)
                    dict_value.append(m)
                    tree["columns"]=("期別","開獎日","兌獎日期","中獎號碼")
                    tree.column("期別",width=100)   #表示列,不顯示
                    tree.column("開獎日",width=100)
                    tree.column("兌獎日期",width=100)
                    tree.column("中獎號碼",width=150)

                    tree.heading("期別",text="期別")  #顯示錶頭
                    tree.heading("開獎日",text="開獎日")
                    tree.heading("兌獎日期",text="兌獎日期")
                    tree.heading("中獎號碼",text="中獎號碼")
                    tree.insert("",1,values=(n[0],m[0],m[1],m[2:8])) #插入資料
    
            tree.pack()
            win.resizable(0,0)
            win.mainloop()
        
        #威力彩
        #得到字典(鍵:期別 值0:開獎日 值1:兌獎截止日 值2~8:第一區(由小到大) 值9:第二區)
        if a=="威力彩":
            url="https://www.taiwanlottery.com.tw/Lotto/SuperLotto638/history.aspx"
            a=requests.get(url)
            b=bs4.BeautifulSoup(a.text,"lxml")

            dict_value=[]
            dict_key=[]
            win=tkinter.Tk()
            win.title("威力彩")
            tree=ttk.Treeview(win,show='headings')#表格
            for x in range(0,50):
                if b.find(id=("SuperLotto638Control_history1_dlQuery_DrawTerm_"+str(x)))==None:
                    break
                else:
                    p=[]
                    q=[]
                    q.append(b.find(id=("SuperLotto638Control_history1_dlQuery_DrawTerm_"+str(x))).text)
                    p.append(b.find(id=("SuperLotto638Control_history1_dlQuery_Date_"+str(x))).text)
                    p.append(b.find(id=("SuperLotto638Control_history1_dlQuery_EDate_"+str(x))).text)
                    for y in range(1,8):
                        p.append(b.find(id=("SuperLotto638Control_history1_dlQuery_No"+str(y)+"_"+str(x))).text)
                    dict_value.append(p)
                    tree["columns"]=("期別","開獎日","兌獎日期","第一區","第二區")
                    tree.column("期別",width=100)   #表示列,不顯示
                    tree.column("開獎日",width=100)
                    tree.column("兌獎日期",width=100)
                    tree.column("第一區",width=150)
                    tree.column("第二區",width=100)

                    tree.heading("期別",text="期別")  #顯示錶頭
                    tree.heading("開獎日",text="開獎日")
                    tree.heading("兌獎日期",text="兌獎日期")
                    tree.heading("第一區",text="第一區")
                    tree.heading("第二區",text="第二區")
                    tree.insert("",1,values=(q[0],p[0],p[1],p[2:8],p[8])) #插入資料
    
            tree.pack()
            win.resizable(0,0)
            win.mainloop()
       

    window3 = Tk()
    window3.title("樂透了沒")
    n2=StringVar()
    w=Canvas(window3,width=600,height=700,background='#ACD6FF')
    w.create_line(190,120,400,120,fill='#009393')
    w.create_line(200,130,390,130,fill='#009393')
    w.create_line(180,40,390,40,fill='#009393')
    w.create_line(190,30,380,30,fill='#009393')
    w.create_line(190,30,190,50,fill='#009393')
    w.create_line(390,130,390,110,fill='#009393')
    w.create_arc(208,162,158,112,fill='#009393')
    w.create_arc(410,50,367,0,fill='#009393',start=180)

    w.create_rectangle(90,210,140,260,fill='#00CACA',outline='#00CACA')
    w.create_rectangle(90,325,140,375,outline='#00CACA')
    w.create_rectangle(90,436,140,486,fill='#00CACA',outline='#00CACA')
    w.create_rectangle(450,210,500,260,fill='#00CACA',outline='#00CACA')
    w.create_rectangle(450,325,500,375,outline='#00CACA')
    w.create_rectangle(450,436,500,486,fill='#00CACA',outline='#00CACA')


    label0=Label(window3,text="近一個月開獎號碼",fg='black',bg='#ACD6FF',
            font=("C:\Windows\Fonts\segoesc.ttf",18)).place(x=190,y=160)
    std2=("大樂透","今彩539","威力彩")
    comboExample1 = tt.Combobox(window3,values=std2,font=("C:\Windows\Fonts\segoesc.ttf",18))
    comboExample1.current(0)
    lab2 = Button(window3,text='確定',font=("C:\Windows\Fonts\segoesc.ttf",16),command=show_lotto).place(x=250,y=270)
    comboExample1.place(x=170,y=210)

    bnt1=Button(window3,text="＃上一頁",fg='#0066FF',width=8,
            font=("C:\Windows\Fonts\segoesc.ttf",17),command=back).place(x=450,y=630)


    label1= Label(window3,text="樂",fg="#003E3E",bg='#ACD6FF',
               font=("C:\Windows\Fonts\segoesc.ttf",28)).place(x=208,y=51)
    label2= Label(window3,text="透",fg="#003E3E",bg='#ACD6FF',
               font=("C:\Windows\Fonts\segoesc.ttf",28)).place(x=250,y=57)
    label2= Label(window3,text="了",fg="#003E3E",bg='#ACD6FF',
               font=("C:\Windows\Fonts\segoesc.ttf",28)).place(x=290,y=51)
    label2= Label(window3,text="沒",fg="#003E3E",bg='#ACD6FF',
               font=("C:\Windows\Fonts\segoesc.ttf",28)).place(x=330,y=57)
    label3= Label(window3,text="page 2",fg="black",bg='#ACD6FF',
               font=("C:\Windows\Fonts\segoesc.ttf",17)).place(x=270,y=630)


    w.pack()
    window3.resizable(0,0)
    window3.mainloop()

recent_lotto()




