from tkinter import *
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="abcde@12345",
    database="batch_2k19")

root=Tk()
root.title("Student Info")
root.iconbitmap('App_icon.ico')
root.geometry("1920x1080")
root.configure(bg='cyan2')

def search_in_database(query):
    mycursor = mydb.cursor()
    mycursor.execute(query)
    return mycursor.fetchall()
    

def find():
    list_box.delete(0,END)
    key = box.get()
    if(len(key) == 8):
            # Search by Student's Roll NO. (Individual Records)
            query = f"Select * from students_info where roll_no = {int(key)}"
            results = search_in_database(query)
            for result in results:
                for item in result:
                    list_box.insert(END, item)
    else:
        # Search by Student's Department (Department-wise Students' Records)
        query = f"Select * from students_info where branch = '{key}'"
        results = search_in_database(query)
        list_box.insert(END, f"Roll No   Name   E-mail ID")
        for result in results:
            data=f"{result[0]} {result[1].upper()} ({result[2]})"
            list_box.insert(END,data)         
        

# App Header or Title
header = Label(root, text='NIT, Jalandhar B.Tech Batch 2k19',bg="cyan4",fg="white",font=("Times", "16", "bold italic"),borderwidth=5, relief=SUNKEN)
header.pack(pady=5)

# Search bar & input frame
input_frame=Frame(root, borderwidth = 5, bg = 'cyan4', relief = SUNKEN, height=20, width=30)
input_frame.pack()

# Search Label, Entry field, & Button
label = Label(input_frame, text='Enter Roll No or Department',bg='black',fg='white',font=("Times", "14", "bold"),borderwidth=5, relief=SUNKEN)
box = Entry(input_frame,font=("Times", "12", "bold"),borderwidth=5, width=30)
button = Button(input_frame, text='Search',bg="black",fg="white",font=("Times", "12", "bold"),borderwidth=5,command=find)

# Position all the elements in the input frame
label.grid(row=0, column=1, padx=10)
box.grid(row=0, column=2, padx=10)
button.grid(row=0, column=3, padx=10)

# List Box to display the search result
list_box= Listbox(root, bg="black", fg="yellow", font=("Times", "12"), borderwidth=5, height = 30 ,width = 175)
list_box.pack(pady=10)

# Copy Right Label
label = Label(root, text='SANJAY KUMAR (C) 2020',bg='cyan2',font=("Times", "12", "bold"),borderwidth=5)
label.pack(pady=5)

root.mainloop()