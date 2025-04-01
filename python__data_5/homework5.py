# Write a function that accepts a list of numbers as an argument
# And returns list with squares for each number

# def list_to_square(array):
#     result = []
#     for arr in array:
#         result.append(arr ** 2)
#
#
#     return result
#
# a = list_to_square((1, 2, 3, 4, 5, 6))
# print(a)




# Write a function that accepts a list of numbers
# And returns a tuple with two numbers, amount of odd and even numbers
# Example: input -> [1, 2, 3, 4, 5] output (3, 2)
# Where 3 is amount of Odds and 2 is amount of evens

# def tupleCounter(list):
#     oddCount = 0
#     evenCount = 0
#
#     for element in list:
#         if element % 2 == 0:
#             evenCount += 1
#         else:
#             oddCount += 1
#
#     result = [oddCount, evenCount]
#     return tuple(result)
#
#
#
# b = tupleCounter((1, 2, 3, 4, 5, 6, 7))
# print(b)



# Write a function that accepts a list of numbers
# and returns largest number

# def largestNum(list):
#
#     list.sort()
#     result = list[-1]
#
#     return result
#
#
# c = largestNum([1, 5, 100, 4, 2, 4, 45])
# print(c)

# Write a function that accepts a start number and end number
# Create a FizzBuzz for given range
# (If number divided by 3 has no remainder, print number + FIZZ
# If number divided by 5 has no remainder, print number + BUZZ
# If number divided by 5 and 3 has no remainder, print number + FIZZBUZZ)

# def FizzBuzz(start: int, end: int):
#     for num in range(start, end):
#         if num % 3 == 0  and num % 5 == 0:
#             print(num, 'FIZZBUZZ')
#         elif num % 5 == 0:
#             print(num, 'BUZZ')
#         elif num % 3 == 0:
#             print(num, 'FIZZ')
#         else:
#             print(num)
#
# FizzBuzz(1, 16)