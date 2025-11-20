a = int(input("Enter:"))

if a % 2 == 0:
    a = a - 1

for i in range(1, a+1, 2):
    print(i, end=" ")
