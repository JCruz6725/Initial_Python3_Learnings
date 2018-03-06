#John Cruz
#2/22/2018
#Gym Exersize based on height and wieght
import time as t

'''
def height_to_wieght():
	#future ideas
	#possible ratio to be over or under like if >1 then do this, else <1 tdo that 	
'''

Continue_YN = 'Y'
while Continue_YN == 'Y'): #Power on or open app

	feet = int (input('how tall are you in feet '))
	inches = int (input('how tall are you in inches '))
	weight = int(input ('how much do you weight '))

	height = feet + inches/12

	print ('you are %d\'%d\" '%(feet, inches))
	print (height)
	print (weight)

	#for 6+feet and 200-250lbs

	Suggestion1 = '1. Cycle 30 min, Tredmill 20 min, lift up to 50lbs for 10min\n'

	#for 5-6feet and 175-200lbs
	Suggestion2 = '2. Cycle 20 min, Tredmill 20 min, lift up to 40lbs for 10min\n'

	#for less than 5feet and 100-150lbs
	Suggestion3 = '3. Cycle 20 min, Tredmill 10 min, lift up to 20lbs for 10min\n'

	#for any thing that does not fall under any cat.
	GoToDr = '4. You should see a doctor.\n'

	if ((height >= 6) and (200 <= weight <=250)):
		print(Suggestion1)
		t.sleep(.5)

	elif((5 <= height < 6) and (175 <= weight <= 200)):
		print(weight)
		print(Suggestion2)
		t.sleep(.5)

	elif((height < 5) and (100 <= weight <= 150)):
		print(Suggestion3)
		t.sleep(.5)
	else:
		print (GoToDr)
		t.sleep(.5)
	
	Continue_YN = str(input ('Continue? Y/N?'))
	Continue_YN.upper()
