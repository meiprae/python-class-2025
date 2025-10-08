f = open("demo.txt", "r")
# content = f.read()
# print(content)

# print(f.readline())
# print(f.readline())
# print(f.readline())

for line in f:
    print(line.strip())  # strip() to remove extra newline characters
    
f.close()

#  with open("demo.txt", "r") as f:
#      cotent = f.read()
#      print(cotent)

# Mode "a" mean append
with open("demo.txt", "a") as f:
    f.write("\This is a new line added to thee file.")
    
with open("demo.txt", "r") as f:
    content = f.read()
    print(content)
    
# Mode "w" mean write (overwrite)
with open("demo.txt", "w") as f:
    f.write("This file has been overwritten.\n")
    f.write("All previous content is lost.\n")
    
import os

if os.path.exists("demo2.txt"):
    os.remove("demo2.txt")
    print("File 'demo2.txt' has been deleted.")
else:
    print("File 'demo2.txt' does not exist.")
