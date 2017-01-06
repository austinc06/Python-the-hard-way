from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline(), end = ' ')
    #end = ' ' will prevent readline() from outputting with an extra '\n' between lines
    #end = ' ' will also print on the same line

current_file = open(input_file)

print("First let's print the whole file:\n")
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
rewind(current_file)

#print("What if we don't rewind?")
#print_all(current_file)
#Answer: nothing will be printed, as the pointer in the file is currently at the end

#Let's try to rewind only partway
current_file.seek(2)
print_all(current_file)
#It will start the print at the new index instead of index=0

#Let's rewind partway again
current_file.seek(2)
#This will start the first line for print_a_line at a new starting index

print("Let's print three lines:")
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line,current_file)
