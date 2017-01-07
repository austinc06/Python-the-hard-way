def add(a,b):
    print("ADDING %d + %d" % (a,b))
    return a+b

def subtract(a,b):
    print("SUBTRACTING %d - %d" % (a,b))
    return a-b

def multiply(a,b):
    print("MULTIPLYING %d * %d" % (a,b))
    return a*b

def divide(a,b):
    print("DIVIDING %d / %d" % (a,b))
    return a/b

print("Let's do some math with just functions!")

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print("Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height,weight,iq))


# A puzzle for extra credit, type it in anyway
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq,2))))
#Nested: Add(35, subtract(74, multiply(180, 25)))
#Nested: Add(35, subtract(74, 4500))
#Nested: Add(35, -4426)
#Answer: 4391
#Formula: Age + (Height - (Weight * (Iq / 2)))

print("That becomes: ", what, "Can you do it by hand?")

#Alternative formula: (24+34)/(100-1023))
#Answer should be: 58/-923 = -0.06283856
what2 = divide(add(24,34),subtract(100,1023))
print(what2)
