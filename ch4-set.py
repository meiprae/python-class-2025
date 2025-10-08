# # set
# # empty set
# empty_set = {}

# # Int 
# my_set1 = {1, 2, 3, 4, 5}

# # String
# my_set2 = {"apple", "banana", "cherry"}

# # Mixed data types
# my_set3 = {1, "apple", 3.14, (1, 2) [1, 2, 3,]}

# # Print sets
# print("Empty Set:", empty_set)

# # list and tuple
# my_set3 = {1 , 5, 8, "AAA"}
# my_set3 = list(my_set3)
# my_set3[3] = "BBB"

# my_set3 = set(my_set3)
# print("Set with mixed data types:", my_set3)


# _list = [1, 2, 3, 4, 5]
# _list = list(set(_list))
# print("List converted to set:", _list)

# for item in my_set3:
#     print(item)
    
# # Add elements to a set
# my_set1.add('CCC':", my_set3)
# print("Set after adding 'CCC':", my_set3)

# # Remove elements from a set
# my_set3.remove('BBB')
# print("Set after removing 'BBB':", my_set3)

# #check if an element exists in a set
# if 'AAA' in my_set3:
#     print("'AAA' is in the set.")            
# else:
#     print("'AAA' is not in the set.")
    
# # Clear the set
# my_set3.clear() 
# print("Set after clearing:", my_set3)

# #set operations
# # Union
# set_a = {1, 2, 3}
# set_b = {3, 4, 5}


# set_union = set_a | set_b
# print("Union of set_a and set_b:", set_union)

# # Intersection
# set_intersection = set_a & set_b
# print("Intersection of set_a and set_b:", set_intersection)

# # Difference
# set_difference = set_a - set_b
# print("Difference of set_a and set_b:", set_difference)

# # Symmetric Difference
# set_symmetric_difference = set_a ^ set_b
# print("Symmetric Difference of set_a and set_b:", set_symmetric_difference)

# python set - 10minutes
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]

#check if a fruit is in the set
print("apple" in fruits)  # True

# A. Check if "apple" is present in the fruits set.
print("apple" in fruits)  # True

# B. Use the add method to add "orange" to the fruits set.
fruits.add("orange")
print(fruits)

# C. Use the correct method to add multiple items (more_fruits) to the fruits set.
fruits.update(more_fruits)
print(fruits)

# D. Use the remove/discard method to remove "banana" from the fruits set.
fruits.discard("banana")  # or fruits.remove("banana")
print(fruits)

