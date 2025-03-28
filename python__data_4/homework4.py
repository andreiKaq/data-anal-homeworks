# Create two empty lists (long_names, short_names)
# Iterate through names list and add names that are longer than 5 characters
# to long_names, and others to short names
names = ['Sarah', 'Jessica', 'Anthony', 'Jack', 'Simon', 'Arthur', 'Maria', 'Samantha']

long_names = []
short_names = []

for name in names:
    if len(name) > 5:
        long_names.append(name)
    else:
        short_names.append(name)

# print(long_names)
# print(short_names)

# Given a list where each element is a year. Determine whether the given year is a leap year. If the year is a leap year,
# print YES, otherwise print NO. According to the Gregorian calendar, a year is a leap year if its number is a multiple of 4,
# but not a multiple of 100 OR if it is a multiple of 400.
years_list = [2012, 2011, 1492, 1861, 1600, 1700, 1800, 1900, 2000]

# for year in years_list:
#     if year % 400 == 0:
#         print(year, 'YES')
#     elif year % 100 == 0:
#         print(year, 'NO')
#     elif year % 4 == 0:
#         print(year, 'YES')


# Write a program that prompts the user for a string and checks if the string contains only unique characters.

# user_input = input('Введите строку: ')
# result = []
# total = True
#
#
# for char in user_input:
#     if char in result:
#         total = False
#     else:
#         result += char
#
# if total:
#     print('unikalen')
# else:
#     print('ne unikalen')


# Write a program that checks gender for each person.
# If person is a male, print "This is NAME SURNAME. He is AGE years old"
# If person is a female, print "This is NAME SURNAME. She is AGE years old"
people = [
    ('Jane', 'Smith', 26, 'female'),
    ('Jack', 'Green', 30, 'male'),
    ('Maria', 'Gold', 29, 'female'),
    ('Simon', 'Bloom', 35, 'male'),
]

for name, surname, age, gender in people:
    if gender == 'male':
        print(f'This is {name} {surname}. He is {age} years old.')
    elif gender == 'female':
        print(f'This is {name} {surname}. She is {age} years old.')













