import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
import mysql.connector
import menuPage

class VenuePage:
    def __init__(self, window):
        self.window = window
        self.window.title('Venue Page')
        self.window.geometry('1600x700')
        self.window.configure(bg="#262626")
        self.window.resizable(0,0)
        #self.window.state('zoomed')
        

        #----------- please change the password and database when using in personal code -----------------------

        # ------------------- AUTO-WRITE the row data into input box --------------------
        # --- after user double clicks (see line 171 or " listBox.bind('<Double-Button-1>', GetValue) "), it copies and pastes the selected row into the input box ------------
        def GetValue(event):
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            row_id = listBox.selection()[0]
            select = listBox.set(row_id)
            e1.insert(0,select['Venue ID'])
            e2.insert(0,select['Location'])
            e3.insert(0,select['Max Capacity'])
            e4.insert(0,select['Booked'])

        def clearBox():
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)

        #------------ def add() INSERTS new data into the column

        def add():
            venID = e1.get() # get the input 
            locat = e2.get()
            maxCap = e3.get()
            bookED = e4.get()
            mysqldb = mysql.connector.connect(host = "localhost", user = "root", password = "s4nsSQLch3n$o", database = "eveo") # connect the database
            mycursor = mysqldb.cursor()

            try:
                sql = "INSERT INTO  venue (VenueId, location, MaxCapacity, Booked) VALUES (%s, %s, %s, %s)"
                val = (venID, locat, maxCap, bookED)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("Information", "Venue inserted successfully...")
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e1.focus_set()
                
            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()
                messagebox.showinfo("Information", "Invalid input, please try again.")


        #---------- def update() UPDATES the existing data in a column after selecting the desired row--------------

        def update():
            venID = e1.get()
            locat = e2.get()
            maxCap = e3.get()
            bookED = e4.get()
            mysqldb=mysql.connector.connect(host="localhost",user="root",password="s4nsSQLch3n$o",database="eveo")
            mycursor=mysqldb.cursor()
        
            try:
                sql = "Update venue set Location = %s, MaxCapacity = %s, Booked = %s where VenueId = %s"
                val = (locat, venID, maxCap, bookED)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("Information", "Record Updated successfully...")
            
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e1.focus_set()
                
        
            except Exception as e:
        
                print(e)
                mysqldb.rollback()
                mysqldb.close()
                messagebox.showinfo("Information", "Invalid input, please try again.")


        # --------------- def delete() DELETES the selected row of data ------------------


        def delete():
            venID = e1.get()
            locat = e2.get()
            maxCap = e3.get()
            bookED = e4.get()
            mysqldb=mysql.connector.connect(host="localhost",user="root",password="s4nsSQLch3n$o",database="eveo")
            mycursor=mysqldb.cursor()
        
            try:
                sql = "delete from venue where VenueId = %s"
                val = (venID,)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("Information", "Record Deleted successfully...")
            
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e1.focus_set()
            
            except Exception as e:
            
                print(e)
                mysqldb.rollback()
                mysqldb.close()
                messagebox.showinfo("Information", "Invalid input, please try again.")


        #----------- def show() only DISPLAYS the available data from the column [specified in code] into the column/row box in the UI -----------------------

        def show():
                mysqldb = mysql.connector.connect(host="localhost", user="root", password="s4nsSQLch3n$o", database="eveo")
                mycursor = mysqldb.cursor()
                mycursor.execute("SELECT VenueID, Location, MaxCapacity, Booked FROM venue")
                records = mycursor.fetchall()
                print(records)

                for i, (VenueId, Location, MaxCapacity, Booked) in enumerate(records, start=1):
                    listBox.insert("", "end", values=(VenueId, Location, MaxCapacity, Booked))
                    mysqldb.close()

        #-------- function to move to main menu
        def go_pageMenu(): 
            win = Toplevel()
            menuPage.MenuPage(win)
            self.window.withdraw()
            win.deiconify()
            #self.window.destroy()

        #------- function to refresh page
        def refreshing():
            self.window.destroy()
            if __name__ == '__main__':
                venuePage()

 
        # ========================== UI ====================================================


        e1 = ''
        e2 = ''
        e3 = ''
        e4 = ''

        # ------------- set up labels ----------------
        tk.Label(self.window, text = "Venue Record", fg = "white", bg = '#262626', font = ('Microsoft Yahei UI Light', 30, 'bold')).place(x = 80, y = 80)
        
        tk.Label(self.window, text = "Double-click on a desired row to automatically fill the text boxes.",
                 fg = "white", bg = '#262626', font = ('Microsoft Yahei UI Light', 12)).place(x = 80, y = 140)

        tk.Label(self.window, text = "Venue ID", fg = "white", bg = '#262626', font = ('Microsoft Yahei UI Light', 11)).place(x=80, y=290)
        Label(self.window, text =  "Location", fg = "white", bg = '#262626', font = ('Microsoft Yahei UI Light', 11)).place(x = 80, y = 330)
        Label(self.window, text =  "Max Capacity", fg = "white", bg = '#262626', font = ('Microsoft Yahei UI Light', 11)).place(x = 80, y = 370)
        Label(self.window, text =  "Booked", fg = "white", bg = '#262626', font = ('Microsoft Yahei UI Light', 11)).place(x = 80, y = 410)

        # ---------- set up the input box ----------------
        
        # -------------------------
        def on_enterE1(e):
            e1.delete(0, 'end')

        def on_leaveE1(e):
                name = e1.get()
                if name == '':
                    e1.insert(0, 'Enter Venue ID')

        e1 = Entry(self.window, width = 61, border = 0, fg = '#F8F8FF', bg = '#262626', font = ('Microsoft Yahei UI Light', 11), insertbackground = 'white')
        e1.place(x = 210, y = 290)
        e1.insert(0, 'Enter Venue ID')
        e1.bind('<FocusIn>', on_enterE1)
        e1.bind('<FocusOut>', on_leaveE1)
        Frame(self.window, width=491, height=2, bg='white').place(x=210, y=315)

        # -------------------------
        def on_enterE2(e):
            e2.delete(0, 'end')

        def on_leaveE2(e):
                name = e2.get()
                if name == '':
                    e2.insert(0, 'Enter Location')

        e2 = Entry(self.window, width = 61, border = 0, fg = '#F8F8FF', bg = '#262626', font = ('Microsoft Yahei UI Light', 11), insertbackground = 'white')
        e2.place(x = 210, y = 330)
        e2.insert(0, 'Enter Location')
        e2.bind('<FocusIn>', on_enterE2)
        e2.bind('<FocusOut>', on_leaveE2)
        Frame(self.window, width=491, height=2, bg='white').place(x=210, y=355)

        # -------------------------
        def on_enterE3(e):
            e3.delete(0, 'end')

        def on_leaveE3(e):
                name = e3.get()
                if name == '':
                    e3.insert(0, 'Enter Max Capacity')

        e3 = Entry(self.window, width = 61, border = 0, fg = '#F8F8FF', bg = '#262626', font = ('Microsoft Yahei UI Light', 11), insertbackground = 'white')
        e3.place(x = 210, y = 370)
        e3.insert(0, 'Max Capacity')
        e3.bind('<FocusIn>', on_enterE3)
        e3.bind('<FocusOut>', on_leaveE3)
        Frame(self.window, width=491, height=2, bg='white').place(x=210, y=395)

        # -------------------------
        def on_enterE4(e):
            e4.delete(0, 'end')

        def on_leaveE4(e):
                name = e4.get()
                if name == '':
                    e4.insert(0, 'Enter Booked')

        e4 = Entry(self.window, width = 61, border = 0, fg = '#F8F8FF', bg = '#262626', font = ('Microsoft Yahei UI Light', 11), insertbackground = 'white')
        e4.place(x = 210, y = 410)
        e4.insert(0, 'Enter Booked')
        e4.bind('<FocusIn>', on_enterE4)
        e4.bind('<FocusOut>', on_leaveE4)
        Frame(self.window, width=491, height=2, bg='white').place(x=210, y=435)

        #----------- buttons set up ----------------------
        Button(self.window, text = "Add", command = add, height = 1, width = 88, pady = 7, border = 0, bg = '#9A32CD', fg = 'white', font = ('Microsoft Yahei UI Light', 9)).place(x=900, y = 420)
        Button(self.window, text = "Update", command = update, height = 1, width = 88, pady = 7, border = 0, bg = '#9A32CD', fg = 'white', font = ('Microsoft Yahei UI Light', 9)).place(x=900, y = 470)
        Button(self.window, text = "Delete", command = delete, height = 1, width = 88, pady = 7, border = 0, bg = '#9A32CD', fg = 'white', font = ('Microsoft Yahei UI Light', 9)).place(x=900, y = 520)
        Button(self.window, text = "Refresh Page", command = refreshing, height = 1, width = 88, pady = 7, border = 0, bg = '#9A32CD', fg = 'white', font = ('Microsoft Yahei UI Light', 9)).place(x=900, y = 570)
        Button(self.window, text = "Main Menu", command = go_pageMenu, height = 1, width = 88, pady = 7, border = 0, bg = '#9A32CD', fg = 'white', font = ('Microsoft Yahei UI Light', 9)).place(x=900, y = 620)

        Button(self.window, text = "Clear", command = clearBox, height = 1, width = 88, pady = 7, border = 0, bg = '#9A32CD', fg = 'white', font = ('Microsoft Yahei UI Light', 9)).place(x=80, y = 620)


        # ------------------set up the columns/rows box in the UI ---------------------------


        cols = ('Venue ID', 'Location', 'Max Capacity', 'Booked')
        listBox = ttk.Treeview(self.window, columns = cols, show = 'headings')



        #------ editing the look ------
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Treeview', 
                        background = '#454545', 
                        foreground = '#F8F8FF',
                        relief = 'flat', 
                        rowheight = 25,
                        highlightcolor = '#404040',
                        fieldbackground = '#454545',
                        font = ('Microsoft Yahei UI Light', 11),
                        
                        )
        style.configure('Treeview.Heading',
                        background = '#454545',
                        foreground = '#F8F8FF',
                        font = ('Microsoft Yahei UI Light', 11),
                        relief = 'flat'
                        )

        style.map('Treeview',
                    background=[('selected', '#808080')]
                    )
        style.map("Treeview.Heading",
                    background = [('active', '#545454')]
                )

        # style.configure('Vertical.Tscrollbar', 
        #         background = 'black',
        #         bordercolor = 'red',
        #         arrowcolor = 'white'
        #         )

        #------ scrollbar --------
        scrollbarx = Scrollbar(self.window, orient = HORIZONTAL)
        scrollbary = Scrollbar(self.window, orient = VERTICAL)
        listBox.configure(yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        listBox.configure(selectmode="extended")

        scrollbarx.configure(command=listBox.xview)
        scrollbary.configure(command=listBox.yview)

        scrollbarx.place(relx=0.563, rely=0.519, width=600, height=22)
        scrollbary.place(relx=0.939, rely=0.114, width=22, height=304)


        for col in cols:
            listBox.heading(col, text = col)
            listBox.grid(row = 1, column = 3, columnspan = 3, padx=5, pady=5, sticky='nsew')
            listBox.place(relx=0.563, rely=0.114, width=602, height=284)


        # --- run show() ------
        show()
        listBox.bind('<Double-Button-1>', GetValue) # double click one of the rows in the column/row box in UI, run GetValue


def venuePage():
    window = Tk()
    VenuePage(window)
    window.mainloop()

if __name__ == '__main__':
    venuePage()