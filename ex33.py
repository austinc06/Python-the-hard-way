i = 0
numbers = []

while i < 6:
    print("At the top i is %d" % i)
    numbers.append(i)

    i += 1
    print("Numbers now: ", numbers)
    print("At the bottom i is %d" % i)

print("The numbers: ")

for num in numbers:
    print(num)



#Convert to a function
def gen_num_list(stop_num,step_num):
    i = 0
    numbers = []

    while i < stop_num:
        print("At the top i is %d" % i)
        numbers.append(i)

        i+= step_num
        print("Numbers now: ", numbers)
        print("At the bottom i is %d" % i)

    print("The numbers: ")

    for num in numbers:
        print(num)

def gen_num_list_for(stop_num, step_num):
    numbers = []
    for i in range(0, stop_num, step_num):
        print("At the top i is %d" % i)
        numbers.append(i)

        print("Numbers now: ", numbers)
        print("At the bottom i is %d" % i)

    print("The numbers: ")

    for num in numbers:
        print(num)
