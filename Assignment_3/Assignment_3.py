# ask user to enter 2 numbers
num_1 = float(input("Enter the Dividend "))
num_2 = float(input("Enter the Divisor "))
filter_result = []


# make a Fucntion to calculate quotient and remainder and return its value
def calc(num_1, num_2):
    quotient = int(num_1 // num_2)
    remainder = int(num_1 % num_2)

    return [quotient, remainder]


# check whether fucction is callable or not
print("\nWhether function is callable : " + str(callable(calc)))

# call the function and print the quotient and remainder
result = calc(num_1, num_2)
print("\nQuotient is " + str(result[0]))
print("Remainder is " + str(result[1]))
print("Whether Quotient is zero : " + str(result[0] == 0))
print("Whether remainder is zero : " + str(result[1] == 0))

# add 4, 5, 6 to the result
result = result + [4, 5, 6]

# separate values greater than 4
for i in result:
    if i > 4:
        filter_result = filter_result + [i]

# print the filtered result
print("\nValues great than 4 after addition of values : " + str(filter_result))

# convert the result to set
filter_result = set(filter_result)
print("\nResult has been converted to set : ", end="")
print(filter_result)

# make the set immutable
print("\nPrint has been made immutable : ", end="")
filter_result = frozenset(filter_result)
print(filter_result)

# find out the maximum value from the list
max_value = max(filter_result)

# print the max value and its hash value
print("\nMax value from set is : " + str(max_value))
print("Its hash value is : " + str(hash(max_value)))
