def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return("cannot divide by zero!")   
    return a / b 

def main():

    while True:

        print("\n ----calculator----")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        choice = input("Enter your operation here : ")
        num1 = float(input("Enter num1 here : "))
        num2 = float(input("Enter num2 here : "))

        if choice == "1":
            print("Result :", add(num1, num2))
        elif choice == "2":
            print("Result :", subtract(num1, num2))
        elif choice == "3":
            print("Result :", multiply(num1, num2)) 
        elif choice == "4":
            print("Result :", divide(num1, num2))      
        else:
            print("Invalid choice!")

        stop = input("continue ? yes/no : ")

        if stop.lower() == "no":
            break


if __name__ == "__main__":
    main()

