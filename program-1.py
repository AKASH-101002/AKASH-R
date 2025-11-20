a= float(input("Enter the first number:"))
b= float(input("Enter the first number:"))
c=input("enter the operator(add,sub,multiple,div):")
if c=="add":
    result=a+b
elif c=="sub":
    result=a-b
elif c=="multiple":
    result=a*b
elif c=="div":
    if b != 0:
        result = a / b
    else:
        result = "Cannot divide by zero!"
else:
    result = "Invalid operation!"

print("Result:", result)