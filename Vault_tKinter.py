#step 1 ========================================================================
import sys
from tkinter import *   #import all from tkinter
import os


#  ========================================================================


mGui = Tk() #create an object out of tk
#create a specified size window
mGui.geometry('450x900+200+200')
mGui.title(' Cyber Vault ') # Personal top title bar
ID_Number = StringVar()

# -------------------------------
# 450x450 is the size of the box.
# +300+200 is the position it will appear on the screen.
# From the top left corner, it will appear 300 units to the left, and 200 units down.
# --------------------------------------------------------------------------
# Now if you go to "Run: Run Module", a small empty window box will pop up.
# This empty box will look like this idle window, with a "Tk" on the top bar.

mlabel = Label(text='Let\'s Get Secure', fg='red', bg ='white').pack() # Label that can display text and bitmaps.
# Also could use:   Label.pack()    on this next line.
# ,fg='red'     --> Will change the label text to red.
# ,bg='blue'    --> Change the background behind the red label to blue.
# .pack() will auto place the label at the top and center of the screen.


# Button to ping
line_label = Label(text='====================', fg='blue', bg ='white').pack() # Label that can display text and
# bitmaps.

mEntry = Entry(mGui, textvariable=ID_Number).pack()

IDNumber_But = Button(mGui, text = 'Enter ID Number ', fg ="red", bg ="blue").pack()

# mtext will get() the current value stored in mEnt.
mtext = ID_Number.get()

# create new label. set equal to mtext which just got the user entry.
mlabel2 = Label(mGui, text=mtext).pack()

mGui.mainloop()