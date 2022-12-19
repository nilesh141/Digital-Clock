from tkinter import *
import datetime

def date_time():
    time=datetime.datetime.now()
    hr=time.strftime("%I")
    mn=time.strftime("%M")
    sc=time.strftime("%S")
    am=time.strftime("%p")

    date=time.strftime("%d")
    month=time.strftime("%m")
    year=time.strftime("%y")
    day=time.strftime("%a")

    labHr.config(text=hr)
    labMn.config(text=mn)
    labSc.config(text=sc)
    labAm.config(text=am)

    labDt.config(text=date)
    labMo.config(text=month)
    labYr.config(text=year) 
    labDy.config(text=day)

    labHr.after(200,date_time)

clock=Tk()

clock.title("   *** Digital Clock ***")
clock.geometry("1000x500")
clock.config(bg="pink")


labHr=Label(clock,text="00",font=("Calibri",50,"bold"),bg="yellow",fg="red")
labHr.place(x=120,y=50,height=110,width=100)
labHrText=Label(clock,text="Hour",font=("Calibri",25,"bold"),bg="yellow",fg="red")
labHrText.place(x=120,y=190,height=40,width=100)

labMn=Label(clock,text="00",font=("Calibri",50,"bold"),bg="yellow",fg="red")
labMn.place(x=340,y=45,height=110,width=100)
labMnText=Label(clock,text="Minute",font=("Calibri",25,"bold"),bg="yellow",fg="red")
labMnText.place(x=340,y=190,height=40,width=100)

labSc=Label(clock,text="00",font=("Calibri",50,"bold"),bg="yellow",fg="red")
labSc.place(x=560,y=45,height=110,width=100)
labScText=Label(clock,text="Second",font=("Calibri",25,"bold"),bg="yellow",fg="red")
labScText.place(x=560,y=190,height=40,width=100)


labAm=Label(clock,text="00",font=("Calibri",50,"bold"),bg="yellow",fg="red")
labAm.place(x=780,y=45,height=110,width=100)
labAmText=Label(clock,text="AM/PM",font=("Calibri",22,"bold"),bg="yellow",fg="red")
labAmText.place(x=780,y=190,height=40,width=100)

##for date and day

labDt=Label(clock,text="00",font=("Calibri",50,"bold"),bg="yellow",fg="red")
labDt.place(x=120,y=270,height=110,width=100)
labDtText=Label(clock,text="Date",font=("Calibri",25,"bold"),bg="yellow",fg="red")
labDtText.place(x=120,y=410,height=40,width=100)

labMo=Label(clock,text="00",font=("Calibri",50,"bold"),bg="yellow",fg="red")
labMo.place(x=340,y=270,height=110,width=100)
labMoText=Label(clock,text="Month",font=("Calibri",25,"bold"),bg="yellow",fg="red")
labMoText.place(x=340,y=410,height=40,width=100)

labYr=Label(clock,text="00",font=("Calibri",50,"bold"),bg="yellow",fg="red")
labYr.place(x=560,y=270,height=110,width=100)
labYrText=Label(clock,text="Year",font=("Calibri",25,"bold"),bg="yellow",fg="red")
labYrText.place(x=560,y=410,height=40,width=100)

labDy=Label(clock,text="00",font=("Calibri",40,"bold"),bg="yellow",fg="red")
labDy.place(x=780,y=270,height=110,width=100)
labDyText=Label(clock,text="Day",font=("Calibri",22,"bold"),bg="yellow",fg="red")
labDyText.place(x=780,y=410,height=40,width=100)

date_time()
clock.mainloop()
