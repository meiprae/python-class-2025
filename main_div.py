def main() :
    try:   
        #prompt user two numbers
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    
        # division
        result = num1 / num2
        print(f"result: {result}")
    
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed!.")
        
    except ValueError:
        print("Error:  Please enter nvalid number!.")
        
if __name__ == "__main__":
    main()
    
    
        