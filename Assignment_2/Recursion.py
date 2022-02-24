def triangle(n):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    else:
        new_row = [1]
        last_row = triangle(n-1)
        for k in range(len(last_row)-1):
            new_row.append(last_row[k] + last_row[k+1])
        new_row += [1]
    return new_row


row = int(input("Enter numbers of rows"))

for i in range(1, row + 1):
    print(triangle(i))
