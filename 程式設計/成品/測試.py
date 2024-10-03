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
            url="https://www.taiwanlottery.com.tw/Lotto/Dailycash/history.aspx"
            a=requests.get(url)
            b=bs4.BeautifulSoup(a.text,"lxml")

            dict_value=[]
            dict_key=[]
            for x in range(0,50):
                if b.find(id=("D539Control_history1_dlQuery_D539_DrawTerm_"+str(x)))==None:
                    break
                else:
                    w=[]
                    k=[]
                    k.append(b.find(id=("D539Control_history1_dlQuery_D539_DrawTerm_"+str(x))).text)
                    dict_key.append(b.find(id=("D539Control_history1_dlQuery_D539_DrawTerm_"+str(x))).text)
                    w.append(b.find(id=("D539Control_history1_dlQuery_D539_DDate_"+str(x))).text)
                    w.append(b.find(id=("D539Control_history1_dlQuery_D539_EDate_"+str(x))).text)
                    for y in range(1,6):
                        w.append(b.find(id=("D539Control_history1_dlQuery_No"+str(y)+"_"+str(x))).text)
                    dict_value.append(w)
            m=dict(zip(dict_key,dict_value))

###爬一個月###
            def exist():
                n1.set("")
                n3.set("")
                n4.set("")
                n5.set("")
                n6.set("")
                n7.set("")
        
            window = tk.Tk()
            window.title("樂透了沒")

            n1=StringVar()
            n1.set("")
            n3=StringVar()
            n3.set("")
            n4=StringVar()
            n4.set("")
            n5=StringVar()
            n5.set("")
            n6=StringVar()
            n6.set("")
            n7=StringVar()
            n7.set("")

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
              font=35)
            bnt1=Button(window,text="＃上一頁",fg='#0066FF',width=8,
            font=16,command=window.destroy).place(x=400,y=610)
            label3= Label(window,text="page 3",fg="black",bg='#B8B8DC',
              font=17).place(x=250,y=610)

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
            label5= Label(window,text="今彩539兌獎系統",fg="black",bg='#B8B8DC',
             width=15,font=("C:\Windows\Fonts\segoesc.ttf",20)).place(x=185,y=155)

            label5= Label(window,text="期別 :",fg="black",bg='#B8B8DC',
             width=5,font=16).place(x=160,y=235)
            e1=Entry(window,width=15,textvariable=n1,font=16).place(x=220,y=235)#期別
            label5= Label(window,text="ex:111000128",fg="black",bg='#B8B8DC',
             font=3).place(x=220,y=265)

            label5=Label(window,text="您的號碼 :",fg="black",bg='#B8B8DC',
             font=16).place(x=145,y=315)
            e3=Entry(window,width=6,textvariable=n3,font=16).place(x=194,y=360)#1
            label5= Label(window,text="1 : ",fg="black",bg='#B8B8DC',
             font=16).place(x=160,y=360)
            e4=Entry(window,width=6,textvariable=n4,font=16).place(x=314,y=360)#2
            label5= Label(window,text="2 : ",fg="black",bg='#B8B8DC',
             font=16).place(x=280,y=360)
            e5=Entry(window,width=6,textvariable=n5,font=16).place(x=314,y=410)#4
            label5= Label(window,text="3 : ",fg="black",bg='#B8B8DC',
             font=16).place(x=160,y=410)
            e6=Entry(window,width=6,textvariable=n6,font=16).place(x=194,y=410)#3
            label5= Label(window,text="4 : ",fg="black",bg='#B8B8DC',
             font=16).place(x=280,y=410)
            e7=Entry(window,width=6,textvariable=n7,font=16).place(x=194,y=460)#5
            label5= Label(window,text="5 : ",fg="black",bg='#B8B8DC',
            font=16).place(x=160,y=460)
            global u1
            global u3
            global u4
            global u5
            global u6
            global u7
            u1=n1.get()
            u3=n3.get()
            u4=n4.get()
            u5=n5.get()
            u6=n6.get()
            u7=n7.get()
     #"測試用的期別:111000136,中獎號碼:06,17,23,29,38"
            def win():#兌獎系統
                 s_list=[u3,u4,u5,u6,u7]#使用者號碼
                 s_list2=s_list[:]
                 while "" in s_list:#刪除空值
                      s_list.remove("")
                 for i in s_list:
                      if int(i)<1 or int(i)>39:
                          s_list.remove(i)
                          s_list2.remove(i)
                 s_list=s_list2
                 s_set=set(s_list)#轉換成set型態刪除重複值
                 s=list(s_set)
                 if (len(u1)!=9):#判斷期別值是否有誤
                      messagebox.showwarning("warn!","期別有誤！！！")
                      exist()
                 elif (len(s)!=5):#判斷s串列號碼是有5個
                      messagebox.showwarning("warn!","輸入值有誤、有少或重複！！！")
                      exist()
                 
                 elif u1 in m:
                      G=m.get(u1)
                      del G[0:2]
                      same_num1=[]
                      for i in s:
                          if i in G:
                              same_num1.append(i)
                      same_num_1 = len(same_num1)
                      subject="今彩539中獎查詢"
                      if same_num_1 == 5  :
                           messagebox.showinfo("","恭喜老爺，賀喜夫人中頭獎!!!")
                           exist()
                      elif same_num_1 == 4:
                           messagebox.showinfo("","恭喜你中了貳獎")
                           exist()
                      elif same_num_1 == 3:
                           messagebox.showinfo("","恭喜你中了參獎")
                           exist()
                      elif same_num_1 == 2:
                           messagebox.showinfo("","恭喜你中了肆獎")
                           exist()
                      else:
                           messagebox.showinfo("","sorry，你沒有中獎！！！ ")
                           exist()
                 else:
                       messagebox.showinfo("","僅能查詢一個月的中獎資訊，請重新檢查期別!!!")
                       exist()
            
                

#送出
            bnt2=Button(window,text="送出",fg='black',width=4,
            font=17,command=win).place(x=190,y=540)
#取消
            bnt2=Button(window,text="取消",fg='black',width=4,
            font=17,command=exist).place(x=310,y=540)

    
            w.pack()
            window.mainloop()
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

