from time import sleep as Wait

##03/04/2018
'''3/16/2018 i made some minor adjustments to the class name and methode names using universal progrmming standars such as
capital class and lower case methodes names '''
######################################
##CLASS CALC (CALCULATOR) TO CUT CODE AND READABLITIY IN THE MAIN LOOP 
######################################

## class and object practice
class Calc:
	'''Calc Class is a basic calculator for 2 numbers, for number \'A\' and \'B\' '''
	def __init__ (self,A,B):
		self.A = A
		self.B = B


	def add (A, B):
		''' To add a and b '''
		return A+B


	def sub (A, B):
		''' #to subtract a and b '''
		return A-B


	def multi (A, B):
		'''to multiply a and b'''
		return A*B

	def div (A, B):
		''' #to divide a and b. Being that you cannot divide by zero a simple if statements are added to keep user from doing so'''	
		zero_error = 'Error: Cannot divide by zero, try again.'		
		if (A == 0):
			return zero_error
		elif (B == 0):
			return zero_error
		else:
			C = A/B
			return C 


	def ui_a():
		''' Crude User Interface for the calc '''
		print('''
1. To Add 2 numbers
2. To Subtract 2 numbers
3. To Multiply 2 numbers
4. To Divide 2 numbers
5. To Quit''')

	def try_a():
		''' Error if user choses none of the options availible'''
		print ('Try agian. ')

	def ask2 ():
		'''To continue with the idea pf modularity this methode ask for 2 inputs/vairables.The variables are global so that they can be used and/or modifided in other methodes of the class '''
		global user_a  
		global user_b
		user_a = float (input('Enter you first number: '))
		user_b = float (input('Enter you second number: '))

	def debug ():
		''' this is specifically for debugging and an area to add on with out interferring with other sections os the code '''
		print ('Debug (sandbox)')
		

#############################################################################
#			Main Loop 
#############################################################################
# posibly future ideas, to contain all  mainloop code in a methode inside the class 

to_quit = 'n'	#Flag to start or stop the mian loop
while (to_quit.lower() == 'n'):

	Calc.ui_a()
	user = str (input('What to do? '))


	if user == '1':
		Calc.ask2()
		end_user =  Calc.add(user_a, user_b)	
		print ('Your answer is: ',end_user)

	elif user == '2':
		Calc.ask2()
		end_user =  Calc.sub(user_a, user_b)		
		print ('Your answer is: ',end_user)

	elif user == '3':
		Calc.ask2()
		end_user =  Calc.multi(user_a, user_b)		
		print ('Your answer is: ',end_user)

	elif user == '4':
		Calc.ask2()
		end_user =  Calc.div(user_a, user_b)		
		print ('Your answer is: ',end_user)

	elif user == '5':	#this elfi statement is user to exit the entire program
		to_quit = str(input ('Are you sure you want to quit? y/n'))
		to_quit = to_quit.lower()

		'''# debug zone for testing methodes typed on and other things that may be added. uses Db to 
		pull up
		elif user == 'Db':
			Calc.debug()'''

	else:
		Calc.try_a()
		Wait(1) 
	#used to be more visually appealing between iterations and to help keep track of user answer visually with in the terminal.


