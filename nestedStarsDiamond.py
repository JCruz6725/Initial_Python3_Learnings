############################
#John Cruz
#nested for loop Diamond

for i in range (10):

	for k in range (10,i,-1):
		print(' ', end='')

	for j in range (i):
		print('*', end='')

	for j in range (i):	
		print('*', end='')

	for k in range (10,i,-1):
		print(' ', end='')

	print('')

for i in range (10, 0, -1):
	'''for j in range (i):
		print ('*', end='')
	'''
	for k in range (10,i,-1):
		print(' ', end='')

	for j in range (i):
		print('*', end='')

	for j in range (i):	
		print('*', end='')

	for k in range (10,i,-1):
		print(' ', end='')

	print('')

