a=int(input("enter the num1:"))
b=int(input("enter the num2:"))
def greet(operator):
    if operator == '+':
        print("results:",a+b)
    elif operator == "-" :
        print("results:",a-b)
    elif operator == "*":
        print("results:",a*b)
    elif operator == '/':
        print("results:",a/b)
    else:
        print("there is no operator")
operator=input("enter the user:")
greet(operator)
