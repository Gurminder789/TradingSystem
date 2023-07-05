from tkinter import *
from tkinter import ttk
from tkinter import messagebox

obj = Tk()
obj.geometry("1325x650+0+0")
obj.title("Car Trading Management System")
obj.configure(background= 'light blue')


Tops = Frame(obj, width=1350, height=100, bd=15, relief="raise")
Tops.pack(side=TOP)

lblInfo = Label(Tops,font=('arial', 49, 'bold'),text= "Car Sales Trading System", bd=5, anchor='w')
lblInfo.grid(row=0,column=0)

bottom = Frame(obj, width=1350, height=600, bd=4, relief="raise")
bottom.pack(side=TOP)

bottomLeft = Frame(bottom, width=1000, height=600, bd=4, relief="raise")
bottomLeft.pack(side=LEFT)

bottomLeftTop = Frame(bottomLeft, width=1000, height=300, bd=2, relief="raise")
bottomLeftTop.pack(side=TOP)

bottomLeftTopL = Frame(bottomLeftTop, width=500, height=200, bd=2, relief="raise")
bottomLeftTopL.pack(side=LEFT)

bottomLeftTopR = Frame(bottomLeftTop, width=500, height=200,bd=2, relief="raise")
bottomLeftTopR.pack(side=RIGHT)


bottomLeftBottom = Frame(bottomLeft, width=1000, height=300, bd=2, relief="raise")
bottomLeftBottom.pack(side=BOTTOM)

bottomLeftBottomL = Frame(bottomLeftBottom, width=500, height=400, bd=2, relief="raise")
bottomLeftBottomL.pack(side=LEFT)

bottomLeftBottomR= Frame(bottomLeftBottom, width=500, height=400, bd=2, relief="raise")
bottomLeftBottomR.pack(side=RIGHT)


bottomRight = Frame(bottom, width=350, height=600, bd=4, relief="raise")
bottomRight.pack(side=RIGHT)



def iExit():
    iExit = messagebox.askyesno("Car Showroom System","Confirm if you want to exit")
    if iExit > 0:
        obj.destroy()
    return



def Reset():
    Modified.set("0")
    Stereo.set("0")
    Leather.set("0")
    Customised.set("0")
    GPS.set("0")
    CostofCar.set("0")
    CarMileage.set("0")

    CustomerName.set("")
    CustomerAddress.set("")
    CustomerPostcode.set("")
    CustomerTelephone.set("")

    VAT.set("0")
    Discount.set("0")
    Tax.set("")
    SubTotal.set("")
    Total.set("")

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)

    var8.set(0)
    var9.set(0)
    var18.set(0)

    textReceipt.delete("1.0",END)


def CarCost():

    if (var7.get()== 'Kwid'):
        myCar = float(590000.91)
        CostofCar.set(myCar)
    elif(var7.get()== 'Swift Desire'):
        myCar = float(780000.91)
        CostofCar.set(myCar)
    elif (var7.get()== 'Dustor'):
        myCar =float(830000.00)
        CostofCar.set(myCar)
    elif (var7.get()== 'Innova'):
        myCar = float(1680000.00)
        CostofCar.set(myCar)
    elif (var7.get()== 'Fortuner'):
        myCar = float(1790000.00)
        CostofCar.set(myCar)
    elif (var7.get()== 'Creta'):
        myCar = float(1980000.00)
        CostofCar.set(myCar)

    if (var18.get() == '100-5000' and var7.get() == 'Kwid'):
        myCar = float(590000.00)
        iMile = float(2500.10)
        CostofCar.set(myCar)
        CarMileage.set(iMile)

    if (var18.get() == '5001-20000' and var7.get() == 'Kwid'):
        myCar = float(590000.00)
        iMile = float(5010.70)
        CostofCar.set(myCar)
        CarMileage.set(iMile)

    if (var18.get() == '20001-100000' and var7.get() == 'Kwid'):
        myCar = float(590000.00)
        iMile = float(3789.90)
        CostofCar.set(myCar)
        CarMileage.set(iMile)

    if (var18.get() == '100001-1000000' and var7.get() == 'Kwid'):
        myCar = float(590000.00)
        iMile = float(1890.56)
        CostofCar.set(myCar)
        CarMileage.set(iMile)

    if (var18.get()== '100-5000' and var7.get()== 'Swift Desire'):
        myCar = float(780000.91)
        iMile = float(5012.90)
        CostofCar.set(myCar)
        CarMileage.set(iMile)

    if (var18.get()== '5001-20000' and var7.get()== 'Swift Desire'):
            myCar = float(780000.91)
            iMile = float(4010.70)
            CostofCar.set(myCar)
            CarMileage.set(iMile)

    if (var18.get() == '20001-100000' and var7.get() == 'Swift Desire'):
            myCar = float(780000.91)
            iMile = float(4010.70)
            CostofCar.set(myCar)
            CarMileage.set(iMile)

    if (var18.get() == '100001-1000000' and var7.get() == 'Swift Desire'):
            myCar = float(780000.91)
            iMile = float(1310.90)
            CostofCar.set(myCar)
            CarMileage.set(iMile)

    if (var18.get() == '100-5000' and var7.get() == 'Dustor'):
                myCar = float(830000.00)
                iMile = float(6500.10)
                CostofCar.set(myCar)
                CarMileage.set(iMile)

    if (var18.get() == '5001-20000' and var7.get() == 'Dustor'):
            myCar = float(830000.00)
            iMile = float(5010.70)
            CostofCar.set(myCar)
            CarMileage.set(iMile)

    if (var18.get() == '20001-100000' and var7.get() =='Dustor'):
            myCar = float(830000.00)
            iMile = float(3789.90)
            CostofCar.set(myCar)
            CarMileage.set(iMile)

    if (var18.get() == '100001-1000000' and var7.get() == 'Dustor'):
            myCar = float(830000.00)
            iMile = float(1890.56)
            CostofCar.set(myCar)
            CarMileage.set(iMile)


    if (var18.get() == '100-5000' and var7.get() == 'Innova'):
        myCar = float(1680000.00)
        iMile = float(6500.10)
        CostofCar.set(myCar)
        CarMileage.set(iMile)

    if (var18.get() == '5001-20000' and var7.get() == 'Innova'):
        myCar = float(1680000.00)
        iMile = float(5010.70)
        CostofCar.set(myCar)
        CarMileage.set(iMile)

    if (var18.get() == '20001-100000' and var7.get() == 'Innova'):
        myCar = float(1680000.00)
        iMile = float(3789.90)
        CostofCar.set(myCar)
        CarMileage.set(iMile)

    if (var18.get() == '100001-1000000' and var7.get() == 'Innova'):
        myCar = float(1680000.00)
        iMile = float(1890.56)
        CostofCar.set(myCar)
        CarMileage.set(iMile)


    if (var18.get() == '100-5000' and var7.get() == 'Fortuner'):
        myCar = float(1790000.00)
        iMile = float(6500.10)
        CostofCar.set(myCar)
        CarMileage.set(iMile)

    if (var18.get() == '5001-20000' and var7.get() == 'Fortuner'):
        myCar = float(1790000.00)
        iMile = float(5010.70)
        CostofCar.set(myCar)
        CarMileage.set(iMile)

    if (var18.get() == '20001-100000' and var7.get() == 'Fortuner'):
        myCar = float(1790000.00)
        iMile = float(3789.90)
        CostofCar.set(myCar)
        CarMileage.set(iMile)

    if (var18.get() == '100001-1000000' and var7.get() == 'Fortuner'):
        myCar = float(1790000.00)
        iMile = float(1890.56)
        CostofCar.set(myCar)
        CarMileage.set(iMile)

    if (var18.get() == '100-5000' and var7.get() == 'Creta'):
        myCar = float(1980000.00)
        iMile = float(1900.10)
        CostofCar.set(myCar)
        CarMileage.set(iMile)

    if (var18.get() == '5001-20000' and var7.get() == 'Creta'):
        myCar = float(1980000.00)
        iMile = float(5010.70)
        CostofCar.set(myCar)
        CarMileage.set(iMile)

    if (var18.get() == '20001-100000' and var7.get() == 'Creta'):
        myCar = float(1980000.00)
        iMile = float(3789.90)
        CostofCar.set(myCar)
        CarMileage.set(iMile)

    if (var18.get() == '100001-1000000' and var7.get() == 'Creta'):
        myCar = float(1980000.00)
        iMile = float(1890.56)
        CostofCar.set(myCar)
        CarMileage.set(iMile)




    if (var1.get() == 1):
        Modified.set(5023)
    elif (var1.get() == 0):
        Modified.set(0)
    if (var2.get() == 1):
        Stereo.set(356)
    elif (var2.get() == 0):
        Stereo.set(0)
    if (var3.get() == 1):
        Leather.set(4699)
    elif (var3.get() == 0):
        Leather.set(0)
    if (var4.get() == 1):
        Customised.set(10089)
    elif (var4.get() == 0):
        Customised.set(0)
    if (var5.get() == 1):
        GPS.set(250)
    elif (var5.get() == 0):
        GPS.set(0)
    if (var8.get() == 1):
        VAT.set(300)
    elif (var8.get() == 0):
        VAT.set(0)
    if (var9.get() == 1):
        Discount.set(5000)
    elif (var9.get() == 0):
        Discount.set(0)

    Item1 = float (CostofCar.get())
    Item2 = float (CarMileage.get())
    Item3 = float (Modified.get())
    Item4 = float (Stereo.get())
    Item5 = float (Leather.get())
    Item6 = float (Customised.get())
    Item7 = float (GPS.get())
    Item8 = float (VAT.get())
    Item9 = float (Discount.get())
    Item10 = "Rs", str('%.2f' % ((Item1 - Item2) + Item3 + Item4 + Item5 + Item6 + Item7+ Item8+ Item9))
    Item11 = (((Item1 - Item2) + Item3 + Item4 + Item5 + Item6 + Item7 + Item8 + Item9) * 0.45) / 100
    Item11 = "Rs", str('%.2f' % (Item11))
    Item12 = (((Item1 - Item2) + Item3 + Item4 + Item5 + Item6 + Item7+ Item8 + Item9) * 0.45) / 100
    Item13 = ((Item1 - Item2) + Item3 + Item4 + Item5 + Item6 + Item7 + Item8 + Item9)
    Item14 = "Rs", str('%.2f' % (Item12 + Item13))
    SubTotal.set(Item10)
    Tax.set(Item11)
    Total.set(Item14)



def Receipt():
    textReceipt.delete("1.0", END)
    textReceipt.insert(END, 'Items\t\t\t\t' + "Cost of Items \n\n")
    textReceipt.insert(END, '================================' "\n")
    textReceipt.insert(END, 'CustomerName: \t\t' + CustomerName.get() + "\n")
    textReceipt.insert(END, '==============================' "\n")
    textReceipt.insert(END, 'Type of Car: \t\t' + var7.get() + "\n")
    textReceipt.insert(END, 'Cost of Car: \t\t' + CostofCar.get() + "\n")
    textReceipt.insert(END, 'Total Mileage: \t\t' + CarMileage.get() + "\n")
    textReceipt.insert(END, 'Trade in value: \t\t' + var18.get() + "\n")
    textReceipt.insert(END, 'Cost of Modified: \t\t' + Modified.get() + "\n")
    textReceipt.insert(END, 'Cost of Stereo: \t\t' + Stereo.get() + "\n")
    textReceipt.insert(END, 'Cost of Leather: \t\t' + Leather.get() + "\n")
    textReceipt.insert(END, 'Cost of Customised: \t\t' + Customised.get() + "\n")
    textReceipt.insert(END, 'Cost of GPS\t\t: ' + GPS.get() + "\n")
    textReceipt.insert(END, '================================' "\n")
    textReceipt.insert(END, 'Tax:\t\t' + Tax.get() + "\n")
    textReceipt.insert(END, 'SubTotal: \t\t' + SubTotal.get() + "\n")
    textReceipt.insert(END, 'Total Cost: \t\t' + Total.get() + "\n")
    textReceipt.insert(END, '===================================' "\n")




CustomerName = StringVar()
CustomerAddress = StringVar()
CustomerPostcode = StringVar()
CustomerTelephone = StringVar()

lblName = Label(bottomLeftTopL, font=('arial', 16, 'bold'), text="Name", fg="blue", width=15, bd=10, anchor='w')
lblName.grid(row=0, column=0)
txtName = Entry(bottomLeftTopL, font=('arial', 16, 'bold'), bd=2, width=24, bg="white", justify='left',
                textvariable=CustomerName)
txtName.grid(row=0, column=1)

lblName = Label(bottomLeftTopL, font=('arial', 16, 'bold'), text="Name", fg="blue", width=15, bd=10, anchor='w')
lblName.grid(row=0, column=0)
txtName = Entry(bottomLeftTopL, font=('arial', 16, 'bold'), bd=2, width=24, bg="white", justify='left',
                textvariable=CustomerName)
txtName.grid(row=0, column=1)

lblAddress = Label(bottomLeftTopL, font=('arial', 16, 'bold'), text="Address", fg="blue", width=15, bd=10, anchor='w')
lblAddress.grid(row=1,column=0)
txtAddress = Entry(bottomLeftTopL, font=('arial', 16, 'bold'), bd=2, width=24, bg="white", justify='left',
                   textvariable=CustomerAddress)
txtAddress.grid(row=1, column=1)

lblPostcode = Label(bottomLeftTopL, font=('arial', 16, 'bold'), text="Postcode", fg="blue", width=15, bd=10,
                    anchor='w')
lblPostcode.grid(row=2, column=0)
txtPostcode = Entry(bottomLeftTopL, font=('arial', 16, 'bold'), bd=2, width=24, bg="white", justify='left',
                    textvariable=CustomerPostcode)
txtPostcode.grid(row=2, column=1)

lblTelephone = Label(bottomLeftTopL, font=('arial', 16, 'bold'), text="Telephone", fg="blue", width=15, bd=10,
                    anchor='w' )
lblTelephone.grid(row=3, column=0)
txtTelephone = Entry(bottomLeftTopL, font=('arial', 16, 'bold'), bd=2, width=24, bg="white", justify='left',
                     textvariable=CustomerTelephone)
txtTelephone.grid(row=3, column=1)


Modified = StringVar()
Stereo = StringVar()
Leather = StringVar()
Customised = StringVar()
GPS = StringVar()
VAT = StringVar()
Discount = StringVar()

Modified.set("0")
Stereo.set("0")
Leather.set("0")
Customised.set("0")
GPS.set("0")
VAT.set("0")
Discount.set("0")

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()



lblModified = Checkbutton(bottomLeftBottomL, font=('arial', 16, 'bold'), text="Modified", fg="blue", width=20, bd=10,
                          anchor='w'
                         ,onvalue=1, offvalue=0, variable=var1 )
lblModified.grid(row=0, column=0)
txtModified = Entry(bottomLeftBottomL, font=('arial', 16, 'bold'), bd=2, width=14, bg="white", justify='left',
                    textvariable= Modified)
txtModified.grid(row=0, column=1)

lblStereo =Checkbutton(bottomLeftBottomL, font=('arial', 16, 'bold'), text="Stereo System", fg="blue", width=20,
                       bd=10, anchor='w'
                       , onvalue=1, offvalue=0, variable=var2)
lblStereo.grid(row=1, column=0)
txtStereo = Entry(bottomLeftBottomL, font=('araial', 16, 'bold'), bd=2, width=14, bg="white", justify='left',
                  textvariable=Stereo)
txtStereo.grid(row=1, column=1)

lblLeather = Checkbutton(bottomLeftBottomL, font=('arial', 16, 'bold'), text="Leather Interior", fg="blue",width=20,
                         bd=10, anchor='w'
                        , onvalue=1, offvalue=0, variable=var3)
lblLeather.grid(row=2, column=0)
txtLeather = Entry(bottomLeftBottomL, font=('arial', 16, 'bold'), bd=2, width=14, bg="white", justify='left',
                   textvariable=Leather)
txtLeather.grid(row=2, column=1)

lblCustomised = Checkbutton(bottomLeftBottomL, font=('arial', 16, 'bold'), text="Customised Details", fg="blue",
                            width=20, bd=10, anchor='w'
                             ,onvalue=1, offvalue=0, variable=var4)
lblCustomised.grid(row=3, column=0)
txtCustomised = Entry(bottomLeftBottomL, font=('arial', 16, 'bold'), bd=2, width=14, bg="white", justify='left',
                   textvariable=Customised)
txtCustomised.grid(row=3, column=1)

lblGPS = Checkbutton(bottomLeftBottomL, font=('arial', 16, 'bold'), text="GPS", fg="blue",width=20,
                         bd=10, anchor='w'
                        , onvalue=1, offvalue=0, variable=var5)
lblGPS.grid(row=4, column=0)
txtGPS = Entry(bottomLeftBottomL, font=('arial', 16, 'bold'), bd=2, width=14, bg="white", justify='left',
                   textvariable=GPS)
txtGPS.grid(row=4, column=1)

btnTotalCost = Button(bottomLeftBottomL, pady=8, bd=2, fg="blue", font=('arial', 16, 'bold'), width=13, text="TOTAL",
                      bg= "white", command=CarCost).grid(row=5, column=0)
btnReceipt = Button(bottomLeftBottomL, pady=8, bd=2, fg="blue", font=('arial', 16, 'bold'), width=13, text="Receipt",
                    bg= "white", command= Receipt).grid(row=5, column=1)


var6 = IntVar()
var7 = StringVar()
var18 = StringVar()

CostofCar = StringVar()
CarMileage = StringVar()

CostofCar.set("0")
CarMileage.set("0")

lblChooseaCar = Label(bottomLeftTopR, font=('arial',16,'bold'), text="Choose a Car", fg="blue", width=13, bd=14,
                      anchor='w')
lblChooseaCar.grid(row=0, column=0)

cboChooseaCar = ttk.Combobox(bottomLeftTopR, textvariable=var7, state='readonly',font=('arial', 20,'bold'), width=12)
cboChooseaCar['value']= ( '','Kwid','Swift Desire', 'Dustor', 'Innova', 'Fortuner', 'Creta')
cboChooseaCar.current(0)
cboChooseaCar.grid(row=1, column=0)

lblCostofCar = Label(bottomLeftTopR, font=('arial', 16, 'bold'), text="Cost of a Car", fg="blue", width=13, bd=14,
                     anchor='w')
lblCostofCar.grid(row=2, column=0)

txtCostofCar = Entry(bottomLeftTopR, font=('arial', 16, 'bold'), bd=2, width=16, bg="white", justify='left',
                     textvariable=CostofCar)
txtCostofCar.grid(row=3, column=0)

lblTradeInaCar = Label(bottomLeftTopR, font=('arial', 16, 'bold'),text= "Trade in a Car", fg="blue", width=13, bd=14,
                       anchor='w')
lblTradeInaCar.grid(row=0, column=1)
cboTradeInaCar = ttk.Combobox(bottomLeftTopR, textvariable=var18, state='readonly', font=('arial', 20, 'bold'),
                              width=12)
cboTradeInaCar['value'] = ('', '100-5000', '5001-20000','20001-100000','100001-1000000')
cboTradeInaCar.current(0)
cboTradeInaCar.grid(row=1, column=1)

lblCarMileage = Label(bottomLeftTopR, font=('arial', 16, 'bold'), text="CarMileage", fg="blue", width=13, bd=14,
                      anchor='w')
lblCarMileage.grid(row=2, column=1)
txtCarMileage = Entry(bottomLeftTopR, font=('arial', 16, 'bold'), bd=2, width=16, bg="white", justify='left',
                      textvariable=CarMileage)
txtCarMileage.grid(row=3, column=1)

VAT = StringVar()
Discount = StringVar()
Tax = StringVar()
SubTotal = StringVar()
Total = StringVar()

var8 = IntVar()
var9 = IntVar()

lblVAT = Checkbutton(bottomLeftBottomR, font=('arial', 16, 'bold'), text= "VAT", fg="blue", width=13, bd=12, anchor='w',
                     onvalue=1, offvalue=0, variable=var8)
lblVAT.grid(row=0, column=0)
txtVAT = Entry(bottomLeftBottomR, font=('arial', 16, 'bold'),bd=2, width=17, bg="white", justify='left',
               textvariable=VAT)
txtVAT.grid(row=0, column=1)

lblDiscount = Checkbutton(bottomLeftBottomR, font=('arial', 16, 'bold'), text="Discount", fg="blue", width=13, bd=12,
                          anchor='w',onvalue=1, offvalue=0, variable=var9)
lblDiscount.grid(row=1, column=0)
txtDiscount = Entry(bottomLeftBottomR, font=('arial', 16, 'bold'), bd=2, width=17, bg="white", justify='left',
                    textvariable = Discount)
txtDiscount.grid(row=1, column=1)

lblTax = Label(bottomLeftBottomR, font=('arial', 16, 'bold'), text="Tax", fg="blue", width=13, bd=12, anchor='w')
lblTax.grid(row=2, column=0)
txtTax = Entry(bottomLeftBottomR, font=('arial', 16, 'bold'), bd=2, width=17, bg="white", justify='left',
               textvariable=Tax)
txtTax.grid(row=2, column=1)

lblSubTotal = Label(bottomLeftBottomR, font=('arial', 16, 'bold'), text="SubTotal", fg="blue", width=13, bd=12,
                    anchor='w')
lblSubTotal.grid(row=3, column=0)
txtSubTotal = Entry(bottomLeftBottomR, font=('arial', 16, 'bold'), bd=2, width=17,bg="white", justify='left',
                    textvariable=SubTotal)
txtSubTotal.grid(row=3,column=1)

lblTotal = Label(bottomLeftBottomR, font=('arial', 16, 'bold'),text= "Total", fg="blue", width=13, bd=12, anchor='w')
lblTotal.grid(row=4, column=0)
txtTotal = Entry(bottomLeftBottomR, font=('arial', 16, 'bold'),bd=2, width=17, bg="white", justify='left',
                 textvariable=Total)
txtTotal.grid(row=4, column=1)

btnTotalCost = Button(bottomLeftBottomR, pady=8, bd=2, fg="blue", font=('arial', 16, 'bold'), width=13, text="Reset",
                      bg="white", command=Reset).grid(row=5, column=0)
btnReceipt = Button(bottomLeftBottomR, pady=8, bd=2, fg="blue", font=('arial', 16, 'bold'), width=13, text="Exit",
                    bg="white", command=iExit).grid(row=5, column=1)


lblReceipt = Label(bottomRight, font=('arial', 16, 'bold'), text="Receipt", bd=2, anchor='w')
lblReceipt.grid(row=0, column=0, sticky=W)
textReceipt = Text(bottomRight, font=('arial', 11, 'bold'), bd=8, width=86, height=26, bg='white')
textReceipt.grid(row=1, column=0)
obj.mainloop()