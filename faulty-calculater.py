#Faulty Calculator
#faulty values: 45*3=555, 56+9=77,56/6=4

num1=int(input("Enter first value: "))
num2=int(input("Enter second value: "))
op=input("Enter operetor: ")
if num1==45 and num2==3 and op=="*":
    print("Result: 555")
elif num1==56 and num2==9 and op=="+":
    print("Result: 77")
elif num1==56 and num2==6 and op=="/":
    print("Result: 4")
else:
    if op == "+":
        print("Result: ", num1 + num2)
    elif (op == "-"):
        print("Result: ", num1 - num2)
    elif (op == "*"):
        print("Result: ", num1 * num2)
    elif (op == "/"):
        print("Result: ", num1 / num2)
    elif (op == "%"):
        print("Result: ", num1 % num2)
    else:
        print("invalid operetor")
