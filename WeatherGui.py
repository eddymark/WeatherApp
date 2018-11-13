from tkinter import *
from WeatherRequest import WeatherRequest

# created a gui class that passes in a title constructor

# geomerty sets the size of the gui so that when it opens that is the size of it

class GUI:
    def __init__(self, title):
        self.window = Tk()
        self.window.title(title)
        self.window.geometry("600x300+0+0")
        self.request = WeatherRequest()

        # entry gives input text box

        self.e1 = Entry(self.window)
        self.e1.grid(row=0, column=1)

        Label(self.window, text="Zipcode").grid(row=0, column=0)

        button = Button(self.window, text="Print Me", command=self.getUserRequest)

        # had an escape button but it was worthless because i can quit the window
        # escape = Button(self.window, text="quit", command=quit)

        button.grid(row=3, column=0)
        # escape.grid(row=3, column=1)

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

        # seperates the variables

        Label(self.window, text="temperature :").grid(row=5, column=0)
        Label(self.window, text=self.request.get_val("temperature")).grid(row=5, column=1)

        Label(self.window, text="location :").grid(row=6, column=0)
        Label(self.window, text=self.request.get_val("city")).grid(row=6, column=1)

        Label(self.window, text="humidity :").grid(row=7, column=0)
        Label(self.window, text=self.request.get_val("humidity")).grid(row=7, column=1)

        Label(self.window, text="main description :").grid(row=8, column=0)
        Label(self.window, text=self.request.get_val("main_description")).grid(row=8, column=1)

        Label(self.window, text="max temp :").grid(row=9, column=0)
        Label(self.window, text=self.request.get_val("temp_max")).grid(row=9, column=1)

        Label(self.window, text="min temp :").grid(row=10, column=0)
        Label(self.window, text=self.request.get_val("temp_min")).grid(row=10, column=1)

        print(self.request.getData())

    def getZip(self):
        return self.e1.get()
