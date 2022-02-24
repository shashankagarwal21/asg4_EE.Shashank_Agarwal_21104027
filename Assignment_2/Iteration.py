def facto(num):
    if num == 0:
        return 1
    else:
        return num * facto(num-1)


def combi(num_1, num_2):
    combination = (facto(num_1))/((facto(num_2))*(facto(num_1-num_2)))
    return int(combination)


line = int(input("Enter number of lines of pascle's triangle "))

for i in range(0, line):
    for j in range(0, i+1):
        print(combi(i, j), end="  ")
    print("\n")
