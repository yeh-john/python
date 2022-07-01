###--- Start import
from tkinter import *
import os
import time


########   Start program    ########

def setTimer():
    if True:
        try:
            # Get value
            videoUrl = str(videoUrl_input.get())
            timer_time = int(time_input.get())

            # Start timer
            minte = 60
            timer = int(minte)*int(timer_time)
            time.sleep(timer)
            video_cmd = "call powershell start "+videoUrl
            os.system(video_cmd)
        except Exception:
            # Print success to set timer
            Label(framel, text="Please enter value!", font=('verdana 13 bold'), fg='red').place(x=160, y=190)


########    Start user interface   ########

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
videoUrl_value = StringVar()
videoUrl_input = Entry(framel, textvariable=videoUrl_value, width=25, relief=RIDGE, border=3, font=('verdana', 13))
videoUrl_input.place(x=150, y=100)

# Set time
time_text = Label(framel, text="Set minutes :", font=("Helvetica 15"))
time_text.place(x=30, y=140)
time_value = StringVar()
time_input = Entry(framel, textvariable=time_value, width=7, relief=RIDGE, border=3, font=("verdana", 13))
time_input.place(x=160, y=140)

# Start timer button
start_btn = Button(framel, command=setTimer, text="Start", relief=RAISED, borderwidth=2, font=('verdana', 10, 'bold'), bg="#5DADE2", fg="#17202A", cursor="hand2")
start_btn.place(x=220, y=230)

root.mainloop() 
