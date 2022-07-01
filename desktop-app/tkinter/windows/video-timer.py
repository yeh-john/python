###--- Start import
from cgitb import text
from tkinter import *


###--- Settings
root = Tk()
root.geometry("480x320") # Start window size
root.title("Test") # Application title


###--- Create GUI
framel = Frame(root, width=480, height=320, relief=RIDGE, borderwidth=5)
framel.place(x=0, y=0)


###--- Start content
# header text
Label(root, text="YOUTUBE TIMER", font=("Helvetica 15 bold")).pack(pady=20)

# Description
desc = Label(framel, text="Start set timer to play video.", font=("Helvetica 15"))
desc.place(x=110, y=60)

# Set video link
videoUrl_text = Label(framel, text="Video link :", font=("Helvetica 15"))
videoUrl_text.place(x=30, y=100)
videoUrl_input = Entry(framel, width=25, relief=RIDGE, border=3, font=('verdana', 13))
videoUrl_input.place(x=150, y=100)

root.mainloop()
