# https://www.w3schools.com/python/python_string_formatting.asp


# Write a code to return "Hero" from given string
from itertools import count
example_string1 = "Hello bro"
sub_str1 = example_string1[:2] + example_string1[7:9]
print(sub_str1)


# Write a code to return "Jack is my name"
example_string2 = "jack Is My NAME"
sub_str2 = example_string2.lower().replace('jack', 'Jack')
print(sub_str2)



# Write a code to return "Get rid of junk please"
example_string3 = "%-*Get rid of *junk* please*-L%*"
sub_str3 = example_string3.strip('%-*L').replace('*', '')
print(sub_str3)

# Write a code to return "Hello my name is Jack"
example_string4 = "hello my name is jack"
sub_str4 = example_string4[0].upper() + example_string4[1:17] + example_string4[17].upper() + example_string4[18:]
print(sub_str4)

# Find all occurrences of “Estonia” in a given string ignoring the case.
example_string5 = "Welcome to estonia. Estonia is awesome, isn't it? I moved to ESTONIA 5 years ago."
sub_str5 = example_string5.lower().split()
count = 0

for item in sub_str5:
    if item == 'estonia':
        count += 1


print(f'String "Estonia" was founded {count} times ignoring the case')




# Write a code to return f-string "Hello, my name is Jack"
var1 = "jack"
var2 = "hello"
var3 = "MY NAME IS"

print(f'{var2.title()}, {var3.lower()} {var1.title()}')



# Write a code to return byte_string text value
byte_string = b"\316\273"
print(byte_string.decode("utf-8"))