list1 = [1, 2, 3, 4, 5]
list2 = list1
list3 = list1.copy()
list2.remove(2)
list4 = [number for number in list1]
list1.remove(1)

#print(list1)
#print(list2)
#print(list3)
#print(list4)

number = 123456
isFinish = False
new_number = []
counter_comma = 0
counter_len_number = 0
len_number = len(str(number))
while isFinish is False:
    number = int(number)
    counter_comma = counter_comma + 1
    counter_len_number = counter_len_number + 1
    x = number % 10
    number = str(number)
    number = number[:-1]
    new_number.append(str(x))
    if counter_comma == 3 and counter_len_number < len_number:
        new_number.append(",")
        counter_comma = 0

    if counter_len_number == len_number:
        isFinish = True
        new_number.reverse()

str_new_number = ' '.join(map(str, new_number))
str_new_number = str_new_number.replace(" ", "")
#print(str(str_new_number))

number = 1234561
number = ("{:,}".format(number))
#print(number)

number1 = 1000
number1 = list(str(number1))
number1.reverse()
len = len(number1)
for i in range(len, 1, -1):
    if i % 3 == 0:
        number1[i] = number1[i] + ","
number1.reverse()
number1 = ' '.join(map(str, number1)).replace(" ", "")
#print(number1)

counter = 1
number = list(reversed(list("10000000")))
for c in number:
    if counter % 3 == 0:
        number[counter] = number[counter] + ","
    counter += 1
number.reverse()
number= ' '.join(map(str, number)).replace(" ", "")
#print(number)


from itertools import combinations
counter = 0
list1.clear()
for i in range(1, 50):
    list1.append(i)


comb = combinations(list1, 6)

# Print the obtained combinations
for i in list(comb):
    counter += 1
    print(i)

print(str(counter))
# A Python program to print all
# permutations using library function
from itertools import permutations

# Get all permutations of [1, 2, 3]
perm = permutations(list1,1)


# Print the obtained permutations
for i in list(perm):
    #print(i)
    counter+=1

