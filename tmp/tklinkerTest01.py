import cv2
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import Frame
from PIL import ImageTk
from PIL import Image

white 		= "#ffffff"
lightBlue2 	= "#adc5ed"
font 		= "Constantia"
fontButtons = (font, 12)
maxWidth  	= 800
maxHeight 	= 480

#Graphics window
mainWindow = tk.Tk()
mainWindow.configure(bg=lightBlue2)
mainWindow.geometry('%dx%d+%d+%d' % (maxWidth,maxHeight,0,0))
mainWindow.resizable(0,0)
mainWindow.overrideredirect(1)

mainFrame = Frame(mainWindow)
mainFrame.place(x=20, y=20)

#Capture video frames
lmain = tk.Label(mainFrame)
lmain.grid(row=0, column=0)

cap = cv2.VideoCapture('TestMov.mp4')

def show_frame():
	ret, frame = cap.read()

	cv2image   = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

	img   = Image.fromarray(cv2image).resize((760, 400))
	imgtk = ImageTk.PhotoImage(image = img)
	lmain.imgtk = imgtk
	lmain.configure(image=imgtk)
	lmain.after(10, show_frame)

closeButton = Button(mainWindow, text = "CLOSE", font = fontButtons, bg = white, width = 20, height= 1)
closeButton.configure(command=lambda: mainWindow.destroy())
closeButton.place(x=270, y=430)

playButton = Button(mainWindow, text = "Play", font = fontButtons, bg = white, width = 20, height= 1)
playButton.configure(command=show_frame)
playButton.place(x=50, y=430)

# show_frame()  #Display

mainWindow.mainloop()  #Starts GUI

