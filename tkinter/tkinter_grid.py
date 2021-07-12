import tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

# in-built test
# tkinter._test()

mainWindow = tkinter.Tk()
mainWindow.title("Hello World")
mainWindow.geometry('640x480-8-200')

# top level item
label = tkinter.Label(mainWindow, text="Hello World")
label.grid(row=0, column=0)

# top level item
leftFrame = tkinter.Frame(mainWindow)
leftFrame.grid(row=1, column=1)

canvas = tkinter.Canvas(leftFrame, relief="raised", borderwidth=1)
canvas.grid(row=1, column=0)

# top level item
rightFrame = tkinter.Frame(mainWindow)
rightFrame.grid(row=1, column=2, sticky="n")

button1 = tkinter.Button(rightFrame, text="Button 1")
button2 = tkinter.Button(rightFrame, text="Button 2")
button3 = tkinter.Button(rightFrame, text="Button 3")
button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)

#configure the columns
mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=1)

leftFrame.config(relief="sunken", borderwidth=1)
rightFrame.config(relief="sunken", borderwidth=1)
leftFrame.grid(sticky="ns")
rightFrame.grid(sticky="new")

rightFrame.columnconfigure(0, weight=1)
button2.grid(sticky="ew")  # sticky only works when a weight is assigned to the column

mainWindow.mainloop()  # handover control to the TkInter main loop
