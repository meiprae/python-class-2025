def main():
    filename = input("Enter the filename")
    try:
        with open(filename,"r")as file:
            content = file.read
            print("\nFile content:\n")
            print(content)
    except FileNotFoundError:
        print(" Error: The file dose not exist.")

if __name__ == "__main__":
    main()    