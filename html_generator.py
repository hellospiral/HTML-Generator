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


    




# elements of GUI window
tk.Label(root, text = "Web Page Creator", font = ("Helvetica", 28)).pack()
entry = tk.Entry(root, width = 50, textvariable = user_input)
entry.pack(padx = 5, pady = 5)

addButton = tk.Button(root, text = "Add webpage")
addButton.pack(padx = 5, pady = 5)

listbox = Listbox(root, width = 50)
listbox.pack(padx = 5, pady = 5)

generateButton = tk.Button(root, text = "Generate web page")
generateButton.pack(padx = 5, pady = 5)

root.mainloop()