from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import math

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
        root.geometry("490x500")
        #root.resizable(False, False)

        def buttonClick(number):
            self.current = self.result.get()
            self.result.delete(0, END)
            self.result.insert(0, str(self.current) + str(number))
            if number == "%":
                number = 0.01

        def clearEntry():
            self.current = self.result.get()
            self.result.delete(0, END)

        def clear():
            self.current = self.result.get()
            self.result.delete(0, END)
            self.memory = 0
            if self.historyclicks >= 1 and self.historyclicks <= self.equalclicks:
                if self.Label1["text"] != "":
                    self.Label1["text"] = ""
            if self.historyclicks >= 2 and self.historyclicks <= self.equalclicks:
                if self.Label2["text"] != "":
                    self.Label2["text"] = ""
            if self.historyclicks >= 3 and self.historyclicks <= self.equalclicks:
                if self.Label3["text"] != "":
                    self.Label3["text"] = ""
            if self.historyclicks >= 4 and self.historyclicks <= self.equalclicks:
                if self.Label4["text"] != "":
                    self.Label4["text"] = ""
            if self.historyclicks >= 5 and self.historyclicks <= self.equalclicks:
                if self.Label5["text"] != "":
                    self.Label5["text"] = ""
            if self.historyclicks >= 6 and self.historyclicks <= self.equalclicks:
                if self.Label6["text"] != "":
                    self.Label6["text"] = ""
            if self.historyclicks >= 7 and self.historyclicks <= self.equalclicks:
                if self.Label7["text"] != "":
                    self.Label7["text"] = ""
            if self.historyclicks >= 8 and self.historyclicks <= self.equalclicks:
                if self.Label8["text"] != "":
                    self.Label8["text"] = ""

        def delete():
            self.backspace = str(self.result.get())
            self.result.delete(0, END)
            self.result.insert(0, self.backspace[0:-1])

        self.plusclicks = 0
        self.minusclicks = 0

        def add():
            self.plusclicks += 1
            self.calculation = "Add"
            self.firstNumber = self.result.get()
            self.result.delete(0, END)
            if "." in str(self.firstNumber):
                self.firstNumber = float(self.firstNumber)
            else:
                self.firstNumber = int(self.firstNumber)

        def subtract():
            self.minusclicks += 1
            self.calculation = "Subtract"
            self.firstNumber = self.result.get()
            self.result.delete(0, END)
            if "." in str(self.firstNumber):
                self.firstNumber = float(self.firstNumber)
            else:
                self.firstNumber = int(self.firstNumber)

        self.multiplyclicks = 0

        def multiply():
            self.multiplyclicks += 1
            self.firstNumber = self.result.get()
            if "." in str(self.firstNumber):
                self.firstNumber = float(self.firstNumber)
            else:
                self.firstNumber = int(self.firstNumber)
            self.calculation = "Multiply"
            self.multiplyClicksList = []
            self.result.delete(0, END)

        def divide():
            self.firstNumber = self.result.get()
            if "." in str(self.firstNumber):
                self.firstNumber = float(self.firstNumber)
            else:
                self.firstNumber = int(self.firstNumber)
            self.calculation = "Divide"
            self.result.delete(0, END)

        self.percentclicks = 0

        def percent():
            self.percentclicks += 1
            self.firstNumber = self.result.get()
            if "." in str(self.firstNumber):
                self.firstNumber = float(self.firstNumber)
            else:
                self.firstNumber = int(self.firstNumber)
            self.calculation = "Percent"
            self.result.delete(0, END)

        def modulo():
            self.firstNumber = self.result.get()
            if "." in str(self.firstNumber):
                self.firstNumber = float(self.firstNumber)
            else:
                self.firstNumber = int(self.firstNumber)
            self.calculation = "Modulo"
            self.result.delete(0, END)

        def squareRootOfx():
            self.firstNumber = self.result.get()
            if "." in str(self.firstNumber):
                self.firstNumber = float(self.firstNumber)
            else:
                self.firstNumber = int(self.firstNumber)
            self.calculation = "SquareRootOfx"


        def powerOf2():
            self.firstNumber = self.result.get()
            if "." in str(self.firstNumber):
                self.firstNumber = float(self.firstNumber)
            else:
                self.firstNumber = int(self.firstNumber)
            self.calculation = "PowerOf2"

        def oneOverX():
            self.firstNumber = self.result.get()
            if "." in str(self.firstNumber):
                self.firstNumber = float(self.firstNumber)
            else:
                self.firstNumber = int(self.firstNumber)
            self.calculation = "OneOverx"
            self.result.delete(0, END)
            try:
                self.result.insert(0, round(1 / self.firstNumber, 4))
            except ZeroDivisionError:
                messagebox.showinfo("Error", "You can't divide by zero!")


        self.equalclicks = 0
        self.historyclicks = 0

        def equals():
            self.equalclicks += 1
            self.secondNumber = self.result.get()
            self.result.delete(0, END)
            if self.calculation == "Add":
                if "." in str(self.firstNumber) or str(self.secondNumber):
                    if self.equalclicks == 1:
                        self.result.insert(0, round(float(self.firstNumber) + float(self.secondNumber), 4))
                        self.sum = round(float(self.firstNumber) + float(self.secondNumber), 4)
                        self.equation1 = "{} + {} = {}".format(self.firstNumber, self.secondNumber, self.sum)
                        print("Equation1 = ", self.equation1)

                    if self.equalclicks == 2:
                        self.result.insert(0, round(float(self.firstNumber) + float(self.secondNumber), 4))
                        self.sum = float(self.firstNumber)
                        self.sum = round(float(self.firstNumber) + float(self.secondNumber), 4)
                        self.equation2 = "{} + {} = {}".format(self.firstNumber, self.secondNumber, self.sum)
                        print("Equation2 = ", self.equation2)

                    if self.equalclicks == 3:
                        self.result.insert(0, round(float(self.firstNumber) + float(self.secondNumber), 4))
                        self.sum = float(self.firstNumber)
                        self.sum = round(float(self.firstNumber) + float(self.secondNumber), 4)
                        self.equation3 = "{} + {} = {}".format(self.firstNumber, self.secondNumber, self.sum)
                        print("Equation3 = ", self.equation3)

                    if self.equalclicks == 4:
                        self.result.insert(0, round(float(self.firstNumber) + float(self.secondNumber), 4))
                        self.sum = float(self.firstNumber)
                        self.sum = round(float(self.firstNumber) + float(self.secondNumber), 4)
                        self.equation4 = "{} + {} = {}".format(self.firstNumber, self.secondNumber, self.sum)
                        print("Equation4 = ", self.equation4)

                    if self.equalclicks == 5:
                        self.result.insert(0, round(float(self.firstNumber) + float(self.secondNumber), 4))
                        self.sum = float(self.firstNumber)
                        self.sum = round(float(self.firstNumber) + float(self.secondNumber), 4)
                        self.equation5 = "{} + {} = {}".format(self.firstNumber, self.secondNumber, self.sum)
                        print("Equation5 = ", self.equation5)

                    if self.equalclicks == 6:
                        self.result.insert(0, round(float(self.firstNumber) + float(self.secondNumber), 4))
                        self.sum = float(self.firstNumber)
                        self.sum = round(float(self.firstNumber) + float(self.secondNumber), 4)
                        self.equation6 = "{} + {} = {}".format(self.firstNumber, self.secondNumber, self.sum)
                        print("Equation6 = ", self.equation6)

                    if self.equalclicks == 7:
                        self.result.insert(0, round(float(self.firstNumber) + float(self.secondNumber), 4))
                        self.sum = float(self.firstNumber)
                        self.sum = round(float(self.firstNumber) + float(self.secondNumber), 4)
                        self.equation7 = "{} + {} = {}".format(self.firstNumber, self.secondNumber, self.sum)
                        print("Equation7 = ", self.equation7)

                    if self.equalclicks == 8:
                        self.result.insert(0, round(float(self.firstNumber) + float(self.secondNumber), 4))
                        self.sum = float(self.firstNumber)
                        self.sum = round(float(self.firstNumber) + float(self.secondNumber), 4)
                        self.equation8 = "{} + {} = {}".format(self.firstNumber, self.secondNumber, self.sum)
                        print("Equation8 = ", self.equation8)

                else:
                    self.result.insert(0, int(self.firstNumber) + int(self.secondNumber))
                    self.sum = self.firstNumber + int(self.secondNumber)
                    if self.equalclicks == 1:
                        self.equation1 = "{} + {} = {}".format(self.firstNumber, self.secondNumber, self.sum)
                        print("Equation1 = ", self.equation1)

                    if self.equalclicks == 2:
                        self.sum = self.firstNumber
                        self.sum = self.firstNumber + int(self.secondNumber)
                        self.equation2 = "{} + {} = {}".format(self.firstNumber, self.secondNumber, self.sum)
                        print("Equation2 = ", self.equation2)

                    if self.equalclicks == 3:
                        self.sum = self.firstNumber
                        self.sum = self.firstNumber + int(self.secondNumber)
                        self.equation3 = "{} + {} = {}".format(self.firstNumber, self.secondNumber, self.sum)
                        print("Equation3 = ", self.equation3)

                    if self.equalclicks == 4:
                        self.sum = self.firstNumber
                        self.sum = self.firstNumber + int(self.secondNumber)
                        self.equation4 = "{} + {} = {}".format(self.firstNumber, self.secondNumber, self.sum)
                        print("Equation4 = ", self.equation4)

                    if self.equalclicks == 5:
                        self.sum = self.firstNumber
                        self.sum = self.firstNumber + int(self.secondNumber)
                        self.equation5 = "{} + {} = {}".format(self.firstNumber, self.secondNumber, self.sum)
                        print("Equation5 = ", self.equation5)

                    if self.equalclicks == 6:
                        self.sum = self.firstNumber
                        self.sum = self.firstNumber + int(self.secondNumber)
                        self.equation6 = "{} + {} = {}".format(self.firstNumber, self.secondNumber, self.sum)
                        print("Equation6 = ", self.equation6)

                    if self.equalclicks == 7:
                        self.sum = self.firstNumber
                        self.sum = self.firstNumber + int(self.secondNumber)
                        self.equation7 = "{} + {} = {}".format(self.firstNumber, self.secondNumber, self.sum)
                        print("Equation7 = ", self.equation7)

                    if self.equalclicks == 8:
                        self.sum = self.firstNumber
                        self.sum = self.firstNumber + int(self.secondNumber)
                        self.equation8 = "{} + {} = {}".format(self.firstNumber, self.secondNumber, self.sum)
                        print("Equation8 = ", self.equation8)

            if self.calculation == "Subtract":
                if "." in str(self.firstNumber) or str(self.secondNumber):
                    if self.equalclicks == 1:
                        self.diff = round(float(self.firstNumber) - float(self.secondNumber), 4)
                        self.result.insert(0, self.diff)
                        self.equation1 = "{} - {} = {}".format(float(self.firstNumber), float(self.secondNumber), self.diff)
                        print("Equation1 = ", self.equation1)

                    if self.equalclicks == 2:
                        self.diff = round(float(self.firstNumber) - float(self.secondNumber), 4)
                        self.result.insert(0, self.diff)
                        self.equation2 = "{} - {} = {}".format(float(self.firstNumber), float(self.secondNumber),
                                                               self.diff)
                        print("Equation2 = ", self.equation2)

                    if self.equalclicks == 3:
                        self.diff = round(float(self.firstNumber) - float(self.secondNumber), 4)
                        self.result.insert(0, self.diff)
                        self.equation3 = "{} - {} = {}".format(float(self.firstNumber), float(self.secondNumber),
                                                               self.diff)
                        print("Equation3 = ", self.equation3)

                    if self.equalclicks == 4:
                        self.diff = round(float(self.firstNumber) - float(self.secondNumber), 4)
                        self.result.insert(0, self.diff)
                        self.equation4 = "{} - {} = {}".format(float(self.firstNumber), float(self.secondNumber),
                                                               self.diff)
                        print("Equation4 = ", self.equation4)

                    if self.equalclicks == 5:
                        self.diff = round(float(self.firstNumber) - float(self.secondNumber), 4)
                        self.result.insert(0, self.diff)
                        self.equation5 = "{} - {} = {}".format(float(self.firstNumber), float(self.secondNumber),
                                                               self.diff)
                        print("Equation5 = ", self.equation5)

                    if self.equalclicks == 6:
                        self.diff = round(float(self.firstNumber) - float(self.secondNumber), 4)
                        self.result.insert(0, self.diff)
                        self.equation6 = "{} - {} = {}".format(float(self.firstNumber), float(self.secondNumber),
                                                               self.diff)
                        print("Equation6 = ", self.equation6)

                    if self.equalclicks == 7:
                        self.diff = round(float(self.firstNumber) - float(self.secondNumber), 4)
                        self.result.insert(0, self.diff)
                        self.equation7 = "{} - {} = {}".format(float(self.firstNumber), float(self.secondNumber),
                                                               self.diff)
                        print("Equation7 = ", self.equation7)

                    if self.equalclicks == 8:
                        self.diff = round(float(self.firstNumber) - float(self.secondNumber), 4)
                        self.result.insert(0, self.diff)
                        self.equation8 = "{} - {} = {}".format(float(self.firstNumber), float(self.secondNumber),
                                                               self.diff)
                        print("Equation8 = ", self.equation8)
                else:
                    if self.equalclicks == 1:
                        self.diff = int(self.firstNumber) - int(self.secondNumber)
                        self.result.insert(0, self.diff)
                        self.equation1 = "{} - {} = {}".format(int(self.firstNumber), int(self.secondNumber), self.diff)
                        print("Equation1 = ", self.equation1)

                    if self.equalclicks == 2:
                        self.diff = int(self.firstNumber) - int(self.secondNumber)
                        self.result.insert(0, self.diff)
                        self.equation2 = "{} - {} = {}".format(int(self.firstNumber), int(self.secondNumber), self.diff)
                        print("Equation2 = ", self.equation2)

                    if self.equalclicks == 3:
                        self.diff = int(self.firstNumber) - int(self.secondNumber)
                        self.result.insert(0, self.diff)
                        self.equation3 = "{} - {} = {}".format(int(self.firstNumber), int(self.secondNumber), self.diff)
                        print("Equation3 = ", self.equation3)

                    if self.equalclicks == 4:
                        self.diff = int(self.firstNumber) - int(self.secondNumber)
                        self.result.insert(0, self.diff)
                        self.equation4 = "{} - {} = {}".format(int(self.firstNumber), int(self.secondNumber), self.diff)
                        print("Equation4 = ", self.equation4)

                    if self.equalclicks == 5:
                        self.diff = int(self.firstNumber) - int(self.secondNumber)
                        self.result.insert(0, self.diff)
                        self.equation5 = "{} - {} = {}".format(int(self.firstNumber), int(self.secondNumber), self.diff)
                        print("Equation5 = ", self.equation5)

                    if self.equalclicks == 6:
                        self.diff = int(self.firstNumber) - int(self.secondNumber)
                        self.result.insert(0, self.diff)
                        self.equation6 = "{} - {} = {}".format(int(self.firstNumber), int(self.secondNumber), self.diff)
                        print("Equation6 = ", self.equation6)

                    if self.equalclicks == 7:
                        self.diff = int(self.firstNumber) - int(self.secondNumber)
                        self.result.insert(0, self.diff)
                        self.equation7 = "{} - {} = {}".format(int(self.firstNumber), int(self.secondNumber), self.diff)
                        print("Equation7 = ", self.equation7)

                    if self.equalclicks == 8:
                        self.diff = int(self.firstNumber) - int(self.secondNumber)
                        self.result.insert(0, self.diff)
                        self.equation8 = "{} - {} = {}".format(int(self.firstNumber), int(self.secondNumber), self.diff)
                        print("Equation8 = ", self.equation8)

            if self.calculation == "Multiply":
                self.multiplyClicksList = []
                if self.multiplyclicks > 1:
                    self.multiplyClicksList.append(self.multiplyclicks)

                if "." in str(self.firstNumber) or str(self.secondNumber):
                    if self.equalclicks == 1:
                        self.mult = round(float(self.firstNumber) * float(self.secondNumber), 4)
                        self.result.insert(0, self.mult)
                        self.equation1 = "{} * {} = {}".format(self.firstNumber, self.secondNumber, self.mult)
                        print("Equation1 = ", self.equation1)

                    if self.equalclicks == 2:
                        self.mult = round(float(self.firstNumber) * float(self.secondNumber), 4)
                        self.result.insert(0, self.mult)
                        self.equation2 = "{} * {} = {}".format(self.firstNumber, self.secondNumber, self.mult)
                        print("Equation2 = ", self.equation2)

                    if self.equalclicks == 3:
                        self.mult = round(float(self.firstNumber) * float(self.secondNumber), 4)
                        self.result.insert(0, self.mult)
                        self.equation3 = "{} * {} = {}".format(self.firstNumber, self.secondNumber, self.mult)
                        print("Equation3 = ", self.equation3)

                    if self.equalclicks == 4:
                        self.mult = round(float(self.firstNumber) * float(self.secondNumber), 4)
                        self.result.insert(0, self.mult)
                        self.equation4 = "{} * {} = {}".format(self.firstNumber, self.secondNumber, self.mult)
                        print("Equation4 = ", self.equation4)

                    if self.equalclicks == 5:
                        self.mult = round(float(self.firstNumber) * float(self.secondNumber), 4)
                        self.result.insert(0, self.mult)
                        self.equation5 = "{} * {} = {}".format(self.firstNumber, self.secondNumber, self.mult)
                        print("Equation5 = ", self.equation5)

                    if self.equalclicks == 6:
                        self.mult = round(float(self.firstNumber) * float(self.secondNumber), 4)
                        self.result.insert(0, self.mult)
                        self.equation6 = "{} * {} = {}".format(self.firstNumber, self.secondNumber, self.mult)
                        print("Equation6 = ", self.equation6)

                    if self.equalclicks == 7:
                        self.mult = round(float(self.firstNumber) * float(self.secondNumber), 4)
                        self.result.insert(0, self.mult)
                        self.equation7 = "{} * {} = {}".format(self.firstNumber, self.secondNumber, self.mult)
                        print("Equation7 = ", self.equation7)

                    if self.equalclicks == 8:
                        self.mult = round(float(self.firstNumber) * float(self.secondNumber), 4)
                        self.result.insert(0, self.mult)
                        self.equation8 = "{} * {} = {}".format(self.firstNumber, self.secondNumber, self.mult)
                        print("Equation8 = ", self.equation8)
                else:
                    if self.equalclicks == 1:
                        self.mult = self.firstNumber * int(self.secondNumber)
                        self.result.insert(0, self.mult)
                        self.equation1 = "{} * {} = {}".format(self.firstNumber, self.secondNumber, self.mult)
                        print("Equation1 = ", self.equation1)

                    if self.equalclicks == 2:
                        self.mult = self.firstNumber * int(self.secondNumber)
                        self.result.insert(0, self.mult)
                        self.equation2 = "{} * {} = {}".format(self.firstNumber, self.secondNumber, self.mult)
                        print("Equation2 = ", self.equation2)

                    if self.equalclicks == 3:
                        self.mult = self.firstNumber * int(self.secondNumber)
                        self.result.insert(0, self.mult)
                        self.equation3 = "{} * {} = {}".format(self.firstNumber, self.secondNumber, self.mult)
                        print("Equation3 = ", self.equation3)

                    if self.equalclicks == 4:
                        self.mult = self.firstNumber * int(self.secondNumber)
                        self.result.insert(0, self.mult)
                        self.equation4 = "{} * {} = {}".format(self.firstNumber, self.secondNumber, self.mult)
                        print("Equation4 = ", self.equation4)

                    if self.equalclicks == 5:
                        self.mult = self.firstNumber * int(self.secondNumber)
                        self.result.insert(0, self.mult)
                        self.equation5 = "{} * {} = {}".format(self.firstNumber, self.secondNumber, self.mult)
                        print("Equation5 = ", self.equation5)

                    if self.equalclicks == 6:
                        self.mult = self.firstNumber * int(self.secondNumber)
                        self.result.insert(0, self.mult)
                        self.equation6 = "{} * {} = {}".format(self.firstNumber, self.secondNumber, self.mult)
                        print("Equation6 = ", self.equation6)

                    if self.equalclicks == 7:
                        self.mult = self.firstNumber * int(self.secondNumber)
                        self.result.insert(0, self.mult)
                        self.equation7 = "{} * {} = {}".format(self.firstNumber, self.secondNumber, self.mult)
                        print("Equation7 = ", self.equation7)

                    if self.equalclicks == 8:
                        self.mult = self.firstNumber * int(self.secondNumber)
                        self.result.insert(0, self.mult)
                        self.equation8 = "{} * {} = {}".format(self.firstNumber, self.secondNumber, self.mult)
                        print("Equation8 = ", self.equation8)

            if self.calculation == "Divide":
                try:
                    if "." in str(self.firstNumber) or str(self.secondNumber):
                        if self.equalclicks == 1:
                            self.divide = round(self.firstNumber / float(self.secondNumber), 4)
                            self.result.insert(0, self.divide)
                            self.equation1 = "{} / {} = {}".format(self.firstNumber, self.secondNumber, self.divide)
                            print("Equation1 = ", self.equation1)

                        if self.equalclicks == 2:
                            self.divide = round(self.firstNumber / float(self.secondNumber), 4)
                            self.result.insert(0, self.divide)
                            self.equation2 = "{} / {} = {}".format(self.firstNumber, self.secondNumber, self.divide)
                            print("Equation2 = ", self.equation2)

                        if self.equalclicks == 3:
                            self.divide = round(self.firstNumber / float(self.secondNumber), 4)
                            self.result.insert(0, self.divide)
                            self.equation3 = "{} / {} = {}".format(self.firstNumber, self.secondNumber, self.divide)
                            print("Equation3 = ", self.equation3)

                        if self.equalclicks == 4:
                            self.divide = round(self.firstNumber / float(self.secondNumber), 4)
                            self.result.insert(0, self.divide)
                            self.equation4 = "{} / {} = {}".format(self.firstNumber, self.secondNumber, self.divide)
                            print("Equation4 = ", self.equation4)

                        if self.equalclicks == 5:
                            self.divide = round(self.firstNumber / float(self.secondNumber), 4)
                            self.result.insert(0, self.divide)
                            self.equation5 = "{} / {} = {}".format(self.firstNumber, self.secondNumber, self.divide)
                            print("Equation5 = ", self.equation5)

                        if self.equalclicks == 6:
                            self.divide = round(self.firstNumber / float(self.secondNumber), 4)
                            self.result.insert(0, self.divide)
                            self.equation6 = "{} / {} = {}".format(self.firstNumber, self.secondNumber, self.divide)
                            print("Equation6 = ", self.equation6)

                        if self.equalclicks == 7:
                            self.divide = round(self.firstNumber / float(self.secondNumber), 4)
                            self.result.insert(0, self.divide)
                            self.equation7 = "{} / {} = {}".format(self.firstNumber, self.secondNumber, self.divide)
                            print("Equation7 = ", self.equation7)

                        if self.equalclicks == 8:
                            self.divide = round(self.firstNumber / float(self.secondNumber), 4)
                            self.result.insert(0, self.divide)
                            self.equation8 = "{} / {} = {}".format(self.firstNumber, self.secondNumber, self.divide)
                            print("Equation8 = ", self.equation8)

                    else:
                        if self.equalclicks == 1:
                            self.divide = round(self.firstNumber / int(self.secondNumber), 4)
                            self.result.insert(0, self.divide)
                            self.equation1 = "{} / {} = {}".format(self.firstNumber, self.secondNumber, self.divide)
                            print("Equation1 = ", self.equation1)

                        if self.equalclicks == 2:
                            self.divide = round(self.firstNumber / int(self.secondNumber), 4)
                            self.result.insert(0, self.divide)
                            self.equation2 = "{} / {} = {}".format(self.firstNumber, self.secondNumber, self.divide)
                            print("Equation2 = ", self.equation2)

                        if self.equalclicks == 3:
                            self.divide = round(self.firstNumber / int(self.secondNumber), 4)
                            self.result.insert(0, self.divide)
                            self.equation3 = "{} / {} = {}".format(self.firstNumber, self.secondNumber, self.divide)
                            print("Equation3 = ", self.equation3)

                        if self.equalclicks == 4:
                            self.divide = round(self.firstNumber / int(self.secondNumber), 4)
                            self.result.insert(0, self.divide)
                            self.equation4 = "{} / {} = {}".format(self.firstNumber, self.secondNumber, self.divide)
                            print("Equation4 = ", self.equation4)

                        if self.equalclicks == 5:
                            self.divide = round(self.firstNumber / int(self.secondNumber), 4)
                            self.result.insert(0, self.divide)
                            self.equation5 = "{} / {} = {}".format(self.firstNumber, self.secondNumber, self.divide)
                            print("Equation5 = ", self.equation5)

                        if self.equalclicks == 6:
                            self.divide = round(self.firstNumber / int(self.secondNumber), 4)
                            self.result.insert(0, self.divide)
                            self.equation6 = "{} / {} = {}".format(self.firstNumber, self.secondNumber, self.divide)
                            print("Equation6 = ", self.equation6)

                        if self.equalclicks == 7:
                            self.divide = round(self.firstNumber / int(self.secondNumber), 4)
                            self.result.insert(0, self.divide)
                            self.equation7 = "{} / {} = {}".format(self.firstNumber, self.secondNumber, self.divide)
                            print("Equation7 = ", self.equation7)

                        if self.equalclicks == 8:
                            self.divide = round(self.firstNumber / int(self.secondNumber), 4)
                            self.result.insert(0, self.divide)
                            self.equation8 = "{} / {} = {}".format(self.firstNumber, self.secondNumber, self.divide)
                            print("Equation8 = ", self.equation8)

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

                    if self.equalclicks == 2:
                        self.result.insert(0, self.percentage)
                        self.equation2 = "{} % of {} = {}".format(self.firstNumber, self.secondNumber, self.percentage)
                        print("Equation2 = ", self.equation2)

                    if self.equalclicks == 3:
                        self.result.insert(0, self.percentage)
                        self.equation3 = "{} % of {} = {}".format(self.firstNumber, self.secondNumber, self.percentage)
                        print("Equation3 = ", self.equation3)

                    if self.equalclicks == 4:
                        self.result.insert(0, self.percentage)
                        self.equation4 = "{} % of {} = {}".format(self.firstNumber, self.secondNumber, self.percentage)
                        print("Equation4 = ", self.equation4)

                    if self.equalclicks == 5:
                        self.result.insert(0, self.percentage)
                        self.equation5 = "{} % of {} = {}".format(self.firstNumber, self.secondNumber, self.percentage)
                        print("Equation5 = ", self.equation5)

                    if self.equalclicks == 6:
                        self.result.insert(0, self.percentage)
                        self.equation6 = "{} % of {} = {}".format(self.firstNumber, self.secondNumber, self.percentage)
                        print("Equation6 = ", self.equation6)

                    if self.equalclicks == 7:
                        self.result.insert(0, self.percentage)
                        self.equation7 = "{} % of {} = {}".format(self.firstNumber, self.secondNumber, self.percentage)
                        print("Equation7 = ", self.equation7)

                    if self.equalclicks == 8:
                        self.result.insert(0, self.percentage)
                        self.equation8 = "{} % of {} = {}".format(self.firstNumber, self.secondNumber, self.percentage)
                        print("Equation8 = ", self.equation8)

                else:
                    if self.equalclicks == 1:
                        self.result.insert(0, self.percentage)
                        self.equation1 = "{} % of {} = {}".format(self.firstNumber, self.secondNumber, self.percentage)
                        print("Equation1 = ", self.equation1)

                    if self.equalclicks == 2:
                        self.result.insert(0, self.percentage)
                        self.equation2 = "{} % of {} = {}".format(self.firstNumber, self.secondNumber, self.percentage)
                        print("Equation2 = ", self.equation2)

                    if self.equalclicks == 3:
                        self.result.insert(0, self.percentage)
                        self.equation3 = "{} % of {} = {}".format(self.firstNumber, self.secondNumber, self.percentage)
                        print("Equation3 = ", self.equation3)

                    if self.equalclicks == 4:
                        self.result.insert(0, self.percentage)
                        self.equation4 = "{} % of {} = {}".format(self.firstNumber, self.secondNumber, self.percentage)
                        print("Equation4 = ", self.equation4)

                    if self.equalclicks == 5:
                        self.result.insert(0, self.percentage)
                        self.equation5 = "{} % of {} = {}".format(self.firstNumber, self.secondNumber, self.percentage)
                        print("Equation5 = ", self.equation5)

                    if self.equalclicks == 6:
                        self.result.insert(0, self.percentage)
                        self.equation6 = "{} % of {} = {}".format(self.firstNumber, self.secondNumber, self.percentage)
                        print("Equation6 = ", self.equation6)

                    if self.equalclicks == 7:
                        self.result.insert(0, self.percentage)
                        self.equation7 = "{} % of {} = {}".format(self.firstNumber, self.secondNumber, self.percentage)
                        print("Equation7 = ", self.equation7)

                    if self.equalclicks == 8:
                        self.result.insert(0, self.percentage)
                        self.equation8 = "{} % of {} = {}".format(self.firstNumber, self.secondNumber, self.percentage)
                        print("Equation8 = ", self.equation8)

            if self.calculation == "Modulo":
                try:
                    if "." in str(self.firstNumber) or str(self.secondNumber):
                        self.mod = round(self.firstNumber % float(self.secondNumber), 4)
                        if self.equalclicks == 1:
                            self.result.insert(0, self.mod)
                            self.equation1 = "{} % {} = {}".format(self.firstNumber, self.secondNumber, self.mod)
                            print("Equation1 = ", self.equation1)

                        if self.equalclicks == 2:
                            self.result.insert(0, self.mod)
                            self.equation2 = "{} % {} = {}".format(self.firstNumber, self.secondNumber, self.mod)
                            print("Equation2 = ", self.equation2)

                        if self.equalclicks == 3:
                            self.result.insert(0, self.mod)
                            self.equation3 = "{} % {} = {}".format(self.firstNumber, self.secondNumber, self.mod)
                            print("Equation3 = ", self.equation3)

                        if self.equalclicks == 4:
                            self.result.insert(0, self.mod)
                            self.equation4 = "{} % {} = {}".format(self.firstNumber, self.secondNumber, self.mod)
                            print("Equation4 = ", self.equation4)

                        if self.equalclicks == 5:
                            self.result.insert(0, self.mod)
                            self.equation5 = "{} % {} = {}".format(self.firstNumber, self.secondNumber, self.mod)
                            print("Equation5 = ", self.equation5)

                        if self.equalclicks == 6:
                            self.result.insert(0, self.mod)
                            self.equation6 = "{} % {} = {}".format(self.firstNumber, self.secondNumber, self.mod)
                            print("Equation6 = ", self.equation6)

                        if self.equalclicks == 7:
                            self.result.insert(0, self.mod)
                            self.equation7 = "{} % {} = {}".format(self.firstNumber, self.secondNumber, self.mod)
                            print("Equation7 = ", self.equation7)

                        if self.equalclicks == 8:
                            self.result.insert(0, self.mod)
                            self.equation8 = "{} % {} = {}".format(self.firstNumber, self.secondNumber, self.mod)
                            print("Equation8 = ", self.equation8)

                    else:
                        self.mod = round(self.firstNumber % int(self.secondNumber), 4)
                        if self.equalclicks == 1:
                            self.result.insert(0, self.mod)
                            self.equation1 = "{} % {} = {}".format(self.firstNumber, self.secondNumber, self.mod)
                            print("Equation1 = ", self.equation1)

                        if self.equalclicks == 2:
                            self.result.insert(0, self.mod)
                            self.equation2 = "{} % {} = {}".format(self.firstNumber, self.secondNumber, self.mod)
                            print("Equation2 = ", self.equation2)

                        if self.equalclicks == 3:
                            self.result.insert(0, self.mod)
                            self.equation3 = "{} % {} = {}".format(self.firstNumber, self.secondNumber, self.mod)
                            print("Equation3 = ", self.equation3)

                        if self.equalclicks == 4:
                            self.result.insert(0, self.mod)
                            self.equation4 = "{} % {} = {}".format(self.firstNumber, self.secondNumber, self.mod)
                            print("Equation4 = ", self.equation4)

                        if self.equalclicks == 5:
                            self.result.insert(0, self.mod)
                            self.equation5 = "{} % {} = {}".format(self.firstNumber, self.secondNumber, self.mod)
                            print("Equation5 = ", self.equation5)

                        if self.equalclicks == 6:
                            self.result.insert(0, self.mod)
                            self.equation6 = "{} % {} = {}".format(self.firstNumber, self.secondNumber, self.mod)
                            print("Equation6 = ", self.equation6)

                        if self.equalclicks == 7:
                            self.result.insert(0, self.mod)
                            self.equation7 = "{} % {} = {}".format(self.firstNumber, self.secondNumber, self.mod)
                            print("Equation7 = ", self.equation7)

                        if self.equalclicks == 8:
                            self.result.insert(0, self.mod)
                            self.equation8 = "{} % {} = {}".format(self.firstNumber, self.secondNumber, self.mod)
                            print("Equation8 = ", self.equation8)

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
            self.firstNumber = self.result.get()
            self.result.delete(0, END)
            self.result.insert(0, self.memory)
            self.memory = self.firstNumber

        def MC():
            self.memory = 0
            self.result.delete(0, END)
            if self.memoryLabel["text"] != "":
                self.memoryLabel["text"] = ""

        def plusMinus():
            self.plsMinus = self.result.get()
            self.result.delete(0, END)
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

        def decimal():
            self.result.insert(len(self.result.get()), ".")

        frame1 = Frame(root, bg="#80c1ff", bd=5)
        frame1.place(relx=.1, rely=.1, relwidth=0.70, relheight=0.80)

        buttonMC = Button(frame1, text="MC", height=3, width=5, command=MC)
        buttonMC.grid(row=3, column=0)

        MRButton = Button(frame1, text="MR", height=3, width=5, command=MR)
        MRButton.grid(row=3, column=1)

        MPlusButton = Button(frame1, text="M+", height=3, width=5, command=MPlus)
        MPlusButton.grid(row=3, column=2)

        percentButton = Button(frame1, text="%", height=3, width=5, command=percent)
        percentButton.grid(row=3, column=3)

        buttonModulo = Button(frame1, text="Mod", height=3, width=5, command=modulo)
        buttonModulo.grid(row=4, column=0)

        buttonSqRoot = Button(frame1, text="√(x)", height=3, width=5, command=squareRootOfx)
        buttonSqRoot.grid(row=4, column=1)

        button2ndPower = Button(frame1, text="x²", height=3, width=5, command=powerOf2)
        button2ndPower.grid(row=4, column=2)

        buttonOneOverX = Button(frame1, text="1/x", height=3, width=5, command=oneOverX)
        buttonOneOverX.grid(row=4, column=3)

        buttonCE = Button(frame1, text="CE", height=3, width=5, command=clearEntry)
        buttonCE.grid(row=5, column=0)

        buttonClear = Button(frame1, text="C", height=3, width=5, command=clear)
        buttonClear.grid(row=5, column=1)

        buttonDelete = Button(frame1, text="del", height=3, width=5, command=delete)
        buttonDelete.grid(row=5, column=2)

        buttonDivide = Button(frame1, text="/", height=3, width=5, command=divide)
        buttonDivide.grid(row=5, column=3)

        button7 = Button(frame1, text="7", height=3, width=5, command=lambda: buttonClick(7))
        button7.grid(row=6, column=0)

        button8 = Button(frame1, text="8", height=3, width=5, command=lambda: buttonClick(8))
        button8.grid(row=6, column=1)

        button9 = Button(frame1, text="9", height=3, width=5, command=lambda: buttonClick(9))
        button9.grid(row=6, column=2)

        buttonMultiply = Button(frame1, text="x", height=3, width=5, command=multiply)
        buttonMultiply.grid(row=6, column=3)

        button4 = Button(frame1, text="4", height=3, width=5, command=lambda: buttonClick(4))
        button4.grid(row=7, column=0)

        button5 = Button(frame1, text="5", height=3, width=5, command=lambda: buttonClick(5))
        button5.grid(row=7, column=1)

        button6 = Button(frame1, text="6", height=3, width=5, command=lambda: buttonClick(6))
        button6.grid(row=7, column=2)

        buttonMinus = Button(frame1, text="-", height=3, width=5, command=subtract)
        buttonMinus.grid(row=7, column=3)

        button1 = Button(frame1, text="1", height=3, width=5, command=lambda: buttonClick(1))
        button1.grid(row=8, column=0)

        button2 = Button(frame1, text="2", height=3, width=5, command=lambda: buttonClick(2))
        button2.grid(row=8, column=1)

        button3 = Button(frame1, text="3", height=3, width=5, command=lambda: buttonClick(3))
        button3.grid(row=8, column=2)

        buttonAdd = Button(frame1, text="+", height=3, width=5, command=add)
        buttonAdd.grid(row=8, column=3)

        buttonPlusMinus = Button(frame1, text="+/-", height=3, width=5, command=plusMinus)
        buttonPlusMinus.grid(row=9, column=0)

        buttonZero = Button(frame1, text="0", height=3, width=5, command=lambda: buttonClick(0))
        buttonZero.grid(row=9, column=1)

        buttonDecimal = Button(frame1, text=".", height=3, width=5, command=decimal)
        buttonDecimal.grid(row=9, column=2)

        buttonEquals = Button(frame1, text="=", height=3, width=5, command=equals)
        buttonEquals.grid(row=9, column=3)

        # self.grid_columnconfigure(0, weight=1)
        # self.grid_columnconfigure(1, weight=1)
        # self.grid_columnconfigure(2, weight=1)
        # self.grid_columnconfigure(3, weight=1)
        # self.grid_rowconfigure(0, weight=1)
        # self.grid_rowconfigure(1, weight=1)
        # self.grid_rowconfigure(2, weight=1)
        # self.grid_rowconfigure(3, weight=1)
        # self.grid_rowconfigure(4, weight=1)
        # self.grid_rowconfigure(5, weight=1)
        # self.grid_rowconfigure(6, weight=1)
        # self.grid_rowconfigure(7, weight=1)
        # self.grid_rowconfigure(8, weight=1)


        frame2 = Frame(root, bg="lightgrey", bd=5)
        frame2.place(relx=.5, rely=.1, relwidth=0.40, relheight=0.80)


        def history():
            self.historyclicks += 1
            if self.historyclicks == 1 and self.equalclicks == 0:
                messagebox.showinfo("Error", "You haven't used the calculator yet!")

            if self.historyclicks > self.equalclicks:
                    messagebox.showinfo("Error", "History items requested exceeds number of equations calculated!")
                    self.historyclicks = self.equalclicks

            if self.historyclicks >= 1 and self.historyclicks <= self.equalclicks:
                self.Label1 = Label(frame2, text=self.equation1,
                bg="#80c1ff", fg="navy", width=25, anchor="w")
                self.Label1.place(x=5, y=85)

            if self.historyclicks >= 2 and self.historyclicks <= self.equalclicks:
                self.Label2 = Label(frame2, text=self.equation2,
                bg="#80c1ff", fg="navy", width=25, anchor="w")
                self.Label2.place(x=5, y=125)

            if self.historyclicks >= 3 and self.historyclicks <= self.equalclicks:
                self.Label3 = Label(frame2, text=self.equation3,
                bg="#80c1ff", fg="navy", width=25, anchor="w")
                self.Label3.place(x=5, y=165)

            if self.historyclicks >= 4 and self.historyclicks <= self.equalclicks:
                self.Label4 = Label(frame2, text=self.equation4,
                bg="#80c1ff", fg="navy", width=25, anchor="w")
                self.Label4.place(x=5, y=205)

            if self.historyclicks >= 5 and self.historyclicks <= self.equalclicks:
                self.Label5 = Label(frame2, text=self.equation5,
                bg="#80c1ff", fg="navy", width=25, anchor="w")
                self.Label5.place(x=5, y=245)

            if self.historyclicks >= 6 and self.historyclicks <= self.equalclicks:
                self.Label6 = Label(frame2, text=self.equation6,
                bg="#80c1ff", fg="navy", width=25, anchor="w")
                self.Label6.place(x=5, y=285)

            if self.historyclicks >= 7 and self.historyclicks <= self.equalclicks:
                self.Label7 = Label(frame2, text=self.equation7,
                bg="#80c1ff", fg="navy", width=25, anchor="w")
                self.Label7.place(x=5, y=325)

            if self.historyclicks == 8 and self.historyclicks <= self.equalclicks:
                self.Label8 = Label(frame2, text=self.equation8,
                bg="#80c1ff", fg="navy", width=25, anchor="w")
                self.Label8.place(x=5, y=365)

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

        memoryButton = Button(frame2, text="Memory", bg="#80c1ff", fg="navy", command=memory)
        memoryButton.configure(font=("Verdana", 12))
        memoryButton.place(x=85, y=40)

        self.result = Entry(frame2, width=15, borderwidth=3)
        self.result.configure(font=("Verdana", 14))
        self.result.grid(row=0, column=0, pady=5)

        root.mainloop()


Calculator()

