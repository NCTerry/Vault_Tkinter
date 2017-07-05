
from Tkinter import *
import tkMessageBox

# ==Random Bezier Start =============================================================
# ==Random Bezier Start =============================================================
# ==Random Bezier Start =============================================================
# ==Random Bezier Start =============================================================
# ==Random Bezier Start =============================================================
# ==Random Bezier Start =============================================================
# ==Random Bezier Start =============================================================
# ==Random Bezier Start =============================================================
# ---- Bezier ---------------
import numpy as np
from scipy.misc import comb
from matplotlib import pyplot as plt  # This is for the graph abilities in py 2.7
# ---- Bezier ---------------
def random_Bezier():
# ==Random Bezier Start =============================================================
    numOFpoints = 4  # We want a cubic make sure you include 4 points.
    #  If the user doesn't input points we will create 4 randoms --> (x,y)
    ''' np = numpy import
    Three-by-two array of random numbers from [100, 100):

    >>>
    >>> np.random.random_sample((4, 2)) * 100

    randomPoints =  [[ 51.00560787  32.6507618 ]
                     [ 42.09595555  52.35276752]
                     [ 22.12235427   4.37116838]
                     [ 64.23212466  36.31339936]]
       '''
    # tkMessageBox.showinfo("Do you want 4 random points?", radioValue)

    # =================================================
    # =================================================
    # This is for a random selection
    # We will keep our graph expansion to 100
    randomPoints = np.random.rand(numOFpoints, 2) * 100
    # print 'randomPoints = ', randomPoints
    # =================================================
    # =================================================

    # Make sure that we distinguish our points after each selections
    # List of x-points to match the list of y-points
    xpoint = [p[0] for p in randomPoints]
    ypoint = [p[1] for p in randomPoints]

    # ========================================================
    # ========================================================
    # ========================================================
    # Now we have to create the bezier curve
    # The second value will be the number of points we are creating on our final graph
    # The more, the smoother the graph interp will be.
    # This is set to 100 final points, but we should give the user a choice for line smoothness.
    # xvalue, yvalue = bezier_curve(randomPoints, 100)
    """
       Given a set of control points, return the
       bezier curve defined by the control points.

       points should be a list of lists, or list of tuples
       such as [ [1,1],
                 [2,3],
                 [4,5], ..[Xn, Yn] ]
        nTimes is the number of time steps, defaults to 1000

    """
    numInterpPoints = 100

    nPoints = len(randomPoints)
    xPoints = np.array([p[0] for p in randomPoints])
    yPoints = np.array([p[1] for p in randomPoints])

    t = np.linspace(0.0, 1.0, numInterpPoints)

    polynomial_array = np.array(
        [comb(nPoints - 1, i) * (t ** (nPoints - 1 - i)) * (1 - t) ** i for i in range(0, nPoints)])

    xvals = np.dot(xPoints, polynomial_array)
    yvals = np.dot(yPoints, polynomial_array)

    # ========================================================
    # ========================================================
    # ========================================================

    plt.plot(xvals, yvals)
    # Remem. rs is the graph--> redline, squarepoints
    # This is for our 4point graph.
    plt.plot(xpoint, ypoint, "rs")

    # Our basic set for range will be just 4 points.
    for num in range(len(randomPoints)):
        # Used this plot format
        # matplotlib.pyplot.text(x, y, s, fontdict=None, withdash=False, **kwargs)
        # http://matplotlib.org/api/pyplot_api.html
        # We want ot stick a text-number on each point on the group for display
        plt.text(randomPoints[num][0], randomPoints[num][1], num)
        # kwargs : Text properties.

    plt.show()
# ==Random Bezier Function End ==================================================
# ==Random Bezier Function End ==================================================
# ==Random Bezier Function End ==================================================
# ==Random Bezier Function End ==================================================
# ==Random Bezier Function End ==================================================
# ===============================================================================
# ==User Input Bezier Function Start ==================================================
# ==User Input Bezier Function Start ==================================================
# ==User Input Bezier Function Start ==================================================
# ==User Input Bezier Function Start ==================================================
# ==User Input Bezier Function Start ==================================================
def user_Input_Bezier():

    numOFpoints = 4  # We want a cubic make sure you include 4 points.
    numInterpPoints = 10

    #  If the user doesn't input points we will create 4 randoms --> (x,y)
    ''' np = numpy import
    Three-by-two array of random numbers from [100, 100):
    >>> np.random.random_sample((4, 2)) * 100

    randomPoints =  [[ 51.00560787  32.6507618 ]
                     [ 42.09595555  52.35276752]
                     [ 22.12235427   4.37116838]
                     [ 64.23212466  36.31339936]]
       '''
    # =================================================
    # =================================================
    # This is for a user selection

    print randomPoints
    print 'length = ', len(randomPoints) # Just for show, this is 4
    print randomPoints[2,1] # 3rd element, y-coordinate

    pointLabel1x.set('Point 1           [X]')
    pointLabel2x.set('Point 2           [X]')
    pointLabel3x.set('Point 3           [X]')
    pointLabel4x.set('Point 4           [X]')
    # ---------------------------------
    pointLabel1y.set('[Y]')
    pointLabel2y.set('[Y]')
    pointLabel3y.set('[Y]')
    pointLabel4y.set('[Y]')

    smoothLabel.set('# of User Inter Points?')
    instructionLabel.set('Use only whole numbers.')

    randomPoints[0,0] = x1_Entry.get()
    randomPoints[0,1] = y1_Entry.get()
    randomPoints[1,0] = x2_Entry.get()
    randomPoints[1,1] = y2_Entry.get()
    randomPoints[2,0] = x3_Entry.get()
    randomPoints[2,1] = y3_Entry.get()
    randomPoints[3,0] = x4_Entry.get()
    randomPoints[3,1] = y4_Entry.get()

    numInterpPoints = smoothInput_Entry.get()

    # Make sure that we distinguish our points after each selections
    # List of x-points to match the list of y-points
    xpoint = [p[0] for p in randomPoints]
    ypoint = [p[1] for p in randomPoints]

    # ========================================================
    # ========================================================
    # ========================================================
    # Now we have to create the bezier curve
    # The second value will be the number of points we are creating on our final graph
    # The more, the smoother the graph interp will be.
    # This is set to 100 final points, but we should give the user a choice for line smoothness.
    # xvalue, yvalue = bezier_curve(randomPoints, 100)
    """
       Given a set of control points, return the
       bezier curve defined by the control points.

       points should be a list of lists, or list of tuples
       such as [ [1,1],
                 [2,3],
                 [4,5], ..[Xn, Yn] ]
        nTimes is the number of time steps, defaults to 1000

    """

    nPoints = len(randomPoints)
    xPoints = np.array([p[0] for p in randomPoints])
    yPoints = np.array([p[1] for p in randomPoints])

    t = np.linspace(0.0, 1.0, numInterpPoints)

    polynomial_array = np.array(
        [comb(nPoints - 1, i) * (t ** (nPoints - 1 - i)) * (1 - t) ** i for i in range(0, nPoints)])

    xvals = np.dot(xPoints, polynomial_array)
    yvals = np.dot(yPoints, polynomial_array)

    # ========================================================
    # ========================================================
    # ========================================================

    plt.plot(xvals-1, yvals-1)
    # Remem. rs is the graph--> redline, squarepoints
    # This is for our 4point graph.
    plt.plot(xpoint, ypoint, "rs")

    # Our basic set for range will be just 4 points.
    for num in range(len(randomPoints)):
        # Used this plot format
        # matplotlib.pyplot.text(x, y, s, fontdict=None, withdash=False, **kwargs)
        # http://matplotlib.org/api/pyplot_api.html
        # We want ot stick a text-number on each point on the group for display
        plt.text(randomPoints[num][0], randomPoints[num][1], num)
        # kwargs : Text properties.

    plt.show()
    # String variable to be used for a labels.

# ==User Input Bezier Function End ==================================================
# ==User Input Bezier Function End ==================================================
# ==User Input Bezier Function End ==================================================
# ==User Input Bezier Function End ==================================================
# ==User Input Bezier Function End ==================================================
# ==User Input Bezier Function End ==================================================
# ==User Input Bezier Function End ==================================================
# ==User Input Bezier Function End ==================================================
# ==User Input Bezier Function End ==================================================
# ==User Input Bezier Function End ==================================================
def aboutMe():
    pass

def openFiles():
    pass

def saveResults():
    pass


# Create the app itself, add the app title, create the window size.
app = Tk()
app.title('Project 2.1')
app.geometry('800x500+200+200')


randomPoints = np.array([[0, 0], [1, 1], [2, 6], [3, 3]])
# ------------------------
# CREATION SECTION
# LABELS
pointLabel1x = StringVar()
pointLabel2x = StringVar()
pointLabel3x = StringVar()
pointLabel4x = StringVar()
# ------------------------
pointLabel1y = StringVar()
pointLabel2y = StringVar()
pointLabel3y = StringVar()
pointLabel4y = StringVar()
xLabel = StringVar()
yLabel = StringVar()
smoothLabel = StringVar()
instructionLabel =StringVar()
# ----------
# ------------------------
label1x = Label(app, textvariable=pointLabel1x, height=1)  # Create a label object
label1x.grid(row=3, column=0, columnspan=1, sticky=W)
# ------------------------
label1y = Label(app, textvariable=pointLabel1y, height=1)  # Create a label object
label1y.grid(row=3, column=3, columnspan=1, sticky=W)
# ------------------------
label2x = Label(app, textvariable=pointLabel2x, height=1)  # Create a label object
label2x.grid(row=4, column=0, sticky=W)
# ------------------------
label2y = Label(app, textvariable=pointLabel2y, height=1)  # Create a label object
label2y.grid(row=4, column=3, columnspan=1, sticky=W)
# ------------------------
label3x = Label(app, textvariable=pointLabel3x, height=1)  # Create a label object
label3x.grid(row=5, column=0, sticky=W)
# ------------------------
label3y = Label(app, textvariable=pointLabel3y, height=1)  # Create a label object
label3y.grid(row=5, column=3, columnspan=1, sticky=W)
# ------------------------
label4x = Label(app, textvariable=pointLabel4x, height=1)  # Create a label object
label4x.grid(row=6, column=0, sticky=W)
# ------------------------
label4y = Label(app, textvariable=pointLabel4y, height=1)  # Create a label object
label4y.grid(row=6, column=3, columnspan=1, sticky=W)
# ------------------------
# ------------------------
smoothLabelxxx = Label(app, textvariable=smoothLabel, height=1)
smoothLabelxxx.grid(row=8, column=0, columnspan=1, sticky=W)
# ------------------------
# ------------------------
instructionLabel.set('Choose from the file menu!')
instructionLabelxxx = Label(app, textvariable=instructionLabel, height=1)
instructionLabelxxx.grid(row=1, column=0, columnspan=1, sticky=W)
# ------------------------
# ENTRY BOXES
X1 = StringVar(None)
Y1 = StringVar(None)
X2 = StringVar(None)
Y2 = StringVar(None)
X3 = StringVar(None)
Y3 = StringVar(None)
X4 = StringVar(None)
Y4 = StringVar(None)
smoothInput = StringVar(None)
# ------------------------
x1_Entry = Entry(app, textvariable=X1, width=5)
x1_Entry.grid(row=3, column=1, sticky=W)
# --------
y1_Entry = Entry(app, textvariable=Y1, width=5)
y1_Entry.grid(row=3, column=4, sticky=W)
# --------
x2_Entry = Entry(app, textvariable=X2, width=5)
x2_Entry.grid(row=4, column=1, sticky=W)
# --------
y2_Entry = Entry(app, textvariable=Y2, width=5)
y2_Entry.grid(row=4, column=4, sticky=W)
# --------
x3_Entry = Entry(app, textvariable=X3, width=5)
x3_Entry.grid(row=5, column=1, sticky=W)
# --------
y3_Entry = Entry(app, textvariable=Y3, width=5)
y3_Entry.grid(row=5, column=4, sticky=W)
# --------
x4_Entry = Entry(app, textvariable=X4, width=5)
x4_Entry.grid(row=6, column=1, sticky=W)
# --------
y4_Entry = Entry(app, textvariable=Y4, width=5)
y4_Entry.grid(row=6, column=4, sticky=W)
# --------
# --------
smoothInput_Entry = Entry(app, textvariable=smoothInput, width=10)
smoothInput_Entry.grid(row=9, column=0, sticky=W)
# --------
# We want a menubar
menubar = Menu(app)

# This is the drop-down part of the menu under 'File'
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Bezier Cubic Random", command=random_Bezier)
filemenu.add_command(label="Bezier Cubic User Input", command=user_Input_Bezier)

# When the user clicks on this, it will call in a created function above
#  to open up a file for the random_Bezier.
# ----------------------------
filemenu.add_separator() # This is a simple menu separator for aesthetics.
# ----------------------------
# ----------------------------
filemenu.add_command(label='Quit', command=app.quit)    # Built in quit function.
menubar.add_cascade(label='File', menu=filemenu)        # Make sure that this is
#  the final piece of the file drop down. Do these in sequential order. They are
#  attached to the filemenu object, but this can be misplaced if you do not keep
#  it in order.
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# This is the same as the filemenu. Both are tied to the Menu(menubar assocation.
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_cascade(label='About Me', command=aboutMe)
menubar.add_cascade(label="Help", menu=helpmenu)
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
app.config(menu=menubar) # This is just defining the name for the menubar.
# So we have just built a menubar that should work.
# Remember that we have called menu functions even though we may not have
# created them. If so just make sure to create them with a 'pass'
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# This is to create a multi-line statement about the student.
# Create it, then allow to have any string to be inserted.
# We will start with the opening phrase seen here, but then we will use the top two functions to delete,
#  this and overwrite with the information pulled from the file, line by line.
# Each time, it will delete what is there and overwrite from the remaining file,
# so if you make changes without pressing the save button the changes will be lost.
# NOTE. This is in column 0 but is large so column 1 is pushed out
#aboutStudent = Text(app)
#aboutStudent.insert(END, 'Select a project to run from the file menu')
#aboutStudent.grid( sticky=W)
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

# We will need a button for everything to operate the way we want.
# We have a dropdown that will call in our txt file, and allow you to edit the text in the file.
# The button calls in the function that will overwrite our current file.
button1 = Button(app, text="Save 4 User Points", width=15, command=user_Input_Bezier)
button1.grid(column=10, sticky=W, padx=15, pady=15)




app.mainloop()