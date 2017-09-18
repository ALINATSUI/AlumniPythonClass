#write a program that tells the user if their input is a positive number or negative number

	#positive number = n >=0
	#if n<=0, positive number

	#negative number = n<0
	#if n<0, then negative number

#write a program that tells the user if their input is divisible by 4
	#n%4
#write a program that tells if the input is in the range of 6 to 12 and 121 to 151.

from sys import argv
#script = argv
#n = int (argv[1])
n=int(input('>>'))
if(n>=0):
	print(f"The number you entered is a positive number.")
else:
	print(f"The number you entered is a negative number.")
