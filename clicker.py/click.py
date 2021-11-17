from tkinter import *
import time

master = Tk()

def uiPrint():

    print(click)






click = 0
mult = 1

def blankLine():
    for i in range(20):
        print("")



def buttonCommand():
    global click
    global mult
    click += 1*(mult)
    uiPrint()

    if click == 100:
        print('''You hit 100 clicks! Good job!''')
        
    elif click == 200:
         print('''You hit 200 clicks! Good job!''')

    elif click == 300:
        print ('''You hit 300 clicks! Good job!''')

    elif click == 400:
        print ('''You hit 400 clicks! Good job!''')

    elif click == 500:
        print ('''You hit 500 clicks! Good job!''')

    elif click == 600:
        print ('''You hit 600 clicks! Good job!''')

    elif click == 700:
        print ('''You hit 700 clicks! Good job!''')
   
    elif click == 800:
        print ('''You hit 800 clicks! Good job!''')

    elif click == 900:
        print ('''You hit 900 clicks! Good job!''')

    elif click == 1000:
        print ('''You hit 1000 clicks! Good job! That is the end of me talking. You may keep clicking.''')

mainClickButton = Button(master, text="Click here!", command = buttonCommand)
mainClickButton.pack()



master.title("Clicker! Made by Sathvik. https://sathvik.website")
master.geometry("%sx%s+%s+%s" % (400,70,250,512))
mainloop()