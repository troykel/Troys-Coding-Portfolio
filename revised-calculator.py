
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import math
import numpy


"""This Calculator was a result of having watched the Codemy video called, 
'Build A Simple Calculator App - Python Tkinter GUI Tutorial #5.  I added the 
rest of the button functionality, and the History / Memory functionality as well.

Working on reducing the repetition of code. (See the code I commented out, since
it's no longer needed)  I changed the calculator, so that now it's going to 
dynamically create a new history label after completion of each equation. I have
figured out how to automatically increment the equation numbers, so that they are
automatically printed as Equation1, Equation2, and so on. I couldn't do that with
the label names, so I had to make them all one name with different x,y coordinates."""

class Calculator(ttk.Frame):
    def __init__(self):
        root = Tk()
        root.title("TK's Calculator")
        root.geometry("700x500")
        root.resizable(False, False)

        self.nbrlist = []
        self.labellist = []
        self.buttonclicks = 0
        self.equalclicks = 0
        self.plusclicks = 0
        self.multiplyclicks = 0
        self.minusclicks = 0
        self.divideclicks = 0
        self.percentclicks = 0
        self.moduloclicks = 0
        self.chainAdd = 0
        self.chainMult = 0
        self.historyclicks = 0
        self.decimalclicks = 0

        def buttonClick(number):
            self.buttonclicks += 1
            self.current = self.result.get()
            self.result.delete(0, END)
            self.result.insert(0, str(self.current) + str(number))
            if number == "%":
               number = 0.01

        def clearEntry():
            self.current = self.result.get()
            self.result.delete(0, END)

        def clear():
            self.nbrlist.clear()
            self.plusclicks = 0
            self.multiplyclicks = 0
            self.current = self.result.get()
            self.result.delete(0, END)
            self.memory = 0
            for label in self.labellist:
                label.destroy()
            self.equalclicks = 0
            self.historyclicks = 0

        def decimal():
            self.result.insert(len(self.result.get()), ".")
            self.decimalclicks += 1
            if len(self.nbrlist) == 0 and self.decimalclicks >= 2:
                messagebox.showinfo("Error:", "A number can have only 1 decimal in it!")
                self.result.delete(0, END)
                self.decimalclicks = 0

        def delete():
            self.backspace = str(self.result.get())
            self.result.delete(0, END)
            self.result.insert(0, self.backspace[0:-1])

        def getfirstNumber():
            try:
                self.firstNumber = self.result.get()
                if "." in str(self.firstNumber):
                    self.firstNumber = float(self.firstNumber)
                else:
                    self.firstNumber = int(self.firstNumber)
                self.nbrlist.append(self.firstNumber)
                print(f"self.firstNumber = {self.firstNumber}")
            except ValueError:
                messagebox.showinfo("Error", "You haven't clicked any number yet")

        def getsecondNumber():
            self.secondNumber = self.result.get()
            if "." in str(self.firstNumber):
                self.secondNumber = float(self.secondNumber)
                print(f"self.secondNumber = {self.secondNumber}")
            if "." in str(self.secondNumber):
                self.firstNumber = float(self.firstNumber)
                print(f"self.secondNumber = {self.secondNumber}")
            else:
                self.secondNumber = int(self.secondNumber)
            self.nbrlist.append(self.secondNumber)

        def add():
            self.plusclicks += 1
            print(f"self.plusclicks = {self.plusclicks}")
            self.calculation = "Add"
            getfirstNumber()
            self.result.delete(0, END)

        def subtract():
            self.minusclicks += 1
            print(f"self.minusclicks = {self.minusclicks}")
            self.calculation = "Subtract"
            getfirstNumber()
            self.result.delete(0, END)

        def multiply():
            self.multiplyclicks += 1
            print("self.multiplyclicks = ", self.multiplyclicks)
            self.calculation = "Multiply"
            getfirstNumber()
            self.result.delete(0, END)

        def divide():
            self.divideclicks += 1
            print(f"self.divideclicks = {self.divideclicks}")
            self.calculation = "Divide"
            getfirstNumber()
            self.result.delete(0, END)

        def percent():
            self.percentclicks += 1
            print(f"self.percentclicks = {self.percentclicks}")
            self.calculation = "Percent"
            getfirstNumber()
            self.result.delete(0, END)

        def modulo():
            self.moduloclicks += 1
            print(f"self.moduloclicks = {self.moduloclicks}")
            self.calculation = "Modulo"
            getfirstNumber()
            self.result.delete(0, END)

        def squareRootOfx():
            self.calculation = "SquareRootOfx"
            getfirstNumber()

        def powerOf2():
            self.calculation = "PowerOf2"
            getfirstNumber()

        def oneOverX():
            getfirstNumber()
            self.calculation = "OneOverx"
            self.result.delete(0, END)
            #try:
            #    self.result.insert(0, round(1 / self.firstNumber, 4))
            #except ZeroDivisionError:
            #    messagebox.showinfo("Error", "You can't divide by zero!")

        def equals():
            self.equalclicks += 1
            self.historyclicks += 1
            print("self.equalclicks = ", self.equalclicks)
            if self.calculation != "OneOverx":
                getsecondNumber()
            self.result.delete(0, END)

            if self.calculation == "Add":
                if self.plusclicks == 1:
                    def addnbrs(self):
                        """A self.equalclicks click means that a single equation has
                        completed, so when 1 click of self.equalclicks occurs, we're
                        on Equation1, when 2 clicks, Equation2, and so on."""
                        self.result.delete(0, END)
                        self.sum = (self.firstNumber + self.secondNumber)
                        self.result.insert(0, round(self.sum, 4))
                        self.eq = f"Eq{self.equalclicks} = {self.firstNumber} + {self.secondNumber} = {round(self.sum, 4):,}"

                        print(self.eq)
                        if self.equalclicks <= 8:
                            history()
                        self.nbrlist.clear()

                    addnbrs(self)
                    self.plusclicks = 0

                if len(self.nbrlist) > 2:
                    if self.plusclicks >= 2:
                        self.chaineq = ""
                        self.result.insert(0, sum(self.nbrlist))
                        elementCount = 0
                        for nbr in self.nbrlist:
                            elementCount += 1
                            if elementCount == len(self.nbrlist):
                                self.chaineq += f"{nbr} = {sum(self.nbrlist):,}"
                            else:
                                self.chaineq += f"{nbr} + "

                        print("\n", self.nbrlist)
                        print(self.chaineq)
                        if self.equalclicks <= 8:
                            history()
                        self.plusclicks = 0
                        self.nbrlist.clear()

            if self.calculation == "Multiply":
                if self.multiplyclicks == 1:
                    def multiplyNbrs():
                        self.result.delete(0, END)
                        self.mult = round(self.firstNumber * self.secondNumber, 4)
                        print(f"self.mult = {self.mult}")
                        self.result.insert(0, self.mult)
                        self.eq = f"Eq{self.equalclicks} = {self.firstNumber} * {self.secondNumber} = {self.mult:,}"
                        print(self.eq)

                    multiplyNbrs()
                    if self.equalclicks <= 8:
                        history()
                    self.nbrlist.clear()
                    self.multiplyclicks = 0

                if len(self.nbrlist) > 2:
                    if self.multiplyclicks >= 2:
                        self.chaineq = ""
                        product = round(numpy.prod(self.nbrlist), 4)
                        self.result.insert(0, product)
                        elementCount = 0
                        for nbr in self.nbrlist:
                            elementCount += 1
                            if elementCount == len(self.nbrlist):
                                self.chaineq += f"{nbr} = {product:,}"
                            else:
                                self.chaineq += f"{nbr} * "

                        print("\n", self.nbrlist)
                        print(self.chaineq)
                        if self.equalclicks <= 8:
                            history()
                        self.nbrlist.clear()
                        self.multiplyclicks = 0

            if self.calculation == "Subtract":
                if self.minusclicks == 1:
                    def subtractNbrs():
                        self.diff = round(self.firstNumber - self.secondNumber, 4)
                        self.result.insert(0, self.diff)
                        self.eq = f"Eq{self.equalclicks} = {self.firstNumber} - {self.secondNumber} = {self.diff:,}"
                        print(self.eq)
                        self.nbrlist.clear()
                        self.minusclicks = 0

                    subtractNbrs()
                    history()

                if len(self.nbrlist) > 2:
                    if self.minusclicks >= 2:
                        self.chaineq = ""
                        elementCount = 0
                        self.finaldiff = self.nbrlist[0]
                        for nbr in self.nbrlist[1:]:
                            self.finaldiff -= nbr
                        for nbr in self.nbrlist:
                            elementCount += 1
                            if elementCount == len(self.nbrlist):
                                self.chaineq += f"{nbr} = {self.finaldiff:,}"
                            else:
                                self.chaineq += f"{nbr} - "
                        self.result.insert(0, self.finaldiff)
                        print("\n", self.nbrlist)
                        print(self.chaineq)
                        if self.equalclicks <= 8:
                            history()
                        self.nbrlist.clear()
                        self.minusclicks = 0

            if self.calculation == "Divide":
                try:
                    if self.divideclicks == 1:
                        def divideNbrs():
                            self.divide = round(self.firstNumber / float(self.secondNumber), 4)
                            self.result.insert(0, self.divide)
                            self.eq = f"Eq{self.equalclicks} = {self.firstNumber} / {self.secondNumber} = {self.divide:,}"
                            print(self.eq)
                            self.nbrlist.clear()
                            self.divideclicks = 0

                        divideNbrs()
                        if self.equalclicks <= 8:
                            history()

                    if len(self.nbrlist) > 2:
                        if self.divideclicks >= 2:
                            self.chainDiveq = ""
                            elementCount = 0
                            self.finaldiv = self.nbrlist[0]
                            for nbr in self.nbrlist[1:]:
                                self.finaldiv /= nbr
                            for nbr in self.nbrlist:
                                elementCount += 1
                                if elementCount == len(self.nbrlist):
                                    self.chaineq += f"{nbr} = {self.finaldiv:,}"
                                else:
                                    self.chaineq += f"{nbr} / "

                            self.result.insert(0, self.finaldiv)

                            print("\n", self.nbrlist)
                            print(self.chaineq)

                            if self.equalclicks <= 8:
                                history()
                            self.nbrlist.clear()
                            self.divideclicks = 0

                except ZeroDivisionError:
                    messagebox.showinfo("Division by 0 error!", "Error:  You can't divide by zero!")
                    self.equalclicks -= 1
                    self.historyclicks -= 1

            if self.calculation == "Percent":
                self.percentage = round((self.firstNumber * 0.01) * float(self.secondNumber), 4)
                self.result.insert(0, self.percentage)
                self.eq = f"Eq{self.equalclicks} = {self.firstNumber} % of {self.secondNumber} = {self.percentage:,}"
                print(self.eq)
                if self.equalclicks <= 8:
                    history()
                self.nbrlist.clear()

            if self.calculation == "Modulo":
                if self.moduloclicks == 1:
                    self.mod = round(self.firstNumber % self.secondNumber, 4)
                    self.result.insert(0, self.mod)
                    self.eq = f"Eq{self.equalclicks} = {self.firstNumber} % {self.secondNumber} = {self.mod:,}"
                    print(self.eq)
                    if self.equalclicks <= 8:
                        history()
                    self.nbrlist.clear()

                if self.moduloclicks >= 2:
                    self.chaineq = ""
                    elementCount = 0
                    self.finalmod = self.nbrlist[0]
                    for nbr in self.nbrlist[1:]:
                        self.finalmod %= nbr
                    for nbr in self.nbrlist:
                        elementCount += 1
                        if elementCount == len(self.nbrlist):
                            self.chaineq += f"{nbr} = {self.finalmod:,}"
                        else:
                            self.chaineq += f"{nbr} % "

                    self.result.insert(0, self.finalmod)

                    print("\n", self.nbrlist)
                    print(self.chaineq)

                    if self.equalclicks <= 8:
                        history()
                    self.nbrlist.clear()
                    self.moduloclicks = 0

            if self.calculation == "SquareRootOfx":
                self.squareRootOfx = round(math.sqrt(self.firstNumber), 15)
                self.result.delete(0, END)
                self.result.insert(0, self.squareRootOfx)
                self.eq = f"Eq{self.equalclicks} = √{self.firstNumber} = {self.squareRootOfx:,}"
                print(self.eq)
                if self.equalclicks <= 8:
                    history()
                self.nbrlist.clear()

            if self.calculation == "PowerOf2":
                self.power2 = round(self.firstNumber ** 2, 4)
                self.result.delete(0, END)
                self.result.insert(0, self.power2)
                self.eq = f"Eq{self.equalclicks} = {self.firstNumber}² = {self.power2:,}"
                print(self.powerOf2eq)
                if self.equalclicks <= 8:
                    history()
                self.nbrlist.clear()

            if self.calculation == "OneOverx":
                try:
                    self.oneoverx = round(1 / float(self.firstNumber), 4)
                    self.result.insert(0, self.oneoverx)
                    self.eq = f"Eq{self.equalclicks} = 1 / {self.firstNumber} = {self.oneoverx:,}"
                    print(self.eq)
                    if self.equalclicks <= 8:
                        history()
                    self.nbrlist.clear()

                except ZeroDivisionError:
                    messagebox.showinfo("Division by 0 error!", "You can't divide by zero!")
                    self.historyclicks -= 1
                    self.equalclicks -= 1

                if self.historyclicks > self.equalclicks:
                    messagebox.showinfo("Error!", "You haven't made any new calculations yet")



        def MPlus():
            self.memory = self.result.get()
            #Check to see if self.firstNumber even exists (been defined)
            try:
                self.firstNumber
            #If it doesn't exist, an AttributeError will pop up.
            except AttributeError:
                self.firstNumber = self.memory
            try:
                self.secondNumber
            except AttributeError:
                self.secondNumber = self.memory
            self.result.delete(0, END)

        def memory():
            try:
                self.memoryLabel = Label(frame2, text=self.memory, bg="#80c1ff", fg="navy", width=25, anchor="w")
                self.memoryLabel.place(x=5, y=85)
                self.labellist.append(self.memoryLabel)

                self.result.insert(0, self.memory)
            except AttributeError:
                messagebox.showinfo("Error!", "You haven't added a number into memory yet. \n"
                                              " Click a number and M+")

        def MR():
            try:
                self.result.insert(0, self.memory)
            except AttributeError:
                messagebox.showinfo("Error!", "You haven't added a number into memory yet. \n"
                                              " Click a number and M+")

        def MC():
            try:
                self.memory
            except AttributeError:
                messagebox.showinfo("Error!", "You haven't added a number into memory yet. \n"
                                             "Click a number and M+")
            else:
                if self.memory != 0:
                    self.memory = 0

            try:
                self.memoryLabel
            except AttributeError:
                pass

            else:
                if self.memoryLabel["text"] != "":
                    self.memoryLabel["text"] = ""



        def plusMinus():
            self.plsMinus = self.result.get()
            self.result.delete(0, END)
            try:
                if "." in str(self.plsMinus):
                    self.plsMinus = float(self.plsMinus)
                if float(self.plsMinus) > 0:
                    self.result.insert(0, -float(self.plsMinus))
                else:
                    if float(self.plsMinus) < 0:
                        self.result.insert(0, float(self.plsMinus) * -1)
                    else:
                        if int(self.plsMinus) > 0:
                            self.result.insert(0, -int(self.plsMinus))
                        if int(self.plsMinus) < 0:
                            self.result.insert(0, int(self.plsMinus) * -1)
            except ValueError:
                messagebox.showinfo("Error", "You haven't clicked a number yet")
                self.plusclicks -= 1

        def history():
            if self.historyclicks == 1 and self.equalclicks == 0:
                messagebox.showinfo("Error", "You haven't used the calculator yet!")

            if self.historyclicks > self.equalclicks:
                    messagebox.showinfo("Error", "History items requested exceeds number of equations calculated!")
                    self.historyclicks = self.equalclicks

            #This dictionary dynamically locates the hlabels up to 8 total labels
            labellocdict = {1: 85, 2: 125, 3: 165, 4: 205, 5: 245, 6: 285, 7: 325, 8: 365}

            #hlabel as in historylabel
            #hlabels are for non-chain equations
            def hlabel():
                self.Label = Label(frame2, text=self.eq, bg="#80c1ff", fg="navy", anchor="w")
                self.Label.configure(font=("Verdana", 10), fg="Navy")
                # If 2 self.equalclicks, then labellocdict[2] means y = 125
                self.Label.place(x=5, y=labellocdict[self.equalclicks])
                self.labellist.append(self.Label)

            #An hlabel for chain equations: 1 self.equalclick (the equal sign) and >= 2 operands
            def hlabelchaineq():
                self.Label = Label(frame2, text=f"Eq{self.equalclicks} = {self.chaineq}",
                                   bg="#80c1ff", fg="navy", anchor="w")
                self.Label.configure(font=("Verdana", 10), fg="Navy")
                self.Label.place(x=5, y=labellocdict[self.equalclicks])
                self.labellist.append(self.Label)
                self.nbrlist.clear()

            def biglabelchaineq():
                try:
                    self.bigLabelnc
                except AttributeError:
                    pass
                else:
                    self.bigLabelnc.destroy()
                self.bigLabel = Label(root, text=f"Eq{self.equalclicks} = {self.chaineq}",
                                   fg="navy", anchor="w")
                self.bigLabel.configure(font=("Verdana", 18), fg="Navy")
                self.bigLabel.place(x=35, y=5)
                self.labellist.append(self.bigLabel)
                self.nbrlist.clear()

            #nc as in no chain(regular equation with only 2 numbers and 1 operand between them.)
            def biglabelnc():
                try:
                    self.bigLabel
                except AttributeError:
                    pass
                else:
                    self.bigLabel.destroy()
                self.bigLabelnc = Label(root, text=self.eq,
                                   fg="navy", anchor="w")
                self.bigLabelnc.configure(font=("Verdana", 18))
                self.bigLabelnc.place(x=35, y=5)
                self.labellist.append(self.bigLabelnc)
                self.nbrlist.clear()

            if self.calculation == "Add":
                if len(self.nbrlist) > 2:  # If it's chain addition: 1+2+3 vs 1+2
                    hlabelchaineq()
                    biglabelchaineq()

                else:
                    hlabel()
                    biglabelnc()

            if self.calculation == "Multiply":
                if len(self.nbrlist) > 2:  # If it's chain addition: 1+2+3 vs 1+2
                    hlabelchaineq()
                    biglabelchaineq()

                else:
                    hlabel()
                    biglabelnc()

            if self.calculation == "Subtract":
                if len(self.nbrlist) > 2:  # If it's chain subtraction: 3-2-1 vs 3-2
                    hlabelchaineq()
                    biglabelchaineq()

                else:
                    hlabel()
                    biglabelnc()

            if self.calculation == "Divide":
                if len(self.nbrlist) > 2:  # If it's chain division: 48/8/2 vs 48/8
                    hlabelchaineq()
                    biglabelchaineq()

                else:
                    hlabel()
                    biglabelnc()

            if self.calculation == "Percent":
                hlabel()
                biglabelnc()

            if self.calculation == "Modulo":
                if len(self.nbrlist) > 2:  # If it's chain modulo: 48%8%2 vs 48%8
                    hlabelchaineq()
                    biglabelchaineq()

                else:
                    hlabel()
                    biglabelnc()

            if self.calculation == "SquareRootOfx":
                hlabel()
                biglabelnc()

            if self.calculation == "PowerOf2":
                hlabel()
                biglabelnc()

            if self.calculation == "OneOverx":
                hlabel()
                biglabelnc()

            if self.equalclicks == 8:
                if self.historyclicks > 8:
                    messagebox.showinfo("Error", "History = ONLY the last 8 equations")

        def clearhistory():
            for label in self.labellist:
                label.destroy()

        frame1 = Frame(root, bg="#80c1ff", bd=5)
        frame1.place(relx=.05, rely=.1, relwidth=0.70, relheight=0.86)

        #Grid.rowconfigure(frame1, 0, weight=1)
        #Grid.columnconfigure(frame1, 0, weight=1)

        buttonMC = Button(frame1, text="MC", height=3, width=5, command=MC)
        buttonMC.grid(row=3, column=0)
        buttonMC.configure(width=7, height=3, font=("Verdana", 10, "bold"), fg="Navy")

        MRButton = Button(frame1, text="MR", height=3, width=5, command=MR)
        MRButton.grid(row=3, column=1)
        MRButton.configure(width=7, height=3, font=("Verdana", 10, "bold"), fg="Navy")

        MPlusButton = Button(frame1, text="M+", height=3, width=5, command=MPlus)
        MPlusButton.grid(row=3, column=2)
        MPlusButton.configure(width=7, height=3, font=("Verdana", 10, "bold"), fg="Navy")

        percentButton = Button(frame1, text="%", height=3, width=5, command=percent)
        percentButton.grid(row=3, column=3)
        percentButton.configure(width=7, height=3, font=("Verdana", 10, "bold"), fg="Navy")

        buttonModulo = Button(frame1, text="Mod", height=3, width=5, command=modulo)
        buttonModulo.grid(row=4, column=0)
        buttonModulo.configure(width=7, height=3, font=("Verdana", 10, "bold"), fg="Navy")

        buttonSqRoot = Button(frame1, text="√(x)", height=3, width=5, command=squareRootOfx)
        buttonSqRoot.grid(row=4, column=1)
        buttonSqRoot.configure(width=7, height=3, font=("Verdana", 10, "bold"), fg="Navy")

        button2ndPower = Button(frame1, text="x²", height=3, width=5, command=powerOf2)
        button2ndPower.grid(row=4, column=2)
        button2ndPower.configure(width=7, height=3, font=("Verdana", 10, "bold"), fg="Navy")

        buttonOneOverX = Button(frame1, text="1/x", height=3, width=5, command=oneOverX)
        buttonOneOverX.grid(row=4, column=3)
        buttonOneOverX.configure(width=7, height=3, font=("Verdana", 10, "bold"), fg="Navy")

        buttonCE = Button(frame1, text="CE", height=3, width=5, command=clearEntry)
        buttonCE.grid(row=5, column=0)
        buttonCE.configure(width=7, height=3, font=("Verdana", 10, "bold"), fg="Navy")

        buttonClear = Button(frame1, text="C", height=3, width=5, command=clear)
        buttonClear.grid(row=5, column=1)
        buttonClear.configure(width=7, height=3, font=("Verdana", 10, "bold"), fg="Navy")

        buttonDelete = Button(frame1, text="del", height=3, width=5, command=delete)
        buttonDelete.grid(row=5, column=2)
        buttonDelete.configure(width=7, height=3, font=("Verdana", 10, "bold"), fg="Navy")

        buttonDivide = Button(frame1, text="/", height=3, width=5, command=divide)
        buttonDivide.grid(row=5, column=3)
        buttonDivide.configure(width=7, height=3, font=("Verdana", 10, "bold"), fg="Navy")

        button7 = Button(frame1, text="7", height=3, width=5, command=lambda: buttonClick(7))
        button7.grid(row=6, column=0)
        button7.configure(width=7, height=3, font=("Verdana", 10, "bold"), fg="Navy")

        button8 = Button(frame1, text="8", height=3, width=5, command=lambda: buttonClick(8))
        button8.grid(row=6, column=1)
        button8.configure(width=7, height=3, font=("Verdana", 10, "bold"), fg="Navy")

        button9 = Button(frame1, text="9", height=3, width=5, command=lambda: buttonClick(9))
        button9.grid(row=6, column=2)
        button9.configure(width=7, height=3, font=("Verdana", 10, "bold"), fg="Navy")

        buttonMultiply = Button(frame1, text="x", height=3, width=5, command=multiply)
        buttonMultiply.grid(row=6, column=3)
        buttonMultiply.configure(width=7, height=3, font=("Verdana", 10, "bold"), fg="Navy")

        button4 = Button(frame1, text="4", height=3, width=5, command=lambda: buttonClick(4))
        button4.grid(row=7, column=0)
        button4.configure(width=7, height=3, font=("Verdana", 10, "bold"), fg="Navy")

        button5 = Button(frame1, text="5", height=3, width=5, command=lambda: buttonClick(5))
        button5.grid(row=7, column=1)
        button5.configure(width=7, height=3, font=("Verdana", 10, "bold"), fg="Navy")

        button6 = Button(frame1, text="6", height=3, width=5, command=lambda: buttonClick(6))
        button6.grid(row=7, column=2)
        button6.configure(width=7, height=3, font=("Verdana", 10, "bold"), fg="Navy")

        buttonMinus = Button(frame1, text="-", height=3, width=5, command=subtract)
        buttonMinus.grid(row=7, column=3)
        buttonMinus.configure(width=7, height=3, font=("Verdana", 10, "bold"), fg="Navy")

        button1 = Button(frame1, text="1", height=3, width=5, command=lambda: buttonClick(1))
        button1.grid(row=8, column=0)
        button1.configure(width=7, height=3, font=("Verdana", 10, "bold"), fg="Navy")

        button2 = Button(frame1, text="2", height=3, width=5, command=lambda: buttonClick(2))
        button2.grid(row=8, column=1)
        button2.configure(width=7, height=3, font=("Verdana", 10, "bold"), fg="Navy")

        button3 = Button(frame1, text="3", height=3, width=5, command=lambda: buttonClick(3))
        button3.grid(row=8, column=2)
        button3.configure(width=7, height=3, font=("Verdana", 10, "bold"), fg="Navy")

        buttonAdd = Button(frame1, text="+", height=3, width=5, command=add)
        buttonAdd.grid(row=8, column=3)
        buttonAdd.configure(width=7, height=3, font=("Verdana", 10, "bold"), fg="Navy")

        buttonPlusMinus = Button(frame1, text="+/-", height=3, width=5, command=plusMinus)
        buttonPlusMinus.grid(row=9, column=0)
        buttonPlusMinus.configure(width=7, height=3, font=("Verdana", 10, "bold"), fg="Navy")

        buttonZero = Button(frame1, text="0", height=3, width=5, command=lambda: buttonClick(0))
        buttonZero.grid(row=9, column=1)
        buttonZero.configure(width=7, height=3, font=("Verdana", 10, "bold"), fg="Navy")

        buttonDecimal = Button(frame1, text=".", height=3, width=5, command=decimal)
        buttonDecimal.grid(row=9, column=2)
        buttonDecimal.configure(width=7, height=3, font=("Verdana", 10, "bold"), fg="Navy")

        buttonEquals = Button(frame1, text="=", height=3, width=5, command=equals)
        buttonEquals.grid(row=9, column=3, sticky=N + S + E + W)
        buttonEquals.configure(width=7, height=3, font=("Verdana", 10, "bold"), fg="Navy")

        frame2 = Frame(root, bg="lightgrey", bd=5)
        frame2.place(relx=.5, rely=.1, relwidth=0.44, relheight=0.86)

        historyButton = Button(frame2, text="Clear History", fg="Navy", bg="#80c1ff", command=clearhistory)
        historyButton.configure(font=("Verdana", 12, "bold"), fg="Navy")
        historyButton.place(x=5, y=40)

        memoryButton = Button(frame2, text="Memory", bg="#80c1ff", fg="navy", command=memory)
        memoryButton.configure(font=("Verdana", 12, "bold"), fg="Navy")
        memoryButton.place(x=150, y=40)

        self.result = Entry(frame2, width=24, borderwidth=3)
        self.result.configure(font=("Verdana", 14))
        self.result.grid(row=0, column=0, pady=5)

        root.mainloop()


Calculator()

