#Set variable x to the sentence "There are __ types of people" where the value of __ can be changed
x = "There are %d types of people." % 10

#Set variable binary to the string "binary"
binary = "binary"

#Set variable do_not to string "don't"
do_not = "don't"

#Set variable y to a string that uses the formatted variables binary and do_not
y = "Those who know %s and those who %s." % (binary, do_not)

#Print x an dy
print(x)
print(y)

#Print x as a formatted variable converted to a string with repr()
print("I said: %r." % x)

#Print y as a formatted variable converted to a string with str()
print("I also said: '%s'." % y)

#Set the variable hilarious to the boolean False
hilarious = False

#Set the variable joke_evaluation to a string that already includes a formatter
joke_evaluation = "Isn't that joke so funny?! %r"

#Prints joke evaluation with hilarious being used as the formatted variable
print(joke_evaluation % hilarious)

#Assign variable w and e to two halves of a string
w = "This is the left side of ..."
e = "a string with a right side."

#Concatenate strings w and e
print(w+e)
