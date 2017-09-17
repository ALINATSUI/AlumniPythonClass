people = 30
cars= 40
trucks = 15

if cars > people:
	print("We should take the cars.")

# if the value of cars is greater than value of people, print out statement "We should take the cars."

elif cars <people:
	print("We should not take the cars.")
#else if value of cars is less than value of people, print out statement "We should not take the cars."


if trucks>cars:
	print("That's too many trucks.")

#if the value of trucks is greater than value of cars, print out this statement.

elif trucks<cars:
	print("Maybe we could take the trucks.")
#else if the value of trucks is less than value of cars, then print out this statement.

else:
	print("We can't decide.")
#If both conditions aren't met (the if, elif), then the message "We can't decide." will be #printed.

if people>trucks:
	print("Alright, let's just take the trucks.")
#if people is greater than trucks, then the statement "Alright, let's just take the trucks." will #print out.
else:
	print("Fine, let's just stay home then.")
#Otherwise, since the if condition wasn't satisfied, the else statement will print out. 	
