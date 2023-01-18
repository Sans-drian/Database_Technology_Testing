import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
import mysql.connector


#================= THE CURRENT CODE ONLY EDITS THE 'customer' TABLE =========================
#----------- please change the password and database when using in personal code -----------------------


# ------------------- AUTO-WRITE the row data into input box --------------------
# --- after user double clicks (see line 171 or " listBox.bind('<Double-Button-1>', GetValue) "), it copies and pastes the selected row into the input box ------------
def GetValue(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0,select['Customer ID'])
    e2.insert(0,select['Full Name'])
    e3.insert(0,select['Tickets'])

#------------ def add() INSERTS new data into the column

def add():
    cusId = e1.get() # get the input 
    cusFName = e2.get()
    cusTick = e3.get()
    mysqldb = mysql.connector.connect(host = "localhost", user = "root", password = "s4nsSQLch3n$o", database = "eveo") # connect the database
    mycursor = mysqldb.cursor()

    try:
       sql = "INSERT INTO  customer (id, full_name, tickets) VALUES (%s, %s, %s)"
       val = (cusId, cusFName, cusTick)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Customer inserted successfully...")
       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e1.focus_set()
    except Exception as e:
       print(e)
       mysqldb.rollback()
       mysqldb.close()


#---------- def update() UPDATES the existing data in a column after selecting the desired row--------------

def update():
    cusId = e1.get()
    cusFName = e2.get()
    cusTick = e3.get()
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="s4nsSQLch3n$o",database="eveo")
    mycursor=mysqldb.cursor()
 
    try:
       sql = "Update customer set full_name = %s, tickets = %s where id = %s"
       val = (cusFName, cusTick, cusId)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Record Updated successfully...")
 
       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e1.focus_set()
 
    except Exception as e:
 
       print(e)
       mysqldb.rollback()
       mysqldb.close()


# --------------- def delete() DELETES the selected row of data ------------------


def delete():
    cusId = e1.get()
    #cusFName = e2.get()
    #cusTick = e3.get()
 
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="s4nsSQLch3n$o",database="eveo")
    mycursor=mysqldb.cursor()
 
    try:
       sql = "delete from customer where id = %s"
       val = (cusId,)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Record Deleted successfully...")
 
       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e1.focus_set()
 
    except Exception as e:
 
       print(e)
       mysqldb.rollback()
       mysqldb.close()


#----------- def show() only DISPLAYS the available data from the column [specified in code] into the column/row box in the UI -----------------------

def show():
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="s4nsSQLch3n$o", database="eveo")
        mycursor = mysqldb.cursor()
        mycursor.execute("SELECT id,full_name,tickets FROM customer")
        records = mycursor.fetchall()
        print(records)
 
        for i, (id, full_name, tickets) in enumerate(records, start=1):
            listBox.insert("", "end", values=(id, full_name, tickets))
            mysqldb.close()


# ======================= SETTING UP THE UI ======================================


root = Tk()
root.geometry("1000x500")
#global e1
#global e2
#global e3
e1 = ''
e2 = ''
e3 = ''

# ------------- set up labels ----------------
tk.Label(root, text = "Ticket Management System", fg = "black", font = (None, 30)).place(x = 400, y = 5)

tk.Label(root, text = "Customer ID").place(x=10, y=10)
Label(root, text =  "Full Name").place(x = 10, y = 40)
Label(root, text = "Tickets").place(x = 10, y = 70)

# ---------- set up the input box ----------------
e1 = Entry(root)
e1.place(x = 140, y = 10)

e2 = Entry(root)
e2.place(x = 140, y = 40)

e3 = Entry(root)
e3.place(x = 140, y = 70)


#----------- buttons set up ----------------------
Button(root, text = "Add", command = add, height = 3, width = 13).place(x=30, y = 130)
Button(root, text = "Update", command = update, height = 3, width = 13).place(x=140, y = 130)
Button(root, text = "Delete", command = delete, height = 3, width = 13).place(x=250, y = 130)


# ------------------set up the columns/rows box in the UI ---------------------------
cols = ('Customer ID', 'Full Name', 'Tickets')
listBox = ttk.Treeview(root, columns = cols, show = 'headings')

for col in cols:
    listBox.heading(col, text = col)
    listBox.grid(row = 1, column = 0, columnspan = 2)
    listBox.place(x = 10, y = 200)


# --- run show() ------
show()
listBox.bind('<Double-Button-1>', GetValue) # double click one of the rows in the column/row box in UI, run GetValue

# --- run the code ---------
root.mainloop()