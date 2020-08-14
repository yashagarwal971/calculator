a = int(input("Enter first number: "))
b = int(input("Enter first number: "))

n = int(input("Enter 1-Addition, 2-Subtraction, 3-Multiplication, 4-Division: "))



if n == 1:
    print("Result: ")
    addition(a,b)
    #Charitha code
elif n == 2:
    print("Result: ")
    subtraction(a,b)
    #Mudit code
elif n == 3:
    print("Result: ")
    multiplication(a,b)
    #Sarthak code
elif n == 4:
    print("Result: ")
    division(a,b)
    #Yash code
else:
    print("Invalid input")