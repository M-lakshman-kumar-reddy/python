def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2
# making an dictionary
operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide, 
} 
# print(operation["*"](4,8))

def calculator():
    should_accumulate = True
    num1 = float(input("what is u r first number:-"))

    while should_accumulate:
        for symbol in operation:
            print(symbol)
        operation_symbol = input("pick an operation:-")
        num2 = float(input("what is u r last number:-"))
        answer = (operation[operation_symbol](num1,num2))
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"type 'y' to continue calculating with {answer},or type 'n' to start a new calculation :-").lower()

        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n"*20)
            calculator()


calculator()
