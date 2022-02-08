from tkinter import*
window=Tk()
window.title("Simple calculator")
window.configure(background="aqua")

labelintro=Label(window,text="Calculator",bg="aqua",font="digital-7 30")
labelintro.place(x=50,y=0)

label1=Label(window,text="NO1",bg="aqua",font="digital-7 20")
label1.place(x=0,y=50)

label2=Label(window,text="NO2",bg="aqua",font="digital-7 20")
label2.place(x=0,y=100)

data1=Entry(window,width=30)
data1.place(x=50,y=60)

data2=Entry(window,width=30)
data2.place(x=50,y=105)

labelresult=Label(window,text="Result :",bg="aqua",font="digital-7 20")
labelresult.place(x=30,y=150)


labeltotal=Label(window,bg="aqua",font="digital-7 20")
labeltotal.place(x=130,y=150)

labelpython=Label(window,bg="aqua",text="Python GUI",font="Courier 10")
labelpython.place(x=100,y=380)

labelsanka=Label(window,bg="aqua",text="@ Sanka Siribaddana",font="Courier 10")
labelsanka.place(x=65,y=400)

labelname=Label(window,bg="white",width=40,text="Made by:Hashan Sudeera",font="Courier 10")
labelname.place(x=-10,y=420)

labelresult1=Label(window,bg="aqua",font="digital-7 20")
labelresult1.place(x=80,y=330)


def totbutton():
    no1=int(data1.get())
    no2=int(data2.get())
    tot=int(no1+no2)
    labeltotal.config(text=tot)
    
    if  tot>=1000 :
       labelresult1.config(tot*100/10)
    
    elif tot>=75 :
       labelresult1.config(text="Between 75 and 100")
    
    elif tot>=50 :
       labelresult1.config(text="Between 50 and 75")
    
    else :
       labelresult1.config(text="Less than 50")    







def minesbutton():
    no1=int(data1.get())
    no2=int(data2.get())
    tot=str(no1-no2)
    labeltotal.config(text=tot)


def gunibutton():
    no1=int(data1.get())
    no2=int(data2.get())
    tot=str(no1*no2)
    labeltotal.config(text=tot)


def bedeebutton():
    no1=int(data1.get())
    no2=int(data2.get())
    tot=str(no1/no2)
    labeltotal.config(text=tot)


def clearbutton():
    data1.delete(0)
    data2.delete(0)
    tot=( )
    labeltotal.config(text=tot)



buttontot=Button(window,text="+",command=totbutton,width=4,font="digital-7 20",bg="lightpink",cursor="hand2")
buttontot.place(x=10,y=200)

buttonmines=Button(window,text="-",command=minesbutton,width=4,font="digital-7 20",bg="lightgray",cursor="hand2")
buttonmines.place(x=80,y=200)

buttonguni=Button(window,text="*",command=gunibutton,width=4,font="digital-7 20",bg="lightblue",cursor="hand2")
buttonguni.place(x=155,y=200)

buttonbedee=Button(window,text="/",command=bedeebutton,width=4,font="digital-7 20",bg="lightyellow",cursor="hand2")
buttonbedee.place(x=225,y=200)

buttonclear=Button(window,text="Clear",command=clearbutton,width=10,font="digital-7 20",cursor="hand2")
buttonclear.place(x=80,y=260)

window.geometry("300x450")
window.mainloop()