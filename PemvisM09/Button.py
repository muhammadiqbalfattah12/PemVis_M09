import tkinter 
from tkinter import * 

root = Tk()
frame = Frame(root)
frame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side = BOTTOM)

redButton = Button(frame, text="red", fg="red")
redButton.pack(side=LEFT)

greenButton = Button(frame, text="Brown", fg="brown")
greenButton.pack(side=LEFT)

blueButton = Button(frame, text="Blue", fg="blue")
blueButton.pack(side=LEFT)

blackButton = Button(bottomFrame, text="Black", fg="black")
blackButton.pack(side=BOTTOM)

root.mainloop()
