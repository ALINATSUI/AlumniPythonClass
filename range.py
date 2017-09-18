#write a program that tells if the input is in the range of 6 to 12 and 121 to 151

from sys import argv
#script = argv
#n = int (argv[1])
n=int(input('>>'))

range1=6
range2=12
range3 = 121
range4 =151

if(range1<=n<=range2):
    print(f"The number you entered is in the range of 6 to 12.")
elif(range3<=n<=range4):
    print(f"The number you entered is in the range of 121 to 151.")
else:
    print(f"The number you entered is not in the range of 6 to 12 or in the range of 121 to 151.")
