import tkinter as tk
from tkinter import *
import webbrowser
import sqlite3
import os

# connect to database 'pages.db'
conn = sqlite3.connect('pages.db')

# create the "pages_info" table if it doesn't already exist
conn.execute("CREATE TABLE IF NOT EXISTS pages_info(ID INTEGER PRIMARY KEY AUTOINCREMENT, CONTENT TEXT);")

root = tk.Tk()

user_input = tk.StringVar(root)

# function to generate a new html page
def generatePage():
    pick = listbox.get(listbox.curselection())
    with open("index.html", "wt") as out_file:
        out_file.write("<html>\n<body>\n{}\n</body>\n</html>".format(pick))
        messagebox.showinfo("Success", "Web page has been generated.")
        x = os.getcwd()
        filename = 'file://' + x + '/' + 'index.html'
        print(filename)
        webbrowser.open_new_tab(filename)
    
# Update database with current content of text widget
def addPage():
    text = user_input.get()
    conn.execute('INSERT INTO pages_info(CONTENT) VALUES("' + text + '")');
    conn.commit()
    getData()

# Function to retrieve updates from the database and insert them into the listbox
def getData():
    listbox.delete(0, END)
    cursor = conn.execute("SELECT * from pages_info")
    s = cursor.fetchall()
    for i in s:
        listbox.insert(i[0], i[1])



# elements of GUI window
tk.Label(root, text = "Web Page Creator", font = ("Helvetica", 28)).pack()
tk.Label(root, text = "What would you like your new web page to say?", font = ("Helvetica", 16)).pack()
entry = tk.Entry(root, width = 50, textvariable = user_input, font = ("Helvetica", 16))
entry.pack(padx = 5, pady = 10)

addButton = tk.Button(root, text = "Add webpage", font = ("Helvetica", 16), command = addPage)
addButton.pack(padx = 5, pady = 5)

listbox = Listbox(root, width = 50)
listbox.pack(padx = 5, pady = 5)

generateButton = tk.Button(root, text = "Generate web page", font = ("Helvetica", 16), command = generatePage)
generateButton.pack(padx = 5, pady = 5)

root.title("HTML Generator")

root.mainloop()
