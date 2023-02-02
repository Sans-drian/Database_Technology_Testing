import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
import organizerPage
import customerPage
import venuePage

class MenuPage:
    def __init__(self, window):
        self.window = window
        self.window.title('Menu Page')
        self.window.geometry('1600x700')
        self.window.configure(bg="#262626")
        self.window.resizable(0,0)
        #self.window.state('zoomed')

        def go_pageOrgan(): 
            win = Toplevel()
            organizerPage.OrganizerPage(win)
            self.window.withdraw()
            win.deiconify()

        def go_pageCustomer(): 
            win = Toplevel()
            customerPage.CustomerPage(win)
            self.window.withdraw()
            win.deiconify()

        def go_pageVenue(): 
            win = Toplevel()
            venuePage.VenuePage(win)
            self.window.withdraw()
            win.deiconify()

        tk.Label(self.window, text = "Ticket Management System", fg = "white", bg = '#262626', font = ('Microsoft Yahei UI Light', 30, 'bold')).place(x = 540, y = 80)

        Button(self.window, text = "Customer Record", height = 1, command = go_pageCustomer, width = 88, pady = 7, border = 0, bg = '#9A32CD', fg = 'white', font = ('Microsoft Yahei UI Light', 10)).place(x=450, y = 200)
        Button(self.window, text = "Organizer Record", command = go_pageOrgan, height = 1, width = 88, pady = 7, border = 0, bg = '#9A32CD', fg = 'white', font = ('Microsoft Yahei UI Light', 10)).place(x=450, y = 250)
        Button(self.window, text = "Event Record", height = 1, width = 88, pady = 7, border = 0, bg = '#9A32CD', fg = 'white', font = ('Microsoft Yahei UI Light', 10)).place(x=450, y = 300)
        Button(self.window, text = "Event Booking Record", height = 1, width = 88, pady = 7, border = 0, bg = '#9A32CD', fg = 'white', font = ('Microsoft Yahei UI Light', 10)).place(x=450, y = 350)
        Button(self.window, text = "Ticket Order Record", height = 1, width = 88, pady = 7, border = 0, bg = '#9A32CD', fg = 'white', font = ('Microsoft Yahei UI Light', 10)).place(x=450, y = 400)
        Button(self.window, text = "Venue Record", height = 1, command = go_pageVenue, width = 88, pady = 7, border = 0, bg = '#9A32CD', fg = 'white', font = ('Microsoft Yahei UI Light', 10)).place(x=450, y = 450)

        Button(self.window, text = "Log Out", height = 1, width = 88, pady = 7, border = 0, bg = '#9A32CD', fg = 'white', font = ('Microsoft Yahei UI Light', 10)).place(x=450, y = 550)


def menuPage():
    window = Tk()
    MenuPage(window)
    window.mainloop()

if __name__ == '__main__':
    menuPage()