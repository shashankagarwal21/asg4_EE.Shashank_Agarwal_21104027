#  A recursive function to solve the tower of hanoi
def hanoi(num_disk, source, destination, auxiliary):

    # if there is only one disk then simply shift it
    if num_disk == 1:
        print("Move disk 1 from source", source, "to destination", destination)
        return

    else:
        hanoi(num_disk - 1, source, auxiliary, destination)
        print("Move disk", num_disk, "from source", source, "to destination", destination)
        hanoi(num_disk - 1, auxiliary, destination, source)


# Ask user for the number of disk
num_input = int(input("Enter the number of disk in Tower of Hanoi : "))
# call the function
hanoi(num_input, 'A', 'B', 'C')
