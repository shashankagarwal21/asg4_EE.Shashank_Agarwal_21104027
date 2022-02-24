num_1 = float(input("Enter the Dividend "))
num_2 = float(input("Enter the Divisor "))
filter_result = []


def calc(num_1, num_2):
    quotient = int(num_1 // num_2)
    remainder = int(num_1 % num_2)

    return [quotient, remainder]


print("\nWhether function is callable : " + str(callable(calc)))

result = calc(num_1, num_2)
print("\nQuotient is " + str(result[0]))
print("Remainder is " + str(result[1]))
print("Whether Quotient is zero : " + str(result[0] == 0))
print("Whether remainder is zero : " + str(result[1] == 0))

result = result + [4, 5, 6]

for i in result:
    if i > 4:
        filter_result = filter_result + [i]

print("\nValues great than 4 after addition of values : " + str(filter_result))

filter_result = set(filter_result)
print("\nResult has been converted to set : ", end="")
print(filter_result)

print("\nPrint has been made immutable : ", end="")
filter_result = frozenset(filter_result)
print(filter_result)

max_value = max(filter_result)
print("\nMax value from set is : " + str(max_value))
print("Its hash value is : " + str(hash(max_value)))
