# 1 บาทไทย = 0.027 KRW (วอน)
# 1 บาทไทย =  0.030 USD (ดอลลาร์สหรัฐ)
# 1 บาทไทย =  3.600 JPY (เยน)
# 1 บาทไทย =  0.023 GBP (ปอนด์อังกฤษ)


from tkinter import *
from tkinter import ttk
root = Tk()
root.title("โปรกรมแปลงสกุลเงิน")


money = IntVar()
Label(bg="aqua",text="จำนวนเงิน (THB)",padx=10,font=30).grid(row=0,sticky=W)
et1=Entry(bg="orange",font=30,width=30,textvariable=money)
et1.grid(row=0,column=1)


choice = StringVar(value="โปรดเลือกสกุลเงิน")
Label(bg="aqua",text="เลือกสกุลเงิน",padx=10,font=30).grid(row=1,sticky=W)
combo=ttk.Combobox(width=28,font=30,textvariable=choice)
combo["values"]=("KRW","USD","JPY","GBP")
combo.grid(row=1,column=1)

Label(bg="aqua",text="ผลการคำนวณ",padx=10,font=30).grid(row=2,sticky=W)
et2=Entry(bg="grey",font=30,width=30)
et2.grid(row=2,column=1)


def calculate():
    amount=money.get()
    currency=choice.get()

    if currency == "KRW":
        et2.delete(0,END)
        result = ((amount*0.027),"KRW(วอน)")
        et2.insert(0,result)
    elif currency == "USD":
        et2.delete(0,END)
        result = ((amount*0.030),"USD(ดอลลาร์สหรัฐ)")
        et2.insert(0,result)
    elif currency == "JPY":
        et2.delete(0,END)
        result = ((amount*3.600),"JPY(เยน)")
        et2.insert(0,result)
    elif currency == "GBP":
        et2.delete(0,END)
        result = ((amount*0.023),"GBP(ปอนด์อังกฤษ)")
        et2.insert(0,result)
    else :
        et2.delete(0,END)
        result = "ไม่พบข้อมูล"
        et2.insert(0,result)


def deleteText():
    et1.delete(0, END)
    et2.delete(0, END)

Button(text="คำนวณ",bg="pink",font=30,width=15,command=calculate).grid(row=3,column=1,sticky=W)
Button(text="ล้าง",bg="pink",font=30,width=15,command=deleteText).grid(row=3,column=1,sticky=E)




root.mainloop()
