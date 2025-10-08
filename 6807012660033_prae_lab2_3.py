name= input  ("Enter your name: ")
Last_name= input("Enter your surname: ")
age = input("Enter your age: ")
print(f"Hello, my name is {name} {Last_name}, I am Gender age of {age}")

#Hint : use split
str = "perecttly#perfected#perfection"
print(str.split("#"))

# 3. Copy this string of DNA into your code

dna = "CACGCCTAGTTTCAGACATAACCCTGGACATAGCCATAACGGAGTCAG"

# Print the size of the dna string, and identify the positions that the following substrings appear in dna string.
# a) print size of the dna string
print(f"This DNA have {len(dna)} characters")

# b) "TGGA"
print(f"Position of 'TGGA' in dna string is {dna.find('TGGA')}")

# c) "TCAG" (This substring appears twice. Try writing code to find them both)
print(f"Position of 'TCAG' in dna string is {dna.find('TCAG')}")
print(f"Position of 'TCAG' in dna string is {dna.find('TCAG', dna.find('TCAG') + 1)}")

# d) "GACG" (Does this substring appear in dna string?)
print(f"Position of 'GACG' in dna string is {dna.find('GACG')}")
print("GACG" in dna)
if "GACG" in dna:
    print("GACG is found in the dna string")
else:
    print("GACG is not found in the dna string")
# Hint: use index() or find()

# 4. Slice the dna string into substrings of 3 characters and then print them all in one line. For example, CAC GCC TAG ... CAG
for i in range(0, len(dna), 3):
    print(dna[i : i + 3], end=" ")

    