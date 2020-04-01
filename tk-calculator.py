
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import math
import numpy


"""This Calculator was a result of having watched the Codemy video called, 
'Build A Simple Calculator App - Python Tkinter GUI Tutorial #5.  I added the 
rest of the button functionality, and the History / Memory functionality as well.

At this point, the calculator works, but is not able to chain calculations without
hitting the equal button between them. In other words, you can't do 2*2*2 = 8, you 
must do 2*2 = 4*2 = 8. I have not figured that part out... yet. 

You can use the History button to view the last 8 equations calculated. For each click
of the History button, you see another equation among the last x number of equations.  
If you click the History button more than 8 times, or more than the number of equations 
calculated, you get an error message.

By the way, I realize this is not the most optimal or DRY way to build an app.  
There's tons of repeated code, most of which was cut and pasted. If I had found a way to
put each equation scenario into a function, with changing the names of the equations by 
just their numbers:  equation1, then equation2 etc, that might have helped. 
(I tried using a list, and then dictionary, but I ran into problems with both approaches)."""


class Calculator(ttk.Frame):
    def __init__(self):
        root = Tk()
        root.title("TK's Calculator")
        root.geometry("700x500")
        root.resizable(True, True)

        self.buttonclicks = 0
        self.nbrlist = []

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

        def delete():
            self.backspace = str(self.result.get())
            self.result.delete(0, END)
            self.result.insert(0, self.backspace[0:-1])

        def getfirstnumber():
            try:
                self.firstNumber = self.result.get()
                if "." in str(self.firstNumber):
                    self.firstNumber = float(self.firstNumber)
                else:
                    self.firstNumber = int(self.firstNumber)
            except ValueError:
                messagebox.showinfo("Error", "You haven't clicked any number yet")

        def getsecondnumberAdd():
            if "." in str(self.secondNumber):
                self.nbrlist.append(float(self.secondNumber))
                self.result.insert(0, round(sum(self.nbrlist), 2))
            else:
                self.nbrlist.append(int(self.secondNumber))
                self.result.insert(0, round(sum(self.nbrlist), 2))

        def getsecondnumberMult():
            if "." in str(self.secondNumber):
                self.nbrlist.append(float(self.secondNumber))
                self.result.insert(0, numpy.prod(self.nbrlist))
            else:
                self.nbrlist.append(int(self.secondNumber))
                self.result.insert(0, numpy.prod(self.nbrlist))

        self.plusclicks = 0
        self.minusclicks = 0


        def add():
            self.plusclicks += 1
            print("plusclicks =", self.plusclicks)
            self.calculation = "Add"
            getfirstnumber()
            self.nbrlist.append(self.firstNumber)
            print("self.firstNumber = ", self.firstNumber)
            self.result.delete(0, END)

        def subtract():
            self.minusclicks += 1
            self.calculation = "Subtract"
            getfirstnumber()
            self.result.delete(0, END)

        self.multiplyclicks = 0

        def multiply():
            self.multiplyclicks += 1
            print("multiplyclicks = ", self.multiplyclicks)
            getfirstnumber()
            self.nbrlist.append(self.firstNumber)
            print("self.firstNumber = ", self.firstNumber)
            self.calculation = "Multiply"
            self.result.delete(0, END)

        def divide():
            getfirstnumber()
            self.calculation = "Divide"
            self.result.delete(0, END)

        self.percentclicks = 0

        def percent():
            self.percentclicks += 1
            getfirstnumber()
            self.calculation = "Percent"
            self.result.delete(0, END)

        def modulo():
            getfirstnumber()
            self.calculation = "Modulo"
            self.result.delete(0, END)

        def squareRootOfx():
            getfirstnumber()
            self.calculation = "SquareRootOfx"


        def powerOf2():
            getfirstnumber()
            self.calculation = "PowerOf2"

        def oneOverX():
            getfirstnumber()
            self.calculation = "OneOverx"
            self.result.delete(0, END)
            #try:
            #    self.result.insert(0, round(1 / self.firstNumber, 4))
            #except ZeroDivisionError:
            #    messagebox.showinfo("Error", "You can't divide by zero!")

        self.equalclicks = 0
        self.historyclicks = 0

        def equals():
            self.equalclicks += 1
            print("equalclicks = ", self.equalclicks)
            self.secondNumber = self.result.get()
            self.result.delete(0, END)
            print("self.secondNumber = ", self.secondNumber)
            self.chainMult = 0
            self.chainAdd = 0
            try:
                if self.calculation == "Add":
                    if self.plusclicks > 1 and self.equalclicks == 1:
                        self.chainAdd = True
                        getsecondnumberAdd()

                        self.equation1 = ""
                        elementCount = 0
                        for nbr in self.nbrlist:
                            print("The next nbr in self.nbrlist is: ", nbr, end="")
                            print("\n")
                            elementCount += 1
                            if elementCount == len(self.nbrlist):
                                self.equation1 += "{} = {}".format(self.secondNumber, sum(self.nbrlist))
                            else:
                                self.equation1 += "{} + ".format(nbr)

                        print("self.equation1 = ", self.equation1)
                        self.nbrlist.clear()
                        self.plusclicks = 0

                    if self.plusclicks > 1 and self.equalclicks == 2:
                        self.chainAdd = True
                        getsecondnumberAdd()

                        self.equation2 = ""
                        elementCount = 0
                        for nbr in self.nbrlist:
                            elementCount += 1
                            if elementCount == len(self.nbrlist):
                                self.equation2 += "{} = {}".format(self.secondNumber, sum(self.nbrlist))
                            else:
                                self.equation2 += "{} + ".format(nbr)

                        print("self.equation2 = ", self.equation2)
                        self.nbrlist.clear()
                        self.plusclicks = 0

                    if self.plusclicks > 1 and self.equalclicks == 3:
                        self.chainAdd = True
                        getsecondnumberAdd()

                        self.equation3 = ""
                        elementCount = 0
                        for nbr in self.nbrlist:
                            elementCount += 1
                            if elementCount == len(self.nbrlist):
                                self.equation3 += "{} = {}".format(self.secondNumber, sum(self.nbrlist))
                            else:
                                self.equation3 += "{} + ".format(nbr)

                        print("self.equation3 = ", self.equation3)
                        self.nbrlist.clear()
                        self.plusclicks = 0

                    if self.plusclicks > 1 and self.equalclicks == 4:
                        self.chainAdd = True
                        getsecondnumberAdd()

                        self.equation4 = ""
                        elementCount = 0
                        for nbr in self.nbrlist:
                            elementCount += 1
                            if elementCount == len(self.nbrlist):
                                self.equation4 += "{} = {}".format(self.secondNumber, sum(self.nbrlist))
                            else:
                                self.equation4 += "{} + ".format(nbr)

                        print("self.equation4 = ", self.equation4)
                        self.nbrlist.clear()

                    if self.plusclicks > 1 and self.equalclicks == 5:
                        self.chainAdd = True
                        getsecondnumberAdd()

                        self.equation5 = ""
                        elementCount = 0
                        for nbr in self.nbrlist:
                            elementCount += 1
                            if elementCount == len(self.nbrlist):
                                self.equation5 += "{} = {}".format(self.secondNumber, sum(self.nbrlist))
                            else:
                                self.equation5 += "{} + ".format(nbr)

                        print("self.equation5 = ", self.equation5)
                        self.nbrlist.clear()

                    if self.plusclicks > 1 and self.equalclicks == 6:
                        self.chainAdd = True
                        getsecondnumberAdd()

                        self.equation6 = ""
                        elementCount = 0
                        for nbr in self.nbrlist:
                            elementCount += 1
                            if elementCount == len(self.nbrlist):
                                self.equation6 += "{} = {}".format(self.secondNumber, sum(self.nbrlist))
                            else:
                                self.equation6 += "{} + ".format(nbr)

                        print("self.equation6 = ", self.equation6)
                        self.nbrlist.clear()

                    if self.plusclicks > 1 and self.equalclicks == 7:
                        self.chainAdd = True
                        getsecondnumberAdd()

                        self.equation7 = ""
                        elementCount = 0
                        for nbr in self.nbrlist:
                            elementCount += 1
                            if elementCount == len(self.nbrlist):
                                self.equation7 += "{} = {}".format(self.secondNumber, sum(self.nbrlist))
                            else:
                                self.equation7 += "{} + ".format(nbr)

                        print("self.equation7 = ", self.equation7)
                        self.nbrlist.clear()

                    if self.plusclicks > 1 and self.equalclicks == 8:
                        self.chainAdd = True
                        getsecondnumberAdd()

                        self.equation8 = ""
                        elementCount = 0
                        for nbr in self.nbrlist:
                            elementCount += 1
                            if elementCount == len(self.nbrlist):
                                self.equation8 += "{} = {}".format(self.secondNumber, sum(self.nbrlist))
                            else:
                                self.equation8 += "{} + ".format(nbr)

                        print("self.equation8 = ", self.equation8)
                        self.nbrlist.clear()

                #If NOT a chain equation:
                #If a float, has to be converted to a float.

                    if "." in str(self.firstNumber) or str(self.secondNumber):
                        if self.equalclicks == 1 and self.plusclicks == 1:
                            self.result.insert(0, round(float(self.firstNumber) + float(self.secondNumber), 4))
                            self.sum = round(float(self.firstNumber) + float(self.secondNumber), 4)
                            self.equation1 = "{} + {} = {}".format(self.firstNumber, self.secondNumber, self.sum)
                            print("Equation1 = ", self.equation1)
                            self.nbrlist.clear()

                        if self.equalclicks == 2 and self.plusclicks == 1:
                            self.result.insert(0, round(float(self.firstNumber) + float(self.secondNumber), 4))
                            self.sum = float(self.firstNumber)
                            self.sum = round(float(self.firstNumber) + float(self.secondNumber), 4)
                            self.equation2 = "{} + {} = {}".format(self.firstNumber, self.secondNumber, self.sum)
                            print("Equation2 = ", self.equation2)
                            self.nbrlist.clear()

                        if self.equalclicks == 3 and self.plusclicks == 1:
                            self.result.insert(0, round(float(self.firstNumber) + float(self.secondNumber), 4))
                            self.sum = float(self.firstNumber)
                            self.sum = round(float(self.firstNumber) + float(self.secondNumber), 4)
                            self.equation3 = "{} + {} = {}".format(self.firstNumber, self.secondNumber, self.sum)
                            print("Equation3 = ", self.equation3)
                            self.nbrlist.clear()

                        if self.equalclicks == 4 and self.plusclicks == 1:
                            self.result.insert(0, round(float(self.firstNumber) + float(self.secondNumber), 4))
                            self.sum = float(self.firstNumber)
                            self.sum = round(float(self.firstNumber) + float(self.secondNumber), 4)
                            self.equation4 = "{} + {} = {}".format(self.firstNumber, self.secondNumber, self.sum)
                            print("Equation4 = ", self.equation4)
                            self.nbrlist.clear()

                        if self.equalclicks == 5 and self.plusclicks == 1:
                            self.result.insert(0, round(float(self.firstNumber) + float(self.secondNumber), 4))
                            self.sum = float(self.firstNumber)
                            self.sum = round(float(self.firstNumber) + float(self.secondNumber), 4)
                            self.equation5 = "{} + {} = {}".format(self.firstNumber, self.secondNumber, self.sum)
                            print("Equation5 = ", self.equation5)
                            self.nbrlist.clear()

                        if self.equalclicks == 6 and self.plusclicks == 1:
                            self.result.insert(0, round(float(self.firstNumber) + float(self.secondNumber), 4))
                            self.sum = float(self.firstNumber)
                            self.sum = round(float(self.firstNumber) + float(self.secondNumber), 4)
                            self.equation6 = "{} + {} = {}".format(self.firstNumber, self.secondNumber, self.sum)
                            print("Equation6 = ", self.equation6)
                            self.nbrlist.clear()

                        if self.equalclicks == 7 and self.plusclicks == 1:
                            self.result.insert(0, round(float(self.firstNumber) + float(self.secondNumber), 4))
                            self.sum = float(self.firstNumber)
                            self.sum = round(float(self.firstNumber) + float(self.secondNumber), 4)
                            self.equation7 = "{} + {} = {}".format(self.firstNumber, self.secondNumber, self.sum)
                            print("Equation7 = ", self.equation7)
                            self.nbrlist.clear()

                        if self.equalclicks == 8 and self.plusclicks == 1:
                            self.result.insert(0, round(float(self.firstNumber) + float(self.secondNumber), 4))
                            self.sum = float(self.firstNumber)
                            self.sum = round(float(self.firstNumber) + float(self.secondNumber), 4)
                            self.equation8 = "{} + {} = {}".format(self.firstNumber, self.secondNumber, self.sum)
                            print("Equation8 = ", self.equation8)
                            self.nbrlist.clear()

                #If NOT a float, then has to be treated like an integer

                    else:
                        if self.plusclicks == 1 and self.equalclicks == 1:
                            self.result.delete(0, END)
                            self.result.insert(0, int(self.firstNumber) + int(self.secondNumber))
                            self.sum = self.firstNumber + int(self.secondNumber)
                            self.equation1 = "{} + {} = {}".format(self.firstNumber, self.secondNumber, self.sum)
                            print("Equation1 = ", self.equation1)
                            self.nbrlist.clear()

                        if self.equalclicks == 2 and self.plusclicks == 1:
                            self.sum = self.firstNumber
                            self.sum = self.firstNumber + int(self.secondNumber)
                            self.equation2 = "{} + {} = {}".format(self.firstNumber, self.secondNumber, self.sum)
                            print("Equation2 = ", self.equation2)
                            self.nbrlist.clear()

                        if self.equalclicks == 3 and self.plusclicks == 1:
                            self.sum = self.firstNumber
                            self.sum = self.firstNumber + int(self.secondNumber)
                            self.equation3 = "{} + {} = {}".format(self.firstNumber, self.secondNumber, self.sum)
                            print("Equation3 = ", self.equation3)
                            self.nbrlist.clear()

                        if self.equalclicks == 4 and self.plusclicks == 1:
                            self.sum = self.firstNumber
                            self.sum = self.firstNumber + int(self.secondNumber)
                            self.equation4 = "{} + {} = {}".format(self.firstNumber, self.secondNumber, self.sum)
                            print("Equation4 = ", self.equation4)
                            self.nbrlist.clear()

                        if self.equalclicks == 5 and self.plusclicks == 1:
                            self.sum = self.firstNumber
                            self.sum = self.firstNumber + int(self.secondNumber)
                            self.equation5 = "{} + {} = {}".format(self.firstNumber, self.secondNumber, self.sum)
                            print("Equation5 = ", self.equation5)
                            self.nbrlist.clear()

                        if self.equalclicks == 6 and self.plusclicks == 1:
                            self.sum = self.firstNumber
                            self.sum = self.firstNumber + int(self.secondNumber)
                            self.equation6 = "{} + {} = {}".format(self.firstNumber, self.secondNumber, self.sum)
                            print("Equation6 = ", self.equation6)
                            self.nbrlist.clear()

                        if self.equalclicks == 7 and self.plusclicks == 1:
                            self.sum = self.firstNumber
                            self.sum = self.firstNumber + int(self.secondNumber)
                            self.equation7 = "{} + {} = {}".format(self.firstNumber, self.secondNumber, self.sum)
                            print("Equation7 = ", self.equation7)
                            self.nbrlist.clear()

                        if self.equalclicks == 8 and self.plusclicks == 1:
                            self.sum = self.firstNumber
                            self.sum = self.firstNumber + int(self.secondNumber)
                            self.equation8 = "{} + {} = {}".format(self.firstNumber, self.secondNumber, self.sum)
                            print("Equation8 = ", self.equation8)
                            self.nbrlist.clear()

                if self.calculation == "Subtract":
                    if "." in str(self.firstNumber) or str(self.secondNumber):
                        if self.equalclicks == 1:
                            self.diff = round(float(self.firstNumber) - float(self.secondNumber), 4)
                            self.result.insert(0, self.diff)
                            self.equation1 = "{} - {} = {}".format(float(self.firstNumber), float(self.secondNumber), self.diff)
                            print("Equation1 = ", self.equation1)
                            self.nbrlist.clear()

                        if self.equalclicks == 2:
                            self.diff = round(float(self.firstNumber) - float(self.secondNumber), 4)
                            self.result.insert(0, self.diff)
                            self.equation2 = "{} - {} = {}".format(float(self.firstNumber), float(self.secondNumber),
                                                                   self.diff)
                            print("Equation2 = ", self.equation2)
                            self.nbrlist.clear()

                        if self.equalclicks == 3:
                            self.diff = round(float(self.firstNumber) - float(self.secondNumber), 4)
                            self.result.insert(0, self.diff)
                            self.equation3 = "{} - {} = {}".format(float(self.firstNumber), float(self.secondNumber),
                                                                   self.diff)
                            print("Equation3 = ", self.equation3)
                            self.nbrlist.clear()

                        if self.equalclicks == 4:
                            self.diff = round(float(self.firstNumber) - float(self.secondNumber), 4)
                            self.result.insert(0, self.diff)
                            self.equation4 = "{} - {} = {}".format(float(self.firstNumber), float(self.secondNumber),
                                                                   self.diff)
                            print("Equation4 = ", self.equation4)
                            self.nbrlist.clear()

                        if self.equalclicks == 5:
                            self.diff = round(float(self.firstNumber) - float(self.secondNumber), 4)
                            self.result.insert(0, self.diff)
                            self.equation5 = "{} - {} = {}".format(float(self.firstNumber), float(self.secondNumber),
                                                                   self.diff)
                            print("Equation5 = ", self.equation5)
                            self.nbrlist.clear()

                        if self.equalclicks == 6:
                            self.diff = round(float(self.firstNumber) - float(self.secondNumber), 4)
                            self.result.insert(0, self.diff)
                            self.equation6 = "{} - {} = {}".format(float(self.firstNumber), float(self.secondNumber),
                                                                   self.diff)
                            print("Equation6 = ", self.equation6)
                            self.nbrlist.clear()

                        if self.equalclicks == 7:
                            self.diff = round(float(self.firstNumber) - float(self.secondNumber), 4)
                            self.result.insert(0, self.diff)
                            self.equation7 = "{} - {} = {}".format(float(self.firstNumber), float(self.secondNumber),
                                                                   self.diff)
                            print("Equation7 = ", self.equation7)
                            self.nbrlist.clear()

                        if self.equalclicks == 8:
                            self.diff = round(float(self.firstNumber) - float(self.secondNumber), 4)
                            self.result.insert(0, self.diff)
                            self.equation8 = "{} - {} = {}".format(float(self.firstNumber), float(self.secondNumber),
                                                                   self.diff)
                            print("Equation8 = ", self.equation8)
                            self.nbrlist.clear()
                    else:
                        if self.equalclicks == 1:
                            self.diff = int(self.firstNumber) - int(self.secondNumber)
                            self.result.insert(0, self.diff)
                            self.equation1 = "{} - {} = {}".format(int(self.firstNumber), int(self.secondNumber), self.diff)
                            print("Equation1 = ", self.equation1)
                            self.nbrlist.clear()

                        if self.equalclicks == 2:
                            self.diff = int(self.firstNumber) - int(self.secondNumber)
                            self.result.insert(0, self.diff)
                            self.equation2 = "{} - {} = {}".format(int(self.firstNumber), int(self.secondNumber), self.diff)
                            print("Equation2 = ", self.equation2)
                            self.nbrlist.clear()

                        if self.equalclicks == 3:
                            self.diff = int(self.firstNumber) - int(self.secondNumber)
                            self.result.insert(0, self.diff)
                            self.equation3 = "{} - {} = {}".format(int(self.firstNumber), int(self.secondNumber), self.diff)
                            print("Equation3 = ", self.equation3)
                            self.nbrlist.clear()

                        if self.equalclicks == 4:
                            self.diff = int(self.firstNumber) - int(self.secondNumber)
                            self.result.insert(0, self.diff)
                            self.equation4 = "{} - {} = {}".format(int(self.firstNumber), int(self.secondNumber), self.diff)
                            print("Equation4 = ", self.equation4)
                            self.nbrlist.clear()

                        if self.equalclicks == 5:
                            self.diff = int(self.firstNumber) - int(self.secondNumber)
                            self.result.insert(0, self.diff)
                            self.equation5 = "{} - {} = {}".format(int(self.firstNumber), int(self.secondNumber), self.diff)
                            print("Equation5 = ", self.equation5)
                            self.nbrlist.clear()

                        if self.equalclicks == 6:
                            self.diff = int(self.firstNumber) - int(self.secondNumber)
                            self.result.insert(0, self.diff)
                            self.equation6 = "{} - {} = {}".format(int(self.firstNumber), int(self.secondNumber), self.diff)
                            print("Equation6 = ", self.equation6)
                            self.nbrlist.clear()

                        if self.equalclicks == 7:
                            self.diff = int(self.firstNumber) - int(self.secondNumber)
                            self.result.insert(0, self.diff)
                            self.equation7 = "{} - {} = {}".format(int(self.firstNumber), int(self.secondNumber), self.diff)
                            print("Equation7 = ", self.equation7)
                            self.nbrlist.clear()

                        if self.equalclicks == 8:
                            self.diff = int(self.firstNumber) - int(self.secondNumber)
                            self.result.insert(0, self.diff)
                            self.equation8 = "{} - {} = {}".format(int(self.firstNumber), int(self.secondNumber), self.diff)
                            print("Equation8 = ", self.equation8)
                            self.nbrlist.clear()


                if self.calculation == "Multiply":
                    if self.multiplyclicks > 1 and self.equalclicks == 1:
                        self.chainMult = True
                        getsecondnumberMult()

                        self.equation1 = ""
                        elementCount = 0
                        for nbr in self.nbrlist:
                            print("Next nbr in nbrlist is: ", nbr, end="")
                            print("\n")
                            elementCount += 1
                            if elementCount == len(self.nbrlist):
                                self.equation1 += "{} = {}".format(self.secondNumber, numpy.prod(self.nbrlist))
                            else:
                                self.equation1 += "{} * ".format(nbr)

                        print("self.equation1 = ", self.equation1)
                        self.nbrlist.clear()
                        self.multiplyclicks = 0

                    if self.multiplyclicks > 1 and self.equalclicks == 2:
                        self.chainMult = True
                        getsecondnumberMult()

                        self.equation2 = ""
                        elementCount = 0
                        for nbr in self.nbrlist:
                            print("Next nbr in nbrlist is: ", nbr, end="")
                            print("\n")
                            elementCount += 1
                            if elementCount == len(self.nbrlist):
                                self.equation2 += "{} = {}".format(self.secondNumber, numpy.prod(self.nbrlist))
                            else:
                                self.equation2 += "{} * ".format(nbr)

                        print("self.equation2 = ", self.equation2)
                        self.nbrlist.clear()
                        self.multiplyclicks = 0

                    if self.multiplyclicks > 1 and self.equalclicks == 3:
                        self.chainMult = True
                        getsecondnumberMult()

                        self.equation3 = ""
                        elementCount = 0
                        for nbr in self.nbrlist:
                            print("Next nbr in nbrlist is: ", nbr, end="")
                            print("\n")
                            elementCount += 1
                            if elementCount == len(self.nbrlist):
                                self.equation3 += "{} = {}".format(self.secondNumber, numpy.prod(self.nbrlist))
                            else:
                                self.equation3 += "{} * ".format(nbr)

                        print("self.equation3 = ", self.equation3)
                        self.nbrlist.clear()
                        self.multiplyclicks = 0

                    if self.multiplyclicks > 1 and self.equalclicks == 4:
                        self.chainMult = True
                        getsecondnumberMult()

                        self.equation4 = ""
                        elementCount = 0
                        for nbr in self.nbrlist:
                            print("Next nbr in nbrlist is: ", nbr, end="")
                            print("\n")
                            elementCount += 1
                            if elementCount == len(self.nbrlist):
                                self.equation4 += "{} = {}".format(self.secondNumber, numpy.prod(self.nbrlist))
                            else:
                                self.equation4 += "{} * ".format(nbr)

                        print("self.equation4 = ", self.equation4)
                        self.nbrlist.clear()
                        self.multiplyclicks = 0

                    if self.multiplyclicks > 1 and self.equalclicks == 5:
                        self.chainMult = True
                        getsecondnumberMult()

                        self.equation5 = ""
                        elementCount = 0
                        for nbr in self.nbrlist:
                            print("Next nbr in self.nbrlist is: ", nbr, end="")
                            print("\n")
                            elementCount += 1
                            if elementCount == len(self.nbrlist):
                                self.equation5 += "{} = {}".format(self.secondNumber, numpy.prod(self.nbrlist))
                            else:
                                self.equation5 += "{} * ".format(nbr)

                        print("self.equation5 = ", self.equation5)
                        self.multiplyclicks = 0
                        self.nbrlist.clear()

                    if self.multiplyclicks > 1 and self.equalclicks == 6:
                        self.chainMult = True
                        getsecondnumberMult()

                        self.equation6 = ""
                        elementCount = 0
                        for nbr in self.nbrlist:
                            print("Next nbr in nbrlist is: ", nbr, end="")
                            print("\n")
                            elementCount += 1
                            if elementCount == len(self.nbrlist):
                                self.equation6 += "{} = {}".format(self.secondNumber, numpy.prod(self.nbrlist))
                            else:
                                self.equation6 += "{} * ".format(nbr)

                            print("self.equation6 = ", self.equation6)
                            self.nbrlist.clear()
                            self.multiplyclicks = 0

                    if self.multiplyclicks > 1 and self.equalclicks == 7:
                        self.chainMult = True
                        getsecondnumberMult()

                        self.equation7 = ""
                        elementCount = 0
                        for nbr in self.nbrlist:
                            print("Next nbr in nbrlist is: ", nbr, end="")
                            print("\n")
                            elementCount += 1
                            if elementCount == len(self.nbrlist):
                                self.equation7 += "{} = {}".format(self.secondNumber, numpy.prod(self.nbrlist))
                            else:
                                self.equation7 += "{} * ".format(nbr)

                        print("self.equation7 = ", self.equation7)
                        self.nbrlist.clear()
                        self.multiplyclicks = 0

                    if self.multiplyclicks > 1 and self.equalclicks == 8:
                        self.chainMult = True
                        getsecondnumberMult()

                        self.equation8 = ""
                        elementCount = 0
                        for nbr in self.nbrlist:
                            print("Next nbr in nbrlist is: ", nbr, end="")
                            print("\n")
                            elementCount += 1
                            if elementCount == len(self.nbrlist):
                                self.equation8 += "{} = {}".format(self.secondNumber, numpy.prod(self.nbrlist))
                            else:
                                self.equation8 += "{} * ".format(nbr)

                        print("self.equation8 = ", self.equation8)
                        self.nbrlist.clear()
                        self.multiplyclicks = 0


                if "." in str(self.firstNumber) or str(self.secondNumber):
                    if self.equalclicks == 1 and self.multiplyclicks == 1:
                        self.mult = round(float(self.firstNumber) * float(self.secondNumber), 4)
                        self.result.insert(0, self.mult)
                        self.equation1 = "{} * {} = {}".format(self.firstNumber, self.secondNumber, self.mult)
                        print("Equation1 = ", self.equation1)
                        self.nbrlist.clear()
                        self.multiplyclicks = 0

                    if self.equalclicks == 2 and self.multiplyclicks == 1:
                        self.mult = round(float(self.firstNumber) * float(self.secondNumber), 4)
                        self.result.insert(0, self.mult)
                        self.equation2 = "{} * {} = {}".format(self.firstNumber, self.secondNumber, self.mult)
                        print("Equation2 = ", self.equation2)
                        self.nbrlist.clear()
                        self.multiplyclicks = 0

                    if self.equalclicks == 3 and self.multiplyclicks == 1:
                        self.mult = round(float(self.firstNumber) * float(self.secondNumber), 4)
                        self.result.insert(0, self.mult)
                        self.equation3 = "{} * {} = {}".format(self.firstNumber, self.secondNumber, self.mult)
                        print("Equation3 = ", self.equation3)
                        self.nbrlist.clear()
                        self.multiplyclicks = 0

                    if self.equalclicks == 4 and self.multiplyclicks == 1:
                        self.mult = round(float(self.firstNumber) * float(self.secondNumber), 4)
                        self.result.insert(0, self.mult)
                        self.equation4 = "{} * {} = {}".format(self.firstNumber, self.secondNumber, self.mult)
                        print("Equation4 = ", self.equation4)
                        self.nbrlist.clear()
                        self.multiplyclicks = 0

                    if self.equalclicks == 5 and self.multiplyclicks == 1:
                        self.mult = round(float(self.firstNumber) * float(self.secondNumber), 4)
                        self.result.insert(0, self.mult)
                        self.equation5 = "{} * {} = {}".format(self.firstNumber, self.secondNumber, self.mult)
                        print("Equation5 = ", self.equation5)
                        self.nbrlist.clear()
                        self.multiplyclicks = 0

                    if self.equalclicks == 6 and self.multiplyclicks == 1:
                        self.mult = round(float(self.firstNumber) * float(self.secondNumber), 4)
                        self.result.insert(0, self.mult)
                        self.equation6 = "{} * {} = {}".format(self.firstNumber, self.secondNumber, self.mult)
                        print("Equation6 = ", self.equation6)
                        self.nbrlist.clear()
                        self.multiplyclicks = 0

                    if self.equalclicks == 7 and self.multiplyclicks == 1:
                        self.mult = round(float(self.firstNumber) * float(self.secondNumber), 4)
                        self.result.insert(0, self.mult)
                        self.equation7 = "{} * {} = {}".format(self.firstNumber, self.secondNumber, self.mult)
                        print("Equation7 = ", self.equation7)
                        self.nbrlist.clear()
                        self.multiplyclicks = 0

                    if self.equalclicks == 8 and self.multiplyclicks == 1:
                        self.mult = round(float(self.firstNumber) * float(self.secondNumber), 4)
                        self.result.insert(0, self.mult)
                        self.equation8 = "{} * {} = {}".format(self.firstNumber, self.secondNumber, self.mult)
                        print("Equation8 = ", self.equation8)
                        self.nbrlist.clear()
                        self.multiplyclicks = 0

                else:
                    if self.multiplyclicks == 1 and self.equalclicks == 1:
                        #if chainAdd == False:
                            #if chainMult == False:
                                self.mult = self.firstNumber * int(self.secondNumber)
                                self.result.insert(0, self.mult)
                                self.equation1 = "{} * {} = {}".format(self.firstNumber, self.secondNumber, self.mult)
                                print("Equation1 = ", self.equation1)
                                self.nbrlist.clear()
                                self.multiplyclicks = 0

                    if self.multiplyclicks == 1 and self.equalclicks == 2:
                        #if chainAdd == False:
                            #if chainMult == False:
                                self.mult = self.firstNumber * int(self.secondNumber)
                                self.result.insert(0, self.mult)
                                self.equation2 = "{} * {} = {}".format(self.firstNumber, self.secondNumber, self.mult)
                                print("Equation2 = ", self.equation2)
                                self.nbrlist.clear()
                                self.multiplyclicks = 0

                    if self.multiplyclicks == 1 and self.equalclicks == 3:
                        #if chainAdd == False:
                            #if chainMult == False:
                                self.mult = self.firstNumber * int(self.secondNumber)
                                self.result.insert(0, self.mult)
                                self.equation3 = "{} * {} = {}".format(self.firstNumber, self.secondNumber, self.mult)
                                print("Equation3 = ", self.equation3)
                                self.nbrlist.clear()
                                self.multiplyclicks = 0

                    if self.multiplyclicks == 1 and self.equalclicks == 4:
                        #if chainAdd == False:
                            #if chainMult == False:
                                self.mult = self.firstNumber * int(self.secondNumber)
                                self.result.insert(0, self.mult)
                                self.equation4 = "{} * {} = {}".format(self.firstNumber, self.secondNumber, self.mult)
                                print("Equation4 = ", self.equation4)
                                self.nbrlist.clear()
                                self.multiplyclicks = 0

                    if self.multiplyclicks == 1 and self.equalclicks == 5:
                        #if chainAdd == False:
                            #if chainMult == False:
                                self.mult = self.firstNumber * int(self.secondNumber)
                                self.result.insert(0, self.mult)
                                self.equation5 = "{} * {} = {}".format(self.firstNumber, self.secondNumber, self.mult)
                                print("Equation5 = ", self.equation5)
                                self.nbrlist.clear()
                                self.multiplyclicks = 0

                    if self.multiplyclicks == 1 and self.equalclicks == 6:
                        #if chainAdd == False:
                            #if chainMult == False:
                                self.mult = self.firstNumber * int(self.secondNumber)
                                self.result.insert(0, self.mult)
                                self.equation6 = "{} * {} = {}".format(self.firstNumber, self.secondNumber, self.mult)
                                print("Equation6 = ", self.equation6)
                                self.nbrlist.clear()
                                self.multiplyclicks = 0

                    if self.multiplyclicks == 1 and self.equalclicks == 7:
                        #if chainAdd == False:
                            #if chainMult == False:
                                self.mult = self.firstNumber * int(self.secondNumber)
                                self.result.insert(0, self.mult)
                                self.equation7 = "{} * {} = {}".format(self.firstNumber, self.secondNumber, self.mult)
                                print("Equation7 = ", self.equation7)
                                self.nbrlist.clear()
                                self.multiplyclicks = 0

                    if self.multiplyclicks == 1 and self.equalclicks == 8:
                        #if chainAdd == False:
                            #if chainMult == False:
                                self.mult = self.firstNumber * int(self.secondNumber)
                                self.result.insert(0, self.mult)
                                self.equation8 = "{} * {} = {}".format(self.firstNumber, self.secondNumber, self.mult)
                                print("Equation8 = ", self.equation8)
                                self.nbrlist.clear()
                                self.multiplyclicks = 0

                if self.calculation == "Divide":
                    try:
                        if "." in str(self.firstNumber) or str(self.secondNumber):
                            if self.equalclicks == 1:
                                self.divide = round(self.firstNumber / float(self.secondNumber), 4)
                                self.result.insert(0, self.divide)
                                self.equation1 = "{} / {} = {}".format(self.firstNumber, self.secondNumber, self.divide)
                                print("Equation1 = ", self.equation1)
                                self.nbrlist.clear()

                            if self.equalclicks == 2:
                                self.divide = round(self.firstNumber / float(self.secondNumber), 4)
                                self.result.insert(0, self.divide)
                                self.equation2 = "{} / {} = {}".format(self.firstNumber, self.secondNumber, self.divide)
                                print("Equation2 = ", self.equation2)
                                self.nbrlist.clear()

                            if self.equalclicks == 3:
                                self.divide = round(self.firstNumber / float(self.secondNumber), 4)
                                self.result.insert(0, self.divide)
                                self.equation3 = "{} / {} = {}".format(self.firstNumber, self.secondNumber, self.divide)
                                print("Equation3 = ", self.equation3)
                                self.nbrlist.clear()

                            if self.equalclicks == 4:
                                self.divide = round(self.firstNumber / float(self.secondNumber), 4)
                                self.result.insert(0, self.divide)
                                self.equation4 = "{} / {} = {}".format(self.firstNumber, self.secondNumber, self.divide)
                                print("Equation4 = ", self.equation4)
                                self.nbrlist.clear()

                            if self.equalclicks == 5:
                                self.divide = round(self.firstNumber / float(self.secondNumber), 4)
                                self.result.insert(0, self.divide)
                                self.equation5 = "{} / {} = {}".format(self.firstNumber, self.secondNumber, self.divide)
                                print("Equation5 = ", self.equation5)
                                self.nbrlist.clear()

                            if self.equalclicks == 6:
                                self.divide = round(self.firstNumber / float(self.secondNumber), 4)
                                self.result.insert(0, self.divide)
                                self.equation6 = "{} / {} = {}".format(self.firstNumber, self.secondNumber, self.divide)
                                print("Equation6 = ", self.equation6)
                                self.nbrlist.clear()

                            if self.equalclicks == 7:
                                self.divide = round(self.firstNumber / float(self.secondNumber), 4)
                                self.result.insert(0, self.divide)
                                self.equation7 = "{} / {} = {}".format(self.firstNumber, self.secondNumber, self.divide)
                                print("Equation7 = ", self.equation7)
                                self.nbrlist.clear()

                            if self.equalclicks == 8:
                                self.divide = round(self.firstNumber / float(self.secondNumber), 4)
                                self.result.insert(0, self.divide)
                                self.equation8 = "{} / {} = {}".format(self.firstNumber, self.secondNumber, self.divide)
                                print("Equation8 = ", self.equation8)
                                self.nbrlist.clear()

                        else:
                            if self.equalclicks == 1:
                                self.divide = round(self.firstNumber / int(self.secondNumber), 4)
                                self.result.insert(0, self.divide)
                                self.equation1 = "{} / {} = {}".format(self.firstNumber, self.secondNumber, self.divide)
                                print("Equation1 = ", self.equation1)
                                self.nbrlist.clear()

                            if self.equalclicks == 2:
                                self.divide = round(self.firstNumber / int(self.secondNumber), 4)
                                self.result.insert(0, self.divide)
                                self.equation2 = "{} / {} = {}".format(self.firstNumber, self.secondNumber, self.divide)
                                print("Equation2 = ", self.equation2)
                                self.nbrlist.clear()

                            if self.equalclicks == 3:
                                self.divide = round(self.firstNumber / int(self.secondNumber), 4)
                                self.result.insert(0, self.divide)
                                self.equation3 = "{} / {} = {}".format(self.firstNumber, self.secondNumber, self.divide)
                                print("Equation3 = ", self.equation3)
                                self.nbrlist.clear()

                            if self.equalclicks == 4:
                                self.divide = round(self.firstNumber / int(self.secondNumber), 4)
                                self.result.insert(0, self.divide)
                                self.equation4 = "{} / {} = {}".format(self.firstNumber, self.secondNumber, self.divide)
                                print("Equation4 = ", self.equation4)
                                self.nbrlist.clear()

                            if self.equalclicks == 5:
                                self.divide = round(self.firstNumber / int(self.secondNumber), 4)
                                self.result.insert(0, self.divide)
                                self.equation5 = "{} / {} = {}".format(self.firstNumber, self.secondNumber, self.divide)
                                print("Equation5 = ", self.equation5)
                                self.nbrlist.clear()

                            if self.equalclicks == 6:
                                self.divide = round(self.firstNumber / int(self.secondNumber), 4)
                                self.result.insert(0, self.divide)
                                self.equation6 = "{} / {} = {}".format(self.firstNumber, self.secondNumber, self.divide)
                                print("Equation6 = ", self.equation6)
                                self.nbrlist.clear()

                            if self.equalclicks == 7:
                                self.divide = round(self.firstNumber / int(self.secondNumber), 4)
                                self.result.insert(0, self.divide)
                                self.equation7 = "{} / {} = {}".format(self.firstNumber, self.secondNumber, self.divide)
                                print("Equation7 = ", self.equation7)
                                self.nbrlist.clear()

                            if self.equalclicks == 8:
                                self.divide = round(self.firstNumber / int(self.secondNumber), 4)
                                self.result.insert(0, self.divide)
                                self.equation8 = "{} / {} = {}".format(self.firstNumber, self.secondNumber, self.divide)
                                print("Equation8 = ", self.equation8)
                                self.nbrlist.clear()

                    except ZeroDivisionError:
                        messagebox.showinfo("Division by 0 error!", "Error:  You can't divide by zero!")
                        self.equalclicks -= 1
                        self.historyclicks -= 1

                if self.calculation == "Percent":
                    self.percentage = round((self.firstNumber * 0.01) * float(self.secondNumber), 4)
                    if "." in str(self.firstNumber) or str(self.secondNumber):
                        if self.equalclicks == 1:
                            self.result.insert(0, self.percentage)
                            self.equation1 = "{} % of {} = {}".format(self.firstNumber, self.secondNumber, self.percentage)
                            print("Equation1 = ", self.equation1)
                            self.nbrlist.clear()

                        if self.equalclicks == 2:
                            self.result.insert(0, self.percentage)
                            self.equation2 = "{} % of {} = {}".format(self.firstNumber, self.secondNumber, self.percentage)
                            print("Equation2 = ", self.equation2)
                            self.nbrlist.clear()

                        if self.equalclicks == 3:
                            self.result.insert(0, self.percentage)
                            self.equation3 = "{} % of {} = {}".format(self.firstNumber, self.secondNumber, self.percentage)
                            print("Equation3 = ", self.equation3)
                            self.nbrlist.clear()

                        if self.equalclicks == 4:
                            self.result.insert(0, self.percentage)
                            self.equation4 = "{} % of {} = {}".format(self.firstNumber, self.secondNumber, self.percentage)
                            print("Equation4 = ", self.equation4)
                            self.nbrlist.clear()

                        if self.equalclicks == 5:
                            self.result.insert(0, self.percentage)
                            self.equation5 = "{} % of {} = {}".format(self.firstNumber, self.secondNumber, self.percentage)
                            print("Equation5 = ", self.equation5)
                            self.nbrlist.clear()

                        if self.equalclicks == 6:
                            self.result.insert(0, self.percentage)
                            self.equation6 = "{} % of {} = {}".format(self.firstNumber, self.secondNumber, self.percentage)
                            print("Equation6 = ", self.equation6)
                            self.nbrlist.clear()

                        if self.equalclicks == 7:
                            self.result.insert(0, self.percentage)
                            self.equation7 = "{} % of {} = {}".format(self.firstNumber, self.secondNumber, self.percentage)
                            print("Equation7 = ", self.equation7)
                            self.nbrlist.clear()

                        if self.equalclicks == 8:
                            self.result.insert(0, self.percentage)
                            self.equation8 = "{} % of {} = {}".format(self.firstNumber, self.secondNumber, self.percentage)
                            print("Equation8 = ", self.equation8)
                            self.nbrlist.clear()
                    else:
                        if self.equalclicks == 1:
                            self.result.insert(0, self.percentage)
                            self.equation1 = "{} % of {} = {}".format(self.firstNumber, self.secondNumber, self.percentage)
                            print("Equation1 = ", self.equation1)
                            self.nbrlist.clear()

                        if self.equalclicks == 2:
                            self.result.insert(0, self.percentage)
                            self.equation2 = "{} % of {} = {}".format(self.firstNumber, self.secondNumber, self.percentage)
                            print("Equation2 = ", self.equation2)
                            self.nbrlist.clear()

                        if self.equalclicks == 3:
                            self.result.insert(0, self.percentage)
                            self.equation3 = "{} % of {} = {}".format(self.firstNumber, self.secondNumber, self.percentage)
                            print("Equation3 = ", self.equation3)
                            self.nbrlist.clear()

                        if self.equalclicks == 4:
                            self.result.insert(0, self.percentage)
                            self.equation4 = "{} % of {} = {}".format(self.firstNumber, self.secondNumber, self.percentage)
                            print("Equation4 = ", self.equation4)
                            self.nbrlist.clear()

                        if self.equalclicks == 5:
                            self.result.insert(0, self.percentage)
                            self.equation5 = "{} % of {} = {}".format(self.firstNumber, self.secondNumber, self.percentage)
                            print("Equation5 = ", self.equation5)
                            self.nbrlist.clear()

                        if self.equalclicks == 6:
                            self.result.insert(0, self.percentage)
                            self.equation6 = "{} % of {} = {}".format(self.firstNumber, self.secondNumber, self.percentage)
                            print("Equation6 = ", self.equation6)
                            self.nbrlist.clear()

                        if self.equalclicks == 7:
                            self.result.insert(0, self.percentage)
                            self.equation7 = "{} % of {} = {}".format(self.firstNumber, self.secondNumber, self.percentage)
                            print("Equation7 = ", self.equation7)
                            self.nbrlist.clear()

                        if self.equalclicks == 8:
                            self.result.insert(0, self.percentage)
                            self.equation8 = "{} % of {} = {}".format(self.firstNumber, self.secondNumber, self.percentage)
                            print("Equation8 = ", self.equation8)
                            self.nbrlist.clear()

                if self.calculation == "Modulo":
                    try:
                        if "." in str(self.firstNumber) or str(self.secondNumber):
                            self.mod = round(self.firstNumber % float(self.secondNumber), 4)
                            if self.equalclicks == 1:
                                self.result.insert(0, self.mod)
                                self.equation1 = "{} % {} = {}".format(self.firstNumber, self.secondNumber, self.mod)
                                print("Equation1 = ", self.equation1)
                                self.nbrlist.clear()

                            if self.equalclicks == 2:
                                self.result.insert(0, self.mod)
                                self.equation2 = "{} % {} = {}".format(self.firstNumber, self.secondNumber, self.mod)
                                print("Equation2 = ", self.equation2)
                                self.nbrlist.clear()

                            if self.equalclicks == 3:
                                self.result.insert(0, self.mod)
                                self.equation3 = "{} % {} = {}".format(self.firstNumber, self.secondNumber, self.mod)
                                print("Equation3 = ", self.equation3)
                                self.nbrlist.clear()

                            if self.equalclicks == 4:
                                self.result.insert(0, self.mod)
                                self.equation4 = "{} % {} = {}".format(self.firstNumber, self.secondNumber, self.mod)
                                print("Equation4 = ", self.equation4)
                                self.nbrlist.clear()

                            if self.equalclicks == 5:
                                self.result.insert(0, self.mod)
                                self.equation5 = "{} % {} = {}".format(self.firstNumber, self.secondNumber, self.mod)
                                print("Equation5 = ", self.equation5)
                                self.nbrlist.clear()

                            if self.equalclicks == 6:
                                self.result.insert(0, self.mod)
                                self.equation6 = "{} % {} = {}".format(self.firstNumber, self.secondNumber, self.mod)
                                print("Equation6 = ", self.equation6)
                                self.nbrlist.clear()

                            if self.equalclicks == 7:
                                self.result.insert(0, self.mod)
                                self.equation7 = "{} % {} = {}".format(self.firstNumber, self.secondNumber, self.mod)
                                print("Equation7 = ", self.equation7)
                                self.nbrlist.clear()

                            if self.equalclicks == 8:
                                self.result.insert(0, self.mod)
                                self.equation8 = "{} % {} = {}".format(self.firstNumber, self.secondNumber, self.mod)
                                print("Equation8 = ", self.equation8)
                                self.nbrlist.clear()

                        else:
                            self.mod = round(self.firstNumber % int(self.secondNumber), 4)
                            if self.equalclicks == 1:
                                self.result.insert(0, self.mod)
                                self.equation1 = "{} % {} = {}".format(self.firstNumber, self.secondNumber, self.mod)
                                print("Equation1 = ", self.equation1)
                                self.nbrlist.clear()

                            if self.equalclicks == 2:
                                self.result.insert(0, self.mod)
                                self.equation2 = "{} % {} = {}".format(self.firstNumber, self.secondNumber, self.mod)
                                print("Equation2 = ", self.equation2)
                                self.nbrlist.clear()

                            if self.equalclicks == 3:
                                self.result.insert(0, self.mod)
                                self.equation3 = "{} % {} = {}".format(self.firstNumber, self.secondNumber, self.mod)
                                print("Equation3 = ", self.equation3)
                                self.nbrlist.clear()

                            if self.equalclicks == 4:
                                self.result.insert(0, self.mod)
                                self.equation4 = "{} % {} = {}".format(self.firstNumber, self.secondNumber, self.mod)
                                print("Equation4 = ", self.equation4)
                                self.nbrlist.clear()

                            if self.equalclicks == 5:
                                self.result.insert(0, self.mod)
                                self.equation5 = "{} % {} = {}".format(self.firstNumber, self.secondNumber, self.mod)
                                print("Equation5 = ", self.equation5)
                                self.nbrlist.clear()

                            if self.equalclicks == 6:
                                self.result.insert(0, self.mod)
                                self.equation6 = "{} % {} = {}".format(self.firstNumber, self.secondNumber, self.mod)
                                print("Equation6 = ", self.equation6)
                                self.nbrlist.clear()

                            if self.equalclicks == 7:
                                self.result.insert(0, self.mod)
                                self.equation7 = "{} % {} = {}".format(self.firstNumber, self.secondNumber, self.mod)
                                print("Equation7 = ", self.equation7)
                                self.nbrlist.clear()

                            if self.equalclicks == 8:
                                self.result.insert(0, self.mod)
                                self.equation8 = "{} % {} = {}".format(self.firstNumber, self.secondNumber, self.mod)
                                print("Equation8 = ", self.equation8)
                                self.nbrlist.clear()

                    except ZeroDivisionError:
                        messagebox.showinfo("Division by 0 error!", "You can't divide by zero!")
                        self.equalclicks -= 1
                        self.historyclicks -= 1

                if self.calculation == "SquareRootOfx":
                    if self.equalclicks == 1:
                        self.squareRootOfx = round(math.sqrt(self.firstNumber), 4)
                        self.result.delete(0, END)
                        self.result.insert(0, self.squareRootOfx)
                        self.equation1 = "√{} = {}".format(self.firstNumber, self.squareRootOfx)
                        print("Equation1 = ", self.equation1)

                    if self.equalclicks == 2:
                        self.squareRootOfx = round(math.sqrt(self.firstNumber), 4)
                        self.result.delete(0, END)
                        self.result.insert(0, self.squareRootOfx)
                        self.equation2 = "√{} = {}".format(self.firstNumber, self.squareRootOfx)
                        print("Equation2 = ", self.equation2)

                    if self.equalclicks == 3:
                        self.squareRootOfx = round(math.sqrt(self.firstNumber), 4)
                        self.result.delete(0, END)
                        self.result.insert(0, self.squareRootOfx)
                        self.equation3 = "√{} = {}".format(self.firstNumber, self.squareRootOfx)
                        print("Equation3 = ", self.equation3)

                    if self.equalclicks == 4:
                        self.squareRootOfx = round(math.sqrt(self.firstNumber), 4)
                        self.result.delete(0, END)
                        self.result.insert(0, self.squareRootOfx)
                        self.equation4 = "√{} = {}".format(self.firstNumber, self.squareRootOfx)
                        print("Equation4 = ", self.equation4)

                    if self.equalclicks == 5:
                        self.squareRootOfx = round(math.sqrt(self.firstNumber), 4)
                        self.result.delete(0, END)
                        self.result.insert(0, self.squareRootOfx)
                        self.equation5 = "√{} = {}".format(self.firstNumber, self.squareRootOfx)
                        print("Equation5 = ", self.equation5)

                    if self.equalclicks == 6:
                        self.squareRootOfx = round(math.sqrt(self.firstNumber), 4)
                        self.result.delete(0, END)
                        self.result.insert(0, self.squareRootOfx)
                        self.equation6 = "√{} = {}".format(self.firstNumber, self.squareRootOfx)
                        print("Equation6 = ", self.equation6)

                    if self.equalclicks == 7:
                        self.squareRootOfx = round(math.sqrt(self.firstNumber), 4)
                        self.result.delete(0, END)
                        self.result.insert(0, self.squareRootOfx)
                        self.equation7 = "√{} = {}".format(self.firstNumber, self.squareRootOfx)
                        print("Equation7 = ", self.equation7)

                    if self.equalclicks == 8:
                        self.squareRootOfx = round(math.sqrt(self.firstNumber), 4)
                        self.result.delete(0, END)
                        self.result.insert(0, self.squareRootOfx)
                        self.equation8 = "√{} = {}".format(self.firstNumber, self.squareRootOfx)
                        print("Equation8 = ", self.equation8)

                if self.calculation == "PowerOf2":
                    if self.equalclicks == 1:
                        self.powerOf2 = round(self.firstNumber ** 2, 4)
                        self.result.delete(0, END)
                        self.result.insert(0, self.powerOf2)
                        self.equation1 = "{}² = {}".format(self.firstNumber, self.powerOf2)
                        print("Equation1 = ", self.equation1)

                    if self.equalclicks == 2:
                        self.powerOf2 = round(self.firstNumber ** 2, 4)
                        self.result.delete(0, END)
                        self.result.insert(0, self.powerOf2)
                        self.equation2 = "{}² = {}".format(self.firstNumber, self.powerOf2)
                        print("Equation2 = ", self.equation2)

                    if self.equalclicks == 3:
                        self.powerOf2 = round(self.firstNumber ** 2, 4)
                        self.result.delete(0, END)
                        self.result.insert(0, self.powerOf2)
                        self.equation3 = "{}² = {}".format(self.firstNumber, self.powerOf2)
                        print("Equation3 = ", self.equation3)

                    if self.equalclicks == 4:
                        self.powerOf2 = round(self.firstNumber ** 2, 4)
                        self.result.delete(0, END)
                        self.result.insert(0, self.powerOf2)
                        self.equation4 = "{}² = {}".format(self.firstNumber, self.powerOf2)
                        print("Equation4 = ", self.equation4)

                    if self.equalclicks == 5:
                        self.powerOf2 = round(self.firstNumber ** 2, 4)
                        self.result.delete(0, END)
                        self.result.insert(0, self.powerOf2)
                        self.equation5 = "{}² = {}".format(self.firstNumber, self.powerOf2)
                        print("Equation5 = ", self.equation5)

                    if self.equalclicks == 6:
                        self.powerOf2 = round(self.firstNumber ** 2, 4)
                        self.result.delete(0, END)
                        self.result.insert(0, self.powerOf2)
                        self.equation6 = "{}² = {}".format(self.firstNumber, self.powerOf2)
                        print("Equation6 = ", self.equation6)

                    if self.equalclicks == 7:
                        self.powerOf2 = round(self.firstNumber ** 2, 4)
                        self.result.delete(0, END)
                        self.result.insert(0, self.powerOf2)
                        self.equation7 = "{}² = {}".format(self.firstNumber, self.powerOf2)
                        print("Equation7 = ", self.equation7)

                    if self.equalclicks == 8:
                        self.powerOf2 = round(self.firstNumber ** 2, 4)
                        self.result.delete(0, END)
                        self.result.insert(0, self.powerOf2)
                        self.equation8 = "{}² = {}".format(self.firstNumber, self.powerOf2)
                        print("Equation8 = ", self.equation8)


                if self.calculation == "OneOverx":
                    try:
                        if "." in str(self.firstNumber):
                            if self.equalclicks == 1:
                                self.oneoverx = 1 / float(self.firstNumber)
                                self.result.insert(0, self.oneoverx)
                                self.equation1 = "1 / {} = {}".format(self.firstNumber, self.oneoverx)
                                print("Equation1 = ", self.equation1)

                            if self.equalclicks == 2:
                                self.oneoverx = 1 / float(self.firstNumber)
                                self.result.insert(0, self.oneoverx)
                                self.equation2 = "1 / {} = {}".format(self.firstNumber, self.oneoverx)
                                print("Equation2 = ", self.equation2)

                            if self.equalclicks == 3:
                                self.oneoverx = 1 / float(self.firstNumber)
                                self.result.insert(0, self.oneoverx)
                                self.equation3 = "1 / {} = {}".format(self.firstNumber, self.oneoverx)
                                print("Equation3 = ", self.equation3)

                            if self.equalclicks == 4:
                                self.oneoverx = 1 / float(self.firstNumber)
                                self.result.insert(0, self.oneoverx)
                                self.equation4 = "1 / {} = {}".format(self.firstNumber, self.oneoverx)
                                print("Equation4 = ", self.equation4)

                            if self.equalclicks == 5:
                                self.oneoverx = 1 / float(self.firstNumber)
                                self.result.insert(0, self.oneoverx)
                                self.equation5 = "1 / {} = {}".format(self.firstNumber, self.oneoverx)
                                print("Equation5 = ", self.equation5)

                            if self.equalclicks == 6:
                                self.oneoverx = 1 / float(self.firstNumber)
                                self.result.insert(0, self.oneoverx)
                                self.equation6 = "1 / {} = {}".format(self.firstNumber, self.oneoverx)
                                print("Equation6 = ", self.equation6)

                            if self.equalclicks == 7:
                                self.oneoverx = 1 / float(self.firstNumber)
                                self.result.insert(0, self.oneoverx)
                                self.equation7 = "1 / {} = {}".format(self.firstNumber, self.oneoverx)
                                print("Equation7 = ", self.equation7)

                            if self.equalclicks == 8:
                                self.oneoverx = 1 / float(self.firstNumber)
                                self.result.insert(0, self.oneoverx)
                                self.equation8 = "1 / {} = {}".format(self.firstNumber, self.oneoverx)
                                print("Equation8 = ", self.equation8)
                        else:
                            if self.equalclicks == 1:
                                self.oneoverx = 1 / int(self.firstNumber)
                                self.result.insert(0, self.oneoverx)
                                self.equation1 = "1 / {} = {}".format(self.firstNumber, self.oneoverx)
                                print("Equation1 = ", self.equation1)

                            if self.equalclicks == 2:
                                self.oneoverx = 1 / int(self.firstNumber)
                                self.result.insert(0, self.oneoverx)
                                self.equation2 = "1 / {} = {}".format(self.firstNumber, self.oneoverx)
                                print("Equation2 = ", self.equation2)

                            if self.equalclicks == 3:
                                self.oneoverx = 1 / int(self.firstNumber)
                                self.result.insert(0, self.oneoverx)
                                self.equation3 = "1 / {} = {}".format(self.firstNumber, self.oneoverx)
                                print("Equation3 = ", self.equation3)

                            if self.equalclicks == 4:
                                self.oneoverx = 1 / int(self.firstNumber)
                                self.result.insert(0, self.oneoverx)
                                self.equation4 = "1 / {} = {}".format(self.firstNumber, self.oneoverx)
                                print("Equation4 = ", self.equation4)

                            if self.equalclicks == 5:
                                self.oneoverx = 1 / int(self.firstNumber)
                                self.result.insert(0, self.oneoverx)
                                self.equation5 = "1 / {} = {}".format(self.firstNumber, self.oneoverx)
                                print("Equation5 = ", self.equation5)

                            if self.equalclicks == 6:
                                self.oneoverx = 1 / int(self.firstNumber)
                                self.result.insert(0, self.oneoverx)
                                self.equation6 = "1 / {} = {}".format(self.firstNumber, self.oneoverx)
                                print("Equation6 = ", self.equation6)

                            if self.equalclicks == 7:
                                self.oneoverx = 1 / int(self.firstNumber)
                                self.result.insert(0, self.oneoverx)
                                self.equation7 = "1 / {} = {}".format(self.firstNumber, self.oneoverx)
                                print("Equation7 = ", self.equation7)

                            if self.equalclicks == 8:
                                self.oneoverx = 1 / int(self.firstNumber)
                                self.result.insert(0, self.oneoverx)
                                self.equation8 = "1 / {} = {}".format(self.firstNumber, self.oneoverx)
                                print("Equation8 = ", self.equation8)

                    except ZeroDivisionError:
                        messagebox.showinfo("Division by 0 error!", "You can't divide by zero!")
                        self.historyclicks -= 1
                        self.equalclicks -= 1
                        if self.historyclicks > self.equalclicks:
                            messagebox.showinfo("Error!", "You haven't made any new calculations yet")

            except AttributeError:
                messagebox.showinfo("Error", "You haven't made any calculations yet")

        def MPlus():
            self.memory = self.result.get()
            self.result.delete(0, END)


        def MR():
            try:
                self.result.insert(0, self.memory)
                if self.firstNumber != 0:
                    self.memory = self.secondNumber
                else:
                    self.memory = self.firstNumber
            except AttributeError:
                messagebox.showinfo("Error", "You have nothing in memory yet.")

        def MC():
            self.memory = 0
            self.result.delete(0, END)
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

        self.decimalclicks = 0

        def decimal():
            self.result.insert(len(self.result.get()), ".")
            self.decimalclicks += 1
            if self.decimalclicks >= 2:
                messagebox.showinfo("Error", "A number can have only 1 decimal in it!")
                self.result.delete(0, END)
                self.decimalclicks = 0


        frame1 = Frame(root, bg="#80c1ff", bd=5)
        frame1.place(relx=.1, rely=.1, relwidth=0.70, relheight=0.80)

        buttonMC = Button(frame1, text="MC", height=3, width=5, command=MC)
        buttonMC.grid(row=3, column=0)
        buttonMC.configure(width=7, height=3)

        MRButton = Button(frame1, text="MR", height=3, width=5, command=MR)
        MRButton.grid(row=3, column=1)
        MRButton.configure(width=7, height=3)

        MPlusButton = Button(frame1, text="M+", height=3, width=5, command=MPlus)
        MPlusButton.grid(row=3, column=2)
        MPlusButton.configure(width=7, height=3)

        percentButton = Button(frame1, text="%", height=3, width=5, command=percent)
        percentButton.grid(row=3, column=3)
        percentButton.configure(width=7, height=3)

        buttonModulo = Button(frame1, text="Mod", height=3, width=5, command=modulo)
        buttonModulo.grid(row=4, column=0)
        buttonModulo.configure(width=7, height=3)

        buttonSqRoot = Button(frame1, text="√(x)", height=3, width=5, command=squareRootOfx)
        buttonSqRoot.grid(row=4, column=1)
        buttonSqRoot.configure(width=7, height=3)

        button2ndPower = Button(frame1, text="x²", height=3, width=5, command=powerOf2)
        button2ndPower.grid(row=4, column=2)
        button2ndPower.configure(width=7, height=3)

        buttonOneOverX = Button(frame1, text="1/x", height=3, width=5, command=oneOverX)
        buttonOneOverX.grid(row=4, column=3)
        buttonOneOverX.configure(width=7, height=3)

        buttonCE = Button(frame1, text="CE", height=3, width=5, command=clearEntry)
        buttonCE.grid(row=5, column=0)
        buttonCE.configure(width=7, height=3)

        buttonClear = Button(frame1, text="C", height=3, width=5, command=clear)
        buttonClear.grid(row=5, column=1)
        buttonClear.configure(width=7, height=3)

        buttonDelete = Button(frame1, text="del", height=3, width=5, command=delete)
        buttonDelete.grid(row=5, column=2)
        buttonDelete.configure(width=7, height=3)

        buttonDivide = Button(frame1, text="/", height=3, width=5, command=divide)
        buttonDivide.grid(row=5, column=3)
        buttonDivide.configure(width=7, height=3)

        button7 = Button(frame1, text="7", height=3, width=5, command=lambda: buttonClick(7))
        button7.grid(row=6, column=0)
        button7.configure(width=7, height=3)

        button8 = Button(frame1, text="8", height=3, width=5, command=lambda: buttonClick(8))
        button8.grid(row=6, column=1)
        button8.configure(width=7, height=3)

        button9 = Button(frame1, text="9", height=3, width=5, command=lambda: buttonClick(9))
        button9.grid(row=6, column=2)
        button9.configure(width=7, height=3)

        buttonMultiply = Button(frame1, text="x", height=3, width=5, command=multiply)
        buttonMultiply.grid(row=6, column=3)
        buttonMultiply.configure(width=7, height=3)
        # if len(self.nbrlist) == 0:
        #     buttonMultiply.configure(state=DISABLED)
        # elif len(self.nbrlist) >= 1:
        #     buttonMultiply.configure(state=ACTIVE)

        button4 = Button(frame1, text="4", height=3, width=5, command=lambda: buttonClick(4))
        button4.grid(row=7, column=0)
        button4.configure(width=7, height=3)

        button5 = Button(frame1, text="5", height=3, width=5, command=lambda: buttonClick(5))
        button5.grid(row=7, column=1)
        button5.configure(width=7, height=3)

        button6 = Button(frame1, text="6", height=3, width=5, command=lambda: buttonClick(6))
        button6.grid(row=7, column=2)
        button6.configure(width=7, height=3)

        buttonMinus = Button(frame1, text="-", height=3, width=5, command=subtract)
        buttonMinus.grid(row=7, column=3)
        buttonMinus.configure(width=7, height=3)

        button1 = Button(frame1, text="1", height=3, width=5, command=lambda: buttonClick(1))
        button1.grid(row=8, column=0)
        button1.configure(width=7, height=3)

        button2 = Button(frame1, text="2", height=3, width=5, command=lambda: buttonClick(2))
        button2.grid(row=8, column=1)
        button2.configure(width=7, height=3)

        button3 = Button(frame1, text="3", height=3, width=5, command=lambda: buttonClick(3))
        button3.grid(row=8, column=2)
        button3.configure(width=7, height=3)

        buttonAdd = Button(frame1, text="+", height=3, width=5, command=add)
        buttonAdd.grid(row=8, column=3)
        buttonAdd.configure(width=7, height=3)

        buttonPlusMinus = Button(frame1, text="+/-", height=3, width=5, command=plusMinus)
        buttonPlusMinus.grid(row=9, column=0)
        buttonPlusMinus.configure(width=7, height=3)

        buttonZero = Button(frame1, text="0", height=3, width=5, command=lambda: buttonClick(0))
        buttonZero.grid(row=9, column=1)
        buttonZero.configure(width=7, height=3)

        buttonDecimal = Button(frame1, text=".", height=3, width=5, command=decimal)
        buttonDecimal.grid(row=9, column=2)
        buttonDecimal.configure(width=7, height=3)

        buttonEquals = Button(frame1, text="=", height=3, width=5, command=equals)
        buttonEquals.grid(row=9, column=3)
        buttonEquals.configure(width=7, height=3)

        # root.grid_columnconfigure(0, weight=1)
        # root.grid_rowconfigure(0, weight=1)
        #
        # frame1.grid_columnconfigure(0, weight=1)
        # frame1.grid_columnconfigure(1, weight=1)
        # frame1.grid_rowconfigure(0, weight=1)
        # frame1.grid_rowconfigure(1, weight=1)
        # frame1.grid_rowconfigure(2, weight=1)
        # frame1.grid_rowconfigure(3, weight=1)
        # frame1.grid_rowconfigure(4, weight=1)
        # frame1.grid_rowconfigure(5, weight=1)
        # frame1.grid_rowconfigure(6, weight=1)

        frame2 = Frame(root, bg="lightgrey", bd=5)
        frame2.place(relx=.5, rely=.1, relwidth=0.45, relheight=0.80)

        # frame2.grid_columnconfigure(0, weight=1)
        # frame2.grid_rowconfigure(0, weight=1)
        # frame2.grid_rowconfigure(1, weight=1)
        # frame2.grid_rowconfigure(2, weight=1)
        # frame2.grid_rowconfigure(3, weight=1)
        # frame2.grid_rowconfigure(4, weight=1)
        # frame2.grid_rowconfigure(5, weight=1)
        # frame2.grid_rowconfigure(6, weight=1)
        # frame2.grid_rowconfigure(7, weight=1)
        # frame2.grid_rowconfigure(8, weight=1)
        # frame2.grid_rowconfigure(9, weight=1)

        self.labellist = []

        def history():
            self.historyclicks += 1
            if self.historyclicks == 1 and self.equalclicks == 0:
                messagebox.showinfo("Error", "You haven't used the calculator yet!")

            if self.historyclicks > self.equalclicks:
                    messagebox.showinfo("Error", "History items requested exceeds number of equations calculated!")
                    self.historyclicks = self.equalclicks

            if self.historyclicks >= 1 and self.equalclicks >= 1:
                if self.chainAdd == True:
                    self.Label1 = Label(frame2, text=self.equation1,
                                        bg="#80c1ff", fg="navy", anchor="w")
                    self.Label1.place(x=5, y=85)
                    self.labellist.append(self.Label1)

                if self.chainMult == True:
                    self.Label1 = Label(frame2, text=self.equation1,
                                        bg="#80c1ff", fg="navy", anchor="w")
                    self.Label1.place(x=5, y=85)
                    self.labellist.append(self.Label1)

                else:
                    self.Label1 = Label(frame2, text=self.equation1, bg="#80c1ff", fg="navy", anchor="w")
                    self.Label1.place(x=5, y=85)
                    self.labellist.append(self.Label1)

            if self.historyclicks >= 2 and self.historyclicks <= self.equalclicks:
                if self.chainAdd == True:
                    self.Label2 = Label(frame2, text=self.equation2,
                                        bg="#80c1ff", fg="navy", anchor="w")
                    self.Label2.place(x=5, y=125)
                    self.labellist.append(self.Label2)

                if self.chainMult == True:
                    self.Label2 = Label(frame2, text=self.equation2,
                                        bg="#80c1ff", fg="navy", anchor="w")
                    self.Label2.place(x=5, y=125)
                    self.labellist.append(self.Label2)

                else:
                    self.Label2 = Label(frame2, text=self.equation2, bg="#80c1ff", fg="navy", anchor="w")
                    self.Label2.place(x=5, y=125)
                    self.labellist.append(self.Label2)

            if self.historyclicks >= 3 and self.historyclicks <= self.equalclicks:
                if self.chainAdd == True:
                    self.Label3 = Label(frame2, text=self.equation3,
                                        bg="#80c1ff", fg="navy", anchor="w")
                    self.Label3.place(x=5, y=165)
                    self.labellist.append(self.Label3)

                if self.chainMult == True:
                    self.Label3 = Label(frame2, text=self.equation3,
                                        bg="#80c1ff", fg="navy", anchor="w")
                    self.Label3.place(x=5, y=165)
                    self.labellist.append(self.Label3)

                else:
                    self.Label3 = Label(frame2, text=self.equation3, bg="#80c1ff", fg="navy", anchor="w")
                    self.Label3.place(x=5, y=165)
                    self.labellist.append(self.Label3)

            if self.historyclicks >= 4 and self.historyclicks <= self.equalclicks:
                if self.chainAdd == True:
                    self.Label4 = Label(frame2, text=self.equation4,
                                        bg="#80c1ff", fg="navy", anchor="w")
                    self.Label4.place(x=5, y=205)
                    self.labellist.append(self.Label4)

                if self.chainMult == True:
                    self.Label4 = Label(frame2, text=self.equation4,
                                        bg="#80c1ff", fg="navy", anchor="w")
                    self.Label4.place(x=5, y=205)
                    self.labellist.append(self.Label4)

                else:
                    self.Label4 = Label(frame2, text=self.equation4, bg="#80c1ff", fg="navy", anchor="w")
                    self.Label4.place(x=5, y=205)
                    self.labellist.append(self.Label4)

            if self.historyclicks >= 5 and self.historyclicks <= self.equalclicks:
                if self.chainAdd == True:
                    self.Label5 = Label(frame2, text=self.equation5,
                                        bg="#80c1ff", fg="navy", anchor="w")
                    self.Label5.place(x=5, y=245)
                    self.labellist.append(self.Label5)

                if self.chainMult == True:
                    self.Label5 = Label(frame2, text=self.equation5,
                                        bg="#80c1ff", fg="navy", anchor="w")
                    self.Label5.place(x=5, y=245)
                    self.labellist.append(self.Label5)

                else:
                    self.Label5 = Label(frame2, text=self.equation5, bg="#80c1ff", fg="navy", anchor="w")
                    self.Label5.place(x=5, y=245)
                    self.labellist.append(self.Label5)


            if self.historyclicks >= 6 and self.historyclicks <= self.equalclicks:
                if self.chainAdd == True:
                    self.Label6 = Label(frame2, text=self.equation6,
                                        bg="#80c1ff", fg="navy", anchor="w")
                    self.Label6.place(x=5, y=285)
                    self.labellist.append(self.Label6)

                if self.chainMult == True:
                    self.Label6 = Label(frame2, text=self.equation6,
                                        bg="#80c1ff", fg="navy", anchor="w")
                    self.Label6.place(x=5, y=285)
                    self.labellist.append(self.Label6)

                else:
                    self.Label6 = Label(frame2, text=self.equation6, bg="#80c1ff", fg="navy", anchor="w")
                    self.Label6.place(x=5, y=285)
                    self.labellist.append(self.Label6)

            if self.historyclicks >= 7 and self.historyclicks <= self.equalclicks:
                if self.chainAdd == True:
                    self.Label7 = Label(frame2, text=self.equation7,
                                        bg="#80c1ff", fg="navy", anchor="w")
                    self.Label7.place(x=5, y=325)
                    self.labellist.append(self.Label7)

                if self.chainMult == True:
                    self.Label7 = Label(frame2, text=self.equation7,
                                        bg="#80c1ff", fg="navy", anchor="w")
                    self.Label7.place(x=5, y=325)
                    self.labellist.append(self.Label7)

                else:
                    self.Label7 = Label(frame2, text=self.equation7, bg="#80c1ff", fg="navy", anchor="w")
                    self.Label7.place(x=5, y=325)
                    self.labellist.append(self.Label7)

            if self.historyclicks == 8 and self.historyclicks <= self.equalclicks:
                if self.chainAdd == True:
                    self.Label8 = Label(frame2, text=self.equation8,
                                        bg="#80c1ff", fg="navy", width=25, anchor="w")
                    self.Label8.place(x=5, y=365)
                    self.labellist.append(self.Label8)

                if self.chainMult == True:
                    self.Label8 = Label(frame2, text=self.equation8,
                                        bg="#80c1ff", fg="navy", anchor="w")
                    self.Label8.place(x=5, y=365)
                    self.labellist.append(self.Label8)

                else:
                    self.Label8 = Label(frame2, text=self.equation8, bg="#80c1ff", fg="navy", anchor="w")
                    self.Label8.place(x=5, y=365)
                    self.labellist.append(self.Label8)

            if self.equalclicks > 8:
                if self.historyclicks > 8:
                    messagebox.showinfo("Error", "History = ONLY the last 8 equations")

        historyButton = Button(frame2, text="History", fg="Navy", bg="#80c1ff", command=history)
        historyButton.configure(font=("Verdana", 12))
        historyButton.place(x=5, y=40)

        self.memoryLabel = Label(frame2, text="", bg="#80c1ff", fg="navy", width=25, anchor="w")
        self.memoryLabel.place(x=5, y=85)

        def memory():
            self.memoryLabel = Label(frame2, text=self.memory, bg="#80c1ff", fg="navy", width=25, anchor="w")
            self.memoryLabel.place(x=5, y=85)
            self.labellist.append(self.memoryLabel)

        memoryButton = Button(frame2, text="Memory", bg="#80c1ff", fg="navy", command=memory)
        memoryButton.configure(font=("Verdana", 12))
        memoryButton.place(x=85, y=40)

        self.result = Entry(frame2, width=15, borderwidth=3)
        self.result.configure(font=("Verdana", 14))
        self.result.grid(row=0, column=0, pady=5)

        root.mainloop()

Calculator()

