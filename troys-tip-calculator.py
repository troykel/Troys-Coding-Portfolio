This program is a MODIFICATION of ANOTHER PROGRAM I found on the Internet.  The original
program did not include a tax component, which I felt was not realistic, so I added
that. The original program's tip options stopped at 20%, so I increased that up to
50%, for those people feeling extra generous.  The original program lacked any styling
options, which I added.  I made the fonts larger for those people that are visually
impaired like myself. I made the height of the window resizeable, for those people
who never tip more than 10-18%. The width is fixed."""

"""Originally I kept getting persistent ValueErrors ("Cannot convert string to float"),
which I spent HOURS off-on, trying to solve.  Eventually, with the help of print state-
ments, I realized that taxpercent = float(self.tax_percent.get() was resulting in 
('9.25',), which of course could not be converted to a float. I kept asking myself, "Why
is there a comma there?? pre_tip = float(self.meal_cost.get()) was written in EXACTLY the
same way, BUT was being successfully converted to a float.  Why was that??

I kept looking at every possible similarity, difference between the 2, hoping I would find 
some clue as to why float(self.tax_percent.get() was failing to convert to a float, and was 
being written as ('9.25',), for some reason.  Then it occurred to me:  
float(self.tax_percent.get() was being used on not 1, but 2 different widgets, and was being 
used to update them both simultaneously with not 2 separate functions, or 2 separate variables, 
but 1! The float(self.tax_percent.get() is grabbing BOTH values at once, putting them into a tuple
('9.25', '9.25'), and THEN trying to convert that into a float! That's why the conversion kept 
failing and the ValueErrors kept coming up!! Once I separated the 2 widgets with 2 separate 
variables the conversions to float were successful, and the ValueErrors stopped. Now, the only
reason the ValueErrors occurr, is if the user hits the calculate buttons, without having entered 
any tax or tip information beforehand."""

from tkinter import ttk
from tkinter import *
from tkinter.ttk import *


class TipCalculator(ttk.Frame):
    def __init__(self):

        troys_window = Tk()
        troys_window.geometry("875x250")
        troys_window.resizable(width=False, height=True)
        troys_window.title("Troy's Tip Calculator")

        self.meal_cost = StringVar()
        self.tax_percent = StringVar()
        self.txTotal = StringVar()
        self.tip_percent = IntVar()
        self.tip = StringVar()
        self.total_cost = StringVar()

        style = ttk.Style()
        style.configure("TRadiobutton", font=("Verdana", 12))
        style.configure("TEntry", fg='#00ffff', bg="cyan", font=("Verdana", 12, "bold"))
        style.configure("TButton", fg='#00ffff', font=("Verdana", 12))
        style.configure("TListbox", bg="#808000", fg='#00ffff', bd=4, font=("Verdana", 12))
        style.configure("TLabel", fg='#00ffff', font=("Verdana", 12))
        style.map("C.TButton",
                  foreground=[('pressed', '#843179'), ('active', 'navy')],
                  background=[('pressed', "disabled", 'purple'), ('active', '#008B8B')]
                  )

        tip_amounts = ttk.Label(text="Tip Percentage")
        tip_amounts.grid(column=1, row=1)
        ten_percent_tip = ttk.Radiobutton(text="10%", variable=self.tip_percent, value=10)
        ten_percent_tip.grid(column=1, row=2)
        fifteen_percent_tip = ttk.Radiobutton(text="15%", variable=self.tip_percent, value=15)
        fifteen_percent_tip.grid(column=1, row=3)
        eighteen_percent_tip = ttk.Radiobutton(text="18%", variable=self.tip_percent, value=18)
        eighteen_percent_tip.grid(column=1, row=4)
        twenty_percent_tip = ttk.Radiobutton(text="20%", variable=self.tip_percent, value=20)
        twenty_percent_tip.grid(column=1, row=5)
        twenty_five_percent_tip = ttk.Radiobutton(text="25%", variable=self.tip_percent, value=25)
        twenty_five_percent_tip.grid(column=1, row=6)
        thirty_percent_tip = ttk.Radiobutton(text="30%", variable=self.tip_percent, value=30)
        thirty_percent_tip.grid(column=1, row=7)
        forty_percent_tip = ttk.Radiobutton(text="40%", variable=self.tip_percent, value=40)
        forty_percent_tip.grid(column=1, row=8)
        fifty_percent_tip = ttk.Radiobutton(text="50%", variable=self.tip_percent, value=50)
        fifty_percent_tip.grid(column=1, row=9)

        bill_amount_label = ttk.Label(text="Bill Amount")
        bill_amount_label.grid(column=2, row=1)
        bill_amount_entry = ttk.Entry(textvariable=self.meal_cost, width=7, justify=RIGHT)
        bill_amount_entry.configure(font=("Arial Rounded", 14))
        bill_amount_entry.grid(column=2, row=2)

        tax_amount_label = ttk.Label(text="Tax % Rate: ")
        tax_amount_label.grid(column=3, row=1)
        tax_amount_entry = ttk.Entry(textvariable=self.tax_percent, width=7, justify=RIGHT)
        tax_amount_entry.configure(font=("Arial Rounded", 14))
        tax_amount_entry.grid(column=3, row=2)

        calculate_tax = ttk.Button(text="Calculate Total Tax", style="C.TButton", command=self.calculate_tax)
        calculate_tax.grid(column=6, row=3)

        tax_amount_label = ttk.Label(text="Tax = ")
        tax_amount_label.grid(column=6, row=4)
        tax_amount_lb = Listbox(listvariable=self.txTotal, height=1, width=7, justify=RIGHT)
        tax_amount_lb.configure(font=("Arial Rounded", 14))
        tax_amount_lb.grid(column=7, row=4)

        calculate_tip = ttk.Button(text="Calculate Tip", style="C.TButton", command=self.calculate_tip)
        calculate_tip.grid(column=6, row=1)

        tip_amount_label = Label(text="Tip = ")
        tip_amount_label.grid(column=6, row=2)
        tip_amount_lb = Listbox(listvariable=self.tip, height=1, width=7, justify=RIGHT)
        tip_amount_lb.configure(font=("Arial Rounded", 14))
        tip_amount_lb.grid(column=7, row=2)

        calc_bill_total = ttk.Button(text="Calculate Bill Total: ", style="C.TButton", command=self.calculate_total_bill)
        calc_bill_total.grid(column=8, row=1)

        bill_total_label = Label(text="Total: ", width=7, justify=RIGHT)
        bill_total_label.grid(column=8, row=2)
        bill_total_lb = Listbox(listvariable=self.total_cost, height=1, width=7, justify=RIGHT)
        bill_total_lb.configure(font=("Arial Rounded", 14))
        bill_total_lb.grid(column=9, row=2)

        troys_window.mainloop()

    def calculate_tax(self):
        try:
            while True:
                if self.meal_cost == "" or self.tax_percent == "":
                    #Without the next line I got an error: "Unresolved Reference"(calculate_tax)
                    #The absence of a grid statement makes it so the button doesn't actually show.
                    calculate_tax = ttk.Button(text="Calculate Total Tax", style="C.TButton")
                    calculate_tax.configure(state=DISABLED)
                else:
                    pre_tip = float(self.meal_cost.get())
                    taxpercent = float(self.tax_percent.get()) / 100
                    total_tax = round(pre_tip * taxpercent, 2)
                    self.txTotal.set(total_tax)
                    break

        except ValueError:
            # Value error may occur when get() grabs an empty string.(Nothing has been entered yet)
            troys_window = Tk()
            troys_window.title("OOPS!")
            no_tax_info = ttk.Label(troys_window, text="No tax info entered", padding=20)
            no_tax_info.configure(font=("Arial Rounded", 16))
            no_tax_info.grid(column=2, row=5)

    def calculate_tip(self):
        try:
            while True:
                if self.tip_percent == "" or self.meal_cost == "":
                    #Without the next line I got an error: "Unresolved Reference"(calculator_tip)
                    #The absence of a grid statement makes it so the button doesn't actually show.
                    calculate_tip = ttk.Button(text="Calculate Tip", style="C.TButton")
                    calculate_tip.configure(state=DISABLED)
                else:
                    pre_tip = float(self.meal_cost.get())
                    tipPercentage = self.tip_percent.get() / 100
                    tip_amount = round(pre_tip * tipPercentage, 2)
                    self.tip.set(tip_amount)
                    break

        except ValueError:
            #Value error may occur when get() grabs an empty string.(Nothing has been entered yet)
            troys_window = Tk()
            troys_window.title("OOPS!")
            no_tip_info = ttk.Label(troys_window, text="No tip info entered", padding=20)
            no_tip_info.configure(font=("Arial Rounded", 16))
            no_tip_info.grid(column=2, row=5)

    def calculate_total_bill(self):
        try:
            while True:
                if self.meal_cost == "" or self.tip_percent == "" or self.tax_percent == "":
                    # Without the next line I got an error: "Unresolved Reference"(calc_bill_total)
                    # The absence of a grid statement makes it so the button doesn't actually show.
                    calc_bill_total = ttk.Button(text="Calculate Bill Total: ", style="C.TButton")
                    calc_bill_total.configure(state=DISABLED)
                else:
                    pre_tip = float(self.meal_cost.get())
                    taxpercentage = float(self.tax_percent.get()) / 100
                    tippercentage = self.tip_percent.get() / 100
                    total_tip = round(pre_tip * tippercentage, 2)
                    bill_total = round(pre_tip * (1 + taxpercentage) + total_tip, 2)
                    self.total_cost.set(bill_total)
                    break

        except ValueError:
            # Value error may occur when get() grabs an empty string.(Nothing has been entered yet)
            troys_window = Tk()
            troys_window.title("OOPS!")
            no_inputs = ttk.Label(troys_window, text="Required tax / tip inputs are missing", padding=20)
            no_inputs.configure(font=("Arial Rounded", 16))
            no_inputs.grid(column=6, row=5)


TipCalculator()
