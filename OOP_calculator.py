class Calculator:
    def calculate(self, operator, a, b):
        operations = {
            "+": a + b,
            "-": a - b,
            "*": a * b,
            "/": a / b if b != 0 else "cannot divide by zero" 
        }

        return operations.get(operator, "invalid operator")

calc = Calculator()

def main():
    
    while True:
        operator = input("Enter your operator : ")
        num1 = float(input("Enter your num1 :"))
        num2 = float(input("Enter your num2 :"))
        
        result = calc.calculate(operator, num1, num2)
        print("Result : " , result)

        stop = input("Continue? yes/no :")
        if stop == "no":
            break

if __name__ == "__main__":
    main()
