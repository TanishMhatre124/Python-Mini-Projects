#calculator project 
logo = """
 _____________________
|  _________________  |
| | Python Calc    | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | * | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|______________________|
"""

print(logo)
def add(n1,n2):
    return n1+n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operation={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide    
    } 

def calculator():
    should_accumulate= True 
    num1=float(input("what is the first number:?"))

    while should_accumulate:
        for symbol in operation:
            print(symbol)
        operation_symbol=input("pick up the operation:")
        num2=float(input("what is the second number:?")) 

        answer=operation[operation_symbol](num1,num2)
        print(f"{num1}{operation_symbol}{num2} = {answer}") 

        choice=input(f"type 'y' to continue calculating the {answer} or type 'n' to start a new calculation:")

        if choice =="y":
            num1= answer
        else:
            should_accumulate=False
            print("\n"*20)
            calculator()


calculator()