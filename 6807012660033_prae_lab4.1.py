#collect user input into a list until 'end' or 'END' is entered
mylist = []
while True:
    user_input = input("Enter something (type ' end' or 'END' to stop):")
    if user_input.lower() == 'end':
        break
    mylist.append(user_input)
    
# Print all inputs with a number conter
for index, item in enumerate(mylist, 1):
    print (f"9{index}. {item}")
