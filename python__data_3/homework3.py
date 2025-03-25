# https://en.wikipedia.org/wiki/List_of_Unicode_characters

# Print to console what is different in each set compared to another
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(f'set_a отличается {set_a.difference(set_b)} а set_b отличается, {set_b.difference(set_a)}')
# print(set_b.difference(set_a))


# Create a string from a list and save it to variable
# Make each name on a new line.
names = ['Jack', 'Mary', 'Samantha', 'George', 'Simon', 'John']

for name in names:
    print(name)



# print sum of all numbers in a list
# print sum of all unique numbers in a list
numbers = [2, 53, 12, 87, 65, 32, 12, 2, 65, 32, 100, 100, 100]


def sumAndUnicsum(array):
    numbers_sum = 0
    unique_numbers_sum = 0
    for number in array:
        numbers_sum += number

    for unic_num in set(array):
        unique_numbers_sum += unic_num
        print(unic_num)

    print(f'{numbers_sum} and {unique_numbers_sum}')

sumAndUnicsum(numbers)

# простое решение :)

# total_sum = sum(numbers)
# unique_sum = sum(set(numbers))
# print("Сумма всех чисел:", total_sum)
# print("Сумма всех уникальных чисел:", unique_sum)




# create a new list from studentsA and studentsB
# make sure there is no duplicates in a new lists
studentsA = ['Jack', 'Bob', 'Mary']
studentsB = ['Bob', 'Sarah', 'Simon']

students = set(studentsA + studentsB)
print(students)


# What elements are common for both tuples?
numbersA = (23, 52, 12, 75, 42)
numbersB = (75, 22, 42, 94, 70)

print(f'common elemets of both tuples are: {set(list(numbersA)).intersection(numbersB)}')




# add 5 to the tuple on a right position
a = (1, 2, 3, 4, 6, 7, 8)

def fixingTuple(arg):
    tuple_example = list(arg)
    tuple_example.append(5)
    tuple_example.sort()
    arg = tuple(tuple_example)
    print(arg)

fixingTuple(a)

