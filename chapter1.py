# # variables and data types
# a = 5   # integer
# b = 5.0 # Float
# c ="Suchunyavadee thammachotvarasiri" # string
# d = True # Boolean True | false
# e = 6+5j # complex

# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

# a = 55
# b = 6.5
# print(a)
# print(b)

# z = a+b # Float
# print(z)


# Descriptive name or meaning full NameErrortax = 0.07
# firtname = "Suchunyavadee"
# email = 's6807012660033@email.kmutnb.ac.th'
# age = 18

# # Multi words variablr name
# # snake case
# student_first_name = 'Suchunyavadee'
# student_last_name = 'Thammachotvarasiri'
# student_age = 18
# student = "s6807012660033@email.kmutnb.ac.th"

# print("student name:" + student_first_name)
# print(f"student lastname : {student_last_name}")

# # Data types
# a = 1     #int
# b = 1.1   #float
# c = '1'   #string
 
#  print(a+a) # 2
#  print(b+b) #2.2
#  print(c+c) # 11
#  print(a+b) # 2.1
# #  print(a+c) #Error

# print (type(a) )
# print (type(b) )
# print (type(c) )

# # convert types
# a = float(a) # float
# b = int(b)
# c = int(c)
# print(a+c)

# scope variable - Global AND LOCAL VARIABLE
# x = "awesome" #string

# def myfunction() :
#     x = "fantastic."
#     print("python is " + x)

# myfunction()
# print("python is " + x)
# student_name = input (" Enter your name : ")

# print ("Student name : "  + student_name )

# a= int (input("Enter a number : "))
# b = int (input("Enter another number : "))

# a = int(a)
# b = int(b)
# print (a + b) 

# a = 8
# b = 2
# v += 2 # v=v+
# s -= 3 # s=s-3
# #arithmetic operations
# a= a + b # addition 10
# b = a - b # subtraction 8
# c = a * b # multiplication 80
# d = a / b # division    1.25
# e = a % b # modulus 1
# f = a ** b # exponentiation 10^8
# g = a // b # floor division 2
# print("Addition:", a) 
# print("Subtraction:", b)
# print("Multiplication:", c)
# print("Division:", d)
# print("Modulus:", e)
# print("Exponentiation:", f)
# print("Floor Division:", g)
#comparison operations
# a = 10
# b = 10.0
# #Equal to
# print  (a == b) # True  
# #a=== b # False, because they are different types
# print ( a == b and type(a) == type(b)) # False, because they are different types
# print ( a == b or (a) == type(b)) # True, because a is equal to b and type(a) is not equal to type(b)
# #Not equal to   
# print (a != b) # False, because they are equal
# #Greater than
# print (a > b) # False, because a is not greater than b
# #Less than
# print (a < b) # False, because a is not less than b
# #Greater than or equal to
# print (a >= b) # True, because a is equal to b

# #logical operations
# #and
# print (a > 5 and b < 15) # True, both conditions are true
# #or
# print (a < 5 or b > 15) # False, both conditions are false
# #not
# print (not (a < 5)) # True, because a is not less than 5
# import math
# # Math module sample usage

# # Square root
# num = 16
# sqrt_num = math.sqrt(num)
# print(f"Square root of {num} is {sqrt_num}")

# # Power
# base = 2
# exp = 3
# result = math.pow(base, exp)
# print(f"{base} to the power of {exp} is {result}")

# # Trigonometric functions
# angle = math.radians(90)  # Convert degrees to radians
# print(f"sin(90°) = {math.sin(angle)}")
# print(f"cos(90°) = {math.cos(angle)}")

# # Constants
# print(f"Pi: {math.pi}")
# print(f"Euler's number (e): {math.e}")

# # Absolute value
# print(f"Absolute value of -7: {math.fabs(-7)}")

# # Logarithm
# print(f"Log base 10 of 1000: {math.log10(1000)}")

# --- User Input and Arithmetic/Comparison Operations ---
name = input("Enter your name: ")
surname = input("Enter your surname: ")
print("Full name:", name, surname)

a = int(input("Enter integer a: "))
b = int(input("Enter integer b: "))

print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a ** b =", a ** b)
print("a // b =", a // b)
print("a % b =", a % b)
print("a < b:", a < b)
print("a <= b:", a <= b)
print("a != b:", a != b)
print("a == b:", a == b)