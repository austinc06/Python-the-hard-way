name = 'Zed A. Shaw'
age = 35 #not a lie
height = 74 #inches
cm_height = height*2.54 #cm
weight = 180 #lb
kg_weight = 180/2.2 #kg
eyes = "Blue"
teeth = "White"
hair = "Brown"

print("Let's talk about %s." % name)
print("He's %d inches or %d cm tall." % (height, cm_height))
print("He's %d pounds or %d kg heavy." % (weight, kg_weight))
print("That's to say, he's %d pounds or %d kg heavy." % (180, 180/2.2))
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (eyes,hair))
print("His teeth are usually %s depending on the coffee." % teeth)

#this line is tricky, try to get it exatly right
print("If I add %d, %d, and %d I get %d." % (age,height,weight,age+height+weight))


#python format characters
# c: single character (including integers)
# r: string (converts any python object using repr())
# s: string (converts any python object using str())
# %: no argument is converted
# d: integer decimel
# i: integers
# o: octal
# u: decimal
# x: hexadecimal (lowercase)
# X: hexidecimal (uppercase)
# e: Floating exponential format (lowercase)
# E: floating exponential format (uppercase)
# f: Floating point decimal format#
