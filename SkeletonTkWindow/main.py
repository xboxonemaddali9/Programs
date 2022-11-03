import tkinter as tk
from tkinter import PhotoImage, ttk
from turtle import title

window = tk.Tk()

# image_frame = PhotoImage(file="/Users/nagamaddali/Desktop/logo.png")
s = ttk.Style()
s.configure("A.TLabel", background="black", foreground="red")

windowFrame = ttk.Frame(window, padding=100, style="A.TLabel")
windowFrame.grid()
ttk.Label(windowFrame, text="Hello world").grid(column=0, row=0)
ttk.Button(windowFrame, text="Quit", command=window.destroy).grid(column=2, row=0)
tk.simpledialog.askstring(title="Cars", prompt="Please enter your name")
window.mainloop()
