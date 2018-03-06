from time import sleep as wait

##03/04/2018 
######################################
##CLASS CALC (CALCULATOR) TO CUT CODE AND READABLITIY IN THE MAIN LOOP 
######################################

## class and object practice
class calc:
	def __init__ (self,A,B):
		self.A = A
		self.B = B

	#to add a and b
	def ADD (A, B):
		return A+B

	#to subtract a and b
	def SUB (A, B):
		return A-B

	#to multiply a and b
	def MULTI (A, B):
		return A*B
	
	#to divide a and b
	def DIV (A, B):
	## Being that you cannot divide by zero a simple if stament are added to keep user from doing so	
		zero_error = 'Error: Cannot divide by zero, try again.'		
		if (A == 0):
			return zero_error
		elif (B == 0):
			return zero_error
		else:
			C = A/B
			return C 
	
	#crude UI for the calc
	def UI_A():
	    print('''
1. To Add 2 numbers
2. To Subtract 2 numbers
3. To Multiply 2 numbers
4. To Divide 2 numbers
5. To Quit''')
	
	# Error if user choses none of the options availible
	def TryA():
	    print ('Try agian. ')

	# To cut code in the main loop  a Methode is use to ask for inputs and are global so that they can be 
	# with other methodes
	def ask2 ():
		global user_a
		global user_b
		user_a = float (input('Enter you first number: '))
		user_b = float (input('Enter you second number: '))

	def debug ():
		print ('Debug (sandbox)')
		return 0
	    
#############################################################################
#			Main Loop 
#############################################################################
# posibly future ideas, to contain all  mainloop code in a methode inside the class 

to_quit = 'n'	#Flage to start or stop the mian loop
while (to_quit.lower() == 'n'):

	calc.UI_A()
	user = str (input('What to do? '))


	if user == '1':
		calc.ask2()
		end_user =  calc.ADD(user_a, user_b)	
		print ('Your answer is: ',end_user)

	elif user == '2':
		calc.ask2()
		end_user =  calc.SUB(user_a, user_b)		
		print ('Your answer is: ',end_user)

	elif user == '3':
		calc.ask2()
		end_user =  calc.MULTI(user_a, user_b)		
		print ('Your answer is: ',end_user)

	elif user == '4':
		calc.ask2()
		end_user =  calc.DIV(user_a, user_b)		
		print ('Your answer is: ',end_user)

	elif user == '5':
		to_quit = str(input ('Are you sure you want to quit? y/n'))
		to_quit = to_quit.lower()
	
		'''# debug zone for testing methodes typed on and other things that may be added. uses 6 to 
			pull up
	elif user == 'Db':
		calc.debug()
		'''
	else:
		calc.TryA()
	wait(1) #used to me more appeling between iteration and to help keep track of user answer visually




