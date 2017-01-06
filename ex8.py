formatter = "%r %r %r %r"

print(formatter % (1,2,3,4))

print(formatter % ("one","two","three","four"))

print(formatter % (True, False, False, True))

#%r will convert anything to a string. In this case, it converts each instance of formatter to a string of "%r %r %r %r"
print(formatter % (formatter, formatter, formatter, formatter))

print(formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
))

# %r will read \n and \t directly as strings
print(formatter % ("\n","blah","blah","blah\t"))
