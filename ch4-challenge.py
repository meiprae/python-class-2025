_data = (1,7,3,7,5,3,2,1,4,5,6,7,8,9,)

# Converting tuple to list
_list_data = list(_data)
print("List from tuple:", _list_data)

#sorting the list
for i in range(len(_list_data)):
    for j in range(i + 1,  len(_list_data)):
        if _list_data[i] > _list_data[j]:
            _list_data[i], _list_data[j] = _list_data[j], _list_data[i]

# Removing duplicates
_unique_data = set(_list_data)
print("Unique elements from the tuple;", _unique_data)

# Converting back to tuple 
_unique_data = tuple(_unique_data)
print("Unique  tuple:" , _unique_tuple)
t