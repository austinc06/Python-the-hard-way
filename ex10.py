tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

#Other escape sequences
#\\ (backslash cat)
#\'
print('I can\'t believe you.')
#\"
print("And I quote, \"blah blah blah.\"")
#\a: ASCII bell
#\b: ASCII backspace
#\f: ASCII formfeed
#\n: ASCII linefeed (persian cat)
#\N{name}: Character named name in the Unicode database
#\r: carriage return
#\t: horizontal tab (tabby cat)

while True:
    for i in ["/","-","|","\\","|"]:
        print("%s\r" % i)


print('''
I\'m the next fat_cat and here's my list:
\t* Cat food x2
\t* FIshes x4
\t* Catnip x6\n\t* Grass x8
''')
