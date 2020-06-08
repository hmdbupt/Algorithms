# Unsorted list
list = [3, 1, 2, -15, 15, 100, -5, 86, 22, 96]

print("Unsorted list: ", list)

# The outer loop will run as many times as there are
# items in the list
for outer_loop in range(len(list) - 1):
    # The inner loop will work as index counter
    for index in range(len(list) - 1):
        # If the item on the left is bigger than right
        # it will be swapped.
        if list[index] > list[index + 1]:
            # The bigger item will be stored in temp
            temp = list[index]
            # The smaller item will be stored in the left index
            # pushing the smaller number to the left
            list[index] = list[index + 1]
            # The bigger item will be stored in the right index
            # pushing the bigger number to the right
            list[index + 1] = temp
            
print("Bubble sorted list: ", list)
