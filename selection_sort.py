# Unsorted list
list = [0, -3, 15, -6, 2, 65, 54, 100]

# Declaration of sorted_list variable for saving the sorted items 
sorted_list = []

# Variable to hold smallest value
small = 0

# Flag stops the value of small to be reassigned
flag = 0

# Stores the index number of the smallest item in the list
# This index is used to pop out that value from the list to avoid repetition
pop_index = 0

print('Unsorted list: ', list)

'''
This is the outer loop which runs for one less than total items in the list
The reason is that if it runs till the length of the list then an index out 
of range error occurs. The length of list here is 8. The loop starts from 0
and it will run till 8. However when we give list[8] it will result in an error
because our array has the length of 7.
'''
for ol in range(len(list)-1):
    # Inner loop will compare each item with the next item and assign the 
    # smalles item to the small variable
    for index in range(len(list)-1):
        # If the item on the left is smaller than right and flag == 0 then 
        # the item will be assigned to the small variable
        if flag == 0 and list[index] < list[index + 1]:
            small = list[index]
            # Index of the small item will be saved in pop_index
            pop_index = index
            # Flag is set to 1  so that the value of small doesn't change
            flag = 1
        # This condition will compare the value of list item with small
        # If the value is smaller than the value stored in small then it
        # will be swapped.
        elif flag == 1 and list[index] < small:
            small = list[index]
            pop_index = index
    # The smallest value stored in the small variable will be appended 
    # to the sorted_list
    sorted_list.append(small)
    # The smallest item will be popped out from the unsorted list so that
    # we don't compare it again with other items in the list
    list.pop(pop_index)
    # Flag is set to zero again to assign the smallest value to small variable
    flag = 0
# The last number in the unsorted list will be left out because it will be the 
# largest number in the list. That's why we will add it to our sorted list in the end.
sorted_list += list

print('Sorted list created by linear sort: ', sorted_list)
