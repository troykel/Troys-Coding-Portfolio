import requests
from tkinter import Tk, Canvas, Frame, Label, Button, Entry, Text, INSERT, END
from tkinter import ttk
import sys

window = Tk()
window.title("Outbound Estimated Times of Departure for San Leandro, CA - by Troy Kelley")
window.geometry("860x430")

canvas = Canvas(width=600, height=250)
canvas.grid(row=2, column=0, columnspan=2, pady=50)

frame = Frame(window, bg="lavender", highlightcolor="navy")
frame.place(x=305, y=45, width=525, height=375)

title = Label(window, text="Bart ETD's for San Leandro, CA",
                      width=50, bg="lavender", fg="navy", font=("Arial", 20, "bold"))
# place of the title
title.place(x=0, y=2)

begin = Label(window, text="From: ", width=7, bg="white", fg="navy", font=("Arial", 16, "bold"))

begin.place(x=0, y=50)

hometown = Entry(window, width=15, bg="lavender", fg="navy", font=("Arial", 16, "bold"))

# place of the home
hometown.place(x=95, y=50)

end = Label(window, text="To: ", width=5, bg="white", fg="navy", font=("Arial", 16, "bold"))

end.place(x=0, y=100)


destination = Entry(window, width=15, bg="lavender", fg="navy", font=("Arial", 16, "bold"))
destination.config(state="normal")
# place the destination
destination.place(x=95, y=100)

textbox = Text(frame, bg="lavender", fg="navy", font=("Arial", 10, "bold"))
textbox.config(state="normal")
textbox.place(x=2, y=1)

etd_button = Button(window, text="Get ETD Info", font=("Arial", 14, "bold"), bg="navy", fg="white", \
                    command=lambda: api_response())
etd_button.place(x=20, y=150)


def reset():
    textbox.delete("1.0", END)
    destination.delete(0, END)

clear = Button(window, text="Clear", bg="navy", fg="white", font=("Arial", 14, "bold"), command=lambda: reset())
clear.place(x=212, y=150)

vlist = ["'12th' = 12th St. Oakland City Center",
         "'16th' = 16th St. Mission (SF)",
         "'19th' = 19th St. Oakland",
         "'24th' = 24th St. Mission (SF)",
         "'ashb' = Ashby (Berkeley)",
         "'antc' = Antioch",
         "'balb' = Balboa Park (SF)",
         "'bayf' = Bay Fair (San Leandro)",
         "'bery' = Berryessa",
         "'cast' = Castro Valley",
         "'civc' = Civic Center (SF)",
         "'cols' = Coliseum",
         "'colm' = Colma",
         "'conc' = Concord",
         "'daly' = Daly City",
         "'dbrk' = Downtown Berkeley",
         "'dubl' = Dublin/Pleasanton",
         "'deln' = El Cerrito Del Norte",
         "'plza' = El Cerrito Plaza",
         "'embr' = Embarcadero",
         "'frmt' = Fremont",
         "'frtv' = Fruitvale (Oakland)",
         "'glen' = Glen Park (SF)",
         "'hayw' = Hayward",
         "'lafy' = Lafayette",
         "'lake' = Lake Merritt (Oakland)",
         "'mcar' = MacArthur (Oakland)",
         "'mlbr' = Millbrae",
         "'mlpt' = Milpitas",
         "'mont' = Montgomery St. (SF)",
         "'nbrk' = North Berkeley",
         "'ncon' = North Concord/Martinez",
         "'oakl' = Oakland Int'l Airport",
         "'orin' = Orinda",
         "'pitt' = Pittsburg/Bay Point",
         "'pctr' = Pittsburg Center",
         "'phil' = Pleasant Hill",
         "'powl' = Powell St. (SF)",
         "'rich' = Richmond",
         "'rock' = Rockridge",
         "'sbrn' = San Bruno",
         "'sfia' = San Francisco Int'l Airport",
         "'sanl' = San Leandro",
         "'shay' = South Hayward",
         "'ssan' = South San Francisco",
         "'ucty' = Union City",
         "'warm' = Warm Springs/South Fremont",
         "'wcrk' = Walnut Creek",
         "'wdub' = West Dublin",
         "'woak' = West Oakland"
         ]

Combo = ttk.Combobox(window, font=("Arial", 10), width=35,  values=vlist)
Combo.set("NOTE: Use Station Abbreviations")
Combo.place(x=20, y=200)


def redirector(input_string):
    textbox.insert(INSERT, input_string)


def api_response():
    try:
        antc = ['rock', 'orin', 'lafy', 'wcrk', 'phil', 'conc', 'ncon', 'pitt', 'pctr', 'antc']
        bery = ['sanl','bayf', 'hayw', 'shay', 'frmt', 'warm', 'mlpt', 'bery']
        daly = ['cols', 'frtv', 'lake', 'woak', 'embr', 'mont', 'powl', 'civc', '16th', '24th', 'glen',
                'balb', 'colm', 'daly', 'mlbr']
        rich = ['12th', '19th', 'mcar', 'ashb', 'dbrk', 'nbrk', 'plza', 'deln', 'rich']
        trivalley = ['cast', 'wdub', 'dubl']

        destined = destination.get()
        params_s = {
            'cmd': 'etd',
            'orig': hometown.get(),
            'destination': destination.get(),
            'dir': 's',
            'json': 'y',
            'key': 'QK2V-PUHP-9GRT-DWEI'}

        if destined in bery:
            s = requests.get("https://api.bart.gov/api/etd.aspx", params_s)

            bart_times = s.json()
            #print("\n", bart_times, "\n")
            home = hometown.get()
            destined = destination.get()
            mylist = ["minutes", "platform", "length", "bikeflag", "delay"]

            print(f"{bart_times['root']['station'][0]['etd'][0]['destination'].upper()}-BOUND TRAIN: ")

            for dictionary in bart_times['root']['station'][0]['etd'][0]['estimate'][0:3]:
                print("\n", "*" * 65)
                print("FINAL STOP: BERRYESSA STATION (Near San Jose)")
                print(f"From: {home} To: {destined}")
                print("*" * 65)
                for key, value in dictionary.items():
                    if key in mylist:
                        print(f"\t {key}:{value}")
            print("\n")

        if destined in trivalley:
            s = requests.get("https://api.bart.gov/api/etd.aspx", params_s)

            bart_times = s.json()
            # To check to see if the printout below is correct:
            # print("\n", bart_times, "\n")
            home = hometown.get()
            destined = destination.get()
            mylist = ["destination", "minutes", "platform", "length", "bikeflag", "delay"]

            print(f"{bart_times['root']['station'][0]['etd'][1]['destination'].upper()}-BOUND TRAIN: ")

            for dictionary in bart_times['root']['station'][0]['etd'][1]['estimate'][0:3]:
                print("\n", "*" * 50)
                print("FINAL STOP: DUBLIN/PLEASANTON STATION")
                print(f"From: {home} To: {destined}")
                print("*" * 50)
                for key, value in dictionary.items():
                    if key in mylist:
                        print(f"\t {key}:{value}")
            print("\n")

        params_n = {
            'cmd': 'etd',
            'orig': hometown.get(),
            'destination': destination.get(),
            'dir': 'n',
            'json': 'y',
            'key': 'QK2V-PUHP-9GRT-DWEI'}

        if destined in daly:
            n = requests.get("https://api.bart.gov/api/etd.aspx", params_n)

            bart_times = n.json()
            # To check to see if the printout below is correct:
            # print("\n", bart_times, "\n")
            home = hometown.get()
            destined = destination.get()
            mylist = ["destination", "minutes", "platform", "length", "bikeflag", "delay"]

            print(f"{bart_times['root']['station'][0]['etd'][0]['destination'].upper()}-BOUND TRAIN: ")

            for dictionary in bart_times['root']['station'][0]['etd'][0]['estimate'][0:2]:
                print("\n", "*" * 50)
                print("FINAL STOP: DALY CITY STATION")
                print(f"From: {home} To: {destined}")
                print("*" * 50)
                for key, value in dictionary.items():
                    if key in mylist:
                        print(f"\t {key}:{value}")
            print("\n")

        if destined in rich:
            n = requests.get("https://api.bart.gov/api/etd.aspx", params_n)

            bart_times = n.json()
            # To check to see if the printout below is correct:
            # print("\n", bart_times, "\n")
            home = hometown.get()
            destined = destination.get()
            mylist = ["destination", "minutes", "platform", "length", "bikeflag", "delay"]

            print(f"{bart_times['root']['station'][0]['etd'][1]['destination'].upper()}-BOUND TRAIN")

            for dictionary in bart_times['root']['station'][0]['etd'][1]['estimate'][0:3]:
                print("\n", "*" * 30)
                print(f"FINAL STOP = RICHMOND")
                print(f"From: {home} To: {destined}")
                print("*" * 30)
                for key, value in dictionary.items():
                    if key in mylist:
                        print(f"\t {key}:{value}")
            print("\n")

        if destined in antc:
            n = requests.get("https://api.bart.gov/api/etd.aspx", params_n)

            bart_times = n.json()
            # To check to see if the printout below is correct:
            # print("\n", bart_times, "\n")
            home = hometown.get()
            destined = destination.get()
            mylist = ["minutes", "platform", "length", "bikeflag", "delay"]

            print(f"{bart_times['root']['station'][0]['etd'][1]['destination'].upper()}-BOUND TRAIN")
            print(f"XFER NEEDED to ANTIOCH-BOUND TRAIN")

            for dictionary in bart_times['root']['station'][0]['etd'][1]['estimate'][0:2]:
                print("\n", "*" * 50)
                print(f"XFER NEEDED at: MACARTHUR station")
                print(f"From: {home} To: {destined}")
                print("*" * 50)
                for key, value in dictionary.items():
                    if key in mylist:
                        print(f"\t {key}:{value}")
            print("\n")

    except ConnectionError:
        print("There seems to be a problem retrieving that information from BART")


sys.stdout.write = redirector

window.mainloop()











