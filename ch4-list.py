#list
_list = [] #list to store items
_list = ["a", 20.0,30, "b", 40]
student = ["68007012660033","Suchunyavadee", "Thammachotvarasiri",  "s68007012660033@kmutnb.ac.th", 18]


print("student: ", student)
print("student ID: ", student[0])
print("student name: ", student[1], student[2])
print("student email: ", student[3])
print("length of student: ", len(student))

print(student[1:3]) 

# Adding items to the list
_list1 = [1, 2, 3, 4, 5]
_list1.append(10) # Add 6 to the end of the list
print("List after appending 10:", _list1)
_list1.insert(2, 5) # Insert 0 at the beginning of the list
print("List after inserting 5 at index 2:", _list1)


# Removing items from the list
_list1.remove(3) # Remove the first occurrence of 3
print("List after removing 3:", _list1) #[1, 2, 5, 4, 5, 10
_list1.pop() # Remove the last item
print("List after popping the last item:", _list1) #[1, 2, 5, 4, 5]

# Editing items in the list
_list[0] = 100
_list[1] = 200
print("List after editing items:", _list) #[100, 200, 30, "b", 40]

#Mulpy items in the list
_list2 = [6,7,9]
_list1.extend(_list2) # Add items from _list2 to _list1
print("List after extending with _list2:", _list1) #[1, 2, 5, 4, 5, 10, 6, 7, 9]

#storing items in the list
_list1.sort() # Sort the list in ascending order
print("List after sorting:", _list1) #[1, 2, 4, 5, 5, 6, 7, 9, 10]
# Reversing the list
_list1.reverse() # Reverse the order of the list
print("List after reversing:", _list1) #[200, 100, 9, 7, 6, 5, 4]

#  Copying the list
# a = 3
# b = a
# print("list 1:", _list1)
# print("list 3:", _list3)
# _list3[0] = 1000 # Change the first item in _list3
# print("list 1 after changing list 3:", _list1) # _list1 remains unchanged
# print("list 3 after changing:", _list3) # _list3 is changed

_list3 = _list1.copy() # Create a copy of _list1
_list3[0] = 1000 # Change the first item in _list3
print("list 1 after changing list 3:", _list1) # _list1 remains unchanged
print("list 3:", _list3) # _list3 is changed

#cleaning the list
_list3.clear() # Remove all items from the list
print("List after clearing:", _list3) #  []

# Deleting the listq
# del _list3 # Delete the list

# print("List 3 after deleting:", _list3) # This will raise an error since _list3 is deleted

# checking if an item is in the list
if 100 in _list1:
    print("100 is in the list")
else:
    print("100 is not in the list")

    # Iterating through the list
for item in _list1:
    print("Item:", item)