# # conditions statement
# a = 5
# b = 10

# if (a==b): 
#     print(" a=b")
# else:
#     print("a != b")

# if (a!= b):
#     print("a != b")

#     # scores 0-100, > 80 = A, 70-79 = B, 60-69 = C, 50-59 = D, < 50 = F
#     score = input("Enter your score: ")

#     if (score >=80):
#         if (score<=85):
#             print('You got an A-')  
#         else:
#             print('You got an A+)

#     elif (score >= 70):  
#         print('You got a B.')
#     elif (score >= 60):
#         print('You got a C.')   
#     elif (score >= 50):
#         print('You got a D.')
#     else:
#         print('You got an F.')
   
# result = 3+4-(2+7) /2+5*6
# print(result)
# step 1 = 3+4-(9)/2+5*6
# 3+4-4.5+30
# 7-4.5+30
# 2.5+30 =32.5

# loop statement
#While loop
# count =1 #init counter
# while (count<=10):
#     print(count)
#     count += 1  # count = count +1

# while (True) :
#     print('why always me.')

import random

rand_int = random.randint(1, 100)

while (True):
    answer = int(input("Enter your answer: "))
    if answer == rand_int:
        print("Your nswer is correct!", answer)
        break  # exit the loop
    else:
        if (answer < rand_int):
            print('Your answer is less than random number. Try again.')    
        else:
            print('Your answer is greater than random number. Try again.')

print("Thank you .bye!")


#For loop
# for count in range(1,101,1):
#     #count =1, count <101, count+=5
#     print(count)

#     str = "Suchunyavadee thummachotvarasiri" 
#     for ch in str:
#         print(ch)

# data = ["Suchunyavadee",12, 5.0, "KMUTNB" ]
# for dt in data:
#     print(dt)   4
    
for i in range(1, 10,1):
    if (i==5):
        continue
    print(i)

if (True):
    pass