from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from PIL import Image, ImageTk

# Creating main window
unitConverter = Tk()
unitConverter.title("Unit Converter")
unitConverter.geometry('450x305')
unitConverter.resizable(0, 0)
# path = "logos.ico"
# load = Image.open(path)
# render = ImageTk.PhotoImage(load)
# unitConverter.iconphoto(False, render)

def lconversion():
    lengthConverter = Tk()
    lengthConverter.title("Length Conversion")
    lengthConverter.geometry('350x140')
    lengthConverter.resizable(0, 0)

    Label(lengthConverter, text="Enter the Value", font=("Arial Bold", 17), justify='center').pack(pady=10)

    user = Frame(lengthConverter)
    nums = Entry(user, width=10)
    nums.pack(side=LEFT)

    left = Combobox(user, state='readonly', width=8)
    left['values']= ("mili-m", "centi-m", "deci-m", "m", "deca-m", "hecto-m", "kilo-m", "inch", "foot", "mile")
    left.current(0)
    left.pack(side=LEFT, padx=10)

    Label(user, text="to", font=("Arial", 12)).pack(side=LEFT)

    right = Combobox(user, state='readonly', width=8)
    right['values']= ("mili-m", "centi-m", "deci-m", "m", "deca-m", "hecto-m", "kilo-m", "inch", "foot", "mile")
    right.current(1)
    right.pack(side=LEFT, padx=10)

    user.pack()

    def result():
        # Getting the values
        first = left.get()
        second = right.get()
        try:
            num = int(nums.get())
        except:
            num = float(nums.get())
        
        # Main logic starts here
        res = 0.0
        
        if (first=="mili-m" and second=="centi-m"):
            res = num * 0.1
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="mili-m" and second=="deci-m"):
            res = num * 0.01
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="mili-m" and second=="m"):
            res = num * 0.001
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="mili-m" and second=="deca-m"):
            res = num * 0.0001
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="mili-m" and second=="hecto-m"):
            res = num * 0.00001
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="mili-m" and second=="kilo-m"):
            res = num * 0.000001
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="mili-m" and second=="inch"):
            res = num * 0.0393701
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="mili-m" and second=="foot"):
            res = num * 0.00328084
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="mili-m" and second=="mile"):
            res = num * 0.00000062137
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="centi-m" and second=="mili-m"):
            res = num * 10
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="centi-m" and second=="deci-m"):
            res = num * 0.1
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="centi-m" and second=="m"):
            res = num * 0.01
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="centi-m" and second=="deca-m"):
            res = num * 0.001
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="centi-m" and second=="hecto-m"):
            res = num * 0.0001
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="centi-m" and second=="kilo-m"):
            res = num * 0.00001
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="centi-m" and second=="inch"):
            res = num * 0.393701
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="centi-m" and second=="foot"):
            res = num * 0.0328084
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="centi-m" and second=="mile"):
            res = num * 0.0000062137
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="deci-m" and second=="mili-m"):
            res = num * 100
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="deci-m" and second=="centi-m"):
            res = num * 10
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="deci-m" and second=="m"):
            res = num * 0.1
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="deci-m" and second=="deca-m"):
            res = num * 0.01
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="deci-m" and second=="hecto-m"):
            res = num * 0.001
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="deci-m" and second=="kilo-m"):
            res = num * 0.0001
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="deci-m" and second=="inch"):
            res = num * 3.93700787
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="deci-m" and second=="foot"):
            res = num * 0.32808399
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="deci-m" and second=="mile"):
            res = num * 0.0000621371192
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="m" and second=="mili-m"):
            res = num * 1000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="m" and second=="centi-m"):
            res = num * 100
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="m" and second=="deci-m"):
            res = num * 10
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="m" and second=="deca-m"):
            res = num * 0.1
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="m" and second=="hecto-m"):
            res = num * 0.01
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="m" and second=="kilo-m"):
            res = num * 0.001
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="m" and second=="inch"):
            res = num * 39.3701
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="m" and second=="foot"):
            res = num * 3.28084
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="m" and second=="mile"):
            res = num * 0.000621371
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="deca-m" and second=="mili-m"):
            res = num * 10000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="deca-m" and second=="centi-m"):
            res = num * 1000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="deca-m" and second=="deci-m"):
            res = num * 100
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="deca-m" and second=="m"):
            res = num * 10
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="deca-m" and second=="hecto-m"):
            res = num * 0.1
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="deca-m" and second=="kilo-m"):
            res = num * 0.01
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="deca-m" and second=="inch"):
            res = num * 393.701
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="deca-m" and second=="foot"):
            res = num * 32.8084
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="deca-m" and second=="mile"):
            res = num * 0.00621371
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="hecto-m" and second=="mili-m"):
            res = num * 100000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="hecto-m" and second=="centi-m"):
            res = num * 10000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="hecto-m" and second=="deci-m"):
            res = num * 1000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="hecto-m" and second=="m"):
            res = num * 100
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="hecto-m" and second=="deca-m"):
            res = num * 10
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="hecto-m" and second=="kilo-m"):
            res = num * 0.1
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="hecto-m" and second=="inch"):
            res = num * 3937.01
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="hecto-m" and second=="foot"):
            res = num * 328.084
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="hecto-m" and second=="mile"):
            res = num * 0.0621371
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="kilo-m" and second=="mili-m"):
            res = num * 1000000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="kilo-m" and second=="centi-m"):
            res = num * 100000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="kilo-m" and second=="deci-m"):
            res = num * 10000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="kilo-m" and second=="m"):
            res = num * 1000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="kilo-m" and second=="deca-m"):
            res = num * 100
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="kilo-m" and second=="hecto-m"):
            res = num * 10
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="kilo-m" and second=="inch"):
            res = num * 39370.1
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="kilo-m" and second=="foot"):
            res = num * 3280.84
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="kilo-m" and second=="mile"):
            res = num * 0.621371
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="inch" and second=="mili-m"):
            res = num * 25.4
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="inch" and second=="centi-m"):
            res = num * 2.54
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="inch" and second=="deci-m"):
            res = num * 0.254
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="inch" and second=="m"):
            res = num * 0.0254
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="inch" and second=="deca-m"):
            res = num * 0.00254
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="inch" and second=="hecto-m"):
            res = num * 0.000254
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="inch" and second=="kilo-m"):
            res = num * 0.0000254
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="inch" and second=="foot"):
            res = num * 0.0833333
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="inch" and second=="mile"):
            res = num * 0.000015783
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="foot" and second=="mili-m"):
            res = num * 304.8
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="foot" and second=="centi-m"):
            res = num * 30.48
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="foot" and second=="deci-m"):
            res = num * 3.048
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="foot" and second=="m"):
            res = num * 0.3048
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="foot" and second=="deca-m"):
            res = num * 0.03048
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="foot" and second=="hecto-m"):
            res = num * 0.003048
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="foot" and second=="kilo-m"):
            res = num * 0.0003048
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="foot" and second=="inch"):
            res = num * 12
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="foot" and second=="mile"):
            res = num * 0.000189394
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="mile" and second=="mili-m"):
            res = num * 1609000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="mile" and second=="centi-m"):
            res = num * 160934
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="mile" and second=="deci-m"):
            res = num * 16093.44
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="mile" and second=="m"):
            res = num * 1609.344
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="mile" and second=="deca-m"):
            res = num * 160.934
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="mile" and second=="hecto-m"):
            res = num * 16.093
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="mile" and second=="kilo-m"):
            res = num * 1.60934
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="mile" and second=="inch"):
            res = num * 63360
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="mile" and second=="foot"):
            res = num * 5280
            messagebox.showinfo('Result', f"It's {res} {second}.")
        else:
            messagebox.showinfo('Result', f"It's {num} {second}.")

    submit = Frame(lengthConverter)
    Button(submit, text="Submit", command=result).pack(side=LEFT, padx=4)
    Button(submit, text="Close", command=lengthConverter.destroy).pack(side=LEFT, padx=7)
    submit.pack(pady=20)

    lengthConverter.mainloop()

def mconversion():
    massConverter = Tk()
    massConverter.title("Mass Conversion")
    massConverter.geometry('330x140')
    massConverter.resizable(0, 0)

    Label(massConverter, text="Enter the Value", font=("Arial Bold", 17), justify='center').pack(pady=10)

    user = Frame(massConverter)
    nums = Entry(user, width=10)
    nums.pack(side=LEFT)

    left = Combobox(user, state='readonly', width=7)
    left['values']= ("kilo-g", "g", "mili-g", "micro-g", "nano-g", "pico-g", "pound", "ounce")
    left.current(0)
    left.pack(side=LEFT, padx=10)

    Label(user, text="to", font=("Arial", 12)).pack(side=LEFT)

    right = Combobox(user, state='readonly', width=7)
    right['values']= ("kilo-g", "g", "mili-g", "micro-g", "nano-g", "pico-g", "pound", "ounce")
    right.current(1)
    right.pack(side=LEFT, padx=10)

    user.pack()

    def result():
        # Getting the values
        first = left.get()
        second = right.get()
        try:
            num = int(nums.get())
        except:
            num = float(nums.get())
        
        # Main logic starts here
        res = 0.0
        
        if (first=="kilo-g" and second=="g"):
            res = num * 1000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="kilo-g" and second=="mili-g"):
            res = num * 1000000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="kilo-g" and second=="micro-g"):
            res = num * 1000000000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="kilo-g" and second=="nano-g"):
            res = num * 1000000000000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="kilo-g" and second=="pico-g"):
            res = num * 1000000000000000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="kilo-g" and second=="pound"):
            res = num * 2.20462
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="kilo-g" and second=="ounce"):
            res = num * 35.274
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="g" and second=="kilo-g"):
            res = num * 0.001
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="g" and second=="mili-g"):
            res = num * 1000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="g" and second=="micro-g"):
            res = num * 1000000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="g" and second=="nano-g"):
            res = num * 1000000000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="g" and second=="pico-g"):
            res = num * 1000000000000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="g" and second=="pound"):
            res = num * 0.00220462
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="g" and second=="ounce"):
            res = num * 0.035274
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="mili-g" and second=="kilo-g"):
            res = num * 0.000001
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="mili-g" and second=="g"):
            res = num * 0.001
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="mili-g" and second=="micro-g"):
            res = num * 1000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="mili-g" and second=="nano-g"):
            res = num * 1000000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="mili-g" and second=="pico-g"):
            res = num * 1000000000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="mili-g" and second=="pound"):
            res = num * 0.0000022046
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="mili-g" and second=="ounce"):
            res = num * 0.000035274
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="micro-g" and second=="kilo-g"):
            res = num * 0.000000001
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="micro-g" and second=="g"):
            res = num * 0.000001
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="micro-g" and second=="mili-g"):
            res = num * 0.001
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="micro-g" and second=="nano-g"):
            res = num * 1000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="micro-g" and second=="pico-g"):
            res = num * 1000000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="micro-g" and second=="pound"):
            res = num * 0.0000000022046
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="micro-g" and second=="ounce"):
            res = num * 0.000000035274
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="nano-g" and second=="kilo-g"):
            res = num * 0.000000000001
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="nano-g" and second=="g"):
            res = num * 0.000000001
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="nano-g" and second=="mili-g"):
            res = num * 0.000001
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="nano-g" and second=="micro-g"):
            res = num * 0.001
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="nano-g" and second=="pico-g"):
            res = num * 1000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="nano-g" and second=="pound"):
            res = num * 0.0000000000022046
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="nano-g" and second=="ounce"):
            res = num * 0.000000000035274
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="pico-g" and second=="kilo-g"):
            res = num * 0.000000000000001
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="pico-g" and second=="g"):
            res = num * 0.000000000001
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="pico-g" and second=="mili-g"):
            res = num * 0.000000001
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="pico-g" and second=="micro-g"):
            res = num * 0.000001
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="pico-g" and second=="nano-g"):
            res = num * 0.001
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="pico-g" and second=="pound"):
            res = num * 0.0000000000000022046
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="pico-g" and second=="ounce"):
            res = num * 0.000000000000035274
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="pound" and second=="kilo-g"):
            res = num * 0.453592
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="pound" and second=="g"):
            res = num * 453.592
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="pound" and second=="mili-g"):
            res = num * 453592
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="pound" and second=="micro-g"):
            res = num * 453600000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="pound" and second=="nano-g"):
            res = num * 453600000000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="pound" and second=="pico-g"):
            res = num * 453600000000000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="pound" and second=="ounce"):
            res = num * 16
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="ounce" and second=="kilo-g"):
            res = num * 0.0283495
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="ounce" and second=="g"):
            res = num * 28.3495
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="ounce" and second=="mili-g"):
            res = num * 28349.5
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="ounce" and second=="micro-g"):
            res = num * 28350000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="ounce" and second=="nano-g"):
            res = num * 28350000000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="ounce" and second=="pico-g"):
            res = num * 28350000000000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif (first=="ounce" and second=="pound"):
            res = num * 0.0625
            messagebox.showinfo('Result', f"It's {res} {second}.")
        else:
            messagebox.showinfo('Result', f"It's {num} {second}.")

    submit = Frame(massConverter)
    Button(submit, text="Submit", command=result).pack(side=LEFT, padx=4)
    Button(submit, text="Close", command=massConverter.destroy).pack(side=LEFT, padx=7)
    submit.pack(pady=20)

    massConverter.mainloop()

def tconversion():
    timeConverter = Tk()
    timeConverter.title("Time Conversion")
    timeConverter.geometry('325x140')
    timeConverter.resizable(0, 0)

    Label(timeConverter, text="Enter the Value", font=("Arial Bold", 17), justify='center').pack(pady=10)

    user = Frame(timeConverter)
    nums = Entry(user, width=10)
    nums.pack(side=LEFT)

    left = Combobox(user, state='readonly', width=7)
    left['values']= ("min", "hr", "sec", "day", "year", "mili-s", "micro-s", "ns", "ps")
    left.current(0)
    left.pack(side=LEFT, padx=10)

    Label(user, text="to", font=("Arial", 12)).pack(side=LEFT)

    right = Combobox(user, state='readonly', width=7)
    right['values']= ("min", "hr", "sec", "day", "year", "mili-s", "micro-s", "nano-s", "pico-s")
    right.current(1)
    right.pack(side=LEFT, padx=10)

    user.pack()

    def result():
        # Getting the values
        first = left.get()
        second = right.get()
        try:
            num = int(nums.get())
        except:
            num = float(nums.get())
        
        # Main logic starts here
        res = 0.0
        
        if (first=="min" and second=="hr"):
            res = num / 60
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="min" and second=="sec"):
            res = num * 60
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="min" and second=="day"):
            res = num * 0.000694
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="min" and second=="year"):
            res = num  * 0.000001903
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="min" and second=="mili-s"):
            res = num * 60000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="min" and second=="micro-s"):
            res = num * 60000000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="min" and second=="nano-s"):
            res = num * 60000000000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="min" and second=="pico-s"):
            res = num * 60000000000000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="hr" and second=="min"):
            res = num * 60
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="hr" and second=="sec"):
            res = num * 3600
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="hr" and second=="day"):
            res = num / 24
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="hr" and second=="year"):
            res = num * 0.000114155
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="hr" and second=="mili-s"):
            res = num * 3600000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="hr" and second=="micro-s"):
            res = num * 3600000000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="hr" and second=="nano-s"):
            res = num * 3600000000000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="hr" and second=="pico-s"):
            res = num * 3600000000000000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="sec" and second=="min"):
            res = num / 60
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="sec" and second=="hr"):
            res = num / 3600
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="sec" and second=="day"):
            res = num * 0.000011574074
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="sec" and second=="year"):
            res = num * 0.00000003168739
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="sec" and second=="mili-s"):
            res = num * 1000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="sec" and second=="micro-s"):
            res = num * 1000000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="sec" and second=="nano-s"):
            res = num * 1000000000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="sec" and second=="pico-s"):
            res = num * 1000000000000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="day" and second=="min"):
            res = num * 1440
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="day" and second=="hr"):
            res = num * 24
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="day" and second=="sec"):
            res = num * 86400
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="day" and second=="year"):
            res = num * 0.0027379070
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="day" and second=="mili-s"):
            res = num * 86400000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="day" and second=="micro-s"):
            res = num * 86400000000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="day" and second=="nano-s"):
            res = num * 86400000000000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="day" and second=="pico-s"):
            res = num * 86400000000000000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="year" and second=="min"):
            res = num * 525949.2
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="year" and second=="hr"):
            res = num * 8765.82
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="year" and second=="sec"):
            res = num * 31556952
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="year" and second=="day"):
            res = num * 365.2425
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="year" and second=="mili-s"):
            res = num * 31556952000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="year" and second=="micro-s"):
            res = num * 31556952000000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="year" and second=="nano-s"):
            res = num * 31556952000000000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="year" and second=="pico-s"):
            res = num * 31556952000000000000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="mili-s" and second=="min"):
            res = num * 0.000016666667
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="mili-s" and second=="hr"):
            res = num * 0.00000027777778
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="mili-s" and second=="sec"):
            res = num * 0.001
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="mili-s" and second=="day"):
            res = num * 0.00000001574074
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="mili-s" and second=="year"):
            res = num * 0.000000000031688739
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="mili-s" and second=="micro-s"):
            res = num * 1000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="mili-s" and second=="nano-s"):
            res = num * 1000000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="mili-s" and second=="pico-s"):
            res = num * 1000000000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="micro-s" and second=="min"):
            res = num * 0.000000016666667
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="micro-s" and second=="hr"):
            res = num * 0.00000000027777778
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="micro-s" and second=="sec"):
            res = num * 0.000001
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="micro-s" and second=="day"):
            res = num * 0.000000000011574074
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="micro-s" and second=="year"):
            res = num * 0.000000000000031688739
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="micro-s" and second=="mili-s"):
            res = num * 0.001
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="micro-s" and second=="nano-s"):
            res = num * 1000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="micro-s" and second=="pico-s"):
            res = num * 1000000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="nano-s" and second=="min"):
            res = num * 0.000000000016666667
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="nano-s" and second=="hr"):
            res = num * 0.00000000000027777778
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="nano-s" and second=="sec"):
            res = num * 0.000000001
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="nano-s" and second=="day"):
            res = num * 0.000000000000011574074
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="nano-s" and second=="year"):
            res = num * 0.000000000000000031688739
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="nano-s" and second=="mili-s"):
            res = num * 0.000001
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="nano-s" and second=="micro-s"):
            res = num * 0.001
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="nano-s" and second=="pico-s"):
            res = num * 1000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="pico-s" and second=="min"):
            res = num * 166666666666667
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="pico-s" and second=="hr"):
            res = num * 27778000000000000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="pico-s" and second=="sec"):
            res = num * 0.000000000001
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="pico-s" and second=="day"):
            res = num * 0.000000000000000011574
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="pico-s" and second=="year"):
            res = num * 0.00000000000000000003171
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="pico-s" and second=="mili-s"):
            res = num * 0.000000001
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="pico-s" and second=="micro-s"):
            res = num * 0.000001
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="pico-s" and second=="nano-s"):
            res = num * 0.001
            messagebox.showinfo('Result', f"It's {res} {second}.")
        else:
            messagebox.showinfo('Result', f"It's {num} {second}.")

    submit = Frame(timeConverter)
    Button(submit, text="Submit", command=result).pack(side=LEFT, padx=4)
    Button(submit, text="Close", command=timeConverter.destroy).pack(side=LEFT, padx=7)
    submit.pack(pady=20)

    timeConverter.mainloop()

def aconversion():
    areaConverter = Tk()
    areaConverter.title("Area Conversion")
    areaConverter.geometry('350x140')
    areaConverter.resizable(0, 0)

    Label(areaConverter, text="Enter the Value", font=("Arial Bold", 17), justify='center').pack(pady=10)

    user = Frame(areaConverter)
    nums = Entry(user, width=10)
    nums.pack(side=LEFT)

    left = Combobox(user, state='readonly', width=9)
    left['values']= ("sq. inch", "sq. foot", "acre", "hectare", "sq. mile", "sq. meter", "sq. yard")
    left.current(0)
    left.pack(side=LEFT, padx=10)

    Label(user, text="to", font=("Arial", 12)).pack(side=LEFT)

    right = Combobox(user, state='readonly', width=9)
    right['values']= ("sq. inch", "sq. foot", "acre", "hectare", "sq. mile", "sq. meter", "sq. yard")
    right.current(1)
    right.pack(side=LEFT, padx=10)

    user.pack()

    def result():
        # Getting the values
        first = left.get()
        second = right.get()
        try:
            num = int(nums.get())
        except:
            num = float(nums.get())
        
        # Main logic starts here
        res = 0.0
        
        if (first=="sq. inch" and second=="sq. foot"):
            res = num * 0.00694444
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="sq. inch" and second=="acre"):
            res = num * 0.00000015942
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="sq. inch" and second=="hectare"):
            res = num * 0.000000064516
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="sq. inch" and second=="sq. mile"):
            res = num * 0.0000000002491
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="sq. inch" and second=="sq. meter"):
            res = num * 0.00064516
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="sq. inch" and second=="sq. yard"):
            res = num * 0.000771605
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="sq. foot" and second=="sq. inch"):
            res = num * 144
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="sq. foot" and second=="acre"):
            res = num * 0.000022957
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="sq. foot" and second=="hectare"):
            res = num * 0.0000092903
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="sq. foot" and second=="sq. mile"):
            res = num * 0.00000003587
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="sq. foot" and second=="sq. meter"):
            res = num * 0.092903
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="sq. foot" and second=="sq. yard"):
            res = num * 0.111111
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="acre" and second=="sq. inch"):
            res = num * 6273000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="acre" and second=="sq. foot"):
            res = num * 43560
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="acre" and second=="hectare"):
            res = num * 0.404686
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="acre" and second=="sq. mile"):
            res = num * 0.0015625
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="acre" and second=="sq. meter"):
            res = num * 4046.86
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="acre" and second=="sq. yard"):
            res = num * 4840
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="hectare" and second=="sq. inch"):
            res = num * 15500000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="hectare" and second=="sq. foot"):
            res = num * 107639
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="hectare" and second=="acre"):
            res = num * 2.47105
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="hectare" and second=="sq. mile"):
            res = num * 0.00386102
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="hectare" and second=="sq. meter"):
            res = num * 10000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="hectare" and second=="sq. yard"):
            res = num * 11959.9
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="sq. mile" and second=="sq. inch"):
            res = num * 4.014000000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="sq. mile" and second=="sq. foot"):
            res = num * 2.7880000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="sq. mile" and second=="acre"):
            res = num * 640
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="sq. mile" and second=="hectare"):
            res = num * 258.999
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="sq. mile" and second=="sq. meter"):
            res = num * 2.590000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="sq. mile" and second=="sq. yard"):
            res = num * 3.098000
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="sq. meter" and second=="sq. inch"):
            res = num * 1550
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="sq. meter" and second=="sq. foot"):
            res = num * 10.7639
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="sq. meter" and second=="acre"):
            res = num * 0.000247105
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="sq. meter" and second=="hectare"):
            res = num * 0.0001
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="sq. meter" and second=="sq. mile"):
            res = num * 0.0000003861
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="sq. meter" and second=="sq. yard"):
            res = num * 1.19599
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="sq. yard" and second=="sq. inch"):
            res = num * 1296
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="sq. yard" and second=="sq. foot"):
            res = num * 9
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="sq. yard" and second=="acre"):
            res = num * 0.000206612
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="sq. yard" and second=="hectare"):
            res = num * 0.000083613
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="sq. yard" and second=="sq. mile"):
            res = num * 0.00000032283
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="sq. yard" and second=="sq. meter"):
            res = num * 0.836127
            messagebox.showinfo('Result', f"It's {res} {second}.")
        else:
            messagebox.showinfo('Result', f"It's {num} {second}.")

    submit = Frame(areaConverter)
    Button(submit, text="Submit", command=result).pack(side=LEFT, padx=4)
    Button(submit, text="Close", command=areaConverter.destroy).pack(side=LEFT, padx=7)
    submit.pack(pady=20)

    areaConverter.mainloop()

def tempconversion():
    temperatureConverter = Tk()
    temperatureConverter.title("Temperature Conversion")
    temperatureConverter.geometry('370x140')
    temperatureConverter.resizable(0, 0)

    Label(temperatureConverter, text="Enter the Value", font=("Arial Bold", 17), justify='center').pack(pady=10)

    user = Frame(temperatureConverter)
    nums = Entry(user, width=10)
    nums.pack(side=LEFT)

    left = Combobox(user, state='readonly', width=10)
    left['values']= ("Celsius", "Fahrenheit", "Kelvin")
    left.current(0)
    left.pack(side=LEFT, padx=10)

    Label(user, text="to", font=("Arial", 12)).pack(side=LEFT)

    right = Combobox(user, state='readonly', width=10)
    right['values']= ("Celsius", "Fahrenheit", "Kelvin")
    right.current(1)
    right.pack(side=LEFT, padx=10)

    user.pack()

    def result():
        # Getting the values
        first = left.get()
        second = right.get()
        try:
            num = int(nums.get()) # try-except
        except:
            num = float(nums.get())
        
        # Main logic starts here
        res = 0.0
        
        if(first=="Celsius" and second=="Fahrenheit"):
            res = (num * (9/5) + 32)
            messagebox.showinfo('Result', f"Temperature in degree {second} is {res}.")
        elif(first=="Celsius" and second=="Kelvin"):
            res = num + 273.15
            messagebox.showinfo('Result', f"Temperature in degree {second} is {res}.")
        elif(first=="Fahrenheit" and second=="Celsius"):
            res = (num - 32) * (5/9)
            messagebox.showinfo('Result', f"Temperature in degree {second} is {res}.")
        elif(first=="Fahrenheit" and second=="Kelvin"):
            res = (num - 32) * (5/9) + 273.15
            messagebox.showinfo('Result', f"Temperature in degree {second} is {res}.")
        elif(first=="Kelvin" and second=="Fahrenheit"):
            res = (num - 273.15) * (9/5) + 32
            messagebox.showinfo('Result', f"Temperature in degree {second} is {res}.")
        elif(first=="Kelvin" and second=="Celsius"):
            res = num - 273.15
            messagebox.showinfo('Result', f"Temperature in degree {second} is {res}.")
        else:
            messagebox.showinfo('Result', f"Temperature in degree {second} is {num}.")

    submit = Frame(temperatureConverter)
    Button(submit, text="Submit", command=result).pack(side=LEFT, padx=4)
    Button(submit, text="Close", command=temperatureConverter.destroy).pack(side=LEFT, padx=7)
    submit.pack(pady=20)

    temperatureConverter.mainloop()

def cconversion():
    currencyConverter = Tk()
    currencyConverter.title("Currency Conversion")
    currencyConverter.geometry('300x140')
    currencyConverter.resizable(0, 0)

    Label(currencyConverter, text="Enter the Value", font=("Arial Bold", 17), justify='center').pack(pady=10)

    user = Frame(currencyConverter)
    nums = Entry(user, width=10)
    nums.pack(side=LEFT)

    left = Combobox(user, state='readonly', width=5)
    left['values']= ("USD", "CAD", "INR", "JPY", "AED")
    left.current(0)
    left.pack(side=LEFT, padx=10)

    Label(user, text="to", font=("Arial", 12)).pack(side=LEFT)

    right = Combobox(user, state='readonly', width=5)
    right['values']= ("USD", "CAD", "INR", "JPY", "AED")
    right.current(1)
    right.pack(side=LEFT, padx=10)

    user.pack()

    def result():
        # Getting the values
        first = left.get()
        second = right.get()
        try:
            num = int(nums.get())
        except:
            num = float(nums.get())
        
        # Main logic starts here
        res = 0.0
        
        if (first=="USD" and second=="CAD"):
            res = num*1.26
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="USD" and second=="INR"):
            res = num * 74.35
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="USD" and second=="JPY"):
            res = num * 113.93
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="USD" and second=="AED"):
            res = num * 3.67
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="CAD" and second=="USD"):
            res = num * 0.80
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="CAD" and second=="INR"):
            res = num * 59.23
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="CAD" and second=="JPY"):
            res = num * 90.77
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="CAD" and second=="AED"):
            res = num * 2.93
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="INR" and second=="USD"):
            res = num * 0.013
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="INR" and second=="CAD"):
            res = num * 0.017
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="INR" and second=="JPY"):
            res = num * 1.53
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="INR" and second=="AED"):
            res = num * 0.049
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="JPY" and second=="USD"):
            res = num * 0.0088
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="JPY" and second=="CAD"):
            res = num * 0.011
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="JPY" and second=="INR"):
            res = num * 0.65
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="JPY" and second=="AED"):
            res = num * 0.032
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="AED" and second=="USD"):
            res = num * 0.27
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="AED" and second=="CAD"):
            res = num * 0.34
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="AED" and second=="INR"):
            res = num * 20.24
            messagebox.showinfo('Result', f"It's {res} {second}.")
        elif(first=="AED" and second=="JPY"):
            res = num * 31.02
            messagebox.showinfo('Result', f"It's {res} {second}.")
            messagebox.showinfo('Result', f"It's {res} {second}.")
        else:
            messagebox.showinfo('Result', f"It's {num} {second}.")

    submit = Frame(currencyConverter)
    Button(submit, text="Submit", command=result).pack(side=LEFT, padx=4)
    Button(submit, text="Close", command=currencyConverter.destroy).pack(side=LEFT, padx=7)
    submit.pack(pady=20)

    currencyConverter.mainloop()

Label(unitConverter, text="Select anyone to start conversion", font=("Arial Bold", 17), justify='center').pack(pady=10)
conversions = Frame(unitConverter) # To control the position of buttons
Button(conversions, text="Length Conversion", command=lconversion, padx=31).pack(pady=1)
Button(conversions, text="Mass Conversion", command=mconversion, padx=36).pack(pady=1)
Button(conversions, text="Time Conversion", command=tconversion, padx=36).pack(pady=1)
Button(conversions, text="Area Conversion", command=aconversion, padx=38).pack(pady=1)
Button(conversions, text="Temperature Conversion", command=tempconversion).pack(pady=1)
Button(conversions, text="Currency Conversion", command=cconversion, padx=24).pack(pady=1)
Button(conversions, text="Close", command=unitConverter.destroy).pack(pady=10)
conversions.pack()

unitConverter.mainloop() # reloads the main window again & again