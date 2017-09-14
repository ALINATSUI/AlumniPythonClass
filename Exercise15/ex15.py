from sys import argv
#from sys (package), import arguments.

script, filename = argv
#script and filename are the designated arguments

txt = open(filename)
#open the filename (In this case, the filename is: ex15_sample.txt)

print(f"Here's your file {filename}:")
#Print the string "Here's your file {variable name = ex15_sample.txt}"

print(txt.read())
#the contents of the text file is read as a file object by the script



print("Type the filename again:")
file_again = input("> ")
#the system prompts user to "Type the filename again: "

txt.close()
#This closes ex15_sample.txt

txt_again = open(file_again)
#Once the user types in the filename, a new variable 'txt_again' is created to capture the second instance of the opened file.

print(txt_again.read())
#The contents of the opened file is displayed on the screen to the user.

txt_again.close()

#this closes the second instance of the opened file. 
