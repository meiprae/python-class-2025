def factorial(n):
    if n ==1 or n==0:
        return 1
    else:
        print(f"{n} *")
        return n * factorial(n-1)
    
def add_numbers(a=1, b=1, c=1):
    print("The sum is:", a +b +c)