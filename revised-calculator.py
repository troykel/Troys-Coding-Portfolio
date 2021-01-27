
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
        root.resizable(True, True)

        self.nbrlist = []
        self.labellist = []
        self.buttonclicks = 0
        self.equalclicks = 0
        self.plusclicks = 0
        self.multiplyclicks = 0
        self.minusclicks = 0
        self.percentclicks = 0
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
            if self.plusclicks == 0 and self.decimalclicks >= 2:
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
            except ValueError:
                messagebox.showinfo("Error", "You haven't clicked any number yet")


        def getsecondNumber():
            self.secondNumber = self.result.get()
            if "." in str(self.secondNumber):
                self.secondNumber = float(self.secondNumber)
            else:
                self.secondNumber = int(self.secondNumber)
            self.nbrlist.append(self.secondNumber)


        def memory():
            self.memoryLabel = Label(frame2, text=self.memory, bg="#80c1ff", fg="navy", width=25, anchor="w")
            self.memoryLabel.place(x=5, y=85)
            self.labellist.append(self.memoryLabel)

        def add():
            self.plusclicks += 1
            print("self.plusclicks =", self.plusclicks)
            self.calculation = "Add"
            getfirstNumber()
            print("self.firstNumber = ", self.firstNumber)
            self.result.delete(0, END)

        def subtract():
            self.minusclicks += 1
            print(f"self.minusclicks = {self.minusclicks}")
            self.calculation = "Subtract"
            getfirstNumber()
            print(f"self.firstNumber = {self.firstNumber}")
            self.result.delete(0, END)

        def multiply():
            self.multiplyclicks += 1
            print("self.multiplyclicks = ", self.multiplyclicks)
            self.calculation = "Multiply"
            getfirstNumber()
            print("self.firstNumber = ", self.firstNumber)
            self.result.delete(0, END)

        def divide():
            getfirstnumber()
            self.calculation = "Divide"
            self.result.delete(0, END)

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


        def equals():
            self.equalclicks += 1
            self.historyclicks += 1
            # self.minusclicks = 0
            # self.multiplyclicks = 0
            print("self.equalclicks = ", self.equalclicks)
            getsecondNumber()
            self.result.delete(0, END)
            print("self.secondNumber = ", self.secondNumber)
            if self.calculation == "Add":
                if self.plusclicks == 1:
                    def addnbrs(self):
                        """A self.equalclicks click means that a single equation has
                        completed, so when 1 click of self.equalclicks occurs, we're
                        on Equation1, when 2 clicks, Equation2, and so on."""
                        self.result.delete(0, END)
                        self.sum = (self.firstNumber + self.secondNumber)
                        self.result.insert(0, round(self.sum, 4))
                        self.eq = f"Equation{self.equalclicks} = {self.firstNumber} + {self.secondNumber} = " \
                                  f"{round(self.sum, 4)}"

                        print(self.eq)
                        if self.equalclicks <= 8:
                            history()
                        self.nbrlist.clear()

                    addnbrs(self)
                    self.plusclicks = 0

                if len(self.nbrlist) > 2:
                    self.chaineq = ""
                    self.result.insert(0, sum(self.nbrlist))
                    elementCount = 0
                    for nbr in self.nbrlist:
                        elementCount += 1
                        if elementCount == len(self.nbrlist):
                            self.chaineq += f"{nbr} = {sum(self.nbrlist)}"
                        else:
                            self.chaineq += f"{nbr} + "

                    print("\n", self.nbrlist)
                    if self.equalclicks <= 8:
                        history()
                    self.plusclicks = 0
                    self.nbrlist.clear()

                # if self.plusclicks > 1 and self.equalclicks == 2:
                #     self.chainAdd = True
                #     self.equation2 = ""
                #     elementCount = 0
                #     for nbr in self.nbrlist:
                #         elementCount += 1
                #         if elementCount == len(self.nbrlist):
                #             f"self.equation{self.equalclicks}" += "{self.secondNumber} = {sum(self.nbrlist)}"
                #         else:
                #             f"self.equation{self.equalclicks}" += "{nbr} + "
                #
                #     print("self.equation2 = ", self.equation2)
                #     self.nbrlist.clear()
                #     self.plusclicks = 0
                #
                #     if self.plusclicks > 1 and self.equalclicks == 3:
                #         self.chainAdd = True
                #         self.equation3 = ""
                #         elementCount = 0
                #         for nbr in self.nbrlist:
                #             elementCount += 1
                #             if elementCount == len(self.nbrlist):
                #                 self.equation3 += "{} = {}".format(self.secondNumber, sum(self.nbrlist))
                #             else:
                #                 self.equation3 += "{} + ".format(nbr)
                #
                #         print("self.equation3 = ", self.equation3)
                #         self.nbrlist.clear()
                #         self.plusclicks = 0
                #
                #     if self.plusclicks > 1 and self.equalclicks == 4:
                #         self.chainAdd is True
                #         self.equation4 = ""
                #         elementCount = 0
                #         for nbr in self.nbrlist:
                #             elementCount += 1
                #             if elementCount == len(self.nbrlist):
                #                 self.equation4 += "{} = {}".format(self.secondNumber, sum(self.nbrlist))
                #             else:
                #                 self.equation4 += "{} + ".format(nbr)
                #
                #         print("self.equation4 = ", self.equation4)
                #         self.nbrlist.clear()
                #         self.plusclicks = 0
                #
                #     if self.plusclicks > 1 and self.equalclicks == 5:
                #         self.chainAdd is True
                #         self.equation5 = ""
                #         elementCount = 0
                #         for nbr in self.nbrlist:
                #             elementCount += 1
                #             if elementCount == len(self.nbrlist):
                #                 self.equation5 += "{} = {}".format(self.secondNumber, sum(self.nbrlist))
                #             else:
                #                 self.equation5 += "{} + ".format(nbr)
                #
                #         print("self.equation5 = ", self.equation5)
                #         self.nbrlist.clear()
                #         self.plusclicks = 0
                #
                #     if self.plusclicks > 1 and self.equalclicks == 6:
                #         self.chainAdd is True
                #         self.equation6 = ""
                #         elementCount = 0
                #         for nbr in self.nbrlist:
                #             elementCount += 1
                #             if elementCount == len(self.nbrlist):
                #                 self.equation6 += "{} = {}".format(self.secondNumber, sum(self.nbrlist))
                #             else:
                #                 self.equation6 += "{} + ".format(nbr)
                #
                #         print("self.equation6 = ", self.equation6)
                #         self.nbrlist.clear()
                #         self.plusclicks = 0
                #
                #     if self.plusclicks > 1 and self.equalclicks == 7:
                #         self.chainAdd is True
                #         self.equation7 = ""
                #         elementCount = 0
                #         for nbr in self.nbrlist:
                #             elementCount += 1
                #             if elementCount == len(self.nbrlist):
                #                 self.equation7 += "{} = {}".format(self.secondNumber, sum(self.nbrlist))
                #             else:
                #                 self.equation7 += "{} + ".format(nbr)
                #
                #         print("self.equation7 = ", self.equation7)
                #         self.nbrlist.clear()
                #         self.plusclicks = 0
                #
                #     if self.plusclicks > 1 and self.equalclicks == 8:
                #         self.chainAdd is True
                #         self.equation8 = ""
                #         elementCount = 0
                #         for nbr in self.nbrlist:
                #             elementCount += 1
                #             if elementCount == len(self.nbrlist):
                #                 self.equation8 += "{} = {}".format(self.secondNumber, sum(self.nbrlist))
                #             else:
                #                 self.equation8 += "{} + ".format(nbr)
                #
                #         print("self.equation8 = ", self.equation8)
                #         self.nbrlist.clear()
                #         self.plusclicks = 0




                        # if self.equalclicks == 1 and self.plusclicks == 1:
                        #     self.result.delete(0, END)


                        #     self.result.insert(0, round(self.firstNumber + self.secondNumber, 4))
                        #     self.sum = round(float(self.firstNumber) + float(self.secondNumber), 4)
                        #     self.equation1 = "{} + {} = {}".format(self.firstNumber, self.secondNumber, self.sum)
                        #     print("Equation1 = ", self.equation1)
                        #     self.nbrlist.clear()

                        # if self.equalclicks == 2 and self.plusclicks == 1:
                        #     self.result.insert(0, round(float(self.firstNumber) + float(self.secondNumber), 4))
                        #     self.sum = float(self.firstNumber)
                        #     self.sum = round(float(self.firstNumber) + float(self.secondNumber), 4)
                        #     self.equation2 = "{} + {} = {}".format(self.firstNumber, self.secondNumber, self.sum)
                        #     print("Equation2 = ", self.equation2)
                        #     self.nbrlist.clear()

                        # if self.equalclicks == 3 and self.plusclicks == 1:
                        #     self.result.insert(0, round(float(self.firstNumber) + float(self.secondNumber), 4))
                        #     self.sum = float(self.firstNumber)
                        #     self.sum = round(float(self.firstNumber) + float(self.secondNumber), 4)
                        #     self.equation3 = "{} + {} = {}".format(self.firstNumber, self.secondNumber, self.sum)
                        #     print("Equation3 = ", self.equation3)
                        #     self.nbrlist.clear()

                        # if self.equalclicks == 4 and self.plusclicks == 1:
                        #     self.result.insert(0, round(float(self.firstNumber) + float(self.secondNumber), 4))
                        #     self.sum = float(self.firstNumber)
                        #     self.sum = round(float(self.firstNumber) + float(self.secondNumber), 4)
                        #     self.equation4 = "{} + {} = {}".format(self.firstNumber, self.secondNumber, self.sum)
                        #     print("Equation4 = ", self.equation4)
                        #     self.nbrlist.clear()

                        # if self.equalclicks == 5 and self.plusclicks == 1:
                        #     self.result.insert(0, round(float(self.firstNumber) + float(self.secondNumber), 4))
                        #     self.sum = float(self.firstNumber)
                        #     self.sum = round(float(self.firstNumber) + float(self.secondNumber), 4)
                        #     self.equation5 = "{} + {} = {}".format(self.firstNumber, self.secondNumber, self.sum)
                        #     print("Equation5 = ", self.equation5)
                        #     self.nbrlist.clear()

                        # if self.equalclicks == 6 and self.plusclicks == 1:
                        #     self.result.insert(0, round(float(self.firstNumber) + float(self.secondNumber), 4))
                        #     self.sum = float(self.firstNumber)
                        #     self.sum = round(float(self.firstNumber) + float(self.secondNumber), 4)
                        #     self.equation6 = "{} + {} = {}".format(self.firstNumber, self.secondNumber, self.sum)
                        #     print("Equation6 = ", self.equation6)
                        #     self.nbrlist.clear()

                        # if self.equalclicks == 7 and self.plusclicks == 1:
                        #     self.result.insert(0, round(float(self.firstNumber) + float(self.secondNumber), 4))
                        #     self.sum = float(self.firstNumber)
                        #     self.sum = round(float(self.firstNumber) + float(self.secondNumber), 4)
                        #     self.equation7 = "{} + {} = {}".format(self.firstNumber, self.secondNumber, self.sum)
                        #     print("Equation7 = ", self.equation7)
                        #     self.nbrlist.clear()
                        #
                        # if self.equalclicks == 8 and self.plusclicks == 1:
                        #     self.result.insert(0, round(float(self.firstNumber) + float(self.secondNumber), 4))
                        #     self.sum = float(self.firstNumber)
                        #     self.sum = round(float(self.firstNumber) + float(self.secondNumber), 4)
                        #     self.equation8 = "{} + {} = {}".format(self.firstNumber, self.secondNumber, self.sum)
                        #     print("Equation8 = ", self.equation8)
                        #     self.nbrlist.clear()

                #if isinstance(self.firstNumber, int) or isinstance(self.secondNumber, int):

                        # if self.plusclicks == 1 and self.equalclicks == 1:
                        #     self.result.delete(0, END)
                        #     self.result.insert(0, int(self.firstNumber) + int(self.secondNumber))
                        #     self.sum = self.firstNumber + int(self.secondNumber)
                        #     self.equation1 = "{} + {} = {}".format(self.firstNumber, self.secondNumber, self.sum)
                        #     print("Equation1 = ", self.equation1)
                        #     self.nbrlist.clear()

                        # def addints(self, self.plusclicks, self.equalclicks):
                        #     self.plusclicks = self.plusclicks
                        #     self.equalclicks = self.equalclicks
                        #     self.result.delete(0, END)
                        #     self.sum = self.firstNumber + self.secondNumber
                        #     self.result.insert(0, self.sum)
                        #     print(f"self.equation({self.plusclicks}) = {self.firstNumber} + {self.secondNumber} = {self.sum}")
                        #     print(f"Equation {self.plusclicks} = self.equation({self.plusclicks})")
                        #     self.nbrlist.clear()
                        #
                        # addints(self, self.plusclicks, self.equalclicks)

                        # if self.plusclicks == 2 and self.equalclicks == 1:
                        #     self.sum = self.firstNumber + int(self.secondNumber)
                        #     self.equation2 = "{} + {} = {}".format(self.firstNumber, self.secondNumber, self.sum)
                        #     print("Equation2 = ", self.equation2)
                        #     self.nbrlist.clear()
                        #
                        # if self.equalclicks == 3 and self.plusclicks == 1:
                        #     self.sum = self.firstNumber
                        #     self.sum = self.firstNumber + int(self.secondNumber)
                        #     self.equation3 = "{} + {} = {}".format(self.firstNumber, self.secondNumber, self.sum)
                        #     print("Equation3 = ", self.equation3)
                        #     self.nbrlist.clear()
                        #
                        # if self.equalclicks == 4 and self.plusclicks == 1:
                        #     self.sum = self.firstNumber
                        #     self.sum = self.firstNumber + int(self.secondNumber)
                        #     self.equation4 = "{} + {} = {}".format(self.firstNumber, self.secondNumber, self.sum)
                        #     print("Equation4 = ", self.equation4)
                        #     self.nbrlist.clear()
                        #
                        # if self.equalclicks == 5 and self.plusclicks == 1:
                        #     self.sum = self.firstNumber
                        #     self.sum = self.firstNumber + int(self.secondNumber)
                        #     self.equation5 = "{} + {} = {}".format(self.firstNumber, self.secondNumber, self.sum)
                        #     print("Equation5 = ", self.equation5)
                        #     self.nbrlist.clear()
                        #
                        # if self.equalclicks == 6 and self.plusclicks == 1:
                        #     self.sum = self.firstNumber
                        #     self.sum = self.firstNumber + int(self.secondNumber)
                        #     self.equation6 = "{} + {} = {}".format(self.firstNumber, self.secondNumber, self.sum)
                        #     print("Equation6 = ", self.equation6)
                        #     self.nbrlist.clear()
                        #
                        # if self.equalclicks == 7 and self.plusclicks == 1:
                        #     self.sum = self.firstNumber
                        #     self.sum = self.firstNumber + int(self.secondNumber)
                        #     self.equation7 = "{} + {} = {}".format(self.firstNumber, self.secondNumber, self.sum)
                        #     print("Equation7 = ", self.equation7)
                        #     self.nbrlist.clear()
                        #
                        # if self.equalclicks == 8 and self.plusclicks == 1:
                        #     self.sum = self.firstNumber
                        #     self.sum = self.firstNumber + int(self.secondNumber)
                        #     self.equation8 = "{} + {} = {}".format(self.firstNumber, self.secondNumber, self.sum)
                        #     print("Equation8 = ", self.equation8)
                        #     self.nbrlist.clear()

            if self.calculation == "Multiply":
                if self.multiplyclicks == 1:
                    def multiplyNbrs():
                        self.result.delete(0, END)
                        self.mult = self.firstNumber * self.secondNumber
                        print(f"self.mult = {self.mult}")
                        self.result.insert(0, self.mult)
                        self.eq = f"Equation{self.equalclicks} = {self.firstNumber} * {self.secondNumber} = " \
                                  f"{self.mult}"
                        print(self.eq)

                    multiplyNbrs()
                    if self.equalclicks <= 8:
                        history()
                    self.nbrlist.clear()
                    self.multiplyclicks = 0

                if len(self.nbrlist) >= 2:
                    if self.multiplyclicks >= 2:
                        self.chainMulteq = ""
                        self.result.insert(0, numpy.prod(self.nbrlist))
                        elementCount = 0
                        for nbr in self.nbrlist:
                            elementCount += 1
                            if elementCount == len(self.nbrlist):
                                self.chainMulteq += f"{nbr} = {numpy.prod(self.nbrlist)}"
                            else:
                                self.chainMulteq += f"{nbr} * "

                        print("\n", self.nbrlist)
                        if self.equalclicks <= 8:
                            history()
                        self.nbrlist.clear()
                        self.multiplyclicks = 0

                    # if self.multiplyclicks > 1 and self.equalclicks == 2:
                    #     self.chainMult = True
                    #     getsecondnumberMult()
                    #
                    #     self.equation2 = ""
                    #     elementCount = 0
                    #     for nbr in self.nbrlist:
                    #         print("Next nbr in nbrlist is: ", nbr, end="")
                    #         print("\n")
                    #         elementCount += 1
                    #         if elementCount == len(self.nbrlist):
                    #             self.equation2 += "{} = {}".format(self.secondNumber, numpy.prod(self.nbrlist))
                    #         else:
                    #             self.equation2 += "{} * ".format(nbr)
                    #
                    #     print("self.equation2 = ", self.equation2)
                    #     self.nbrlist.clear()
                    #     self.multiplyclicks = 0
                    #
                    # if self.multiplyclicks > 1 and self.equalclicks == 3:
                    #     self.chainMult = True
                    #     getsecondnumberMult()
                    #
                    #     self.equation3 = ""
                    #     elementCount = 0
                    #     for nbr in self.nbrlist:
                    #         print("Next nbr in nbrlist is: ", nbr, end="")
                    #         print("\n")
                    #         elementCount += 1
                    #         if elementCount == len(self.nbrlist):
                    #             self.equation3 += "{} = {}".format(self.secondNumber, numpy.prod(self.nbrlist))
                    #         else:
                    #             self.equation3 += "{} * ".format(nbr)
                    #
                    #     print("self.equation3 = ", self.equation3)
                    #     self.nbrlist.clear()
                    #     self.multiplyclicks = 0
                    #
                    # if self.multiplyclicks > 1 and self.equalclicks == 4:
                    #     self.chainMult = True
                    #     getsecondnumberMult()
                    #
                    #     self.equation4 = ""
                    #     elementCount = 0
                    #     for nbr in self.nbrlist:
                    #         print("Next nbr in nbrlist is: ", nbr, end="")
                    #         print("\n")
                    #         elementCount += 1
                    #         if elementCount == len(self.nbrlist):
                    #             self.equation4 += "{} = {}".format(self.secondNumber, numpy.prod(self.nbrlist))
                    #         else:
                    #             self.equation4 += "{} * ".format(nbr)
                    #
                    #     print("self.equation4 = ", self.equation4)
                    #     self.nbrlist.clear()
                    #     self.multiplyclicks = 0
                    #
                    # if self.multiplyclicks > 1 and self.equalclicks == 5:
                    #     self.chainMult = True
                    #     getsecondnumberMult()
                    #
                    #     self.equation5 = ""
                    #     elementCount = 0
                    #     for nbr in self.nbrlist:
                    #         print("Next nbr in self.nbrlist is: ", nbr, end="")
                    #         print("\n")
                    #         elementCount += 1
                    #         if elementCount == len(self.nbrlist):
                    #             self.equation5 += "{} = {}".format(self.secondNumber, numpy.prod(self.nbrlist))
                    #         else:
                    #             self.equation5 += "{} * ".format(nbr)
                    #
                    #     print("self.equation5 = ", self.equation5)
                    #     self.multiplyclicks = 0
                    #     self.nbrlist.clear()
                    #
                    # if self.multiplyclicks > 1 and self.equalclicks == 6:
                    #     self.chainMult = True
                    #     getsecondnumberMult()
                    #
                    #     self.equation6 = ""
                    #     elementCount = 0
                    #     for nbr in self.nbrlist:
                    #         print("Next nbr in nbrlist is: ", nbr, end="")
                    #         print("\n")
                    #         elementCount += 1
                    #         if elementCount == len(self.nbrlist):
                    #             self.equation6 += "{} = {}".format(self.secondNumber, numpy.prod(self.nbrlist))
                    #         else:
                    #             self.equation6 += "{} * ".format(nbr)
                    #
                    #         print("self.equation6 = ", self.equation6)
                    #         self.nbrlist.clear()
                    #         self.multiplyclicks = 0
                    #
                    # if self.multiplyclicks > 1 and self.equalclicks == 7:
                    #     self.chainMult = True
                    #     getsecondnumberMult()
                    #
                    #     self.equation7 = ""
                    #     elementCount = 0
                    #     for nbr in self.nbrlist:
                    #         print("Next nbr in nbrlist is: ", nbr, end="")
                    #         print("\n")
                    #         elementCount += 1
                    #         if elementCount == len(self.nbrlist):
                    #             self.equation7 += "{} = {}".format(self.secondNumber, numpy.prod(self.nbrlist))
                    #         else:
                    #             self.equation7 += "{} * ".format(nbr)
                    #
                    #     print("self.equation7 = ", self.equation7)
                    #     self.nbrlist.clear()
                    #     self.multiplyclicks = 0
                    #
                    # if self.multiplyclicks > 1 and self.equalclicks == 8:
                    #     self.chainMult = True
                    #     getsecondnumberMult()
                    #
                    #     self.equation8 = ""
                    #     elementCount = 0
                    #     for nbr in self.nbrlist:
                    #         print("Next nbr in nbrlist is: ", nbr, end="")
                    #         print("\n")
                    #         elementCount += 1
                    #         if elementCount == len(self.nbrlist):
                    #             self.equation8 += "{} = {}".format(self.secondNumber, numpy.prod(self.nbrlist))
                    #         else:
                    #             self.equation8 += "{} * ".format(nbr)
                    #
                    #     print("self.equation8 = ", self.equation8)
                    #     self.nbrlist.clear()
                    #     self.multiplyclicks = 0



                    # if self.equalclicks == 1 and self.multiplyclicks == 1:
                    #     self.mult = round(float(self.firstNumber) * float(self.secondNumber), 4)
                    #     self.result.insert(0, self.mult)
                    #     self.equation1 = "{} * {} = {}".format(self.firstNumber, self.secondNumber, self.mult)
                    #     print("Equation1 = ", self.equation1)
                    #     self.nbrlist.clear()
                    #     self.multiplyclicks = 0
                    #
                    # if self.equalclicks == 2 and self.multiplyclicks == 1:
                    #     self.mult = round(float(self.firstNumber) * float(self.secondNumber), 4)
                    #     self.result.insert(0, self.mult)
                    #     self.equation2 = "{} * {} = {}".format(self.firstNumber, self.secondNumber, self.mult)
                    #     print("Equation2 = ", self.equation2)
                    #     self.nbrlist.clear()
                    #     self.multiplyclicks = 0
                    #
                    # if self.equalclicks == 3 and self.multiplyclicks == 1:
                    #     self.mult = round(float(self.firstNumber) * float(self.secondNumber), 4)
                    #     self.result.insert(0, self.mult)
                    #     self.equation3 = "{} * {} = {}".format(self.firstNumber, self.secondNumber, self.mult)
                    #     print("Equation3 = ", self.equation3)
                    #     self.nbrlist.clear()
                    #     self.multiplyclicks = 0
                    #
                    # if self.equalclicks == 4 and self.multiplyclicks == 1:
                    #     self.mult = round(float(self.firstNumber) * float(self.secondNumber), 4)
                    #     self.result.insert(0, self.mult)
                    #     self.equation4 = "{} * {} = {}".format(self.firstNumber, self.secondNumber, self.mult)
                    #     print("Equation4 = ", self.equation4)
                    #     self.nbrlist.clear()
                    #     self.multiplyclicks = 0
                    #
                    # if self.equalclicks == 5 and self.multiplyclicks == 1:
                    #     self.mult = round(float(self.firstNumber) * float(self.secondNumber), 4)
                    #     self.result.insert(0, self.mult)
                    #     self.equation5 = "{} * {} = {}".format(self.firstNumber, self.secondNumber, self.mult)
                    #     print("Equation5 = ", self.equation5)
                    #     self.nbrlist.clear()
                    #     self.multiplyclicks = 0
                    #
                    # if self.equalclicks == 6 and self.multiplyclicks == 1:
                    #     self.mult = round(float(self.firstNumber) * float(self.secondNumber), 4)
                    #     self.result.insert(0, self.mult)
                    #     self.equation6 = "{} * {} = {}".format(self.firstNumber, self.secondNumber, self.mult)
                    #     print("Equation6 = ", self.equation6)
                    #     self.nbrlist.clear()
                    #     self.multiplyclicks = 0
                    #
                    # if self.equalclicks == 7 and self.multiplyclicks == 1:
                    #     self.mult = round(float(self.firstNumber) * float(self.secondNumber), 4)
                    #     self.result.insert(0, self.mult)
                    #     self.equation7 = "{} * {} = {}".format(self.firstNumber, self.secondNumber, self.mult)
                    #     print("Equation7 = ", self.equation7)
                    #     self.nbrlist.clear()
                    #     self.multiplyclicks = 0
                    #
                    # if self.equalclicks == 8 and self.multiplyclicks == 1:
                    #     self.mult = round(float(self.firstNumber) * float(self.secondNumber), 4)
                    #     self.result.insert(0, self.mult)
                    #     self.equation8 = "{} * {} = {}".format(self.firstNumber, self.secondNumber, self.mult)
                    #     print("Equation8 = ", self.equation8)
                    #     self.nbrlist.clear()
                    #     self.multiplyclicks = 0

                #else:
                    # if self.multiplyclicks == 1 and self.equalclicks == 1:
                    #     #if self.chainAdd == False:
                    #         #if self.chainMult == False:
                    #             self.mult = self.firstNumber * int(self.secondNumber)
                    #             self.result.insert(0, self.mult)
                    #             self.equation1 = "{} * {} = {}".format(self.firstNumber, self.secondNumber, self.mult)
                    #             print("Equation1 = ", self.equation1)
                    #             self.nbrlist.clear()
                    #             self.multiplyclicks = 0

                    # if self.multiplyclicks == 1 and self.equalclicks == 2:
                    #     #if self.chainAdd == False:
                    #         #if self.chainMult == False:
                    #             self.mult = self.firstNumber * int(self.secondNumber)
                    #             self.result.insert(0, self.mult)
                    #             self.equation2 = "{} * {} = {}".format(self.firstNumber, self.secondNumber, self.mult)
                    #             print("Equation2 = ", self.equation2)
                    #             self.nbrlist.clear()
                    #             self.multiplyclicks = 0

                    # if self.multiplyclicks == 1 and self.equalclicks == 3:
                    #     #if self.chainAdd == False:
                    #         #if self.chainMult == False:
                    #             self.mult = self.firstNumber * int(self.secondNumber)
                    #             self.result.insert(0, self.mult)
                    #             self.equation3 = "{} * {} = {}".format(self.firstNumber, self.secondNumber, self.mult)
                    #             print("Equation3 = ", self.equation3)
                    #             self.nbrlist.clear()
                    #             self.multiplyclicks = 0

                    # if self.multiplyclicks == 1 and self.equalclicks == 4:
                    #     #if self.chainAdd == False:
                    #         #if self.chainMult == False:
                    #             self.mult = self.firstNumber * int(self.secondNumber)
                    #             self.result.insert(0, self.mult)
                    #             self.equation4 = "{} * {} = {}".format(self.firstNumber, self.secondNumber, self.mult)
                    #             print("Equation4 = ", self.equation4)
                    #             self.nbrlist.clear()
                    #             self.multiplyclicks = 0
                    #
                    # if self.multiplyclicks == 1 and self.equalclicks == 5:
                    #     #if self.chainAdd == False:
                    #         #if self.chainMult == False:
                    #             self.mult = self.firstNumber * int(self.secondNumber)
                    #             self.result.insert(0, self.mult)
                    #             self.equation5 = "{} * {} = {}".format(self.firstNumber, self.secondNumber, self.mult)
                    #             print("Equation5 = ", self.equation5)
                    #             self.nbrlist.clear()
                    #             self.multiplyclicks = 0
                    #
                    # if self.multiplyclicks == 1 and self.equalclicks == 6:
                    #     #if self.chainAdd == False:
                    #         #if self.chainMult == False:
                    #             self.mult = self.firstNumber * int(self.secondNumber)
                    #             self.result.insert(0, self.mult)
                    #             self.equation6 = "{} * {} = {}".format(self.firstNumber, self.secondNumber, self.mult)
                    #             print("Equation6 = ", self.equation6)
                    #             self.nbrlist.clear()
                    #             self.multiplyclicks = 0
                    #
                    # if self.multiplyclicks == 1 and self.equalclicks == 7:
                    #     #if self.chainAdd == False:
                    #         #if self.chainMult == False:
                    #             self.mult = self.firstNumber * int(self.secondNumber)
                    #             self.result.insert(0, self.mult)
                    #             self.equation7 = "{} * {} = {}".format(self.firstNumber, self.secondNumber, self.mult)
                    #             print("Equation7 = ", self.equation7)
                    #             self.nbrlist.clear()
                    #             self.multiplyclicks = 0
                    #
                    # if self.multiplyclicks == 1 and self.equalclicks == 8:
                    #     #if self.chainAdd == False:
                    #         #if self.chainMult == False:
                    #             self.mult = self.firstNumber * int(self.secondNumber)
                    #             self.result.insert(0, self.mult)
                    #             self.equation8 = "{} * {} = {}".format(self.firstNumber, self.secondNumber, self.mult)
                    #             print("Equation8 = ", self.equation8)
                    #             self.nbrlist.clear()
                    #             self.multiplyclicks = 0

            if self.calculation == "Subtract":
                if self.minusclicks == 1:
                    def subtractNbrs():
                        self.diff = round(self.firstNumber - self.secondNumber, 4)
                        self.result.insert(0, self.diff)
                        self.minuseq = f"Equation{self.equalclicks} = {self.firstNumber} - {self.secondNumber} = {self.diff}"
                        print(self.minuseq)
                        self.nbrlist.clear()
                        self.minusclicks = 0

                    subtractNbrs()
                    history()

                if self.minusclicks >= 2:
                    self.chainSubtracteq = ""
                    elementCount = 0
                    self.finaldiff = self.nbrlist[0]
                    for nbr in self.nbrlist[1:]:
                        self.finaldiff -= nbr
                    for nbr in self.nbrlist:
                        elementCount += 1
                        if elementCount == len(self.nbrlist):
                            self.chainSubtracteq += f"{nbr} = {self.finaldiff}"
                        else:
                            self.chainSubtracteq += f"{nbr} - "
                    self.result.insert(0, self.finaldiff)
                    print("\n", self.nbrlist)
                    print(self.chainSubtracteq)
                    if self.equalclicks <= 8:
                        history()
                    self.nbrlist.clear()
                    self.minusclicks = 0


                    #     if self.equalclicks == 2:
                    #         self.diff = round(float(self.firstNumber) - float(self.secondNumber), 4)
                    #         self.result.insert(0, self.diff)
                    #         self.equation2 = "{} - {} = {}".format(float(self.firstNumber), float(self.secondNumber),
                    #                                                self.diff)
                    #         print("Equation2 = ", self.equation2)
                    #         self.nbrlist.clear()
                    #
                    #     if self.equalclicks == 3:
                    #         self.diff = round(float(self.firstNumber) - float(self.secondNumber), 4)
                    #         self.result.insert(0, self.diff)
                    #         self.equation3 = "{} - {} = {}".format(float(self.firstNumber), float(self.secondNumber),
                    #                                                self.diff)
                    #         print("Equation3 = ", self.equation3)
                    #         self.nbrlist.clear()
                    #
                    #     if self.equalclicks == 4:
                    #         self.diff = round(float(self.firstNumber) - float(self.secondNumber), 4)
                    #         self.result.insert(0, self.diff)
                    #         self.equation4 = "{} - {} = {}".format(float(self.firstNumber), float(self.secondNumber),
                    #                                                self.diff)
                    #         print("Equation4 = ", self.equation4)
                    #         self.nbrlist.clear()
                    #
                    #     if self.equalclicks == 5:
                    #         self.diff = round(float(self.firstNumber) - float(self.secondNumber), 4)
                    #         self.result.insert(0, self.diff)
                    #         self.equation5 = "{} - {} = {}".format(float(self.firstNumber), float(self.secondNumber),
                    #                                                self.diff)
                    #         print("Equation5 = ", self.equation5)
                    #         self.nbrlist.clear()
                    #
                    #     if self.equalclicks == 6:
                    #         self.diff = round(float(self.firstNumber) - float(self.secondNumber), 4)
                    #         self.result.insert(0, self.diff)
                    #         self.equation6 = "{} - {} = {}".format(float(self.firstNumber), float(self.secondNumber),
                    #                                                self.diff)
                    #         print("Equation6 = ", self.equation6)
                    #         self.nbrlist.clear()
                    #
                    #     if self.equalclicks == 7:
                    #         self.diff = round(float(self.firstNumber) - float(self.secondNumber), 4)
                    #         self.result.insert(0, self.diff)
                    #         self.equation7 = "{} - {} = {}".format(float(self.firstNumber), float(self.secondNumber),
                    #                                                self.diff)
                    #         print("Equation7 = ", self.equation7)
                    #         self.nbrlist.clear()
                    #
                    #     if self.equalclicks == 8:
                    #         self.diff = round(float(self.firstNumber) - float(self.secondNumber), 4)
                    #         self.result.insert(0, self.diff)
                    #         self.equation8 = "{} - {} = {}".format(float(self.firstNumber), float(self.secondNumber),
                    #                                                self.diff)
                    #         print("Equation8 = ", self.equation8)
                    #         self.nbrlist.clear()
                    # else:
                    #     if self.equalclicks == 1:
                    #         self.diff = int(self.firstNumber) - int(self.secondNumber)
                    #         self.result.insert(0, self.diff)
                    #         self.equation1 = "{} - {} = {}".format(int(self.firstNumber), int(self.secondNumber), self.diff)
                    #         print("Equation1 = ", self.equation1)
                    #         self.nbrlist.clear()
                    #
                    #     if self.equalclicks == 2:
                    #         self.diff = int(self.firstNumber) - int(self.secondNumber)
                    #         self.result.insert(0, self.diff)
                    #         self.equation2 = "{} - {} = {}".format(int(self.firstNumber), int(self.secondNumber), self.diff)
                    #         print("Equation2 = ", self.equation2)
                    #         self.nbrlist.clear()
                    #
                    #     if self.equalclicks == 3:
                    #         self.diff = int(self.firstNumber) - int(self.secondNumber)
                    #         self.result.insert(0, self.diff)
                    #         self.equation3 = "{} - {} = {}".format(int(self.firstNumber), int(self.secondNumber), self.diff)
                    #         print("Equation3 = ", self.equation3)
                    #         self.nbrlist.clear()
                    #
                    #     if self.equalclicks == 4:
                    #         self.diff = int(self.firstNumber) - int(self.secondNumber)
                    #         self.result.insert(0, self.diff)
                    #         self.equation4 = "{} - {} = {}".format(int(self.firstNumber), int(self.secondNumber), self.diff)
                    #         print("Equation4 = ", self.equation4)
                    #         self.nbrlist.clear()
                    #
                    #     if self.equalclicks == 5:
                    #         self.diff = int(self.firstNumber) - int(self.secondNumber)
                    #         self.result.insert(0, self.diff)
                    #         self.equation5 = "{} - {} = {}".format(int(self.firstNumber), int(self.secondNumber), self.diff)
                    #         print("Equation5 = ", self.equation5)
                    #         self.nbrlist.clear()
                    #
                    #     if self.equalclicks == 6:
                    #         self.diff = int(self.firstNumber) - int(self.secondNumber)
                    #         self.result.insert(0, self.diff)
                    #         self.equation6 = "{} - {} = {}".format(int(self.firstNumber), int(self.secondNumber), self.diff)
                    #         print("Equation6 = ", self.equation6)
                    #         self.nbrlist.clear()
                    #
                    #     if self.equalclicks == 7:
                    #         self.diff = int(self.firstNumber) - int(self.secondNumber)
                    #         self.result.insert(0, self.diff)
                    #         self.equation7 = "{} - {} = {}".format(int(self.firstNumber), int(self.secondNumber), self.diff)
                    #         print("Equation7 = ", self.equation7)
                    #         self.nbrlist.clear()
                    #
                    #     if self.equalclicks == 8:
                    #         self.diff = int(self.firstNumber) - int(self.secondNumber)
                    #         self.result.insert(0, self.diff)
                    #         self.equation8 = "{} - {} = {}".format(int(self.firstNumber), int(self.secondNumber), self.diff)
                    #         print("Equation8 = ", self.equation8)
                    #         self.nbrlist.clear()


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


        def MPlus():
            self.memory = self.result.get()
            self.result.delete(0, END)

        def MR():
            self.result.insert(0, self.memory)
            if self.firstNumber != 0:
                self.memory = self.secondNumber
            else:
                self.memory = self.firstNumber

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

        def history():
            if self.historyclicks == 1 and self.equalclicks == 0:
                messagebox.showinfo("Error", "You haven't used the calculator yet!")

            if self.historyclicks > self.equalclicks:
                    messagebox.showinfo("Error", "History items requested exceeds number of equations calculated!")
                    self.historyclicks = self.equalclicks

            labellocdict = {1:85, 2:125, 3:165, 4:205, 5:245, 6:285, 7:325, 8:365}

            if self.calculation == "Add":
                if len(self.nbrlist) > 2:  # If it's chain addition: 1+2+3 vs 1+2
                    """For each click of equalclicks, a complete equation has
                    occurred, so one click = Equation1, 2 clicks = Equation2,
                    and so on."""
                    self.Label = Label(frame2, text=f"Equation{self.equalclicks} = {self.chaineq}",
                                        bg="#80c1ff", fg="navy", anchor="w")
                    #If 2 self.equalclicks, then labellocdict[2] means y = 125
                    self.Label.place(x=5, y=labellocdict[self.equalclicks])
                    self.labellist.append(self.Label)
                    self.nbrlist.clear()
                else:
                    self.Label = Label(frame2, text=self.eq, bg="#80c1ff", fg="navy", anchor="w")
                    self.Label.place(x=5, y=labellocdict[self.equalclicks])
                    self.labellist.append(self.Label)


            if self.calculation == "Multiply":
                if len(self.nbrlist) > 2:  # If it's chain addition: 1+2+3 vs 1+2
                    self.Label = Label(frame2, text=f"Equation{self.equalclicks} = {self.chainMulteq}",
                                        bg="#80c1ff", fg="navy", anchor="w")
                    self.Label.place(x=5, y=labellocdict[self.equalclicks])
                    self.nbrlist.clear()
                    self.labellist.append(self.Label)


                else:
                    self.Label = Label(frame2, text=self.eq, bg="#80c1ff", fg="navy", anchor="w")
                    self.Label.place(x=5, y=labellocdict[self.equalclicks])
                    self.labellist.append(self.Label)


            if self.calculation == "Subtract":
                if len(self.nbrlist) > 2:  # If it's chain subtraction: 3-2-1 vs 3-2
                    self.Label = Label(frame2, text=f"Equation{self.equalclicks} = {self.chainSubtracteq}",
                                        bg="#80c1ff", fg="navy", anchor="w")
                    self.Label.place(x=5, y=labellocdict[self.equalclicks])
                    self.nbrlist.clear()
                    self.labellist.append(self.Label)


                else:
                    self.Label = Label(frame2, text=self.minuseq, bg="#80c1ff", fg="navy", anchor="w")
                    self.Label.place(x=5, y=labellocdict[self.equalclicks])
                    self.labellist.append(self.Label)


            # if self.historyclicks == 2:
            #     if self.chainAdd is True:
            #         self.Label2 = Label(frame2, text=self.chaineq,
            #                             bg="#80c1ff", fg="navy", anchor="w")
            #         self.Label2.place(x=5, y=125)
            #         self.labellist.append(self.Label2)

            #     if self.chainMult is True:
            #         self.Label2 = Label(frame2, text=self.equation2,
            #                             bg="#80c1ff", fg="navy", anchor="w")
            #         self.Label2.place(x=5, y=125)
            #         self.labellist.append(self.Label2)
            #
            #     else:
            #         self.Label2 = Label(frame2, text=self.eq, bg="#80c1ff", fg="navy", anchor="w")
            #         self.Label2.place(x=5, y=125)
            #         self.labellist.append(self.Label2)
            #
            # if self.historyclicks == 3:
            #     if self.chainAdd is True:
            #         self.Label3 = Label(frame2, text=self.equation3,
            #                             bg="#80c1ff", fg="navy", anchor="w")
            #         self.Label3.place(x=5, y=165)
            #         self.labellist.append(self.Label3)
            #
            #     if self.chainMult is True:
            #         self.Label3 = Label(frame2, text=self.equation3,
            #                             bg="#80c1ff", fg="navy", anchor="w")
            #         self.Label3.place(x=5, y=165)
            #         self.labellist.append(self.Label3)
            #
            #     else:
            #         self.Label3 = Label(frame2, text=self.eq, bg="#80c1ff", fg="navy", anchor="w")
            #         self.Label3.place(x=5, y=165)
            #         self.labellist.append(self.Label3)
            #
            # if self.historyclicks == 4:
            #     if self.chainAdd is True:
            #         self.Label4 = Label(frame2, text=self.equation4,
            #                             bg="#80c1ff", fg="navy", anchor="w")
            #         self.Label4.place(x=5, y=205)
            #         self.labellist.append(self.Label4)
            #
            #     if self.chainMult is True:
            #         self.Label4 = Label(frame2, text=self.equation4,
            #                             bg="#80c1ff", fg="navy", anchor="w")
            #         self.Label4.place(x=5, y=205)
            #         self.labellist.append(self.Label4)
            #
            #     else:
            #         self.Label4 = Label(frame2, text=self.eq, bg="#80c1ff", fg="navy", anchor="w")
            #         self.Label4.place(x=5, y=205)
            #         self.labellist.append(self.Label4)
            #
            # if self.historyclicks == 5:
            #     if self.chainAdd is True:
            #         self.Label5 = Label(frame2, text=self.equation5,
            #                             bg="#80c1ff", fg="navy", anchor="w")
            #         self.Label5.place(x=5, y=245)
            #         self.labellist.append(self.Label5)
            #
            #     if self.chainMult is True:
            #         self.Label5 = Label(frame2, text=self.equation5,
            #                             bg="#80c1ff", fg="navy", anchor="w")
            #         self.Label5.place(x=5, y=245)
            #         self.labellist.append(self.Label5)
            #
            #     else:
            #         self.Label5 = Label(frame2, text=self.eq, bg="#80c1ff", fg="navy", anchor="w")
            #         self.Label5.place(x=5, y=245)
            #         self.labellist.append(self.Label5)
            #
            # if self.historyclicks == 6:
            #     if self.chainAdd is True:
            #         self.Label6 = Label(frame2, text=self.equation6,
            #                             bg="#80c1ff", fg="navy", anchor="w")
            #         self.Label6.place(x=5, y=285)
            #         self.labellist.append(self.Label6)
            #
            #     if self.chainMult is True:
            #         self.Label6 = Label(frame2, text=self.equation6,
            #                             bg="#80c1ff", fg="navy", anchor="w")
            #         self.Label6.place(x=5, y=285)
            #         self.labellist.append(self.Label6)
            #
            #     else:
            #         self.Label6 = Label(frame2, text=self.eq, bg="#80c1ff", fg="navy", anchor="w")
            #         self.Label6.place(x=5, y=285)
            #         self.labellist.append(self.Label6)
            #
            # if self.historyclicks == 7:
            #     if self.chainAdd is True:
            #         self.Label7 = Label(frame2, text=self.equation7,
            #                             bg="#80c1ff", fg="navy", anchor="w")
            #         self.Label7.place(x=5, y=325)
            #         self.labellist.append(self.Label7)
            #
            #     if self.chainMult is True:
            #         self.Label7 = Label(frame2, text=self.equation7,
            #                             bg="#80c1ff", fg="navy", anchor="w")
            #         self.Label7.place(x=5, y=325)
            #         self.labellist.append(self.Label7)
            #
            #     else:
            #         self.Label7 = Label(frame2, text=self.eq, bg="#80c1ff", fg="navy", anchor="w")
            #         self.Label7.place(x=5, y=325)
            #         self.labellist.append(self.Label7)
            #
            # if self.historyclicks == 8:
            #     if self.chainAdd is True:
            #         self.Label8 = Label(frame2, text=self.equation8,
            #                             bg="#80c1ff", fg="navy", width=25, anchor="w")
            #         self.Label8.place(x=5, y=365)
            #         self.labellist.append(self.Label8)
            #
            #     if self.chainMult is True:
            #         self.Label8 = Label(frame2, text=self.equation8,
            #                             bg="#80c1ff", fg="navy", anchor="w")
            #         self.Label8.place(x=5, y=365)
            #         self.labellist.append(self.Label8)
            #
            #     else:
            #         self.Label8 = Label(frame2, text=self.eq, bg="#80c1ff", fg="navy", anchor="w")
            #         self.Label8.place(x=5, y=365)
            #         self.labellist.append(self.Label8)

            if self.equalclicks == 8:
                if self.historyclicks > 8:
                    messagebox.showinfo("Error", "History = ONLY the last 8 equations")

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

        frame2 = Frame(root, bg="lightgrey", bd=5)
        frame2.place(relx=.5, rely=.1, relwidth=0.45, relheight=0.80)

        historyButton = Button(frame2, text="History", fg="Navy", bg="#80c1ff", command=history)
        historyButton.configure(font=("Verdana", 12))
        historyButton.place(x=5, y=40)

        memoryButton = Button(frame2, text="Memory", bg="#80c1ff", fg="navy", command=memory)
        memoryButton.configure(font=("Verdana", 12))
        memoryButton.place(x=85, y=40)

        self.memoryLabel = Label(frame2, text="", bg="#80c1ff", fg="navy", width=25, anchor="w")
        self.memoryLabel.place(x=5, y=85)

        self.result = Entry(frame2, width=15, borderwidth=3)
        self.result.configure(font=("Verdana", 14))
        self.result.grid(row=0, column=0, pady=5)

        root.mainloop()

Calculator()

