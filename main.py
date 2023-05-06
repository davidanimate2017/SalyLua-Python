#---# SALYLUA - i was forced to script python

import tkinter

print("SALYLUA d1.0.0 - Cunnent in DEV.")

def SendPrint(any):
	print(any)

def CreateError(any):
	print("Error: ", any)

def SendWarn(any):
	print("Warn: ", any)

def cat():
	print("Fromofu")

def CreateMath():
	import math
	print("Importing Math!")

	if math:
		print("Imported Math!")

	else:
		print("Failed to Import Math! Code: 175")

def ImportGUI():
	print("Importing Python`s Gui Module")
	import tkinter

	if tkinter:
		print("Imported Module!")
		print("FUN FACT: You can make a gui without ImportGUI.")

	else:
		print("Failed to Import Module! Code: 175")

def CreateGUI():
	import tkinter
	import time
	print("Starting...")
	time.sleep(1)
	m = tkinter.Tk()

	
	m.mainloop()

def MsgWindow(any):
	import tkinter
  
	root = tkinter.Tk()
	root.geometry("500x100")
	frame = tkinter.Frame(root)
	frame.pack()
	root.resizable(0,0)

	  
	def close_window():
		root.destroy()
	  

	  
	label = tkinter.Label(frame, text =any)
	label.pack()


	frame = tkinter.Frame(root)
	frame.pack()
	button = tkinter.Button (frame, text = "Close", command = close_window)
	button.pack()


	  

	  
	root.title(any)
	root.mainloop()

def MsgBoxError(any):
	import ctypes
	ctypes.windll.user32.MessageBoxW(None, any, u"Error", 272)

def MsgBoxWarn(any):
	import ctypes
	ctypes.windll.user32.MessageBoxW(None, any, u"Warn", 304)


def MsgBox(any):
	import ctypes
	ctypes.windll.user32.MessageBoxW(None, any, any, 1)