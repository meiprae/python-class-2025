try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))

    if __name__ == "__main__":
        print("Total:", a + b)
    
except ValueError:
    print("Error: You have entred an invalid input.")
    
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
    
except:
    print("something went wrong.")
    
finally:
    print("Execution completed.")