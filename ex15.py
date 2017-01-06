
#Imports the arguments module from the system
from sys import argv

#From the system line, the argv pulls the script name and the filename it took as an arguments
script, filename = argv

#Open the filename and assign it to the variable txt
txt = open(filename)

#print a simple leadup
print("Here's your file %r:" % filename)
#print the txt file contents by calling the read function (a function of text objects)
print(txt.read())

#print a simple question
print("Type the filename again:")
#assign the inputted filename to the variable file_again
file_again = input("> ")

#opens the file again using the new user-input name
txt_again = open(file_again)

#print the txt file contents again
print(txt_again.read())

#Benefits of argv method
#Can be called as part of the function without further input from user-input
#Benefits of input() method
#Explicitly asks user to enter the file name before continuing code (whereas argv would create an error)

txt.close()
txt_again.close()

#print(txt.read())
#The last print will fail because the txt file has already been closed
