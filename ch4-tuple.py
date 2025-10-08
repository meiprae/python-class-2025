# Tuple
_tuple = () # empty tuple
_tuple
_tuple1 = ("Suchunyavadee", "Thammachotvarasiri", 18, )

print("Tuple : ", _tuple1)
print("First item :", _tuple1[0])
print("Second item :", _tuple1[1])

print("length of tuple:", len(_tuple1))

# COnverting tuple to list
_list_from_tuple = list(_tuple1)
print("List from tuple:", _list_from_tuple)

# append item to list
_list_from_tuple.append("hello")
print("List after appending:", _list_from_tuple)

# changing item in list
_list_from_tuple[0] = "New Name"
print("List after changing first item:", _list_from_tuple)

# Converting list back to tuple
_tuple_from_list = tuple(_list_from_tuple)
print("Tuple from list:", _tuple_from_list)

# Deleting tuple
del _tuple_from_list