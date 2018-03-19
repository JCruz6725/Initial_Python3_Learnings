#3/19/2018
from tkinter import Tk as new_win
from tkinter import *
import random

def magic ():
	a = random.randint(0, 2)
	if (a == 0):
		print ('yes')
	
	elif (a == 1):
		print ('no')
	
	else:
		print ('maybe')
	Ask.delete()
	
		
from tkinter import Tk as new_win
name = 'Magic8'
#size = '400x400'



Main_win = new_win()
#Main_win.geometry(size)
Main_win.title(name)

Question = Label(Main_win, text = 'What will you ask the magic8?')
Ask = Entry(Main_win)


Close = Button(Main_win, text = 'Close', command = Main_win.quit )
Close.place(x= 320, y= 350)

Fortune = Button(Main_win, text = 'Fortune', command = magic)

Question.grid(row = 0, column = 1)
Fortune.grid(row = 1 ,column = 0)
Ask.grid(row = 1, column = 1)
Close.grid(row = 2, column = 2)



Main_win.mainloop()
 



