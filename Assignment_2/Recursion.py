# Recursive function for making the Pascal's triangle
def triangle(n):
    # if n = 0 then return empty list to avoid infinite loop
    if n == 0:
        return []
    # if n = 1 return 1 which will be the base of the function
    elif n == 1:
        return [1]
    # else calculate the row by add terms of previous row
    else:
        new_row = [1]
        last_row = triangle(n-1)
        for k in range(len(last_row)-1):
            new_row.append(last_row[k] + last_row[k+1])
        new_row += [1]
    return new_row


# ask user for number of rows for Pascal's triangle
row = int(input("Enter numbers of rows "))

# using a loop print the triangle
for i in range(1, row + 1):
    print(triangle(i))
