from tkinter import *
from WeatherRequest import WeatherRequest

class GUI:
    def __init__(self, title):
        self.window = Tk()
        self.window.title(title)
        self.window.geometry("600x300+0+0")
        self.request = WeatherRequest()

        self.e1 = Entry(self.window)
        self.e1.grid(row=0)
        Label(self.window, text="weatherValue").grid(row=1)

        button = Button(self.window, text="Print Me", command=self.getUserRequest)
        escape = Button(self.window, text="Print Me", command=quit)

        button.grid(row=3)
        escape.grid(row=4)

        self.window.mainloop()

    # def printSomething(self):
    #     # if you want the button to disappear:
    #     # button.destroy() or button.pack_forget()
    #     lab = Label(self.window, text=)
    #     lab.grid(row=2)
    #     #this creates a new label to the GUI

    def getUserRequest(self):
        zipcode = self.getZip()

        # makes request
        self.request.makeRequest(zipcode)

        print(self.request.getData())

    def getZip(self):
        return self.e1.get()