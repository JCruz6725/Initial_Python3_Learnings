import tkinter 

##3/14/2018
''' this is a very simple tkinter programm that i made while learnign the tkinter libary'''

def add_b():
	print ('hello tkinter!!')



Main_win = tkinter.Tk()
Main_win.geometry("750x400")

hi = tkinter.Button(Main_win, text = 'Hi', command = add_b)

hi.pack()
Main_win.mainloop()
